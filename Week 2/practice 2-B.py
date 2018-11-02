
# coding: utf-8

# In[ ]:


print ("1.dinar converter system")
print ("2.dolar converter system")
print ("3.turkish lira converter system")

choice = input("choose 1, 2 or 3:")

if choice == "1":
    print ("1.dinar to lira converter")
    print("2.dinar to dolar converter")
    
    choice2 = input("choose 1 or 2:")
    if choice2 == "1":
        dinar= float(input("enter the dinar currency:"))
        print(f"{dinar} dinar= {dinar*7.7711} turkish lira")
    elif choice2 == "2":
        dinar=float(input("enter the dinar currency:"))
        print (f"{dinar} dinar= {dinar*1.41} dolar")
    else:
        print("invalid choice")
        
elif choice == "2":
    print ("1.dolar to lira converter")
    print("2.dolar to dinar converter")
    
    choice3 = input("choose 1 or 2:")
    if choice3 == "1":
        dolar= float(input("enter the dolar currency:"))
        print(f"{dolar} Dolar=  {dolar*5.51} turkish lira")
    elif choice3 == "2":
        dolar=float(input("enter the dolar currency:"))
        print(f"{dolar} Dolar=  {dolar/1.41} dinar")
    else:
        print("invalid choice")

elif choice == "3":
    print ("1.lira to dinar converter")
    print("2.lira to dolar converter")
    
    choice4= input("choose 1 or 2:")
    if choice4 == "1":
        lira= float(input("enter the lira currency:"))
        print(f"{lira} lira= {lira*0.1287} dinar")
    elif choice4 == "2":
        lira=float(input("enter the lira currency:"))
        print(f"{lira} lira= {lira/5.51 } dolar")
    else:
        print("invalid choice")
else:
    print("invalid choice")


# In[ ]:





# In[ ]:




