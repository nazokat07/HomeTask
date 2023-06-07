import tkinter 
import random
import datetime

window = tkinter.Tk()
window.geometry('400x200')
window.resizable(width=False, height=False)
window.title('Sign in')
window.configure(background='white')

def results():
    pass

label = tkinter.Label(
    window,
    text='Email Address: ',
    background='white',
    font=('Oswald  15')
)
label.place(x=15,y=10)

entry_1 = tkinter.Entry(
    window,
    width=40,
    background='#ebbda2'
)
entry_1.place(x=20, y=50)

label_2 = tkinter.Label(
    window,
    text='Password: ',
    background='white',
    font=('Oswald  15')
)
label_2.place(x=15,y=70)

entry_2 = tkinter.Entry(
    window,
    width=40,
    background='#ebbda2'
)
entry_2.place(x=20, y=110)

btn = tkinter.Button(
        window,
    text='Login',
    command=results,
    width=34
)
btn.place(x=20, y=150)



window.mainloop()
