import pyttsx3
import PyPDF2
book=open('properties of fluid.pdf','rb')
reader=PyPDF2.PdfFileReader(book)
pages=reader.numPages
page=reader.getPage(2)
text=page.extractText()
speaker = pyttsx3.init()
voices=speaker.getProperty('voices')
rates=speaker.getProperty('rate')
speaker.setProperty('rate',125)
speaker.setProperty('voice',voices[1].id)
speaker.setProperty('voice',voices[1].languages)
speaker.say("hurray!")
speaker.runAndWait()
