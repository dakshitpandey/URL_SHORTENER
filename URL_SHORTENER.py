import pyshorteners
from tkinter import *

win=Tk()
win.geometry("400x270")
win.configure(bg="pink")

#Button Function
def short():
    url=entry1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)
    entry2.insert(END,s)




#Label for entering user url
Label(win,text="ENTER YOUR URL LINK",font="impact 17 bold",bg="black",fg='white').pack(fill="x")


#entry box
entry1=Entry(win,font="10",bd=3,width="40")
entry1.pack(pady=30)


#Button
Button(win,text="Click here",font="impact 12 bold",bg='blue',fg="white",width="14",command=short).pack()

#Entry
entry2= Entry(win,font="impact 16  bold",bg="pink",width="24",bd=0)
entry2.pack(pady=30)



mainloop()

