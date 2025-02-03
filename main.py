import os
import sys
import pyfiglet
import pdfplumber
import threading
from tqdm import tqdm
from gtts import lang, gTTS

class App:
    def __init__(self):
        self.lan = 'en'
        self.pdfPath = ''
        self.pdfText = ''
        self.functions = {
                'l': [self.set_language, 'select language to speak, default is english'], 
                'p': [self.set_pdf, 'set pdf path to process'],
                'r': [self.read_full_pdf, 'read full pdf'],
                'd': [self.download_full_pdf, 'download full pdf'],
                's': [self.simultaneous, 'load pdf read in memory, not creator audio'],
                'h': [self.help, 'help'],
                'q': [self.exit_program, 'exit']
            }


    def set_language(self):
        print('Languages:')

        supported_languages = lang.tts_langs()
        for key, value in supported_languages.items():
            print(key, value)

        self.lan = input('select language: ')
        if self.lan in supported_languages:
            print(f'{self.lan} {supported_languages[self.lan]} selected...')


    def set_pdf(self):
        self.pdfPath = input('path to pdf read: ')
        if os.path.exists(self.pdfPath):
            print(f'set {self.pdfPath} to process')    
        else:
            print(f'{self.pdfPath} does not exist')
            self.pdfPath = ''

    
    def read_full_pdf(self):
        print('init read pdf')
        
        with pdfplumber.open(self.pdfPath) as pdf:
            for page in tqdm(pdf.pages, desc='Reading PDF pages', unit='page'):
                self.pdfText += page.extract_text() + '\n'


    def download_full_pdf(self):
        pass


    def simultaneous(self):
        with pdfplumber.open(self.pdfPath) as pdf:
            print('Lets read and listen pdf')
            pageRange = input('set number page to start: ')

            x = 0
            for page in tqdm(pdf.pages, desc='Reading PDF pages', unit='page'):
                if x == pageRange: 
                    self.pdfText
                    
                x += 1


    def help(self):
        for key, value in self.functions.items():
                print(f'{key} : {value[1]}')


    def exit_program(self):
        if input("Do you want to exit? (y/n): ").lower() == 'y':
            sys.exit(0) 


    def command(self):
        select = input('$_> ')
        self.functions[select][0]()


    def main(self):
        hello = pyfiglet.figlet_format('readPY', font='caligraphy', width=100)
        print(hello)
        print('     This is a simple script to create audio books, with lib gTTS and pdfplumber     \n')
        print('\n h to help \n')

        while True:
            self.command()


app = App()
app.main()

