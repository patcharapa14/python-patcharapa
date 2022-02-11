def cal():
    r = tb1.get()
    circle = (22/7)*r*r
    mesagebox.showinfo("พื้นที่วงกลม","ผลลัพธ์ %.2f" %circle)
    result.set(circle)

from tkinter import *
window = Tk()
window.geometry("800x500")
window.title("โดย พัชราภา แก้วมา")

result = stringVar()

lb = Label(window , text="ยินดีต้อนรับสู่ python", font=("freesiaUPC",24))
lb.place(x=50,y=10)


lb2 = Label(window , text="รับค่ารัศมี",font=("freesiaUPC",24))
lb2.place(x=50, y=100)

tb1 = Entry(window)
tb1.place(x=180, y=110, width=200, height=30)

lb3 =Label(window , text="ผลลัพธ์", font=("freesiaUPC",24))
tb1.place(x=50, y=150)

tb2 = Entry()
tb2.place(x=180, y=170, width=200, height=30)

btn = Button(window, text="ผลลัพธ์", font=("freesiaUPC",24))
btn.place(x=400, y=100)

btn = Button(window, text="คำนวณ", font=("freesiaUPC",24),command=cal)
btn.place(x=370, y=100)

window.mainloop()

