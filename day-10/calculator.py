def num1check():
    global first_num
    try:
        first_num = float(input("what is the first number?\n"))
    except ValueError:
        print("invalid input")
        num1check()

def opcheck():
    global operator
    operator = input("which operator would you like to choose? (+, -, *, /)\n")
    if operator != "+" and operator != "-" and operator != "*" and operator != "/":
        print("invalid input")
        opcheck()

def num2check():
    global second_num
    try:
        second_num = float(input("what is the second number?\n"))
    except ValueError:
        print("invalid input")
        num2check()

def startingcheck():
    num1check()
    opcheck()
    num2check()
    calculate(first_num, operator, second_num)

def continuation(number1):
    opcheck()
    num2check()
    calculate(number1, operator, second_num)

def continuequestion(answer):
    continue_answer = input(f"would you like to continue with {answer} or restart? (y or n)\n")
    if continue_answer == "y":
        continuation(answer)
    elif continue_answer == "n":
        startingcheck()
    else:
        print("invalid input")
        continuequestion(answer)

def calculate(num1, operation, num2):
    if operation == "+":
        add_sum = num1 + num2
        print(f"{num1} + {num2} = {add_sum}")
        continuequestion(add_sum)
    elif operation == "-":
        difference = num1 - num2
        print(f"{num1} - {num2} = {difference}")
        continuequestion(difference)
    elif operation == "*":
        product = num1 * num2
        print(f"{num1} * {num2} = {product}")
        continuequestion(product)
    else:
        quotient = num1 / num2
        print(f"{num1} / {num2} = {quotient}")
        continuequestion(quotient)


print("welcome to the cool fun epic awesome calculator")
startingcheck()