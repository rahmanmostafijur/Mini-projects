import pyttsx3
import PyPDF2

book = open(' ', 'rb')
pdf_reader = PyPDF2.PdfReader(book)
page = pdf_reader.numPages
print(page)

ts = pyttsx3.init()
page = pdf_reader.getPage(0)
text = page.extract_text()
ts.say(text)
ts.runAndWait()