# Calculator App

def prompt_operand():
    continue_user_prompt = True
    while (continue_user_prompt):
        operand = input("Enter operand (+ - * /) or q to quit: ")

        if operand == "q":
            return operand

        is_operand_valid = validate_operand(operand)

        if (is_operand_valid == True):
            return operand

        if (is_operand_valid != True):
            print("     (Input operands (+ - * /) or q to quit only)")


def validate_operand(operand):
    if operand in "+-*/":
        return True


def prompt_numbers():
    while (True):
        try:
            first_number = float(input("Enter First Number: "))
            second_number = float(input("Enter Second Number: "))

            return (first_number, second_number)

        except ValueError:
            print("     (Enter numeric values only)")


def validate_number(input_number):
    if input_number.isnumeric():
        return True


def calculate(first_number, operator, second_number):
    if (operator == "*"):
        return multiply(first_number, second_number)
    elif (operator == "+"):
        return add(first_number, second_number)
    elif (operator == "-"):
        return subtract(first_number, second_number)

    try:
        if (operator == "/"):
            return divide(first_number, second_number)
    except ZeroDivisionError:
        return "Divide by zero error!"


def multiply(first_number, second_number):
    return first_number * second_number

def divide(first_number, second_number):
    return first_number / second_number

def add(first_number, second_number):
    return first_number + second_number

def subtract(first_number, second_number):
    return first_number - second_number


# Calculator app started
print("** Calculator Started **")
continue_app = True
while continue_app:

    user_operand = prompt_operand()

    if user_operand == "q":
        continue_app = False
        break

    (user_first_number, user_second_number) = prompt_numbers()

    result = calculate(user_first_number, user_operand, user_second_number)

    print("Result: {} {} {} = {}".format(user_first_number, user_operand, user_second_number, result))

    # We want to continue asking next set of operand, first and second numbers until user enters 'q'
    # Uncomment below if we only want user to be prompted one time
    # continue_app = False  

print("** Calculator Stopped **")
