----------------------------------------
### PROJECT: PDF FILES MANIPULATIONS ###
----------------------------------------
'''
Please install PyPDF2 which is a common python library to wrok with PDF files.
The library can be used to read text from PDF files
You can install the library as follows: pip install PyPDF2
'''
----------------------------------------------
### STEP 1: EXTRACT INFORMATION FROM A PDF ###
----------------------------------------------
from PyPDF2 import PdfFileWriter, PdfFileReader

#similar to CSV files operation
#read it as a binary files
f = open('Harvard_Business_School.pdf', 'rb')

#create a PDF reader object
read_pdf = PdfFileReader(f)

#obtain some document information
read_pdf.getDocumentInfo()

#apply the Number of pages attribute method to get the number of pages
read_pdf.numPages

#frab any page 
sample_page_text = read_pdf.getPage(2).extractText()
sample_page_text
f.close()

--------------------------------------------------------------------
### STEP 2: COPY A SINGLE PAGE AND PUT IT IN A NEWLY CREATED PDF ###
--------------------------------------------------------------------
#read a sample page
f = open('Harvard_Business_School.pdf', 'rb')
read_pdf = PdfFileReader(f)
sample_page = read_pdf.getPage(4)

#create a writer object
write_pdf = PdfFileWriter()
write_pdf.addPage(sample_page)

#open a newly created file
pdf_output = open('Harvard_New.pdf', 'wb')
write_pdf.write(pdf_output)

pdf_output.close() #close the new file
f.close()          #close the source file

-------------------------------------------------------
### STEP 3: ROTATE PDFS AND WRITE THEM TO A NEW PDF ###
-------------------------------------------------------
#open the Source file
f = open('Harvard_Business_School.pdf', 'rb')
read_pdf = PdfFileReader(f)

#create a writer object
write_pdf = PdfFileWriter()

#read a page and rotate it
rotated_page = read_pdf.getPage(2).rotateClockwise(90)

#add the rotated page to the writer object
#PLEASE DO NOT FOREGET THAT 'P' is uppercase!
write_pdf.addPage(rotated_page)

#save the writer object somewhere!
pdf_output = open('Harvard_New_rotated.pdf', 'wb')
write_pdf.write(pdf_output)
pdf_output.close() #close the new file
f.close()          #close the new file

-----------------------------------
### STEP 4: READ MULTIPLE PAGES ###
-----------------------------------
f = open('Harvard_Business_School.pdf', 'rb')
read_pdf = PdfFileReader(f)

pdf_text_all = [] #create an empty list to hold the data
num_pages = read_pdf.numPages

for page in range(num_pages):
    one_page_text = read_pdf.getPage(page).extractText()
    pdf_text_all.append(one_page_text)
    
len(pdf_text_all) 

pdf_text_all #every single page summarized in a list!

---------------------------------------
### STEP 5: ADDING WATERMARK TO PDF ###
---------------------------------------
from PyPDF2 import PdfFileWriter, PdfFileReader

#open watermark
f = open('watermark.pdf', 'rb')
read_watermark = PdfFileReader(f)
watermark_page = read_watermark.getPage(0)

#open file to be watermarked
f = open('Harvard_Business_School.pdf', 'rb')
read_pdf = PdfFileReader(f)

#create a writer object
write_pdf = PdfFileWriter()

#watermark all pages
num_pages = read_pdf.getNumPages()
for page in range(num_pages):
    single_page = read_pdf.getPage(page)
    single_page.mergePage(watermark_page)
    write_pdf.addPage(single_page)

#save the writer object somewhere!
pdf_output = open('Harvard_watermarked.pdf', 'wb')
write_pdf.write(pdf_output)
pdf_output.close() #close the new file
f.close()          #close the new file    
