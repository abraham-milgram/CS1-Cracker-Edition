# Exercise 2

name = input("Enter your name: ")
print("Hello " + name)

# Exercise 3

hours = int(input("Enter Hours: "))
rate = int(input("Enter Rate: "))
print("Pay: " + str(hours * rate))

# Exercise 4

width = 17
height = 12.0

equations = [(width//2), (width/2.0), (height/3), (1 + 2 * 5)]
for e in equations:
    print(e)
    print(type(e))

# Exercise 5

c = int(input("Celcius "))
f = c * 1.8 + 32
print(f)