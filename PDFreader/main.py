from tkinter import *
from downloadpdf import DownloadPDF
from readpdf import PDFReader
import pyttsx3


ORANGE = "#F9D29C"
FONT_NAME = "Calibri"
FONT_SIZE = 13
PRACTICE_TEXT = 'https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf'
initiation = False
reading = False
pdf_to_read = []
tempo = None

def get_pdf_to_read():
    # Download pdf
    pdf_url = url_input.get()
    pdf_path = "C:/Users/aliko/Downloads/downloaded.pdf"
    DownloadPDF(pdf_url, pdf_path)
    # get readable list of pages
    pdf = PDFReader(pdf_path)
    pdf_to_read.extend(pdf.read())

def pause():
    global reading
    global tempo
    reading = False
    window.after_cancel(tempo)

def play():
    global pdf_to_read
    global reading
    global initiation
    if not initiation:
        get_pdf_to_read()
        initiation = True
        reading = True
    run()

def run():
    global pdf_to_read
    global tempo
    if pdf_to_read:
        print(pdf_to_read[0])
        engine = pyttsx3.init()
        engine.say(pdf_to_read[0])
        engine.startLoop()
        engine.stop()
        pdf_to_read.pop(0)
        tempo = window.after(50,run)

window = Tk()
window.title("PDF Audio Reader")
window.config(padx = 25, pady = 50, bg=ORANGE)

#Directions text
directions_label = Label(text="PDF Audio Reader", font = (FONT_NAME,FONT_SIZE,"bold"),
                         background=ORANGE, pady = 25)
directions_label.grid(column=2, row=0, columnspan = 2)

#URL label
url_label = Label(text="PDF URL", font = (FONT_NAME,FONT_SIZE), background=ORANGE,
                  width = 10, pady = 25)
url_label.grid(column=0, row = 2, sticky = "w")

#URL input
url_input = Entry(width=45, font = (FONT_NAME,FONT_SIZE))
url_input.insert(0, PRACTICE_TEXT)
url_input.grid(column=1, row=2, columnspan = 6, sticky = "e")

#pause button
pause_button = Button(text = "Pause", command = pause, bg = "white",
                       width = 15, font = (FONT_NAME,FONT_SIZE))
pause_button.grid(column=1, row=3, columnspan = 1)

#play button
play_button = Button(text = "Play", command = play, bg = "white",
                       width = 15, font = (FONT_NAME,FONT_SIZE))
play_button.grid(column=4, row=3, columnspan = 1)

window.mainloop()