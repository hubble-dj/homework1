#Start of homework 3 work
def say_goodbye(name):
    print("Sayonara,", name)

name = ("Danial") 

#say_goodbye(name)

# Area of a Circle

def give_circle_area(radius):
    return ((radius**2)*3.14)

#print(give_circle_area(2))

#Return Functions

def subtract(a,b):
    return a - b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

# Conditionals 

def temp_huh(list):
    return((min(list),max(list)))

list = [20, 40, 50, 80, 120]
#print(temp_huh(list))

# nani nichi desu ka? 

def is_weekend(daynumber):
    if daynumber <= 5:
        return "False"
    elif 5 < daynumber <= 7:
        return "True"
    else:
        return "Dumbass" 

# Fuel Efficiency Calculator 

def mpg(distance,fuel):
    return(distance/fuel)

# Secret Code 

def JamesBond(code):
    key = code 
    #finds last digit and removes it from current code you're trying to encrypt 
    last = key % 10
    key -= last
    #Finds how many times you need to multiply by 10
    expo = 0 
    while key > 10:
        key //=10
        expo += 1
    #Moves over the code one to the right
    code //= 10
    return code + (last * 10 ** expo) 
  

#print(JamesBond(1234567)) # yayyyyyyyy

# Loops

def yoink(x,y): #Makeshift exponential 
    r = x
    if y == 0:
        return 1
    elif y <= 0:
        return "Below my paygrade bub"
    else:
        for i in range (1, y):
            x *= r
    return(x)

#print(yoink(5,-1))

#Min and Max

def newmin(list):
    n=len(list)
    i=0
    value=list[i]
    for i in range(n):
        if list[i] < value:
            value = list[i]
    return(value)

#print(newmin([100,4,5,2, 5, 1]))

def newmax(list):
    n=len(list)
    i=0
    value=list[i]
    for i in range(n):
        if list[i] > value: 
            value = list[i]
    return(value)


#print(newmax([3,4,5,299, 5]))

#Same thing but while loops??

def whilemin(list):
    n = len(list)
    x = 0
    t = 0
    while 0 < n-1 <= len(list)-1:
        n -= 1 
        t += 1
        if list[t] < list[x]:
            x=t
    return list[x]

list = [5]

#print(whilemin(list))

def whilemax(list):
    n = len(list)
    x = 0
    t = 0
    while 0 < n-1 <= len(list)-1:
        n -= 1 
        t += 1
        if list[t] > list[x]:
            x=t
    return list[x]

list = [100, 4000, 20, 30]

#print(whilemax(list))


#Sum

def smurfs(number):
    n=len(str(number))
    final=0
    for i in range(1,n+1):
        final += (number%(10**i)//10**(i-1))
    return final


#print(smurfs(156))
#print(smurfs(999999931), "LOL"

list = [2,59,328,6700,40,1]
result = whilemax(list) #The max of this list using a while loop

print(f"The result of whilemax with list = that stuff above me is {result}")