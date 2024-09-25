# Langchaindemo
Using my Email data to build an app to make my job search easy

I was doing a course on GenAI using LLM and wanted to do a practical application for my personal use.
So,I thought to use my mail data to get info about my job application and give prompt to check which all companies and applied and what was their response as it was difficult for me to check it manually.

I downloaded my MAil data from takeout and converted to csv using Emailreader.ipynb and save it as Mails.csv.

There are lot of optimizations where I can use API to read mails directly and use it.

Next I am using Streamlit to create a simple application and it takes in the question and provide appropriate ooutput provided by 'Gemini model'

To run use

streamlit run main.py

It opens in the browser.![3ea2ce51-9be3-4198-bf8a-f8d18f39e990](https://github.com/user-attachments/assets/bf5c000d-3cc4-44ae-90bc-aa2394a5ac00)





