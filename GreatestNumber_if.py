print("Enter three digit between 1 and 9")
a = int(input("Enter First digit:-"))
b = int(input("Enter Second digit:-"))
c = int(input("Enter Third digit:-"))

if((a>=b)and (a>=c)):
    if (b>=c):
        gn=100*a+10*b+c
        sn=100*c+10*b+a
    else:
        gn = 100*a+10*c+b
        sn = 100*b+10*c+a

if((b>=a)and (b>=c)):
    if(a>=c):
        gn=100*b+10*a+c
        sn=100*c+10*a+b
    else:
        gn = 100*b+10*c+a
        sn = 100*a+10*c+b
if((c>=a)and (c>=b)):
    if(a>=b):
        gn=100*c+10*a+b
        sn=100*b+10*a+c
    else:
        gn = 100*c+10*b+a
        sn = 100*a+10*b+c
print("The Greatest Number:",gn)
print("The Smallest Number:",sn)



        

      
