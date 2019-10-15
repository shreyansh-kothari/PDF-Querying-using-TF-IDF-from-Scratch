# PDF-Querying-using-TF-IDF-from-Scratch
Given a set of PDFs and the query, the most relevant pdf can be found with the help of TF-IDF. The code has not used any library to implement TF-IDF

# Explanation
The code only uses pdfminer and glob libraries to read pdf and traverse a directory for pdf. The Tf-idf is done manually without using any library. To understand the code, please read the comments in the code.

# PDF Files
A sample folder is uploaded with few pdfs to tryout the code.

# PDF_querying.py
1. Includes the reading of pdf files using pdfminer library
2. Extracting words from each pdf
3. Take query input from the user
4. tf-idf for the pdf and query
5. Ranking the pdfs that have same words from the query

# text querying.py
1. The text from the documents are taken as string initially
2. Rest process is same as the other code.

