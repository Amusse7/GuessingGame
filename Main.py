import random

def guessing_game():
    attempts = 3
    score = 0
    play_again = True

    print("Welcome to the guessing game!")

    while play_again:
        level = input("Select a difficulty level (easy/medium/hard): ")

        if level.lower() == "easy":
            number = random.randint(1, 50)
        elif level.lower() == "medium":
            number = random.randint(1, 100)
        elif level.lower() == "hard":
            number = random.randint(1, 1000)
        else:
            print("Invalid difficulty level. Please try again.")
            continue

        print("I'm thinking of a number between 1 and", number)

        while attempts > 0:
            guess = int(input("Guess the number: "))

            if guess == number:
                print("Congratulations! You guessed the correct number.")
                score += attempts * 10
                break

            attempts -= 1
            print("Wrong guess!")

            if guess > number:
                print("Try guessing lower.")
            else:
                print("Try guessing higher.")

        if attempts == 0:
            print("Sorry, you ran out of attempts. The number was", number)

        print("Score:", score)

        play_again_input = input("Do you want to play again? (yes/no): ")
        play_again = play_again_input.lower() == "yes"
        attempts = 3

    print("Thank you for playing!")

guessing_game()
