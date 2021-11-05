import os
import time
import random
import webbrowser
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
global start_dir
def mkdir(path):
    if os.path.isdir(path) == False:
        os.mkdir(path)
#√
def GitHub():
    webbrowser.open_new_tab('https://github.com/DamienBoi82/MultiSheets/')
start_dir = 'MultiSheets'
mkdir(start_dir)
mkdir(start_dir + '/Addition')
mkdir(start_dir + '/Subtraction')
mkdir(start_dir + '/Multiplication')
mkdir(start_dir + '/Division')
mkdir(start_dir + '/SquareRoot')
try:
    global mathType
    global minimumNumber
    global maximumNumber
    global numberOfProblems
    global problemsPerLine
    def makeSheet():
        log('Making math sheet with options.')
        loadScrn = tk.Tk()
        tk.Label(loadScrn, text='Creating math sheet...')
        progBar = ttk.Progressbar(loadScrn, mode='determinate').grid()
        if mathType.get() == 'Addition':
            mkdir(start_dir + '/Addition/'+str(sheetName.get()))
            with open(start_dir + '/Addition/'+str(sheetName.get())+'/student.txt', 'w') as student:
                with open(start_dir + '/Addition/' + str(sheetName.get()) + '/teacher.txt', 'w') as teacher:
                    curProblems = 0
                    while curProblems <= int(numberOfProblems.get()) * int(problemsPerLine.get()):
                        for problem in range(int(problemsPerLine.get())):
                            num1 = random.randint(int(minimumNumber.get()), int(maximumNumber.get()))
                            num2 = random.randint(int(minimumNumber.get()), int(maximumNumber.get()))
                            studentText = str(num1) + ' + '+str(num2) + ' = _____'
                            student.write(studentText + ' ' * int(20 - len(studentText)))
                            teacher.write(str(num1) + ' + ' + str(num2) + ' = ' + str(num1 * num2)+ '          ')
                            progBar['value'] += 100 / int(numberOfProblems.get())

    def log(text):
        print('[DEBUG]: '+str(text))
    #Setup GUI
    screen = tk.Tk()
    screen.geometry('550x550+300+300')
    screen.title('MultiSheets, By Damien')
    screen.grid()
    font = ('Times 24')
    tk.Label(screen, text="MultiSheets,\nBy Damien B.\n\nSet math type: (Click me)", font=font).grid()
    options = [
        'Addition',
        'Subtraction',
        'Multiplication',
        'Division',
        'Square Root'
    ]
    mathType = tk.StringVar()
    drop = tk.OptionMenu(screen, mathType, *options).grid()
    sheetName = tk.StringVar()
    tk.Label(screen, text='Enter math sheet name:', font=font).grid()
    tk.Entry(screen, textvariable = sheetName).grid()
    minimumNumber = tk.StringVar()
    tk.Label(screen, text='Enter minimum number:', font=font).grid()
    minimumNumber = tk.StringVar()
    tk.Entry(screen, textvariable = minimumNumber).grid()
    tk.Label(screen, text='Enter maximum number:', font=font).grid()
    maximumNumber = tk.StringVar()
    tk.Entry(screen, textvariable = maximumNumber).grid()
    tk.Label(screen, text='Enter number of lines of problems:', font=font).grid()
    numberOfProblems = tk.StringVar()
    tk.Entry(screen, textvariable = numberOfProblems).grid()
    tk.Label(screen, text='Enter problems per line:', font=font).grid()
    problemsPerLine = tk.StringVar()
    tk.Entry(screen, textvariable = problemsPerLine).grid()
    tk.Button(screen, text='Start', command=makeSheet).grid()
    tk.Button(screen, text='View Source Code', command=GitHub).grid()
    screen.mainloop()
except Exception as err:
    tkinter.messagebox.showerror('MultiSheets', err)