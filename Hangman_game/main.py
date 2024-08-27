from words import ai_technology, vehicles, musical_instruments, sports, programming_languages, colors, countries, fruits, animals, subjects
import random

def get_word(category):
    word = random.choice(category)
    return word.lower()

def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print(display_Hangman(tries))
    print(word_completion)
    print("\n")
    
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word!")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job!", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]  # Fix the index calculation
                # replace each underscore with the letter
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess!")
            tries -= 1

        print(display_Hangman(tries))
        print(word_completion)

    if guessed:
        print("Congratulations, you win!")
    else:
        print("Sorry, you ran out of chances. The word was:", word)

def display_Hangman(tries):
    # Number of each stage corresponds to the number of tries left
    stages = [
        """
           _ _ _ _ _ _
            |      |
            O      |
           \|/     |
            |      |
           / \     |
                  ___         
        """,
        """
          _ _ _ _ _ _
           |      |
           O      |
          \|/     |
           |      |
           \      |
                 ___
        """,
        """
          _ _ _ _ _ _
           |      |
           O      |
          \|/     |
           |      |
                  |
                 ___
        """,
        """
         _ _ _ _ _ _
          |      |
          O      |
          |/     |
          |      |
                 |
                ___
        """,
        """
         _ _ _ _ _ _
          |      |
          O      |
          |      |
          |      |
                 |
                ___
        """,
        """
         _ _ _ _ _ _
          |     |
          O     |
                |
                |
                |
               ___
        """,
        """
        _ _ _ _ _ _
          |     |
                |
                |
                |
                |
                _
        """
    ]
    return stages[tries]

def main():
    categories = {
        "ai_technology": ai_technology,
        "vehicles": vehicles,
        "musical_instruments": musical_instruments,
        "sports": sports,
        "programming_languages": programming_languages,
        "colors": colors,
        "countries": countries,
        "fruits": fruits,
        "animals": animals,
        "subjects": subjects
    }
    print("\n")
    print("                  Let's play Hangman")
    print("\n")
    print("Select one of these categories: ai_technology, vehicles, musical_instruments, sports, programming_languages, colors, countries, fruits, animals, subjects.")
    category_input=input().lower()
    if category_input in categories:
        word=get_word(categories[category_input])
        play(word)
        while input("Play again ? (Y/N)").upper()=="Y":
            word=get_word(categories[category_input])
            play(word)

    else:
        print("Invalid category. Please try again.")

if __name__ == "__main__":
    main()
