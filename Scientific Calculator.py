# Python program to  create a simple GUI  
# calculator using Tkinter
# import everything from tkinter module 
from tkinter import *
import math
import tkinter.messagebox
#from gtts import gTTS


expression = ""
expression1 = ""

#--------------------------------------------Functions--------------------------------------------#
def press(num): 
    global expression
    global expression1
    expression = expression + str(num) 
    if num=="math.sin(":
        num="sin("
    if num=="math.cos(":
        num="cos("
    if num=="math.tan(":
        num="tan("
    if num=="math.pow(":
        num="pow("
    if num=="math.sqrt(":
        num="sqrt("
    if num=="math.asin(":
        num="asin("
    if num=="math.acos(":
        num="acos("
    if num=="math.atan(":
        num="atan("
    if num=="math.sinh(":
        num="sinh("
    if num=="math.cosh(":
        num="cosh("
    if num=="math.log(":
        num="log("
    if num=="math.log2(":
        num="log2("
    if num=="math.exp(":
        num="exp("
    if num=="math.pi":
        num="2π"
    
    expression1= expression1+ str(num)
    equation.set(expression) 

def equalpress():
    try:
        global expression, expression1
        global total
        total = str(eval(expression)) 
        equation.set(total)
        expression = str(total)
##        expression1 = int(expression1)
##        total=int(total)
    except: 
        equation.set(" ERROR ") 
        expression = ""
        expression1 = ""
        

def fact(n):
    global expression
    fact = math.factorial(n)
    equation.set(fact)
    expression = str(fact)


def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator","Confirm if you want to Exit:")
    if iExit > 0:
        root.destroy()
        return

def Scientific():
    root.resizable(width =False, height =False)
    root.geometry("928x555+0+0")

def Standard():
    root.resizable(width =False, height =False)
    root.geometry("465x555+0+0")   

# Function to clear the contents of text entry box 
def clear(): 
     global expression, expression1
     expression = ""
     expression1= ""
     total=""
     equation.set("")

def about():
    #about = tkinter.messagebox.showinfo("About Us","Hello!\nThis is a Scientific Calculator made by  \n\nPriyanka Samantaroy \nBhuvnesh Vyas \nAnkit Kumar Mishra\n Thank you for using our Calculator.")
    about = Tk()
    about.title("About Us")
    about.configure(background ="firebrick4")
    about.resizable(width =False, height =False)
    w = Label(about,font=('times new roman',20,'bold'),bg="coral",text="Hello!\nThis is a Scientific Calculator made by -> \n\nPriyanka Samantaroy \nBhuvnesh Vyas \nAnkit Kumar Mishra. Thank you for using our Calculator.")
    w.pack()
    about.mainloop()
    
def helpp():
    helpp = Tk()
    helpp.title("Help Index")
    helpp.configure(background ="firebrick4")
    helpp.resizable(width =False, height =False)
    w = Label(helpp,font=('times new roman',20,'bold'),bg="coral",text="\tHELP INDEX\n\t+ - plus or addition\n\t- - minus or subtraction times\n\t* - times or multiply\n\t/ or ÷ - division\n\t√ - square roo\n\tex - exponent, raise e to the power\n\tLog - natural logarithm, take the log of\n\tSIN - sine function\n\tSIN-1 - inverse sine function, arcsine\n\tCOS - cosine function\n\tCOS-1 - inverse cosine function, arccosine\n\tTAN  - tangent function\n\tTAN-1 - inverse tangent function or arctangent\n\t( ) - parentheses\n")
    w.pack()
    helpp.mainloop()
    
def new():
    new = tkinter.messagebox.showinfo("New... ","New Window to this calculator will be opened in a minute.")
    Scientific()
    clear()


#-----------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk()
root.title("Scientific Calculator")
root.configure(background ="firebrick4")
root.resizable(width =False, height =False)
root.geometry("465x555+0+0")
equation = StringVar()

calc = Frame(root)
calc.grid()   
        
txtdisplay = Entry(calc, font=("arial narrow",20,"bold"), bg="firebrick4",bd=30,width=33, justify=RIGHT,textvariable=equation)
txtdisplay.grid(row=0 ,column=0 ,columnspan=4, pady=1)
txtdisplay.insert(0," 0")


          
#---------------------------------------------BUTTONS--------------------------------------------#
button1 = Button(calc, overrelief=GROOVE, width=6,height=2,command=lambda: press(1),font=('arial',20,'bold'),bg='salmon3',bd=4,text=' 1 ')
button1.grid(row=2, column=0)

button2 = Button(calc, overrelief=GROOVE, width=6,height=2,command=lambda: press(2),font=('arial',20,'bold'),bg='salmon3',bd=4,text=' 2 ')
button2.grid(row=2, column=1)

button3 = Button(calc, overrelief=GROOVE, width=6,height=2,command=lambda: press(3),font=('arial',20,'bold'),bg='salmon3',bd=4,text=' 3 ')
button3.grid(row=2, column=2)

button4 = Button(calc, overrelief=GROOVE, width=6,height=2,command=lambda: press(4),font=('arial',20,'bold'),bg='salmon3',bd=4,text=' 4 ')
button4.grid(row=3, column=0)

button5 = Button(calc, overrelief=GROOVE, width=6,height=2,command=lambda: press(5),font=('arial',20,'bold'),bg='salmon3',bd=4,text=' 5 ')
button5.grid(row=3, column=1)

button6 = Button(calc, overrelief=GROOVE, width=6,height=2,command=lambda: press(6),font=('arial',20,'bold'),bg='salmon3',bd=4,text=' 6 ')
button6.grid(row=3, column=2)

button7 = Button(calc, overrelief=GROOVE, width=6,height=2,command=lambda: press(7),font=('arial',20,'bold'),bg='salmon3',bd=4,text=' 7 ')
button7.grid(row=4, column=0)

button8 = Button(calc, overrelief=GROOVE, width=6,height=2,command=lambda: press(8),font=('arial',20,'bold'),bg='salmon3',bd=4,text=' 8 ')
button8.grid(row=4, column=1)

button9 = Button(calc, overrelief=GROOVE, width=6,height=2,command=lambda: press(9),font=('arial',20,'bold'),bg='salmon3',bd=4,text=' 9 ')
button9.grid(row=4, column=2)


#-------------------------------------------Normal fucntions------------------------------------
btnsci = Button(calc,text='SCI', width=6,height=2,command=lambda:Scientific(), overrelief=GROOVE, font=('arial',20,'bold'),bd=4,bg='coral4')
btnsci.grid(row=1,column=0)

btnclearall = Button(calc,text='C', width=6,height=2,command=lambda:clear(), overrelief=GROOVE, font=('arial',20,'bold'),bd=4,bg='coral4')
btnclearall.grid(row=1,column=2) 

btnstd = Button(calc,text='STD',command=lambda:Standard(), overrelief=GROOVE, width=6,height=2, font=('arial',20,'bold'),bd=4,bg='coral4')
btnstd.grid(row=1,column=1)

btnsqrt = Button(calc,text=' √ ',command=lambda: press("math.sqrt("), overrelief=GROOVE, width=6,height=2, font=('arial',20,'bold'),bd=4,bg='coral4') 
btnsqrt.grid(row=1,column=3)

btnsub = Button(calc,text=' - ',command=lambda: press('-') , overrelief=GROOVE, width=6,height=2, font=('arial',20,'bold'),bd=4,bg='coral4')
btnsub.grid(row=2,column=3)

btnadd = Button(calc,text=' + ',command=lambda: press('+') , overrelief=GROOVE, width=6,height=2, font=('arial',20,'bold'),bd=4,bg='coral4')
btnadd.grid(row=3,column=3)

btnmul= Button(calc,text= 'X ',command=lambda: press('*') , overrelief=GROOVE, width=6,height=2, font=('arial',20,'bold'),bd=4,bg='coral4')
btnmul.grid(row=4,column=3)

buttondot = Button(calc,text=' . ',command=lambda: press('.'), overrelief=GROOVE, width=6,height=2,font=('arial',20,'bold'),bg='salmon3',bd=4)
buttondot.grid(row=5, column=0)

button0 = Button(calc, width=6,height=2,command=lambda: press(0), overrelief=GROOVE,font=('arial',20,'bold'),bg='salmon3',bd=4,text=' 0 ')
button0.grid(row=5, column=1)

btndiv = Button(calc,text=' / ',command=lambda: press('/') ,overrelief=GROOVE, width=6,height=2, font=('arial',20,'bold'),bd=4,bg='coral4')
btndiv.grid(row=5,column=3)

btneq = Button(calc,text=' = ',command=equalpress, width=6,height=2, overrelief=GROOVE, font=('arial',20,'bold'),bd=4,bg='coral4')
btneq.grid(row=5,column=2)
#----------------------------------------------Scientific--------------------------------------------------------


btnpi = Button(calc,text=' π ',command=lambda: press("3.14") , overrelief=GROOVE, width=6,height=2, font=('arial',20,'bold'),bd=4,bg='coral4')
btnpi.grid(row=1,column=4)

btncos = Button(calc,text=' SIN ',command=lambda: press("math.sin(") , overrelief=GROOVE, width=6,height=2, font=('arial',20,'bold'),bd=4,bg='coral4')
btncos.grid(row=1,column=5)

btnsin = Button(calc,text= ' COS ',command=lambda: press("math.cos(") , overrelief=GROOVE, width=6,height=2, font=('arial',20,'bold'),bd=4,bg='coral4')
btnsin.grid(row=1,column=6)

btntan = Button(calc,text=' TAN ',command=lambda: press("math.tan(") , overrelief=GROOVE, width=6,height=2, font=('arial',20,'bold'),bd=4,bg='coral4')
btntan.grid(row=1,column=7)

#----------------------------------------------------------------------------------------------------------

btn2pi = Button(calc,text=' 2π ',command=lambda: press("6.28") , overrelief=GROOVE, width=6,height=2, font=('arial',20,'bold'),bd=4,bg='coral4')
btn2pi.grid(row=2,column=4)

btnsininv = Button(calc,text= ' SIN-1 ',command=lambda: press("math.asin(") , overrelief=GROOVE, width=6,height=2, font=('arial',20,'bold'),bd=4,bg='coral4')
btnsininv.grid(row=2,column=5)

btncosinv = Button(calc,text=' COS-1 ',command=lambda: press("math.acos(") , overrelief=GROOVE, width=6,height=2, font=('arial',20,'bold'),bd=4,bg='coral4')
btncosinv.grid(row=2,column=6)

btntaninv = Button(calc,text=' TAN-1 ',command=lambda: press("math.atan(") , overrelief=GROOVE, width=6,height=2, font=('arial',20,'bold'),bd=4,bg='coral4')
btntaninv.grid(row=2,column=7)

#--------------------------------------------------------------------------------------------------------

btnlog2 = Button(calc,text=' LOG2 ',command=lambda: press("math.log2(") , overrelief=GROOVE, width=6,height=2, font=('arial',20,'bold'),bd=4,bg='coral4')
btnlog2.grid(row=3,column=4)

btnsinh = Button(calc,text= ' SINh ',command=lambda: press("math.sinh(") , overrelief=GROOVE, width=6,height=2, font=('arial',20,'bold'),bd=4,bg='coral4')
btnsinh.grid(row=3,column=5)

btncosh = Button(calc,text=' COSh ',command=lambda: press("math.cosh(") , overrelief=GROOVE, width=6,height=2, font=('arial',20,'bold'),bd=4,bg='coral4')
btncosh.grid(row=3,column=6)

btndeg = Button(calc,text=' DEG ',command=lambda: press("math.degrees(") , overrelief=GROOVE, width=6,height=2, font=('arial',20,'bold'),bd=4,bg='coral4')
btndeg.grid(row=3,column=7)

#----------------------------------------------------------------------------------------------------------

btnlog = Button(calc,text=' LOG ',command=lambda: press("math.log(") , overrelief=GROOVE, width=6,height=2, font=('arial',20,'bold'),bd=4,bg='coral4')
btnlog.grid(row=4,column=4)

btnexp = Button(calc,text=' EXP ',command=lambda: press("math.exp(") , overrelief=GROOVE, width=6,height=2, font=('arial',20,'bold'),bd=4,bg='coral4')
btnexp.grid(row=4,column=5)

btnfact = Button(calc,text= ' FACT. ',command=lambda:fact(int(expression)), overrelief=GROOVE, width=6,height=2, font=('arial',20,'bold'),bd=4,bg='coral4')
btnfact.grid(row=4,column=6)

btnrad = Button(calc,text= '  RAD ',command=lambda: press("math.radians(") , overrelief=GROOVE, width=6,height=2, font=('arial',20,'bold'),bd=4,bg='coral4')
btnrad.grid(row=4,column=7)

#----------------------------------------------------------------------------------------------------------------

btnlp = Button(calc,text=' ( ',command=lambda: press('(') , overrelief=GROOVE, width=6,height=2, font=('arial',20,'bold'),bd=4,bg='coral4')
btnlp.grid(row=5,column=4)

btnrp = Button(calc,text=' ) ',command=lambda: press(')') , overrelief=GROOVE, width=6,height=2, font=('arial',20,'bold'),bd=4,bg='coral4')
btnrp.grid(row=5,column=5)

btnE = Button(calc,text=' e ',command=lambda: press("math.e") , overrelief=GROOVE, width=6,height=2, font=('arial',20,'bold'),bd=4,bg='coral4')
btnE.grid(row=5,column=6)

btntruncate = Button(calc,text=' TRUNCATE ',command=lambda:fact(expression), overrelief=GROOVE, width=6,height=2, font=('arial',20,'bold'),bd=4,bg='coral4')
btntruncate.grid(row=5,column=7)


#--------------------------------------------MENU------------------------------------------------#

menubar=Menu(calc)

filemenu = Menu(menubar, tearoff=0, activebackground="orchid4", activeborder="2px")
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New",command=lambda:new())
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save as...")

filemenu.add_separator()
filemenu.add_command(label="Exit", command=iExit)

editmenu = Menu(menubar, tearoff=0, activebackground="orchid4", activeborder="2px")
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Undo")

editmenu.add_separator()

editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Delete",command=lambda:clear())
editmenu.add_command(label="Select All")

helpmenu = Menu(menubar, tearoff=0, activebackground="orchid4", activeborder="2px")
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Help Index",command=lambda:helpp())
helpmenu.add_command(label="About...",command=lambda:about())

root.config(menu=menubar)
root.mainloop()

