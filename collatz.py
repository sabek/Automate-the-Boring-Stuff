def collatz(number, number_tries):
    if not number % 2:
        value = number // 2
        print(value)
        number_tries += 1
        return value, number_tries
    else:
        value = 3 * number + 1
        number_tries += 1
        print(value)
        return value, number_tries

number = ''

while not number:
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("That is not an integer")
        continue

value, tries = collatz(number, 1)
while value != 1:
    value, tries = collatz(value, tries)

print ("Factored in " + str(tries) + " tries.")
