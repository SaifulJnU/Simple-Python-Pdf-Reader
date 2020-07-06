import pyttsx3
import PyPDF2

book = open('CN.pdf', 'rb')  # read the pdf
pdfreader = PyPDF2.PdfFileReader(book)  # crate an object
pages = pdfreader.numPages  # to calculate the total number of page
print(pages)
speaker = pyttsx3.init()  # create an object for speaker

for i in range(50, pages):  # it will speak from page 50 to end according to loop condition
    page = pdfreader.getPage(i)  # getting page form pdf
    text = page.extractText()  # then extrcted it into text
    speaker.say(text)  # now it is time to speak by object speaker
    speaker.runAndWait()  # to run the speaker
