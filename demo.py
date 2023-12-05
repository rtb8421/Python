
a=input("Enter 1st number:")
b=input("Enter 2nd number")
c=input("choose operator (+,-,*,/,%):")

a=int(a)
b=int(b)
if c =="+":
    print (a+b)
    
elif c=="-":
    print (a-b)
    
elif c=="*":
    print (a*b)
    
elif c=="/":
    print (a/b)
    
elif c=="%":
    print (a%b)
    
else:
    print ("Invalid Operation")
    