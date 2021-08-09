import random

# Defining functions
def all_mystery_game_words(file):
    with open(file) as file_doc:
        words = file_doc.readlines()
        return words

def make_random_word_in_mode(mode, words):
    mode_words = []
    if mode == 'easy':
        for word in words:
            if (len(word) >= 5 and len(word) <= 7):
                mode_words.append(word)
                random_word = random.choice(mode_words)
    elif mode == 'normal':
        for word in words:
            if (len(word) >=7 and len(word) <= 9):
                mode_words.append(word)
                random_word = random.choice(mode_words)
    elif mode == 'hard':
        for word in words:
            if len(word) >= 9:
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

def display_word(new_letter, guessed_lettters):
    if new_letter in guessed_lettters:
        return new_letter
    else: 
        return "_"

def mystery_print(random_word, guessed_letters, user_input, guess_count):
    random_word = random_word_shorten(random_word)
    guessed_letters, user_input, guess_count = letter_validation(user_input, guessed_letters, guess_count, random_word)
    print_letters = [display_word(new_letter, guessed_letters) for new_letter in random_word]
    if '_' not in print_letters:
        print(' ')
        print('You win!')
        print('Random word was ', random_word)
        print(' ')
        print('Would you like to play again? yes or no')
        print(' ')
        user_input = input()
        user_input = user_input.lower()
        user_input = what_now(user_input)
        return guess_count, user_input
    else: 
        return ' '.join(print_letters), user_input, guessed_letters, guess_count

def random_word_shorten(random_word):
    return random_word.upper().rstrip()

def letter_validation(user_input, guessed_letters, guess_count, random_word):
    if len(user_input) < 2:
        guess_count,guessed_letters = is_it_guessed_letter(user_input, guessed_letters, random_word, guess_count)
        return guessed_letters, user_input, guess_count
    else:
        print("One letter at a time please.")
        return guessed_letters, user_input, guess_count

def is_it_guessed_letter(user_input, guessed_letters, random_word, guess_count):
    if user_input in guessed_letters:
        print('You have already guessed ' + user_input + ', please guess again.')
        print('Guessed letters: ' + ', '.join(guessed_letters))
        return guess_count, guessed_letters
    elif (user_input not in guessed_letters) and (user_input not in random_word):
        print('Not a letter in word :<')
        guessed_letters.append(user_input)
        guess_count += 1
        print('Guessed letters: ' + ', '.join(guessed_letters))
        return guess_count,guessed_letters
    else:
        print ('You guessed right!')
        guessed_letters.append(user_input)
        guess_count += 1
        print('Guessed letters: ' + ', '.join(guessed_letters))
        return guess_count, guessed_letters

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
    guessed_letters = []
    while user_input != 'quit':
        print('random word = ', random_word)
        print_letters, user_input, guessed_letters, guess_count = mystery_print(random_word, guessed_letters, user_input, guess_count)
        print(' ')
        print(print_letters)
        print('Number of guesses so far: ', guess_count)
        print(' ')
        guess_count, user_input = guess_count_validation(guess_count)

# Game is called here
words = all_mystery_game_words('words.txt')
mystery_word_game(words)



# When the game ends, ask the user if they want to play again. If they reply yes, start the game again

