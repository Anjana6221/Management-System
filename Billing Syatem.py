from tkinter import *
from tkinter import messagebox
from pymysql import *
import mysql.connector

def Done():
    Customer_Name=StringVar()
    Total_bill=IntVar()
    

    top=Toplevel()
    top.title("Thank You")
    top.geometry('1000x700')
    top.config(bg="white")
    top.resizable(1,1)
    global pic5

    l=Label(top,text='Thank You!',bg="White",fg="Black",font=("Gabriola",100,"bold")).pack()

    l=Label(top,text="For your order,and for",bg="White",fg="Black",font=("Comic Sans MS",30)).pack()
    l=Label(top,text="supporting my small business!",bg="White",fg="Black",font=("Comic Sans MS",30)).pack()
    l=Label(top,text="Every order is baked with love, enjoy!",bg="white",fg="black",font=("Monotype Corsiva",45)).pack()

    
    pic5=PhotoImage(file=r"C:\Users\Rohan\Downloads\kk.png")
    Label(top,text="Images",image=pic5,pady=20,bd=0).pack()    

    

def login():
    user=username.get()
    code=password.get()

    if user=="Anjana" and code=="6221":
        root=Toplevel(screen)
        root.title("Billing System")
        root.geometry("1500x780")
        root.configure(bg="white")
        root.resizable(0,0)


        def Reset():
            entry_Pinepapple.delete(0,END)
            entry_BlackForest.delete(0,END)
            entry_ChocolateTruffle.delete(0,END)
            entry_Strawberry.delete(0,END)
            entry_FruitCake.delete(0,END)
            entry_RasgullaCake.delete(0,END)
            entry_RasmalaiCake.delete(0,END)
            entry_MangoCake.delete(0,END)
            entry_DollCake.delete(0,END)
            entry_RainbowCake.delete(0,END)


        def Total():

            totalcost=IntVar()

            try:a1=int(Pinepapple.get())
            except: a1=0

            try:a2=int(BlackForest.get())
            except: a2=0

            try:a3=int(ChocolateTruffle.get())
            except: a3=0

            try:a4=int(Strawberry.get())
            except: a4=0

            try:a5=int(FruitCake.get())
            except: a5=0

            try:a6=int(RasgullaCake.get())
            except: a6=0

            try:a7=int(RasmalaiCake.get())
            except: a7=0

            try:a8=int(MangoCake.get())
            except: a8=0

            try:a9=int(DollCake.get())
            except: a9=0

            try:a10=int(RainbowCake.get())
            except: a10=0
              

##            

            c1=380*a1
            c2=400*a2
            c3=450*a3
            c4=480*a4
            c5=500*a5
            c6=580*a6
            c7=600*a7
            c8=650*a8
            c9=1200*a9
            c10=1200*a10

            


            lbl_total=Label(f2,font=("Cooper Black",30),text="Total",width=14,fg="saddlebrown",bg="peachpuff")
            lbl_total.place(x=0,y=195)
            entry_total=Entry(f2,font=("Monotype Corsiva",30,"bold"),textvariable=Total_bill,bd=6,width=14,bg="indianred")
            entry_total.place(x=70,y=250)
            
            lbl_CustomerName=Label(f2,font=("Cooper Black",30),text="Customer Name",width=14,fg="saddlebrown",bg="peachpuff")
            lbl_CustomerName.place(x=0,y=80)
            entry_CustomerName=Entry(f2,font=("Monotype Corsiva",30,"bold"),textvariable=Customer_Name,bd=6,width=16,bg="indianred")
            entry_CustomerName.place(x=50,y=130)
            
            mydb = connect(host="localhost",user="root",password="anjana@6621",database="bill")
            my_cur=mydb.cursor()
            my_cur.execute("use bill;")
            my_cur.execute("select * from Cake_Shop;")


            totalcost=c1+c2+c3+c4+c5+c6+c7+c8+c9+c10
            string_bill="Rs.",str("%.2f"%totalcost)
            Total_bill.set(string_bill)

            my_cur.execute("insert into Cake_Shop (Customer_Name,Total) values ('{}',{});".format(Customer_Name.get(),totalcost))
            mydb.commit()
            mydb.close()

            btn_total=Button(f2,bd=2,fg="Black",bg="brown",font=("Gabriola",16,"bold"),width=10,text="Done!",command=Done)
            btn_total.place(x=137,y=325)

            

        global pic2
        global pic3
        global pic4
        Customer_Name=StringVar()
        
        Label(root,text="Billing System",bg="White",fg="black",font=("Script MT Bold",50)).pack(fill="both")
        
        Label(root,text="Customer Name",bg="pink",fg="Black",font=("Lucida Handwriting",16,"bold")).place(x=530,y=120)
        entry=Entry(root,font=("Lucida Handwriting",15,"bold"),textvariable=Customer_Name,bd=2,width=17,bg="peachpuff").place(x=755,y=120)


        pic2=PhotoImage(file=r"C:\Users\Rohan\Downloads\photo1.png")
        Label(root,text="Images",image=pic2).place(x=22,y=30)

        pic3=PhotoImage(file=r"C:\Users\Rohan\Downloads\ccc.png")
        Label(root,text="Images",image=pic3).place(x=995,y=575)

        pic4=PhotoImage(file=r"C:\Users\Rohan\Downloads\bill.png")
        Label(root,text="Images",image=pic4).place(x=1023,y=12)



        ##Menucard

        f=Frame(root,bg="Light Pink",highlightbackground="grey",highlightthickness=3,width=500,height=530)
        f.place(x=25,y=190)

        Label(f,text="Cakes",font=("Gabriola",40,"bold"),fg="black",bg="Light Pink").place(x=30,y=0)
        Label(f,text="1/2kg",font=("Gabriola",35,"bold"),fg="black",bg="Light Pink").place(x=370,y=0)


        Label(f,font=("french Script MT",28,"bold"),text="Pinepapple                         380 ",fg="black",bg="Light Pink").place(x=10,y=75)
        Label(f,font=("french Script MT",28,"bold"),text="Black Forest                      400 ",fg="black",bg="Light Pink").place(x=10,y=120)
        Label(f,font=("french Script MT",28,"bold"),text="Chocolate Truffle                  450 ",fg="black",bg="Light Pink").place(x=10,y=165)
        Label(f,font=("french Script MT",28,"bold"),text="Strawberry                         480 ",fg="black",bg="Light Pink").place(x=10,y=210)
        Label(f,font=("french Script MT",28,"bold"),text="Fruit Cake                         500 ",fg="black",bg="Light Pink").place(x=10,y=255)
        Label(f,font=("french Script MT",28,"bold"),text="Rasgulla Cake                    580 ",fg="black",bg="Light Pink").place(x=10,y=300)
        Label(f,font=("french Script MT",28,"bold"),text="Rasmalai Cake                    600 ",fg="black",bg="Light Pink").place(x=10,y=345)
        Label(f,font=("french Script MT",28,"bold"),text="Mango Cake                      650 ",fg="black",bg="Light Pink").place(x=10,y=390)
        Label(f,font=("french Script MT",28,"bold"),text="Doll Cake                        1200 ",fg="black",bg="Light Pink").place(x=10,y=435)
        Label(f,font=("french Script MT",28,"bold"),text="Rainbow Cake                   1200 ",fg="black",bg="Light Pink").place(x=10,y=476)


        #bill

        f2=Frame(root,bg="peachpuff",highlightbackground="grey",highlightthickness=1,width=400,height=420)
        f2.place(x=1045,y=150)

        Bill=Label(f2,text="Bill",font=("Lucida Handwriting",25,"bold"),bg="peachpuff")
        Bill.place(x=150,y=25)

        ####
        
        f1=Frame(root,bg="bisque",highlightbackground="grey",highlightthickness=1,width=450,height=595,relief=RAISED)
        f1.place(x=535,y=170)

        Pinepapple=IntVar()
        BlackForest=IntVar()
        ChocolateTruffle=IntVar()
        Strawberry=IntVar()
        FruitCake=IntVar()
        RasgullaCake=IntVar()
        RasmalaiCake=IntVar()
        MangoCake=IntVar()
        DollCake=IntVar()
        RainbowCake=IntVar()
        Total_bill=IntVar()
        
        

        ####
        lbl_Pinepapple=Label(f1,font=("Script MT Bold",25,"bold"),text="Pinepapple",width=12,fg="brown",bg="bisque")
        lbl_BlackForest=Label(f1,font=("Script MT Bold",25,"bold"),text="Black Forest",width=12,fg="brown",bg="bisque")
        lbl_ChocolateTruffle=Label(f1,font=("Script MT Bold",25,"bold"),text="Chocolate Truffle",width=12,fg="brown",bg="bisque")
        lbl_Strawberry=Label(f1,font=("Script MT Bold",25,"bold"),text="Strawberry",width=12,fg="brown",bg="bisque")
        lbl_FruitCake=Label(f1,font=("Script MT Bold",25,"bold"),text="Fruit Cake",width=12,fg="brown",bg="bisque")
        lbl_RasgullaCake=Label(f1,font=("Script MT Bold",25,"bold"),text="Rasgulla Cake",width=12,fg="brown",bg="bisque")
        lbl_RasmalaiCake=Label(f1,font=("Script MT Bold",25,"bold"),text="Rasmalai Cake",width=12,fg="brown",bg="bisque")
        lbl_MangoCake=Label(f1,font=("Script MT Bold",25,"bold"),text="Mango Cake",width=12,fg="brown",bg="bisque")
        lbl_DollCake=Label(f1,font=("Script MT Bold",25,"bold"),text="Doll Cake",width=12,fg="brown",bg="bisque")
        lbl_RainbowCake=Label(f1,font=("Script MT Bold",25,"bold"),text="Rainbow Cake",width=12,fg="brown",bg="bisque")

        lbl_Pinepapple.place(x=20,y=19)
        lbl_BlackForest.place(x=20,y=62)
        lbl_ChocolateTruffle.place(x=20,y=112)
        lbl_Strawberry.place(x=20,y=157)
        lbl_FruitCake.place(x=20,y=203)
        lbl_RasgullaCake.place(x=20,y=249)
        lbl_RasmalaiCake.place(x=20,y=297)
        lbl_MangoCake.place(x=20,y=343)
        lbl_DollCake.place(x=20,y=391)
        lbl_RainbowCake.place(x=20,y=437)

        #####

        entry_Pinepapple=Entry(f1,font=("Script MT Bold",25,"bold"),textvariable=Pinepapple,bd=3,width=5,bg="lightcoral")
        entry_BlackForest=Entry(f1,font=("Script MT Bold",25,"bold"),textvariable=BlackForest,bd=3,width=5,bg="lightcoral")
        entry_ChocolateTruffle=Entry(f1,font=("Script MT Bold",25,"bold"),textvariable=ChocolateTruffle,bd=3,width=5,bg="lightcoral")
        entry_Strawberry=Entry(f1,font=("Script MT Bold",25,"bold"),textvariable=Strawberry,bd=3,width=5,bg="lightcoral")
        entry_FruitCake=Entry(f1,font=("Script MT Bold",25,"bold"),textvariable=FruitCake,bd=3,width=5,bg="lightcoral")
        entry_RasgullaCake=Entry(f1,font=("Script MT Bold",25,"bold"),textvariable=RasgullaCake,bd=3,width=5,bg="lightcoral")
        entry_RasmalaiCake=Entry(f1,font=("Script MT Bold",25,"bold"),textvariable=RasmalaiCake,bd=3,width=5,bg="lightcoral")
        entry_MangoCake=Entry(f1,font=("Script MT Bold",25,"bold"),textvariable=MangoCake,bd=3,width=5,bg="lightcoral")
        entry_DollCake=Entry(f1,font=("Script MT Bold",25,"bold"),textvariable=DollCake,bd=3,width=5,bg="lightcoral")
        entry_RainbowCake=Entry(f1,font=("Script MT Bold",25,"bold"),textvariable=RainbowCake,bd=3,width=5,bg="lightcoral")

        entry_Pinepapple.place(x=320,y=18)
        entry_BlackForest.place(x=320,y=65)
        entry_ChocolateTruffle.place(x=320,y=112)
        entry_Strawberry.place(x=320,y=159)
        entry_FruitCake.place(x=320,y=206)
        entry_RasgullaCake.place(x=320,y=253)
        entry_RasmalaiCake.place(x=320,y=300)
        entry_MangoCake.place(x=320,y=347)
        entry_DollCake.place(x=320,y=394)
        entry_RainbowCake.place(x=320,y=441)



        #### button

        btn_reset=Button(f1,bd=5,fg="Black",bg="indianred",font=("Gabriola",16,"bold"),width=10,text="Reset",command=Reset)
        btn_reset.place(x=80,y=500)

        btn_total=Button(f1,bd=5,fg="Black",bg="indianred",font=("Gabriola",16,"bold"),width=10,text="Total",command=Total)
        btn_total.place(x=280,y=500)
        
        
    elif user=="" and code=="":
        messagebox.showerror("Invalid","Please enter username and password")
    elif user=="":
        messagebox.showerror("Invalid","Please enter username")
    elif code=="":
        messagebox.showerror("Invalid","Please enter password")
    elif user=="Anjana" and code!="6221":
        messagebox.showerror("Invalid","Invalid password")
    elif user!="Anjana" and code=="6221":
        messagebox.showerror("Invalid","Invalid username")
    elif user!="Anjana" and code!="6221":
        messagebox.showerror("Invalid","Invalid username and password")

def main_screen():

    global screen
    global username
    global password
    global pic1
    
    screen=Tk()
    screen.geometry("1000x700")
    screen.configure(bg="aquamarine")
    screen. title("Login Page")
    screen.resizable(0,0)

    
    lbltitle=Label(text="THE BAKING GIRL",bg="White",fg="Black",font=("Times New Roman",60,"bold"))
    lbltitle.pack(fill="both")

    pic1=PhotoImage(file=r"C:\Users\Rohan\Downloads\photo.png")
    Label(screen,text="Images",image=pic1,pady=20).place(x=40,y=140)

    bordercolor=Frame(screen,bg="aquamarine",width=420,height=520)
    bordercolor.place(x=560,y=140)

    mainframe=Frame(bordercolor,bg="aquamarine",width=420,height=520)
    mainframe.pack()

    Label(mainframe,text="Username",font=("Cambria",30,"bold"),bg="aquamarine").place(x=110,y=5)
    Label(mainframe,text="Password",font=("Cambria",30,"bold"),bg="aquamarine").place(x=115,y=180)

    username=StringVar()
    password=StringVar()

    entry_username=Entry(mainframe,textvariable=username,width=18,bd=1,font=("Times New Roman",30,"bold"))
    entry_username.place(x=40,y=95)
    entry_password=Entry(mainframe,textvariable=password,width=18,bd=1,font=("Times New Roman",30,"bold"),show="*")
    entry_password.place(x=40,y=275)

    def reset():
        entry_username.delete(0,END)
        entry_password.delete(0,END)


    Button(mainframe,text="Login",font=("Times New Roman",15,"bold"),command=login,height=2,width=12,bd=2).place(x=30,y=380)
    Button(mainframe,text="Reset",font=("Times New Roman",15,"bold"),command=reset,height=2,width=12,bd=2).place(x=230,y=380)




main_screen()
screen.mainloop()
