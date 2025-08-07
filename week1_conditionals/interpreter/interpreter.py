def main():
    expression = input("Expression: ")
    x, operator, z = expression.split()
    x, z = int(x), int(z)

    if operator == '+':
        result = x + z
    elif operator == '-':
        result = x - z
    elif operator == '*':
        result = x * z
    elif operator == '/':
        result = x / z
    else:
        print("Invalid operator")
        return

    print(f"{result:.1f}")

main()
