
myint= 5

myfloat= 5.4

mystr= "Dammar Khadayat"

mybool= True

mylist= [1, 2, "Aayushna", 5, True, 4.5]

mytuple= (1,3,4)

mydict= {"one":1, "Hello":2}

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

# re-declare variable is work in python
myint= "My Something"

# to access a member a sequence type , use []
print(mylist[2])
print(mylist[3])

# use slice to get parts of a sequence
print(mylist[1:5:2]) # where 1 is start, 5 is end and 2 is step

# You can use slices to reverses a sequence
print(mylist[::-1])

# Dictonaries are access via Key 
print(mydict["one"])

# Error variables oƒ differnet type cann't be combined 
# print("hello" + 123)
print("hello" + str(123))


# Global Vs Local Variable declaration
def sheSomething():
    global mystr # access the global varaiable
    mystr= "She is a beautiful"
    print(mystr)

sheSomething()
print(mystr)

# del mystr  #delete variable
# print(mystr)
