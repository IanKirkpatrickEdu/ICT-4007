def main():
    print("6. Do a While loop in Python to print out the numbers 1-10.")
    i = 1
    while i <= 10:
        print(i)
        i += 1

    print("7. Code the infinite loop with a break exercise taking in user input, printing it to the screen, and breaking out of the loop only when the letter “q” is input.")
    while True:
        user_input = input("Type something! (q to quit): ")
        print(user_input)
        if user_input.lower().strip() == "q":
            break

    print("8. Iterate over a string that you create using while and print the characters of the string to the screen until you reach the end of the string.")
    text = "Hello, World!"
    i = 0
    while i < len(text):
        print(text[i])
        i += 1
    
    print("9. Now iterate over the same string using for, and print the characters of the string to the screen until you reach the end of the string.")
    # text = "Hello, World!"
    for char in text:
        print(char)

print("10. Generate a number sequence with range() and print it to the screen.")
for num in range(1, 11):
    print(num)

if __name__ == "__main__":
    main()
