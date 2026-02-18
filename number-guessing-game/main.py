import random

class NumberGuessingGame:
    def __init__(self):
        self.number = random.randint(1, 101)
        self.guesses = 0
        self.max_guesses = 5

    def play(self):
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        print(f"You have {self.max_guesses} guess the correct number.")

        print()
        print("Please select the difficulty level:")
        print('''
        1. Easy (10 chances)
        2. Medium (5 chances)
        3. Hard (3 chances)
        ''')

        difficulty = input("Enter your choice:")
        if difficulty == "1":
            self.max_guesses = 10
            print("Great! You have selected the easy difficulty level.")
        elif difficulty == "2":
            self.max_guesses = 5
            print("Great! You have selected the medium difficulty level.")
        elif difficulty == "3":
            self.max_guesses = 3
            print("Great! You have selected the hard difficulty level.")
        else:
            print("Invalid choice. Please try again.")
            return

        while self.guesses < self.max_guesses:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

            if guess < self.number:
                print("Incorrect! The number is greater than", guess)
                self.guesses += 1
            elif guess > self.number:
                print("Incorrect! The number is less than", guess)
                self.guesses += 1
            else:
                print("Congratulations! You have guessed the correct number in", self.guesses, "guesses.")
                return

        print("Sorry! You have reached the maximum number of guesses. The correct number was", self.number)
        return

    def main(self):
        self.play()
        if input("Do you want to play again? (y/n): ").lower() == "y":
            game.play()
        else:
            print("Thank you for playing the Number Guessing Game!")
            return

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.main()
