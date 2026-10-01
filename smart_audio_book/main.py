import pyttsx3
import PyPDF2

book = r"C:\Users\musta\Downloads\Documents\Shob_Jatra_By_Humayun_Ahmed.pdf"

ts = pyttsx3.init()

with open(book, 'rb') as book:

    pdf_reader = PyPDF2.PdfReader(book)
    page = len(pdf_reader.pages)
    print(page)

    for i in range(page):
        page = pdf_reader.pages[i]
        text = page.extract_text()

        if text and text.strip():  # Check if text is not None and not empty
            ts.say(text)
            ts.runAndWait()
ts.stop()
