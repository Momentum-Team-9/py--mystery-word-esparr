# Computer select random word from words.txt file
import random

# Defining my functions
def all_mystery_game_words(file):
    with open(file) as file_doc:
        words = file_doc.readlines()
        return words

def make_random_word_in_mode(mode, words):
    mode_words = []
    if mode == 'easy':
        for word in words:
            if (len(word) >= 4 and len(word) <= 6):
                mode_words.append(word)
                random_word = random.choice(mode_words)
    elif mode == 'normal':
        for word in words:
            if (len(word) >=6 and len(word) <= 8):
                mode_words.append(word)
                random_word = random.choice(mode_words)
    elif mode == 'hard':
        for word in words:
            if len(word) >= 8:
                mode_words.append(word)
                random_word = random.choice(mode_words)
    else:
        retype_1 = '''
        Mode not recognized. 
        Please enter easy, normal, hard or quit.
        '''
        print(retype_1)
        random_word = 'No random word available'
        mode = input()
        mode = mode.lower()
    return random_word

def ask_for_mode():
# User selects difficulty mode
    question_1 = '''
    What mode would you like to play? 
    // easy, normal, hard // 

    -- Type quit to end
    '''
    print(question_1)
    user_input = input()
    user_input = user_input.lower()
    return user_input

def mystery_display(random_word):
    length_of_word = (len(random_word) - 1) * "_ "
    print (length_of_word)

def guess_tally(number_of_guesses):
    guess_count = number_of_guesses + 1
    return guess_count

def guess_prompt():
    guess_prompt = '''
    Guess a letter ^___^
    '''
    print (guess_prompt)
    user_input = input()
    user_input = user_input.upper()
    return user_input

def guess_count_validation(guess_count):
    if guess_count > 8:
        print('You are out of guesses :/ Sorry. Try again? yes or no')
        user_input = input()
        user_input = user_input.lower()
        user_input = what_now(user_input)
        return guess_count, user_input
    elif guess_count <= 8:
        user_input = guess_prompt()
        guess_count += 1
        print(user_input, ": guess tally - ", guess_count, ": ", type(guess_count))
        return guess_count, user_input
    else:
        print('Where is the guess count? ', type(guess_count))
        guess_count = None
        user_input = 'quit'
        return guess_count, user_input

def what_now(user_input):
    if user_input == 'yes':
        return mystery_word_game(words)
    elif user_input == 'no':
        print('Goodbye :3')
        user_input = 'quit'
        return user_input
    else:
        didnt_hear = 'Sorry I do not understand. Please restart game.'
        print(didnt_hear)
        user_input = 'quit'
        return user_input

# This is where it all comes together:

def mystery_word_game(words):
    guess_count = 0
    user_input = ask_for_mode()
    random_word = make_random_word_in_mode(user_input, words)
    while user_input != 'quit':
        print('random word = ', random_word)
        mystery_display(random_word)
        guess_count, user_input = guess_count_validation(guess_count)

# Game is called here
words = all_mystery_game_words('words.txt')
mystery_word_game(words)
    









# User input one guess at a time
	# - word case does not matter
	# - input invalid if more than one character
	# - have them try again

# Let the user know if the word appears in the selected random word

# Display the partially guessed word

# Display the letters that have not been guessed

# Limit user to 8 incorrect guesses

# Let the user know if they have already guessed what they input and have them try again, not losing any guesses. 

# When the game ends, ask the user if they want to play again. If they reply yes, start the game again

