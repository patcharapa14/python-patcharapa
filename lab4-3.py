def vat(price):
    v = price*(7/100)
    return v

def disc(price):
    d = price*(10/100)
    return d
    
def total(price, vat, disc):
    t = price+vat-disc
    return t

price = int(input("ราคาสินค้า"))
print("ภาษีมูลค่าเพิ่ม ",vat(price))
print("ส่วนลด ", disc(price))
print("ราคารวม", total(price, vat(price), disc(price)))

