import random
play_again = "y"
while play_again == "y":
    for i in range(5):
        print(random.randrange(2), end="")
    print()
    play_again = input("Play again? ")
print("Bye!")
