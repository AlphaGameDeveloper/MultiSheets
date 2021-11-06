import os
import random
import webbrowser
import tkinter as tk
import tkinter.messagebox
import math
global start_dir
def mkdir(path):
    if os.path.isdir(path) == False:
        os.mkdir(path)
#√

VERSION = "1.0"

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
    screen = tk.Tk()
    global sheetName; sheetName=tk.StringVar()
    global mathType; mathType=tk.StringVar()
    global minimumNumber; minimumNumber=tk.IntVar()
    global maximumNumber; maximumNumber=tk.IntVar()
    global numberOfProblems; numberOfProblems=tk.IntVar()
    global problemsPerLine; problemsPerLine=tk.IntVar()
    def DefaultValues():
        if mathType.get() == "Addition":
            minimumNumber.set(0)
            maximumNumber.set(32768)
            numberOfProblems.set(50)
            problemsPerLine.set(5)
        if mathType.get() == "Subtraction":
            minimumNumber.set(0)
            maximumNumber.set(32768)
            numberOfProblems.set(50)
            problemsPerLine.set(5)
        if mathType.get() == "Multiplication":
            minimumNumber.set(0)
            maximumNumber.set(12)
            numberOfProblems.set(50)
            problemsPerLine.set(5)
        if mathType.get() == "Division":
            minimumNumber.set(0)
            maximumNumber.set(100)
            numberOfProblems.set(50)
            problemsPerLine.set(5)
        if mathType.get() == "Square Root":
            minimumNumber.set(0)
            maximumNumber.set(144)
            numberOfProblems.set(50)
            problemsPerLine.set(5)
    def makeSheet():
        if sheetName.get() == '':
            tkinter.messagebox.showerror('MultiSheets', 'The field containing the sheet name is empty.\nPlease fill it.\nThe program will now close.\n\n(FileNotFoundError)')
            exit(1)

        if mathType.get() == "Addition":
            mkdir(start_dir + '/Addition/' + sheetName.get())
            with open(start_dir + '/Addition/' + sheetName.get()+'/student.txt', 'w') as student:
                with open(start_dir + '/Addition/' + sheetName.get() + '/teacher.txt', 'w') as teacher:
                    curProblems = 0
                    while curProblems <= numberOfProblems.get():
                        for problem in range(problemsPerLine.get()):
                            num1 = random.randint(minimumNumber.get(), maximumNumber.get())
                            num2 = random.randint(minimumNumber.get(), maximumNumber.get())

                            studentText = str(num1) + " + " + str(num2) + " = ____  |  "
                            teacherText = str(num1) + " + " + str(num2) + ' = ' + str(num1 + num2) + "  |  "

                            student.write(studentText)
                            teacher.write(teacherText)

                            curProblems += 1

                        student.write('\n')
                        teacher.write('\n')
                    tkinter.messagebox.showinfo('MultiSheets', 'Finished creating math sheet.')
        if mathType.get() == "Subtraction":
            mkdir(start_dir + '/Subtraction/' + sheetName.get())
            with open(start_dir + '/Subtraction/' + sheetName.get()+'/student.txt', 'w') as student:
                with open(start_dir + '/Subtraction/' + sheetName.get() + '/teacher.txt', 'w') as teacher:
                    curProblems = 0
                    while curProblems <= numberOfProblems.get():
                        for problem in range(problemsPerLine.get()):
                            num1 = random.randint(minimumNumber.get(), maximumNumber.get())
                            num2 = random.randint(minimumNumber.get(), maximumNumber.get())

                            studentText = str(num1) + " - " + str(num2) + " = ____  |  "
                            teacherText = str(num1) + " - " + str(num2) + ' = ' + str(num1 - num2) + "  |  "

                            student.write(studentText)
                            teacher.write(teacherText)

                            curProblems += 1

                        student.write('\n')
                        teacher.write('\n')
                    tkinter.messagebox.showinfo('MultiSheets', 'Finished creating math sheet.')
        if mathType.get() == "Multiplication":
            mkdir(start_dir + '/Multiplication/' + sheetName.get())
            with open(start_dir + '/Multiplication/' + sheetName.get()+'/student.txt', 'w') as student:
                with open(start_dir + '/Multiplication/' + sheetName.get() + '/teacher.txt', 'w') as teacher:
                    curProblems = 0
                    while curProblems <= numberOfProblems.get():
                        for problem in range(problemsPerLine.get()):
                            num1 = random.randint(minimumNumber.get(), maximumNumber.get())
                            num2 = random.randint(minimumNumber.get(), maximumNumber.get())

                            studentText = str(num1) + " x " + str(num2) + " = ____  |  "
                            teacherText = str(num1) + " x " + str(num2) + ' = ' + str(num1 * num2) + "  |  "

                            student.write(studentText)
                            teacher.write(teacherText)

                            curProblems += 1

                        student.write('\n')
                        teacher.write('\n')
                    tkinter.messagebox.showinfo('MultiSheets', 'Finished creating math sheet.')
        if mathType.get() == "Division":
            mkdir(start_dir + '/Division/' + sheetName.get())
            with open(start_dir + '/Division/' + sheetName.get()+'/student.txt', 'w') as student:
                with open(start_dir + '/Division/' + sheetName.get() + '/teacher.txt', 'w') as teacher:
                    curProblems = 0
                    while curProblems <= numberOfProblems.get():
                        for problem in range(problemsPerLine.get()):
                            num1 = random.randint(minimumNumber.get(), maximumNumber.get())
                            num2 = random.randint(minimumNumber.get(), maximumNumber.get())

                            studentText = str(num1) + " ÷ " + str(num2) + " = ____  |  "
                            teacherText = str(num1) + " ÷ " + str(num2) + ' = ' + str(num1 / num2) + "  |  "

                            student.write(studentText)
                            teacher.write(teacherText)

                            curProblems += 1

                        student.write('\n')
                        teacher.write('\n')
                    tkinter.messagebox.showinfo('MultiSheets', 'Finished creating math sheet.')
        if mathType.get() == "Square Root":
            mkdir(start_dir + '/SquareRoot/' + sheetName.get())
            with open(start_dir + '/SquareRoot/' + sheetName.get()+'/student.txt', 'w') as student:
                with open(start_dir + '/SquareRoot/' + sheetName.get() + '/teacher.txt', 'w') as teacher:
                    curProblems = 0
                    while curProblems <= numberOfProblems.get():
                        for problem in range(problemsPerLine.get()):
                            num = random.randint(minimumNumber.get(), maximumNumber.get())

                            studentText = "Square Root of: "+str(num) + " = ____  |  "
                            teacherText = "Square root of: "+str(num) + " = " + str(math.sqrt(num)) + "  |  "

                            student.write(studentText)
                            teacher.write(teacherText)

                            curProblems += 1

                        student.write('\n')
                        teacher.write('\n')
                    tkinter.messagebox.showinfo('MultiSheets', 'Finished creating math sheet.')
    def log(text):
        print('[DEBUG]: '+str(text))
    #Setup GUI
    screen.geometry('550x700+300+300')
    screen.title('MultiSheets, By Damien')
    screen.grid()
    font = ('Times 24')
    tk.Label(screen, text="MultiSheets,\nBy Damien B.\n\nVersion: "+VERSION+"\n\nSet math type: (Click me)", font=font).grid()
    options = [
        'Addition',
        'Subtraction',
        'Multiplication',
        'Division',
        'Square Root'
    ]
    mathType = tk.StringVar()
    drop = tk.OptionMenu(screen, mathType, *options).grid()
    tk.Button(screen, text='Use default values for math type', command=DefaultValues).grid()
    tk.Label(screen, text='Enter math sheet name:', font=font).grid()
    tk.Entry(screen, textvariable = sheetName).grid()
    tk.Label(screen, text='Enter minimum number:', font=font).grid()
    tk.Entry(screen, textvariable = minimumNumber).grid()
    tk.Label(screen, text='Enter maximum number:', font=font).grid()
    tk.Entry(screen, textvariable = maximumNumber).grid()
    tk.Label(screen, text='Enter number of lines of problems:', font=font).grid()
    tk.Entry(screen, textvariable = numberOfProblems).grid()
    tk.Label(screen, text='Enter problems per line:', font=font).grid()
    tk.Entry(screen, textvariable = problemsPerLine).grid()
    tk.Button(screen, text='Start', command=makeSheet).grid()
    tk.Button(screen, text='View Source Code', command=GitHub).grid()
    screen.mainloop()
except Exception as err:
    tkinter.messagebox.showerror('MultiSheets', err)