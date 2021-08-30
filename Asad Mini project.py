from tkinter import *
root=Tk()
root.geometry("350x500")
root.resizable(0,0)
root.title("simple calculator with GUI")
def display(number):
    global num
    num=num+str(number)
    label1["text"]=num

def clear_everything():
  global num
  num=''
  label1["text"]=num

def Compute():
    global num
    result=str(eval(num))
    label1['text']=result
num=''

num=""
Var=StringVar()
frame1=Frame(root)
frame1.pack(expand=TRUE,fill=BOTH)
frame2=Frame(root)
frame2.pack(expand=TRUE,fill=BOTH)
frame3=Frame(root)
frame3.pack(expand=TRUE,fill=BOTH)
frame4=Frame(root)
frame4.pack(expand=TRUE,fill=BOTH)

label1=Label(frame1,textvariable='',font=('Arial',20),anchor=SE,bg="white",fg="grey")
label1.pack(expand=TRUE,fill=BOTH)

button_1=Button(frame1,text="1",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:display(1))
button_1.pack(expand=TRUE,fill=BOTH,side=LEFT)
button_2=Button(frame1,text="2",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:display(2))
button_2.pack(expand=TRUE,fill=BOTH,side=LEFT)
button_3=Button(frame1,text="3",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:display(3))
button_3.pack(expand=TRUE,fill=BOTH,side=LEFT)
button_addition=Button(frame1,text="+",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:display("+"))
button_addition.pack(expand=TRUE,fill=BOTH,side=LEFT)

button_4=Button(frame2,text="4",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:display(4))
button_4.pack(expand=TRUE,fill=BOTH,side=LEFT)
button_5=Button(frame2,text="5",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:display(5))
button_5.pack(expand=TRUE,fill=BOTH,side=LEFT)
button_6=Button(frame2,text="6",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:display(6))
button_6.pack(expand=TRUE,fill=BOTH,side=LEFT)
button_subtraction=Button(frame2,text="-",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:display("-"))
button_subtraction.pack(expand=TRUE,fill=BOTH,side=LEFT)

button_7=Button(frame3,text="7",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:display(7))
button_7.pack(expand=TRUE,fill=BOTH,side=LEFT)
button_8=Button(frame3,text="8",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:display(8))
button_8.pack(expand=TRUE,fill=BOTH,side=LEFT)
button_9=Button(frame3,text="9",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:display(9))
button_9.pack(expand=TRUE,fill=BOTH,side=LEFT)
button_multiplication=Button(frame3,text="*",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:display("*"))
button_multiplication.pack(expand=TRUE,fill=BOTH,side=LEFT)

button_clr=Button(frame4,text="C",font=('Arial',20),border=0,bg="black",fg="white",command=clear_everything)
button_clr.pack(expand=TRUE,fill=BOTH,side=LEFT)
button_0=Button(frame4,text="0",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:display(0))
button_0.pack(expand=TRUE,fill=BOTH,side=LEFT)
button_equal=Button(frame4,text="=",font=('Arial',20),border=0,bg="black",fg="white",command=Compute)
button_equal.pack(expand=TRUE,fill=BOTH,side=LEFT)
button_div=Button(frame4,text="/",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:display("/"))
button_div.pack(expand=TRUE,fill=BOTH,side=LEFT)
button_power=Button(frame4,text="**",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:display("**"))
button_power.pack(expand=TRUE,fill=BOTH,side=LEFT)
root.mainloop()