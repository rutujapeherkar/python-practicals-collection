print("Logic 1 : Using arguments to make the same function work differently")

def add(datatype, *args):
    if datatype == "int":
        ans = 0
    elif datatype == "float":
        ans = 0.0
    elif datatype == "str":
        ans = ""

    for ele in args:
        ans = ans + ele
    return ans

a1 = add("int", 10,20,30,40,50)
a2 = add("float", 1.2,1,3)
a3 = add("str","Hello " , "all")

print("Integer Ans :", a1)
print("Float Ans :", a2)
print("String Ans :", a3)

print("\nLogic 2 : Using multipledispatch")

from multipledispatch import dispatch

# passing one parameter


@dispatch(int, int)
def product(first, second):
	result = first*second
	print(result)

# passing two parameters


@dispatch(int, int, int)
def product(first, second, third):
	result = first * second * third
	print(result)

# you can also pass data type of any value as per requirement


@dispatch(float, float, float)
def product(first, second, third):
	result = first * second * third
	print(result)


# calling product method with 2 arguments
product(2, 3) # this will give output of 6

# calling product method with 3 arguments but all int
product(2, 3, 2) # this will give output of 12

# calling product method with 3 arguments but all float
product(2.2, 3.4, 2.3) # this will give output of 17.985999999999997


print("\nLogic 3 ")
# code
def add(a=None, b=None):
	# Checks if both parameters are available
	# if statement will be executed if only one parameter is available
	if a != None and b == None:
		print(a)
	# else will be executed if both are available and returns addition of two
	else:
		print(a+b)


# two arguments are passed, returns addition of two
add(2, 3)
# only one argument is passed, returns a
add(2)
