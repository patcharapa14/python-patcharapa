try:
    weight = int(input("รับค่าน้ำหนัก"))
    high = int(input("รับค่าส่วนสูง"))
    bmi = weight/(high/100)**2
    
except:
    print("")