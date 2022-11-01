# importing webbrowser module
import webbrowser
# importing tkinter
from tkinter import *
# creating root
root = Tk()
# setting GUI title
root.title("Web Browser")
# setting GUI geometry
root.geometry("300x200")
# function to open ggogle in browser
def google():
    webbrowser.open("www.google.com")
    
# button to call google function
mygoogle = Button(root , text="open google",command=google).pack(pady=20)
root.mainloop()

    