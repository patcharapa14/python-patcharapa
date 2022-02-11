def multiply(mul):
    for i in range(1,13):
        z=mul*i
        print(mul,"x",i,"=",z)
        
mul = int(input("รับค่าแม่สูตรคูณ"))
multiply(mul)
