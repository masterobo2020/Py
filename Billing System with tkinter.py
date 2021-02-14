from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("1350x700+0+0")
root.title("Billing System")
bg_color="#074463"
title=Label(root, text="Restaurant Management System", font=('times new roman', 30, 'bold'), bd=12, relief=GROOVE, bg=bg_color, fg="white", pady=2).pack(fill=X)
# ------------------- Variables -------------------
# ------------------- Customer -------------------
def total():
    to = ((soap.get()*40))
    cos_price= (to)
    
soap = IntVar()
face_cream = IntVar()
face_wash = IntVar()
spray = IntVar()
gel = IntVar()
lotion = IntVar()
# ------------------- Grocery -------------------
rice = IntVar()
food = IntVar()
dal = IntVar()
wheat = IntVar()
sugar = IntVar()
tea = IntVar()
# ------------------- Cold-Drink -------------------
mazza = IntVar()
coke = IntVar()
frooti = IntVar()
thums = IntVar()
limca = IntVar()
sprite = IntVar()
# ------------------- Total price & tax ---------------------
cos_price = IntVar()
groc_price = StringVar()
col_price = StringVar()

cos_tax = StringVar()
groc_tax = StringVar()
col_tax = StringVar()
# ------------------- Customer ---------------------
c_name = StringVar()
c_phone = StringVar()
bill_no = StringVar()
search_bill = StringVar()

# ------------------- Customer Details Frame -------------------
f1 = LabelFrame(root, text="Customer Details", bd=10, relief = GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
f1.place(x=0 , y=70, relwidth=1)
c_name = Label(f1, text="Customer Name", bg=bg_color, fg="white", font = ("times new roman" , 15 , "bold")).grid(row=0 , column=0 , padx=20 , pady=5)
c_name_txt = Entry(f1, width = 15, font = "arial 15" , bd=7 , textvariable=c_name , relief = SUNKEN).grid(row = 0 , column = 1 , pady = 5 , padx = 10)

c_phn = Label(f1, text=" Phone No. ", bg=bg_color, fg="white", font = ("times new roman" , 15 , "bold")).grid(row=0 , column=2 , padx=20 , pady=5)
c_phn_txt = Entry(f1, width = 15, font = "arial 15" , bd=7 , textvariable=c_phone, relief = SUNKEN).grid(row = 0 , column = 3 , pady = 5 , padx = 10)

c_bill = Label(f1, text="Address", bg=bg_color, fg="white", font = ("times new roman" , 15 , "bold")).grid(row=0 , column=4 , padx=20 , pady=5)
c_bill_txt = Entry(f1, width = 15, font = "arial 15" , bd=7 ,textvariable=bill_no,  relief = SUNKEN).grid(row = 0 , column = 5 , pady = 5 , padx = 10)

bill_btn = Button(f1, text="Submit" , width=10 , bd=7 , font="arial 12 bold").grid(row = 0 , column = 6 , pady = 10 , padx = 10)

# ------------------- Cosmetics Frame -------------------
f2 = LabelFrame(root, text="Cosmetics", bd=10, relief = GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
f2.place(x=0 , y=170, width=325, height=350)
ba_la=Label(f2, text="Bath Soap", font=("times new roman" , 16 , "bold"), bg=bg_color, fg = "lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
ba_txt = Entry(f2, width = 15, font = "arial 10" , bd=5 , textvariable=soap, relief = SUNKEN).grid(row = 0 , column = 1 , pady = 10 , padx = 10)

fa_la=Label(f2, text="Face Cream", font=("times new roman" , 16 , "bold"), bg=bg_color, fg = "lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
fa_txt = Entry(f2, width = 15, font = "arial 10" , bd=5 , textvariable=face_cream, relief = SUNKEN).grid(row = 2 , column = 1 , pady = 10 , padx = 10)

fa_wa_la=Label(f2, text="Face Wash", font=("times new roman" , 16 , "bold"), bg=bg_color, fg = "lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
fa_wa_txt = Entry(f2, width = 15, font = "arial 10" , bd=5 , textvariable=face_wash, relief = SUNKEN).grid(row = 4 , column = 1 , pady = 10 , padx = 10)

ha_sp=Label(f2, text="Hair Spray", font=("times new roman" , 16 , "bold"), bg=bg_color, fg = "lightgreen").grid(row=6,column=0,padx=10,pady=10,sticky="w")
ha_txt = Entry(f2, width = 15, font = "arial 10" , bd=5 , textvariable=spray, relief = SUNKEN).grid(row = 6 , column = 1 , pady = 10 , padx = 10)

ha_ge_sp=Label(f2, text="Hair Gel", font=("times new roman" , 16 , "bold"), bg=bg_color, fg = "lightgreen").grid(row=8,column=0,padx=10,pady=10,sticky="w")
ha_ge_txt = Entry(f2, width = 15, font = "arial 10" , bd=5 , textvariable=gel, relief = SUNKEN).grid(row = 8 , column = 1 , pady = 10 , padx = 10)

bo_fa_la=Label(f2, text="Body Lotion", font=("times new roman" , 16 , "bold"), bg=bg_color, fg = "lightgreen").grid(row=10,column=0,padx=10,pady=10,sticky="w")
bo_txt = Entry(f2, width = 15, font = "arial 10" , bd=5 , textvariable=lotion, relief = SUNKEN).grid(row = 10 , column = 1 , pady = 10 , padx = 10)

# ------------------- Grocery Frame -------------------
f3 = LabelFrame(root, text="Grocery", bd=10, relief = GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
f3.place(x=325 , y=170, width=325, height=350)
ri=Label(f3, text="Rice", font=("times new roman" , 16 , "bold"), bg=bg_color, fg = "lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
ri_txt = Entry(f3, width = 15, font = "arial 10" , textvariable=rice, bd=5 , relief = SUNKEN).grid(row = 0 , column = 1 , pady = 10 , padx = 10)

fo=Label(f3, text="Food Oil", font=("times new roman" , 16 , "bold"), bg=bg_color, fg = "lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
fo_txt = Entry(f3, width = 15, font = "arial 10" , bd=5 , textvariable=food, relief = SUNKEN).grid(row = 2 , column = 1 , pady = 10 , padx = 10)

da=Label(f3, text="Dal", font=("times new roman" , 16 , "bold"), bg=bg_color, fg = "lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
da_txt = Entry(f3, width = 15, font = "arial 10" , bd=5 , textvariable=dal, relief = SUNKEN).grid(row = 4 , column = 1 , pady = 10 , padx = 10)

whe=Label(f3, text="Wheat", font=("times new roman" , 16 , "bold"), bg=bg_color, fg = "lightgreen").grid(row=6,column=0,padx=10,pady=10,sticky="w")
whe_txt = Entry(f3, width = 15, font = "arial 10" , bd=5 , textvariable=wheat, relief = SUNKEN).grid(row = 6 , column = 1 , pady = 10 , padx = 10)

su=Label(f3, text="Sugar", font=("times new roman" , 16 , "bold"), bg=bg_color, fg = "lightgreen").grid(row=8,column=0,padx=10,pady=10,sticky="w")
su_txt = Entry(f3, width = 15, font = "arial 10" , bd=5 , textvariable=sugar, relief = SUNKEN).grid(row = 8 , column = 1 , pady = 10 , padx = 10)

tea=Label(f3, text="Tea", font=("times new roman" , 16 , "bold"), bg=bg_color, fg = "lightgreen").grid(row=10,column=0,padx=10,pady=10,sticky="w")
tea_txt = Entry(f3, width = 15, font = "arial 10" , bd=5 , textvariable=tea, relief = SUNKEN).grid(row = 10 , column = 1 , pady = 10 , padx = 10)

# ------------------- Cold Drink Frame -------------------
f3 = LabelFrame(root, text="Cold Drink", bd=10, relief = GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
f3.place(x=650 , y=170, width=325, height=350)
ma=Label(f3, text="Mazza", font=("times new roman" , 16 , "bold"), bg=bg_color, fg = "lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
ma_txt = Entry(f3, width = 15, font = "arial 10" , bd=5 , textvariable=mazza,relief = SUNKEN).grid(row = 0 , column = 1 , pady = 10 , padx = 10)

co=Label(f3, text="Coke", font=("times new roman" , 16 , "bold"), bg=bg_color, fg = "lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
co_txt = Entry(f3, width = 15, font = "arial 10" , bd=5 , textvariable=coke,relief = SUNKEN).grid(row = 2 , column = 1 , pady = 10 , padx = 10)

fro=Label(f3, text="Frotti", font=("times new roman" , 16 , "bold"), bg=bg_color, fg = "lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
fro_txt = Entry(f3, width = 15, font = "arial 10" , bd=5 , textvariable=frooti,relief = SUNKEN).grid(row = 4 , column = 1 , pady = 10 , padx = 10)

thu=Label(f3, text="Thums UP", font=("times new roman" , 16 , "bold"), bg=bg_color, fg = "lightgreen").grid(row=6,column=0,padx=10,pady=10,sticky="w")
thu_txt = Entry(f3, width = 15, font = "arial 10" , bd=5 , textvariable=thums,relief = SUNKEN).grid(row = 6 , column = 1 , pady = 10 , padx = 10)

li=Label(f3, text="Limca", font=("times new roman" , 16 , "bold"), bg=bg_color, fg = "lightgreen").grid(row=8,column=0,padx=10,pady=10,sticky="w")
li_txt = Entry(f3, width = 15, font = "arial 10" , bd=5 , textvariable=limca,relief = SUNKEN).grid(row = 8 , column = 1 , pady = 10 , padx = 10)

sp=Label(f3, text="Sprite", font=("times new roman" , 16 , "bold"), bg=bg_color, fg = "lightgreen").grid(row=10,column=0,padx=10,pady=10,sticky="w")
sp_txt = Entry(f3, width = 15, font = "arial 10" , bd=5 , textvariable=sprite,relief = SUNKEN).grid(row = 10 , column = 1 , pady = 10 , padx = 10)

# ------------------- Bill Area Frame -------------------
bill=Frame(root, bd=10, relief=GROOVE)
bill.place(x=970 , y=170 , width=310 , height=350)

bill_ti=Label(bill, text = "BILL AREA", font = "arial 15 bold", bd = 7, relief = GROOVE).pack(fill = X)
scroll_y=Scrollbar(bill, orient=VERTICAL)
text_area = Text(bill, yscrollcommand = scroll_y.set)
scroll_y.pack(side=RIGHT , fill = Y)
scroll_y.config(command=text_area.yview)
text_area.pack(fill=BOTH , expand=1)

# ------------------- Button Frame -------------------
f6 = LabelFrame(root, text="Billing Menu", bd=10, relief = GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
f6.place(x=0 , y=520, relwidth=1, height=140)
    
m1 = Label(f6 , text = "Total Cosmetic Price" , font=("times new roman" , 14 , "bold") , bg=bg_color , fg="white").grid(row = 0 , column = 0 , pady = 1 , padx = 20 , sticky="w")
m1_txt = Entry(f6 , width=18 , font = "arial 10 bold" , bd=7 , textvariable=cos_price,relief=SUNKEN).grid(row=0 , column=1 , padx=10 , pady=1)


m2 = Label(f6 , text = "Total Grocery Price" , font=("times new roman" , 14 , "bold") , bg=bg_color , fg="white").grid(row = 1 , column = 0 , pady = 1 , padx = 20 , sticky="w")
m2_txt = Entry(f6 , width=18 , font = "arial 10 bold" , bd=7 , textvariable=groc_price,relief=SUNKEN).grid(row=1 , column=1 , padx=10 , pady=1)

m3 = Label(f6 , text = "Total Cold-Drink Price" , font=("times new roman" , 14 , "bold") , bg=bg_color , fg="white").grid(row = 2 , column = 0 , pady = 1 , padx = 20 , sticky="w")
m3_txt = Entry(f6 , width=18 , font = "arial 10 bold" , bd=7 , textvariable=col_price,relief=SUNKEN).grid(row=2 , column=1 , padx=10 , pady=1)

m4 = Label(f6 , text = "Cosmetic Tax" , font=("times new roman" , 14 , "bold") , bg=bg_color , fg="white").grid(row = 0 , column = 2 , pady = 1 , padx = 20 , sticky="w")
m4_txt = Entry(f6 , width=18 , font = "arial 10 bold" , bd=7 , textvariable=cos_tax,relief=SUNKEN).grid(row=0 , column=3 , padx=10 , pady=1)

m5 = Label(f6 , text = "Grocery Tax" , font=("times new roman" , 14 , "bold") , bg=bg_color , fg="white").grid(row = 1 , column = 2 , pady = 1 , padx = 20 , sticky="w")
m5_txt = Entry(f6 , width=18 , font = "arial 10 bold" , bd=7 , textvariable=groc_tax,relief=SUNKEN).grid(row=1 , column=3 , padx=10 , pady=1)

m6 = Label(f6 , text = "Cold-Drink Tax" , font=("times new roman" , 14 , "bold") , bg=bg_color , fg="white").grid(row = 2 , column = 2 , pady = 1 , padx = 20 , sticky="w")
m6_txt = Entry(f6 , width=18 , font = "arial 10 bold" , bd=7 , textvariable=col_tax,relief=SUNKEN).grid(row=2 , column=3 , padx=10 , pady=1)

f6a = Frame(root, bd=7, relief = GROOVE)
f6a.place(x=760 , y=545, height=100,width=500)

command=total
tt_bt = Button(f6a, text="Total" , bg="cadetblue" , fg="white" ,pady=15, width=10 , font = "arial 12 bold" , command=total).grid(row = 0 , column = 0 , padx=5 , pady = 5)
G_bt = Button(f6a, text="Generate Bill" , bg="cadetblue" , fg="white" ,pady=15, width=10 , font = "arial 12 bold").grid(row = 0 , column = 1 , padx=5 , pady = 5)
cl_bt = Button(f6a, text="Clear" , bg="cadetblue" , fg="white" ,pady=15, width=10 , font = "arial 12 bold").grid(row = 0 , column = 2 , padx=5 , pady = 5)
ex_bt = Button(f6a, text="Exit" , bg="cadetblue" , fg="white" ,pady=15, width=10 , font = "arial 12 bold").grid(row = 0 , column = 3 , padx=5 , pady = 5)


root.mainloop()
