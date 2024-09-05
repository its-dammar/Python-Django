

# Define a basic Function
def myFunction():
    print("I am Aayushna")
myFunction()




# Function that take argument
def fun2(arg1, arg2):
    print(arg1 + "" + arg2)
fun2("Hi", "Dammar")




# Function that return a Value
def fun3(x):
    return x * x * x




# Function that with default vale for argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result
print(power(2))
print(power(2, 5))



# Function with variable number of argument
def multi_add(*arg):
    result = 0
    for x in arg:
        result =result + x
    return result
print(multi_add(2,3,4,5,6))