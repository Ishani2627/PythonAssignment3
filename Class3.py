#LISTS
#Que1
a = input("enter 1st element :")
b = input("enter 2nd element :")
c = input("enetr 3rd elememt :")
myList = [a,b,c]
print(myList)
print("\n")

#Que2
myList.append("google")
myList.append("apple")
myList.append("facebook")
myList.append("microsoft")
myList.append("tesla")
print(myList)
print("\n")

#Que3
list1 = [2,3,4,2,5,6,2,2]
a =list1.count(2)
print("no of times 2 appears :" ,a)
print("\n")

#Que4
list2 = [2,5,7,3,4,9,6]
list2.sort()
print("sorted list :" ,list2)
print("\n")

#Que5
A = [1,6,3,8]
print("1st array:",A)
B = [4,2,7,5]
print("2nd array:",B)
C = A+B
C.sort()
print("sorted array  :" , C)
print("\n")

#Que6
count_odd = 0
count_even = 0
for i in C:
    if not i % 2:
        count_even = count_even + 1
    else:
        count_odd = count_odd + 1
print("number of even nos :",count_even)
print("number of odd nos :",count_odd)
print("\n")


#TUPLES
#Que1
myTuple = (10, 12 ,14, 16, 18, 20)
print("tuple :", myTuple)
y = reversed(myTuple)
print("In reverse order :" ,tuple(y))
print("\n")

#Que2
tuple1 = (2,4,6,8,10)
print("tuple is:", tuple1)
print("max value :", max(tuple1))
print("min value :", min(tuple1))
print("\n")


#STRINGS
#Que1
myString = "this is my assignment"
print(myString)
x = myString.upper()
print(x)
print("\n")

#Que2
print("27653".isdigit())
print("\n")

#Que3
mystr = "Hello World"
print(mystr)
x = mystr.replace("World","Ishani")
print(x)
print("\n")