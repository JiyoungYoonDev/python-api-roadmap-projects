# Number Guessing Game

A CLI-based number guessing game. Run it in the terminal to play.

---

## Requirements

- **CLI-based**: You interact with the game via the command line.

### Game flow

1. When the game starts, it shows a **welcome message** and the **rules**.
2. The computer picks a **random number between 1 and 100**.
3. The user chooses a **difficulty** (easy / medium / hard), which sets how many **guesses** they get.
4. The user enters their **guess**.
5. **Correct guess**: Show a congratulations message and the **total number of attempts**.
6. **Wrong guess**: Tell the user whether the number is **higher or lower** than their guess.
7. The game ends when the user **guesses correctly** or **runs out of chances**.

---

## Sample output

```plaintext
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
Enter your choice: 2
Great! You have selected the Medium difficulty level.
Let's start the game!
Enter your guess: 50
Incorrect! The number is less than 50.
Enter your guess: 25
Incorrect! The number is greater than 25.
Enter your guess: 35
Incorrect! The number is less than 35.
Enter your guess: 30
Congratulations! You guessed the correct number in 4 attempts.
```

---

## Optional ideas

Ways to make the game more interesting:

- **Multiple rounds**: After each game, ask "Play again?" and keep playing until the user quits.
- **Timer**: Show how long it took to guess the number.
- **Hints**: Give clues when the user is stuck.
- **High score**: Save and show the fewest attempts per difficulty level.

---

## Source

Project requirements: [roadmap.sh – Number Guessing Game](https://roadmap.sh/projects/number-guessing-game)
