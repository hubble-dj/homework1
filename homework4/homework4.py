# Start of Homework
#3.1 List Operations
BestEats = ["Kabob", "Sosis Bandari", "Turkey-Pesto Sandwhich", "Hawaiian-BBQ Pizza", "Clam Chowder"]
#print(BestEats[1])
BestEats.append("Sweet Potato Fries")
BestEats.insert(0, "apple")
#Why are you making me delete Turkey-Pesto Sandwhich :(
BestEats.remove("Turkey-Pesto Sandwhich")
#print(len(BestEats))
#print(BestEats)
#for n in range(len(BestEats)):
    #print(BestEats[n].upper())
#First error: list object has no attribute upper, needed to figure out that I needed to put it after the element number 

BestMeh = BestEats[::(len(BestEats)-1)] 
BestMeh = [BestEats[0], BestEats[len(BestEats)-1]]
print(BestMeh)

BestEats.append("potato")
brr = len(BestEats)
n = brr
while n > 0:
    n -=1 
    if BestEats[n] == "potato":
        print("MR. POTATO HEAD")
#Error, I added a potato but it didn't recognize that it was there. Put my append after my len function oopsies 

#3.2 Slicing and Striding 

noombars = list(range(21))
def get_first_15(aisbf):
    return (aisbf[:16])
def get_every_5th(BOOOOOOOO):
    return (BOOOOOOOO[::5])
def reverse_and_stride(aifuabsb):
    return aifuabsb[::-3]

def homeworksolution(x):
    print((reverse_and_stride(get_every_5th(get_first_15(noombars)))))

homeworksolution(noombars)

# 3.3 Nested Lists 

bazinga = [[1,2,3], [4,5,6], [7,8,9]]

print(bazinga[2])
bazinga.append([10,11,12])

def sum_nested(blah):
    value = 0
    n = len(bazinga)    
    while n > 0:
        n-=1
        nestlength = len(blah[n])
        while nestlength > 0:
            nestlength -=1 
            value += blah[n][nestlength]
    return value

def sum_nested2(something):
    value = 0
    for row in something:
        for bleh in row:
            value += bleh
    return value
print(sum_nested(bazinga))
print(sum_nested2(bazinga))

print(bazinga)

# 3.4 Create a 5x5 List 

def makefives(bleh):
    indilist = bleh[1::5] #Divides the range values into stretches of 5
    newlist = ([]) # Our new list!! 
    n = -len(indilist) # Negative so I can output lists left to right 
    start = 0 #Important for our ranges 
    while n < -1: 
        n += 1
        newlist.append(list(range(start, indilist[n])))
        start = indilist[n]
    return newlist

print(makefives(list(range(27))))

# Okay this was such a pain, I originally got mega lost on how to not include previous lists in my appended list, so I had to see that I needed a new variable start
# With start I could indicate where the list starts and stops

def makefivesnothrees(bleh):
    indilist = bleh[1::5] #Divides the range values into stretches of 5
    newlist = ([]) # Our new list!! 
    n = -len(indilist) # Negative so I can output lists left to right 
    start = 0 #Important for our ranges 
    while n < -1: 
        n += 1
        newlist.append(list(range(start, indilist[n])))
        start = indilist[n]
    for row in newlist:
        i = 0
        while i < len(row):
            if row[i] % 3 == 0:
                row[i] = "?"
            i+=1
    return newlist

print(makefivesnothrees(list(range(27))))

leest= list(range(27))

def sumnothree(list):
    value = 0
    for row in list:
        i = 0
        while i < len(row):
            if row[i] != "?":
                value += row[i]
            i += 1
    return value 

#print(sumnothree(makefivesnothrees(leest)))

# Dictionaries 

#4.1

ages = {"Katie":30, "Mariam":42, "Safia": 25, "Mira":48}

#print(list(ages.keys())[0])
ages["Mira"] = 100
ages.update({"Milana":52})
ages.pop("Mariam")

for x in ages.items():
    print(x)
        
#5 Running Your Code 
print(makefivesnothrees(list(range(0,102))))




