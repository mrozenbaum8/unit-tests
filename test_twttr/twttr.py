def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(d):
    string = ""
    for c in d:
        if c.lower() == "a" or c.lower() == "e" or c.lower() == "i" or c.lower() == "o" or c.lower() == "u":
            string = string + ('')
        else:
            string = string + c
    return string

if __name__ == "__main__":
    main()