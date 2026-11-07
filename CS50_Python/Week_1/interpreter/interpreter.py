def main():
    calc = input("Expression: ")
    x, y, z = calc.split(" ")
    x = int(x)
    z = int(z)

    match y:
        case "+":
            result = float(x + z)
        case "-":
            result = float(x - z)
        case "*":
            result = float(x * z)
        case "/":
            result = float(x / z)

    print(result)

main()
