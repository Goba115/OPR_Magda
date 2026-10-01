import random 

x = 0
y = 0
z = 0

while x + y + z != 100 or 5*x + y + 0.1*z != 50:
    x = random.randint(0, 10)
    y = random.randint(0, 50)
    z = random.randint(0, 100)

print(f"konji: {x} \novce: {y} \nkure: {z}")
