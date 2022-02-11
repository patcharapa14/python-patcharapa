def triangle():
    b = int(base.get())
    h = int(high.get())
    a =1/2*b*h
    messagebox.showinfo("","คำตอบ %.2f" % area)
    area.set(a)

from tkinter import *
main = Tk()
main.geometry("800x600")
main.title("โปรแกรมหาพื้นที่สามเหลี่ยม โดย พัชราภา แก้วมา")
base = StringVar()
high = StringVar()
area = StringVar()

Ib1 = Label(main, text="รับค่าฐาน:", font=("Tahoma",20))
Ib1.place(x=20, y=20)
tb1 = Entry(main, textvariable= base)
tb1.place(x=200, y=30, width=300, height=40)


Ib2 = Label(main, text="รับค่าสูง:", font=("Tahoma",18))
Ib2.place(x=20, y=80)
tb2 = Entry(main, textvariable= base)
tb2.place(x=200, y=80, width=300, height=40)

btn = Button(main, text="คำนวณ",font=("Tahoma",18), command= triangle)
btn.place(x=200, y=150)

Ib3 = Label(main, text="คำตอบ:", font=("Tahoma",18))
Ib3.place(x=20, y=200)

Ib4 = Label(main, font=("Tahoma",18), textvariable=area)
Ib4.place(x=200, y=250)

main.mainloop()

