import RPi.GPIO as GPIO
import time
from tkinter import *
#import tkFont
import RPi.GPIO as GPIO

MORSE_CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29,GPIO.OUT)
win = Tk()
win.title("MORSECODE GUI")
ment = StringVar()

def dot():
    GPIO.output(29,GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(29,GPIO.LOW)
    time.sleep(0.2)

def dash():
    GPIO.output(29,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(29,GPIO.LOW)
    time.sleep(0.2)

def exitProgram():
    print("Exit Button Pressed")
    GPIO.cleanup()
    win.quit()
    
def mhello():
    mtext = ment.get()
    mlabel12 = Label(win, text=mtext).pack()
    for letter in mtext:
        for symbol in MORSE_CODE[letter.upper()]:
            if symbol == '-':
                dash()
            elif symbol == '.':
                dot()
            else:
                time.sleep(0.5)
        time.sleep(0.5)

exitButton = Button(win, text = "EXIT",  command = exitProgram, height = 2, width =  8)
exitButton.pack(side = BOTTOM)
button =  Button(win, text = "OK", command = mhello, height = 2, width = 8).pack()


text = Entry(win, textvariable=ment).pack()

mainloop()

