email = input("Enter Your Email : ") #g@g.in, shub@gmail.com
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():  # first leter alphabet
        if ("@"in email) and (email.count("@")==1): # one @
            if (email[-4]==".") ^ (email[-3]=="."): # "." -3rd or -4 position [xor sign "^" only one conditionn corfrect]
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            J=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("Wrong Email - 5")
                else:
                    print("Thank you for correcting all the conditions.")
            else:
                print("Wrong Email - 4")
        else:
            print("Wrong Email - 3")
    else:
        print("Wrong Eemail - 2")
else:
    print("Wrong Email - 1")