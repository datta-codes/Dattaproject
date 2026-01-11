HISTORY_FILE = "HISTORY.txt"
def show_history():
    file = open(HISTORY_FILE, 'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("No history found.")
    else:
        for line in lines:
            print(line.strip())
    file.close()
def clear_history():
    file = open(HISTORY_FILE, 'w')
    file.close()
    print("History cleared.")

def save_to_history(entry):
    file = open(HISTORY_FILE, 'a')
    file.write(entry + "\n")
    file.close()
def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input format. please use: number1 operator number2")
        return 
    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        return
    save_to_history(user_input + " = " + str(result))
    print("Result:", result)
def main():
    while True:
        user_input = input("enter calculation (+, -, *, /, %) (or 'history', 'clear', 'exit'): ").strip().lower()
        if user_input == 'exit':
            print("exiting calculator. Goodbye!")
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculate(user_input)
main()
