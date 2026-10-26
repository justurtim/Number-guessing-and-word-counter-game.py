import random


# 1. Number Guessing Game
def number_guessing_game():
    print("\n--- Number Guessing Game ---")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess < secret_number:
                print("Too Low! Try again.")
            elif guess > secret_number:
                print("Too High! Try again.")
            else:
                print(
                    f"Congratulations! You guessed the number {secret_number} in {attempts} attempts."
                )
                break
        except ValueError:
            print("Please enter a valid integer.")


# 2. Word Counter
def word_counter():
    print("\n--- Word Counter ---")
    text = input("Enter a sentence or paragraph: ")

    # Split the text by whitespace and count elements
    words = text.split()
    word_count = len(words)

    # Count characters (including and excluding spaces)
    char_count_with_spaces = len(text)
    char_count_no_spaces = len(text.replace(" ", ""))

    print(f"Total Words: {word_count}")
    print(f"Total Characters (with spaces): {char_count_with_spaces}")
    print(f"Total Characters (without spaces): {char_count_no_spaces}")


# Main Menu to choose between the two
def main():
    while True:
        print("\nSelect a program to run:")
        print("1. Number Guessing Game")
        print("2. Word Counter")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            word_counter()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
