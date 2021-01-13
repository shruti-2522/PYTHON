# Guess the number:
num = 10
a = int(input("Enter Any NUMBER:"))
game_over = False
while not game_over:
    if num == a:
        print("You win!");
        game_over = True
    else:
        if num > a:
            print("Your guess num is low:")
            a = a + 1
            a = int(input("Enter any number"))
        else:
            if num < a:
                print("Your guess num is high")
                a = a - 1
                a = int(input("Enter Any Number"))
