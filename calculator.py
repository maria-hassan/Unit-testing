class Calculator:
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        if y != 0:
            return x / y
        else:
            return "0 is not divisible"


if __name__ == "__main__":
    c = Calculator()
    while True:
        choice = (input("what operation do you want to perform"))

        if choice in ['1', '2', '3', '4']:
            x = float(input("Enter first number"))
            y = float(input("Enter second number"))

        if choice == '1':
            result = c.add(x, y)
            print("Result: ", result)

        elif choice == '2':
            result = c.sub(x, y)
            print("Result: ", result)

        elif choice == '3':
            result = c.mul(x, y)
            print("Result: ", result)

        elif choice == '4':
            result = c.div(x, y)
            print("Result: ", result)

        else:
            print("Invalid input")
