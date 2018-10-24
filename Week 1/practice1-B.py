
# coding: utf-8

# In[9]:

#either if x is an integer the best data type for f(x) is float, it is more acuurate to consider the decimals since the function contains some calculations that will result in fractions.
x= float(input("enter your number:"))
if x < -100:
    print(-x)
elif x <= -25 and x >= -100:
    print(x**4)
elif x <= 0 and x >= -25:
    print(3*x**2-1)
elif x > 0 and x <= 100:
    print(3.14/2*x+3**x)
else:
    print(x)
    

