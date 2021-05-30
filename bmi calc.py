from tkinter import *
import tkinter.messagebox

class bmi:
    def __init__(self,root):
        self.root=root
        self.root.title("bmi calculator")
        self.root.geometry("600x490+0+0")
        self.root.config(bg="ghost white")

        name=StringVar()
        age=StringVar()
        weight=IntVar()
        height=IntVar()

        #functions

        def iexit():
            iexit=tkinter.messagebox.askyesno("BMI CALCULATOR","Do you want to exit")
            if iexit>0:
                root.destroy()
                return
        def cleardata():
            self.txtname.delete(0,END)
            self.txtage.delete(0,END)
            self.txtweight.delete(0,END)
            self.txtheight.delete(0,END)
            bmilist.delete(0,END)

        def submit():
            if len(name.get())!=0 and len(age.get())!=0 and len(str(height.get()))!=0 and len(str(weight.get()))!=0:
                if height.get()!=0 and weight.get()!=0:
                    result=weight.get()/(height.get()/100)**2
                    bmilist.delete(0,END)
                    bmilist.insert(0,(name.get()+", your bmi is "+ str(result)))
                else:
                    bmilist.insert(END,("enter a valid data"))
            else:
                bmilist.insert(0,"all fields are mandatory")
                
            
            
            

        

        mainframe=Frame(self.root,bg="cadet blue")
        mainframe.grid()

        titleframe=Frame(mainframe,bd=2,padx=50,pady=8,bg="ghost white",relief=RIDGE)
        titleframe.pack(side=TOP)

        self.lbltit=Label(titleframe,font=('arial',30,'bold'),text="BODY MASS INDEX",bg="ghost white")
        self.lbltit.grid()

        listframe=LabelFrame(mainframe,bd=1,width=570,height=110,padx=10,pady=10,bg="ghost white",font=('arial',20,'bold'),text="Your BMI is:",relief=RIDGE)
        listframe.pack(side=BOTTOM)

        buttonframe=Frame(mainframe,bd=2,width=450,height=50,padx=8,pady=10,bg="light grey",relief=RIDGE)
        buttonframe.pack(side=BOTTOM)
        
        dataframe=Frame(mainframe,bd=1,width=450,height=200,padx=10,pady=10,bg="cadet blue",relief=RIDGE)
        dataframe.pack(side=BOTTOM)

        infoframe=LabelFrame(dataframe,bd=1,width=450,height=200,padx=10,pady=10,bg="ghost white",font=('arial',20,'bold'),text="Personal Info",relief=RIDGE)
        infoframe.pack(side=TOP)
       

        #buttons

        self.btncalc=Button(buttonframe,text="Submit",font=('arial',20,'bold'),height=1,width=11,bd=1,command=submit)
        self.btncalc.grid(row=0,column=0)

        self.btnclear=Button(buttonframe,text="Clear",font=('arial',20,'bold'),height=1,width=11,bd=1,command=cleardata)
        self.btnclear.grid(row=0,column=1)

        self.btnexit=Button(buttonframe,text="Exit",font=('arial',20,'bold'),height=1,width=11,bd=1,command=iexit)
        self.btnexit.grid(row=0,column=2)

        #label and entry
        self.lblname=Label(infoframe,font=('arial',20,'bold'),text="Name:",padx=2,pady=2,bg="ghost white")
        self.lblname.grid(row=0,column=0,sticky=W)
        self.txtname=Entry(infoframe,font=('arial',20,'bold'),textvariable=name,width=23,bg="ghostwhite")
        self.txtname.grid(row=0,column=1,sticky=W)

        self.lblage=Label(infoframe,font=('arial',20,'bold'),text="Age:",padx=2,pady=2,bg="ghost white")
        self.lblage.grid(row=1,column=0,sticky=W)
        self.txtage=Entry(infoframe,font=('arial',20,'bold'),textvariable=age,width=23,bg="ghostwhite")
        self.txtage.grid(row=1,column=1,sticky=W)

        self.lblheight=Label(infoframe,font=('arial',20,'bold'),text="Height(in cms):",padx=2,pady=2,bg="ghost white")
        self.lblheight.grid(row=2,column=0,sticky=W)
        self.txtheight=Entry(infoframe,font=('arial',20,'bold'),textvariable=height,width=23,bg="ghostwhite")
        self.txtheight.grid(row=2,column=1,sticky=W)

        self.lblweight=Label(infoframe,font=('arial',20,'bold'),text="Weight(in kgs):",padx=2,pady=2,bg="ghost white")
        self.lblweight.grid(row=3,column=0,sticky=W)
        self.txtweight=Entry(infoframe,font=('arial',20,'bold'),textvariable=weight,width=23,bg="ghostwhite")
        self.txtweight.grid(row=3,column=1,sticky=W)

        #list

        bmilist=Listbox(listframe,width=60,height=2,font=('arial',12,'bold'))
        bmilist.grid(row=0,column=0,padx=10)

        

        
root=Tk()
application=bmi(root)
root.mainloop()
#sample
