#file 3 : quadratic_lambda.py

def quadtratic_function(a,b,c):
	return lambda x: a*(x**2) + b*x + c
	
a1 = quadtratic_function(1,0,-9)
print(a1(0))
print("Input a,b and c from a quadratic equation in the form of ")
print("f(x) = ax^2 + bx + c")
#we have a problem here
a = input("Input a ")
b = input("Input b ")
c = input("Input c ")
x = input("Input x ")
a2 = quadtratic_function(a,b,c)
fx = a2(x)
print("f(x) = ", fx)
# end of the quadratic.py files


