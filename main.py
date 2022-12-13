#import everything from tkinter library
from tkinter import *

#create variable which is storing a value
expression = ""

#create a function buttonCLicked that will display value
def buttonClicked(value):
    global expression

    #keeps old value and adds another value to it, allows to create numbers with more digits then 1
    expression = expression + value
    equation.set(expression)

#create a function clearScreen that will clear screen
def clearScreen():
    #access expression variable
    global expression
    #remove everything from expression variable
    expression = ""
    #clear screen
    equation.set("")

#create a function evaluate to get the result
def evaluate():
    #we add try and except; if there is some error it's gonna avoid an error and application will not crash
    try:
        #access an expression variable
        global expression
        #function eval evaluates an expression
        finalValue = str(eval(expression))
        #display result on the screen
        equation.set(finalValue)
    except:
        equation.set("Something went wrong.")
        expression=""
    

#create a window
window = Tk()

#set colour of background
window.configure(background="pink")

#set windows windth & height
window.geometry("420x300")

#set title of application
window.title("Calculator")

#display on the screen
equation = StringVar()

#create a screen for user to know what is happening after he clicks buttons
screen = Entry(window, textvariable=equation, width=40)
screen.grid(columnspan=4, ipadx=70)

#create buttons 0-9 and display clicked button number
button1 = Button(window, text=" 1 ", width=8, height=2, command= lambda: buttonClicked('1'))
button1.grid(row=2, column=0)

button2 = Button(window, text=" 2 ", width=8, height=2, command= lambda: buttonClicked('2'))
button2.grid(row=2, column=1)

button3 = Button(window, text=" 3 ", width=8, height=2, command= lambda: buttonClicked('3'))
button3.grid(row=2, column=2)

button4 = Button(window, text=" 4 ", width=8, height=2, command= lambda: buttonClicked('4'))
button4.grid(row=3, column=0)

button5 = Button(window, text=" 5 ", width=8, height=2, command= lambda: buttonClicked('5'))
button5.grid(row=3, column=1)

button6 = Button(window, text=" 6 ", width=8, height=2, command= lambda: buttonClicked('6'))
button6.grid(row=3, column=2)

button7 = Button(window, text=" 7 ", width=8, height=2, command= lambda: buttonClicked('7'))
button7.grid(row=4, column=0)

button8 = Button(window, text=" 8 ", width=8, height=2, command= lambda: buttonClicked('8'))
button8.grid(row=4, column=1)

button9 = Button(window, text=" 9 ", width=8, height=2, command= lambda: buttonClicked('9'))
button9.grid(row=4, column=2)

button0 = Button(window, text=" 0 ", width=8, height=2, command= lambda: buttonClicked('0'))
button0.grid(row=5, column=1)

#create other buttons
plus = Button(window, text=" + ", width=10, height=2, command= lambda: buttonClicked('+'))
plus.grid(row=2, column=3)

minus = Button(window, text=" - ", width=10, height=2, command= lambda: buttonClicked('-'))
minus.grid(row=3, column=3)

multiply = Button(window, text=" * ", width=10, height=2, command= lambda: buttonClicked('*'))
multiply.grid(row=4, column=3)

divide = Button(window, text=" / ", width=10, height=2, command= lambda: buttonClicked('/'))
divide.grid(row=5, column=3)

equal = Button(window, text=" = ", width=10, height=2, command= evaluate)
equal.grid(row=6, column=3)

clear = Button(window, text=" clear ", width=10, height=2, command= clearScreen)
clear.grid(row=6, column=0)

decimal = Button(window, text=".", width=10, height=2, command= lambda: buttonClicked('.'))
decimal.grid(row=6, column=2)

#main function for app to work
window.mainloop()