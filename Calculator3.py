from tkinter import *


def onClick(numbers):
    global operator
    operator += str(numbers)
    text_Input.set(operator)


def btnClear():
    global operator
    text_Input.set('')
    operator = ''


def btnEqual():
    global operator
    answer = str(eval(operator))
    text_Input.set(answer)
    operator = ''


cal = Tk()
cal.title('My Calculator')
operator = ''
text_Input = StringVar()

textDisplay = Entry(cal, font=('times new roman', 20, 'italic'), textvariable=text_Input, bg='cyan', insertwidth=4, width=45, justify='right')
textDisplay.grid(row=0, column=1, columnspan=4)

# Defining Buttons :)
myButton0 = Button(cal, text='0', padx=30, pady=30, bd=4, fg='purple', bg='white', font=('times new roman', 20, 'bold'), command=lambda:onClick(0))
myButton1 = Button(cal, text='1', padx=30, pady=30, bd=4, fg='purple', bg='white', font=('times new roman', 20, 'bold'), command=lambda:onClick(1))
myButton2 = Button(cal, text='2', padx=30, pady=30, bd=4, fg='purple', bg='white', font=('times new roman', 20, 'bold'), command=lambda:onClick(2))
myButton3 = Button(cal, text='3', padx=30, pady=30, bd=4, fg='purple', bg='white', font=('times new roman', 20, 'bold'), command=lambda:onClick(3))
myButton4 = Button(cal, text='4', padx=30, pady=30, bd=4, fg='purple', bg='white', font=('times new roman', 20, 'bold'), command=lambda:onClick(4))
myButton5 = Button(cal, text='5', padx=30, pady=30, bd=4, fg='purple', bg='white', font=('times new roman', 20, 'bold'), command=lambda:onClick(5))
myButton6 = Button(cal, text='6', padx=30, pady=30, bd=4, fg='purple', bg='white', font=('times new roman', 20, 'bold'), command=lambda:onClick(6))
myButton7 = Button(cal, text='7', padx=30, pady=30, bd=4, fg='purple', bg='white', font=('times new roman', 20, 'bold'), command=lambda:onClick(7))
myButton8 = Button(cal, text='8', padx=30, pady=30, bd=4, fg='purple', bg='white', font=('times new roman', 20, 'bold'), command=lambda:onClick(8))
myButton9 = Button(cal, text='9', padx=30, pady=30, bd=4, fg='purple', bg='white', font=('times new roman', 20, 'bold'), command=lambda:onClick(9))
myButton10 = Button(cal, text='+', padx=30, pady=30, bd=4, fg='purple', bg='white', font=('times new roman', 20, 'bold'), command=lambda:onClick('+'))
myButton11 = Button(cal, text='-', padx=30, pady=30, bd=4, fg='purple', bg='white', font=('times new roman', 20, 'bold'), command=lambda:onClick('-'))
myButton12 = Button(cal, text='/', padx=30, pady=30, bd=4, fg='purple', bg='white', font=('times new roman', 20, 'bold'), command=lambda:onClick('/'))
myButton13 = Button(cal, text='*', padx=30, pady=30, bd=4, fg='purple', bg='white', font=('times new roman', 20, 'bold'), command=lambda:onClick('*'))
myButton14 = Button(cal, text='=', padx=30, pady=30, bd=4, fg='purple', bg='white', font=('times new roman', 20, 'bold'), command=lambda:btnEqual())
myButton15 = Button(cal, text='C', padx=30, pady=30, bd=4, fg='purple', bg='white', font=('times new roman', 20, 'bold'), command=lambda:btnClear())

# Adjusting Buttons :)
myButton0.grid(row=4, column=1)
myButton1.grid(row=3, column=1)
myButton2.grid(row=3, column=2)
myButton3.grid(row=3, column=3)
myButton4.grid(row=2, column=1)
myButton5.grid(row=2, column=2)
myButton6.grid(row=2, column=3)
myButton7.grid(row=1, column=1)
myButton8.grid(row=1, column=2)
myButton9.grid(row=1, column=3)
myButton10.grid(row=4, column=4)
myButton11.grid(row=3, column=4)
myButton12.grid(row=2, column=4)
myButton13.grid(row=1, column=4)
myButton14.grid(row=4, column=3)
myButton15.grid(row=4, column=2)

cal.mainloop()

