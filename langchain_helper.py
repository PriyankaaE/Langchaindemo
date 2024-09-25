from langchain_google_genai import GoogleGenerativeAI
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
import os
from langchain.chains import RetrievalQA

from dotenv import load_dotenv
load_dotenv()

llm = GoogleGenerativeAI(model = "gemini-1.5-flash")
instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")
database_name = 'faiss_index'

def load_into_database():

	loader = CSVLoader(
    file_path="Mails.csv",
    source_column = 'Message',
    csv_args={
        "quotechar": '"',
    },
	)

	data = loader.load()

	vectordb = FAISS.from_documents(documents=data,
	                                 embedding=instructor_embeddings)

	# Create a retriever for querying the vector database
	# retriever = vectordb.as_retriever(score_threshold = 0.3,k=200)
	vectordb.save_local(database_name)

def query_question(question):


	vectordb = FAISS.load_local(database_name, instructor_embeddings,allow_dangerous_deserialization=True)
	retriever = vectordb.as_retriever(score_threshold = 0.3,search_kwargs={'k': 10, 'fetch_k': 1000})
	# rdocs = retriever.get_relevant_documents("What is the company name of last application I submitted")

	prompt_template = """Given the following context and a question, try to check the document for the date ,type and company name and provide the response.
	Dont limit the companies search the entire data and ouput all company names not limited to 4 .
	If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

	CONTEXT: {context}

	QUESTION: {question}"""


	PROMPT = PromptTemplate(
	    template=prompt_template, input_variables=["context", "question"]
	)
	chain_type_kwargs = {"prompt": PROMPT}
	chain = RetrievalQA.from_chain_type(llm=llm,
	                            chain_type="stuff",
	                            retriever=retriever,
	                            input_key="query",
	                            return_source_documents=True,
	                            chain_type_kwargs=chain_type_kwargs)

	response = chain(question)
	return response['result']


if __name__ == "__main__":
	load_into_database()
	response = query_question("What was the last company I applied")
	print(response)