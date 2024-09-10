
#part 1
def calculate_bmi(weight, height):
    try:
        bmi = weight / (height ** 2)
        return bmi
    except ZeroDivisionError:
        return "Height can't be zero."

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi}")

#part 2

def division_useri(num1, num2):
    try:
        quotient = num1 / num2
    except ZeroDivisionError:
        return "Division by zero is not allowed"
    return quotient

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
division_result = division_useri(num1, num2)
print(f"Result: [division_result")

#part 3

with open("demo.txt", "w") as file:
    file.write("Random text for randomness.\n")

with open("demo.txt", "r") as file:
    content = file.read()
    print("file after initial write. \n", content)

with open("demo.txt", "a") as file:
    file.write("new text on new line \n")

with open("demo.txt", "r") as file:
    content = file.read()
    print("file after new line \n", content)

    #part 4

# Dictionary to store products and their respective prices
product_prices = {
    "apple": 1.00,
    "banana": 0.50,
    "orange": 0.75,
    "milk": 2.50,
    "bread": 3.00,
    "eggs": 4.50

}


def get_product_price(product_name):
    product_name = product_name.lower()
    if product_name in product_prices:
        return f"The price of {product_name} is ${product_prices[product_name]:.2f}"
    else:
        return "Product not found."

# Input from the user
product_name = input("Enter the name of the product: ")

# Output the result
print(get_product_price(product_name))

#part 5
odd_numbers = list()

for num in range(1, 100):
     if num % 2 != 0:
         odd_numbers.append(num)



print(odd_numbers)