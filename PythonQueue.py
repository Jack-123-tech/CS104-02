names=["jack","Ben","tyler","Sammy","Justin","Brain","Nick","Ryan","Danny","ashley"]


#Hints names=[] name.append(acceptedName)
for i in range(0, 10):
    acceptedName = str(input("Please enter a name: "))
    names.append(acceptedName)
#len(names) print(names.pop(0))
# two for loops must be in the code
#sim a queue at a bank


for j in range(0, len(names)):
    print(names.pop(0))
