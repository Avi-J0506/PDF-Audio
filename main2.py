from tkinter import *
import tkinter
from tkinter import filedialog

from path import Path
from PyPDF4 import PdfFileReader, PdfFileWriter
import pyttsx3
from speech_recognition import Recognizer, AudioFile
from pydub import AudioSegment
import os

# Declaring Global Variables
global end_pgNo, start_pgNo

# Function to open the selected PDF and read from it
def read():
    path = filedialog.askopenfile()
    pdfLoc = open(str(path), 'rb')
    pdfreader = PdfFileReader(pdfLoc)
    speaker = pyttsx3.init()

    start = start_pgNo.get()
    end = end_pgNo.get()

    for i in range(start, end+1):
        page = pdfreader.getPage(i)
        txt = page.extractText()
        speaker.runAndWait()

# Function to create a GUI and get a required inputs for PDF to Audio Conversion
def pdf_to_audio():
    wn1 = tkinter.Tk()
    wn1.title("PDF to Audio Converter")
    wn1.geometry('500x400')
    wn1.config(bg='snow3')

    start_pgNo = IntVar(wn1)
    end_pgNo = IntVar(wn1)

    Label(wn1, text = "PDF to Audio Converter", fg='black', font=('Courier',15)).place(x=60, y=10)

    Label(wn1, text = "Enter the start and the end page to read. If you only want to read a single\n page please enter the start page and enter the next page as the end page:", anchor = 'e', justify = LEFT).place(x=20, y=90)

    Label(wn1, text = "Start Page No.:").place(x=100, y=140)

    startPg = Entry(wn1, width = 20, textvariable=start_pgNo)
    startPg.place(x=100, y=170)

    Label(wn1, text = "End Page No.:").place(x=250, y=140)

    endPg = Entry(wn1, width = 20, textvariable=end_pgNo)
    endPg.place(x=250, y=170)

    Label(wn1, text='Click the button below to choose the pdf and start to listen').place(x=100, y=230)
    Button(wn1, text="Listen", bg='ivory3', font=('Courier',13),command=read).place(x=230, y=260)

    wn1.mainloop()

# Function to update the PDF file with text, both given as parameters
def write_text(filename, text):
    writer = PDFwriter()
    writer.addBlankPage(72,72)
    pdfPath = Path(filename)
    with pdf_path.open('ab') as output_file:
        writer.write(output_file)
        output_file.write(text)

def conver():
    path = filedialog.askopenfilename()
    audioLoc = open(path, 'rb')

    pdf_loc =pdfPath.get()

    audioFileName = os.path.basename(audioLoc).split('.')[0]
    audioFileExt = os.path.basename(audioLoc).split('.')[1]
    if audioFileExt != 'wav' and audioFileext !='mp3':
        messagebox.showerror('Error!','The format of the audio file should be "wav" or "mp3".')

    if audioFileExt == 'mp3':
        audio_file = AudioSegment.from_file(path(audioLoc), format = 'mp3')
        audio_file.export(f'{audioFileName}.wav',format = 'wav')
        source_file = f'{audioFileName}.wav'

        recog= Recognizer()
        with AudioFile(source_file) as source:
            recog.pause_threshold = 5
            speech = recog.record(source)
            text = recog.recognize_google(speech)
            write_text(pdf_loc, text)

#Function to create a GUI and get required inputs for Audio to PDF Conversion
def audio_to_pdf():
#Creating a window
    wn2= tkinter.Tk()
    wn2.title("PythonGeeks Audio to PDF converter")
    wn2.geometry('500x400')
    wn2.config(bg='snow3')

    pdfPath = StringVar(wn2) #Variable to get the PDF path input

    Label(wn2, text='PythonGeeks Audio to PDF converter',
    fg='black', font=('Courier', 15)).place(x=60, y=10)

    #Getting the PDF path input
    Label(wn2, text='Enter the PDF File location where you want to save (with extension):').place(x=20, y=50)
    Entry(wn2, width=50,textvariable=pdfPath).place(x=20, y=90)

    Label(wn2, text='Choose the Audio File location that you want to read (.wav or .mp3 extensions only):',
    fg='black').place(x=20, y=130)

    #Button to select the audio file and do the conversion
    Button(wn2, text='Choose', bg='ivory3',font=('Courier', 13),
    command=convert).place(x=50, y=170)
    wn2.mainloop() #Runs the window till it is closed

#Creating the main window
wn = tkinter.Tk()
wn.title("PythonGeeks PDF to Audio and Audio to PDF converter")
wn.geometry('700x300')
wn.config(bg='LightBlue1')

Label(wn, text='PythonGeeks PDF to Audio and Audio to PDF converter',
fg='black', font=('Courier', 15)).place(x=40, y=10)

#Button to convert PDF to Audio form
Button(wn, text="Convert PDF to Audio", bg='ivory3',font=('Courier', 15),
command=pdf_to_audio).place(x=230, y=80)

#Button to convert Audio to PDF form
Button(wn, text="Convert Audio to PDF", bg='ivory3',font=('Courier', 15),
command=audio_to_pdf).place(x=230, y=150)

#Runs the window till it is closed
wn.mainloop()