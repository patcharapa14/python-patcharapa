f = open("myfile2.txt","w")
txt1="siam Dhurakit \n"
txt1 +="พัชราภา แก้วมา \n"
txt1 += "tel. 0953389486"

s = f.write(txt1)
f.close()

print("เขียนลงไฟล์แล้ว")