def main():
    i = input("Fraction: ")
    print(gauge(convert(i)))

def convert(fraction):
    a, b = fraction.split("/")
    a = int(a)
    b = int(b)
    if b == 0:
        raise ZeroDivisionError
    elif a > b:
        raise ValueError
    else:
        return (a / b) * 100

def gauge(percentage):
    if percentage == 0 or percentage == 1:
        return("E")
    if percentage == 99 or percentage == 100:
        return("F")
    return(f"{round(percentage)}%")

if __name__ == "__main__":
    main()