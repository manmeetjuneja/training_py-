#!/usr/bin/env python
# coding: utf-8

# In[11]:


from tkinter import *


# In[2]:


'''window  = tkinter.Tk()
window.title("my GUI")
label = tkinter.Label(window,text="Welcome to my GUI")
#window.mainloop()


# In[12]:


window = tkinter.Tk()
window.title("Button GUI")
button_widget = tkinter.Button(window,text="Welcome to GUI")
button_widget.pack()
tkinter.mainloop()


# In[46]:


'''window = tkinter.Tk()
window.title("GUI")
top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack()
btn1 = tkinter.Button(top_frame,text = "Buttton1",fg = "red").pack()
btn2 = tkinter.Button(top_frame,text = "Buttton2",fg = "green").pack()
btn3 = tkinter.Button(bottom_frame,text = "Buttton3",fg = "purple").pack()
btn4 = tkinter.Button(bottom_frame,text = "Buttton4",fg = "orange").pack()
window.mainloop()'''


# In[13]:


top = tkinter.Tk()
top = tkinter.Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()

rad1 = tkinter.Checkbutton(top,text='First', variable=CheckVar1) 
rad2 = tkinter.Checkbutton(top,text='Second', variable=CheckVar2)  
top.mainloop()


# In[14]:


window = tkinter.Tk()
window.title("GUI")
window.geometry("500x500")
lab=tkinter.Label(window,text="Username").grid(row=0)
tkinter.Entry(window).grid(row=0,column=1)
lab=tkinter.Label(window,text="Password").grid(row=1)
tkinter.Entry(window).grid(row=1,column=1)
chk = Checkbutton(window,text="keep me logged in").grid(columnspan=2)
def clicked():
    lab.configure(text="Button Clicked")
btn = Button(window,text="Click me",command=clicked)
btn.grid(row=3,column=0)
window.mainloop()


# In[15]:


import tkinter.messagebox
window = tkinter.Tk()
window.geometry("400x200")
window.title("GUI")
tkinter.messagebox.showinfo("Alert Message","this is an alert")
response = tkinter.messagebox.askquestion("Trickeyy que","do you swim??")
if response==YES:
    tkinter.Label(window,text="yes ofcourse")
else:
    tkinter.Label(window,text="Nahh")
window.mainloop()


# In[ ]:




