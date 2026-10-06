# Section 1

name = "CJ"
age = 25
height = 5.8
is_student = False

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

# Section 2

name = input("What is your name? ")
birth_year = input("What year were you born? " )
birth_year = int(birth_year)
age = 2026 - birth_year
print (f"Hi, {name.strip().upper()}! You are {age} years old.")

# Section 3

gas_price = input("What is the cost of gas per gallon? ")
gas_tank = input ("How many gallons of gas can your car store? ")
gas_price = float(gas_price)
gas_tank = float(gas_tank)
print(f"It will cost you approximately ${gas_price * gas_tank:.2f} to fill up your car! ")

# Section 4

item_name = "Samsung TV"
price = 650
quantity = 2
total = price * quantity

print("--------------------------")
print("         Receipt")
print("--------------------------") 
print("Item: ",    item_name)
print(f"Price: $  {price:.2f}")
print("Quantity:", quantity)
print("==========================") 
print(f"Total: $  {total:.2f}")

# Section 5

username = input("What is your name? ")
hometown = input("What is your hometown? ")
hobby = input("Name one of your hobbies. ")
fun_fact = input("What is one fun fact no one knows about you? ")
birth_year = input("What year were you born? ")
birth_year = int(birth_year)
age = 2026 - birth_year

print("╔═════════════════════════╗")
print(f"           {username.strip().upper()}")
print("╚═════════════════════════╝")
print("===========================")
print(f"Age: {age}")
print(f"Hometown: {hometown}")
print(f"Hobby: {hobby}")
print(f"Fun Fact: {fun_fact}")
