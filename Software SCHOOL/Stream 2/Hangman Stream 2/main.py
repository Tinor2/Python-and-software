import json # Used for save files and word lists
import utils # Only used for adding colour
import random
from os import path
class Hangman: # Contains all functions, and infomration for any game that is running, specifically for gameplay
    def __init__(self, target_word:str, total_points, used_guesses = None) -> None:
        #Set up:
        # Empty set to store all used guesses
        if used_guesses == None:
            used_guesses = set()
        self.user_end = False # Flag to see if the game should be terminated
        self.target_word = target_word
        self.used_guesses = used_guesses
        self.points = total_points
        self.formatting_tools = utils.Formatting()
    def check_for_end(self): #uses self.word, self.guesses, self.points
        if self.user_end:
            return True, "Q" # The game will end, with a user quit
        elif self.points <= 0:
            return True, "L" #The game will end, with a loss
        elif  set(sorted(self.target_word)) <= set(sorted(self.used_guesses)): #note: Not scalable
            return True,"W" #The game will end, with a win
        else:
            return False,"-" #The game will continue
    def process_guess(self, guess:str):
        if guess == "QUIT":
            self.user_end = True
            return "Exiting game"
        elif len(guess) == 1:
            if guess in self.used_guesses: #loose points if guess has already been used
                self.used_guesses.add(guess) 
                self.points -= 10 
                print(f"Total points: {self.points}")
                return "Already used letter, loose 10 points"
            elif guess not in self.target_word: #loose points if guess is incorrect
                self.used_guesses.add(guess) 
                self.points -= 10
                print(f"Total points: {self.points}")
                return "Wrong choice, loose 10 points"    
            else: #gain points if guess nothing is wrong with it
                self.used_guesses.add(guess)
                self.points += 10
                print(f"Total points: {self.points}")
                return "Correct Choice, gain 10 points!"
        else: # handles for entire word guesses
            if self.target_word == guess: 
                for letter in guess: self.used_guesses.add(letter)
                self.points += 10
                return "Correct Choice, gain 10 points!"
            else:
                self.points -= 10
                print(f"Total lives left: {self.points}")
                return "Wrong choice, loose 10 points"
    def render_word(self): 
        display = ""
        for char in self.target_word: # Displays the target word, replacing un-guessed letters with blanks
            if char in self.used_guesses:
                display += f" {char} "
            else:
                display += " _ "
        display = self.formatting_tools.colors(display,"green")
        display += self.formatting_tools.colors("\nletters guessed: ","cyan")

        for used_letter in sorted(self.used_guesses): # Display all used guesses, color coding incorrect and correct guesses
            if used_letter in self.target_word:
                display += self.formatting_tools.colors(used_letter,"cyan")
            else:
                display += self.formatting_tools.colors(used_letter,"red") 
            display += " "       
        return display

def use_data(filename:str,relative_path:str|None = None,state:str|None = None,data = None): #loads and acceses database
    """
    Loads and accesses JSON database files with specified access mode.
    Args:
        filename (str): Name of the file to access
        relative_path (str, optional): Relative path to the file location. Defaults to empty string
        state (str, optional): File access mode. Defaults to "r" (read mode)
            Possible modes:
            - "r": Read (default)
            - "w": Write
            - "a": Append
            - "x": Create
            - "r+": Read and write
            - "w+": Write and read
            - "a+": Append and read
    Returns:
        dict or None: Returns JSON data as dictionary if successful, None if file not found
    Raises:
        FileNotFoundError: If specified file cannot be found at given path
    """
    if relative_path == None:
        relative_path = ""
    if state == None:
        state = "r"
    target_file_path = path.join(path.dirname(__file__),relative_path,filename)
    try:
        if state in ["w","a","x"]:
            with open(target_file_path, state) as file:
                json.dump(data, file, indent=4)
                return 
        else:
            with open(target_file_path, state) as file:
                game_data = json.load(file)
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    return game_data

def load_game_state():
    saved_data = use_data("save_file.json")
    blank_game = False # If we ever need to start a brand new game
    if saved_data: # Stores all data from save file
        # Convert guesses to a set if it exists, otherwise create empty set
        guesses = set(saved_data["guesses"]) if saved_data.get("guesses") else set()
        word =str(saved_data["word"])
        points = saved_data["points"]
        if points == '' or word == None:
            print("save file is empty") # if any data is missing, start blank game
            blank_game = True
    else: # Create a new save_file if it cant be found in the same dir as main.py
        print("save file can not be found, creating new save file")
        use_data("save_file.json", state="x",data = {"word": "", "points": 0, "guesses": []})
        blank_game = True
    if blank_game: # completely brand new information for a new game
        print("Starting new game")    
        word, points = choose_dif() 
        guesses = set()
    return Hangman(word, int(points), guesses) # return the desired instance of the hangman class
def save_game_state(game:Hangman):
    save_data = { # template for save state
        "word": game.target_word,
        "points": game.points,
        "guesses": list(game.used_guesses)
    }
    use_data("save_file.json", state="w", data=save_data)

def choose_dif(): # uses loaded data
    game_data= use_data("all_words_info.json")
    if game_data == None:
        print("Exiting program")
        raise SystemExit
    all_words = game_data['all_words']
    difficulty_info = game_data['difficulties']
    options = []
    for difficulty in difficulty_info.values():
        options.extend(difficulty["shortcuts"])
    while True:
        user_choosen_difficulty = input("Choose a difficulty: ").lower()
        if user_choosen_difficulty in options: 
            if user_choosen_difficulty in difficulty_info["easy"]["shortcuts"]:
                final_difficulty = "easy"
            elif user_choosen_difficulty in difficulty_info["medium"]["shortcuts"]:
                final_difficulty = "medium"
            elif user_choosen_difficulty in difficulty_info["hard"]["shortcuts"]:
                final_difficulty = "hard"
            else:
                print("Invalid Difficulty, try again. ")
                continue
            break
        else:
            print("Invalid Difficulty, try again. ")
    return (random.choice(all_words[final_difficulty]), difficulty_info[final_difficulty]["points"])
def write_new_words(new_word:str):
    if new_word.lower() == "quit":
        print("Exiting edit list mode ")
        return True # Function ends in a way the user intends
    if new_word == None or not new_word.isalpha(): # If the input had symbols/digits, or if it was just nothing, then break the function
        print("Enter a valid value")
        return False # Indicates that the function was not succesful
    word_file_info = use_data("all_words_info.json")
    if word_file_info == None: # If 
        print("Exiting program")
        raise SystemExit
    difficulty_lengths = {}
    for difficulty in word_file_info["difficulties"].keys():
        difficulty_lengths[difficulty] = word_file_info["difficulties"][difficulty]['word_length'][1] 

    valid_word = False
    if len(new_word)<word_file_info["difficulties"]["easy"]['word_length'][0]: #break if the suggested word is too small for the first difficulty
        print("Enter a word with the correct length")
        return False 
    
    difficulty_of_word = None
    for difficulty, length_of_word in difficulty_lengths.items():
        if len(new_word) < length_of_word:
            difficulty_of_word = difficulty
            if new_word not in word_file_info['all_words'][difficulty]:
                word_file_info['all_words'][difficulty].append(new_word)
            else:
                print("Word entered already exists ")
                return False 
            break
    if difficulty_of_word == None: # length of word is out of bounds --> break the function
        print("Enter a word with the correct length")
        return False
    use_data("all_words_info.json", state="w", data=word_file_info)
    print(f"\'{new_word}\' has been added into the {difficulty_of_word} list!\n")
    word_file_info = None
    return True # function is executed normally
end_game = False
def main_loop(current_game:Hangman):
        while True:
            # Take a guess, save the game, check it needs to be ended, render the UI at the end, repeat. Check for quits throughout
            print(current_game.process_guess(input("guess: "))) 
            save_game_state(current_game)
            is_end = current_game.check_for_end()
            if is_end[0] == True:
                if is_end[1] == "W":
                    print(current_game.formatting_tools.colors(f"You Won, the word was {current_game.target_word}! \nYou had a total of {current_game.points}", "green"))
                elif is_end[1] == "L":
                    print(current_game.formatting_tools.colors((f"You Lost, the word was {current_game.target_word}! \nYou had a total of {current_game.points}"),"red"))
                elif is_end[1] == "Q":
                    raise SystemExit
                break
            print(current_game.render_word())
        #Game is finished, (check_for_end()[0] == True)
        save_game_state(Hangman("","",set())) #reset the save file 
        if input("Would you like to play again? (y/n) ").lower() in ["y","yes","t"]:
            print("Starting a new game! \n\n") 
            return
        else:
            print("Thanks for playing! \nExiting Program.")
            raise SystemExit
    
def initialize_game():
    while True:
        game_state = input("Start a game, update word list, or load a new save file? ").lower().strip() # make sure the input is completely valid
        if game_state in ["start","update","load","s","u","l"]:
            if game_state in ['start','s']: 
                word, maxPoints = choose_dif() # start a new game, completely normally
                current_game = Hangman(word, maxPoints)
                break # any time break is called, the main_loop function starts.
            elif game_state in ["update", "u"]: # write new words
                while True:
                    if write_new_words(input("Add a new word (type QUIT to exit edit mode):  ")):
                        break #here however, this just breaks out of the edit mode, the game is still within the loop in the init_game 
            elif game_state in ["load","l"]: # load an existing game file
                print("Loading save file . . .")
                current_game=load_game_state()
                break
        elif game_state.lower() in ["quit","q"]:
            end_game = True
            break
        else:
            print("Invalid input, try again. ")
    if end_game:
        print("Exiting program.")
        raise SystemExit
    print(current_game.render_word())
    return current_game
# Intro card
print(f"""
=============================================
                HANGMAN GAME
=============================================

HOW TO PLAY:
-----------
* START: Type "start" or "s" to begin a new game
* LOAD:  Type "load" or "l" to continue a saved game
* UPDATE: Type "update" or "u" to add new words
* QUIT:  Type "QUIT" to exit at any point

DIFFICULTY LEVELS:
----------------
Easy, Medium, or Hard - each with different word 
lengths and starting points.

GAMEPLAY RULES:
-------------
* Guess one letter at a time or the full word
* CORRECT guess: +10 points
* INCORRECT guess: -10 points
* REPEATED guess: -10 points
* Type "QUIT" during a game to exit

WINNING & LOSING:
---------------
* WIN: Successfully guess the complete word
* LOSE: Your points reach zero

Games are automatically saved after each guess.
Green letters = correct guesses, Red letters = incorrect

Type "start", "load", "update" to begin...
======================================================
""")
while True: # main gameplay loop
    current_game = initialize_game()
    # This point is ONLY reached if the user has chosen to start a new game, or loaded a new one
    main_loop(current_game)
    