# 0123456789012345678901234567890123456789012345678901234567890123456789012345678
# Importing the relevant libraries
from tkinter import *
from tkinter import messagebox, ttk
import WordDefinitionSet
import random
import csv
import words

# Defining variables that will be used later in the code
attempts1 = 5
score = 0
ingame_score = 0
# constructing amd configuring the main window
root = Tk()
root.config(bg='DodgerBlue4'), root.title('Login')
# Displaying the login label
Login_label = Label(root, text='Login', font=('Comic Sans Ms', 25), anchor="e",
                    bg='DodgerBlue4')
# Placing tkinter widgets using the grid method (the method will be followed for
# every widget in the project)
Login_label.grid(row=0, column=0, columnspan=2)
# Creating username and password entry fields
username_label = Label(root, text='Username', bg='DodgerBlue4')
username_entry = Entry(root, width=20, bg='white', fg='black',
                       font=("Comic Sans Ms", 12))
username_label.grid(row=2, column=0, columnspan=2)
username_entry.grid(row=3, padx=20, column=0, columnspan=2)

password_label = Label(root, text='Password', bg='DodgerBlue4')
password_entry = Entry(root, width=20, show='*', bg='white', fg='black',
                       font=("Comic Sans Ms", 12))
password_label.grid(row=4, padx=20, column=0, columnspan=2)
password_entry.grid(row=5, column=0, columnspan=2)

# Creating the buttons that appear in the first window
# Creating the login button
login_button = Button(root, text='login',
                      command=lambda: login(username_entry.get(),
                                            password_entry.get()),
                      highlightbackground='white', highlightcolor='white', bd=0)
login_button.grid(row=6, pady=(15, 5), columnspan=2)

# Creating the register button
registerButton = Button(root, text="Register", command=lambda: register(),
                        highlightbackground='white',
                        highlightcolor='white', bd=0)
registerButton.grid(row=7, columnspan=2)

# Creating the exit button
exit_button = Button(root, text="-Exit-", fg='red',
                     command=lambda: root.destroy(),
                     highlightbackground='white',
                     highlightcolor='white', bd=0)
exit_button.grid(row=8, pady=20, columnspan=2)

# defining the main functions used in the code
"""
A function that exits the game, saves the score in the csv file, and writes the
new sorted data
"""


def exit_game(user_name, window1, window2):
    global sorted_list, new_score, ingame_score
    go_back(window1, window2)
    rows = []
    with open('UserData.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] == user_name:
                previous_score = row[2]
                new_score = int(previous_score) + int(ingame_score)
                row[2] = str(new_score)
                if 1 <= new_score <= 10:
                    row[3] = 'Beginner'
                elif 10 < new_score <= 30:
                    row[3] = 'Intermediate'
                elif new_score > 30:
                    row[3] = 'Experienced'
            rows.append(row)
        sorted_list = sorted(rows[1:], key=lambda row: int(row[2]),
                             reverse=True)
    with open('UserData.csv', 'w') as csv_file1:
        csv_writer = csv.writer(csv_file1)
        csv_writer.writerow(['Username', 'Password', 'Score', 'Level'])
        csv_writer.writerows(sorted_list)
    for widget in window1.winfo_children():
        widget.destroy()
    ingame_score = 0


# A function that inserts a csv data record in the treeview format in tkinter
def write_tree_data(tree):
    id_num = 0
    with open('UserData.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            tree.insert(parent='', index='end', iid=id_num, text='',
                        values=(row[0], row[2], row[3]))
            id_num += 1


# A function that writes the information of a newly registered user in the csv
# file


def write_info(username1, password, score1, level):
    with open('UserData.csv', 'a') as UserDataFile:
        csv_append = csv.writer(UserDataFile, delimiter=',')
        csv_append.writerow([username1, password, score1, level])


# The two functions that change the entries' border colours based on different
# conditions


def update_border_colour1(entry):
    if len(entry.get()) < 1:
        entry.config(highlightbackground='red')
    if len(entry.get()) >= 1:
        entry.config(highlightbackground='green')


def update_border_colour2(entry):
    if len(entry.get()) < 3:
        entry.config(highlightbackground='red')
    if len(entry.get()) >= 3:
        entry.config(highlightbackground='green')


# When the user presses any button in the keyboard the border colour changes
# The border colour can be either red or green based on some conditions
username_entry.bind("<Key>",
                    lambda event: update_border_colour1(username_entry))
password_entry.bind("<Key>",
                    lambda event: update_border_colour1(password_entry))


# A function that checks if the username has already been registered


def validate_entry(entry):
    with open('UserData.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0].strip().lower() == str(entry).lower().strip():
                return False
    return True


# A function that checks the current score of the user
def check_score(username):
    with open('UserData.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == str(username).strip().lower():
                return row[2]
            if username == None:
                return 0


# A function that checks whether the password of the entered username is correct


def validate_password(Username, password):
    with open('UserData.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == str(Username).strip().lower():
                if row[1] == password:
                    return False
    return True


# A function that obtains the chosen word's definition from the words_definitions
# csv file
def define_word(word):
    with open('words_definitions.csv', 'r') as definitions_file:
        csv_reader = csv.reader(definitions_file)
        for row in csv_reader:
            if row[0] == word:
                return row[1]


# A function that goes one window back by hiding a window and showing another


def go_back(window_disappeared, window_appeared):
    window_disappeared.withdraw()
    window_appeared.deiconify()
    return ingame_score


# A function that is responsible for the process of user registration
def register():
    # Constructing the 'register' window and adding relevant labels and entries
    # The window, labels and entries are formatted to match the overall theme
    register_window = Tk()
    register_window.config(bg='DodgerBlue4'), register_window.title('Register')
    welcome_message = "Register"
    welcome_label = Label(register_window, text=welcome_message,
                          font=('Comic Sans Ms', 25), fg="white",
                          bg='DodgerBlue4')
    welcome_label.grid(row=1)

    username_label1 = Label(register_window, text='Username', fg='white',
                            bg='DodgerBlue4')
    # Username and password entries are created similar to the login process
    username_entry1 = Entry(register_window, width=20, bg='white', fg='black',
                            font=("Comic Sans Ms", 12))
    username_label1.grid(row=2)
    username_entry1.grid(row=3, padx=20)

    password_label1 = Label(register_window, text='Password', fg='white',
                            bg='DodgerBlue4')
    password_entry1 = Entry(register_window, width=20, bg="white", fg='black',
                            font=("Comic Sans Ms", 12))
    password_label1.grid(row=4)
    password_entry1.grid(row=5, padx=20)

    # Border colour is updated when any key in the keyboard is pressed
    username_entry1.bind("<Key>",
                         lambda event: update_border_colour1(username_entry1))
    password_entry1.bind("<Key>",
                         lambda event: update_border_colour2(password_entry1))

    # A function to register the user information in the database
    def register_user():
        # Username presence is checked
        if len(username_entry1.get()) < 1:
            messagebox.showerror("Username not written",
                                 "Make sure to fill the username field ")
        # The chosen password by the user is validated based on specific rules
        elif len(password_entry1.get()) < 4:
            messagebox.showerror("Password invalid",
                                 "Thw password should be 4 or more "
                                 "characters long")
        else:  # Information is finally written when the conditions are satisfied
            if validate_entry(username_entry1.get()):
                write_info(username_entry1.get(), password_entry1.get(), 0
                           , 'Beginner')
                register_window.destroy()
            else:
                messagebox.showerror("Username taken",
                                     "The entered username is already"
                                     " taken")

    # A register which executes the register_user function button is constructed
    register_button = Button(register_window, text="Register",
                             command=lambda: register_user(),
                             font=("Comic Sans Ms", 12),
                             highlightbackground='white',
                             highlightcolor='white', bd=0)
    register_button.grid(row=6, pady=20)

    # A button which returns the user back to the login window
    register_back_button = Button(register_window, text="Back",
                                  command=lambda: register_window.destroy(),
                                  font=("Comic Sans Ms", 12),
                                  highlightbackground='white',
                                  highlightcolor='white', bd=0)
    register_back_button.grid(row=7, column=0, pady=(0, 15), sticky='n')
    register_window.mainloop()


# A function that combines other functions to process the username and password
# and finally show the main menu of the program if the tests are passed


def login(user_name, password):
    global main_menu
    # Obtaining the user's overall score using the self created check_score func.
    score = check_score(username_entry.get())
    main_menu = Tk()  # Constructing the main menu window
    if validate_entry(user_name):  # Username validation process
        messagebox.showerror('Username not found', 'The username '
                                                   'entered was not found \n'
                                                   'Click on register to '
                                                   'register '
                                                   'for a new account')
        main_menu.withdraw()
    else:  # Password validation process if username validation is passed
        if validate_password(user_name, password):
            messagebox.showerror("Wrong Password",
                                 'You have entered a wrong password')
            main_menu.withdraw()
        else:
            root.withdraw()

    # Formatting the main menu window and adding user relevant messages
    main_menu.title("Main menu"), main_menu.configure(bg='DodgerBlue4')
    welcome_message = "Hello " + str(user_name)
    welcome_label = Label(main_menu, text=welcome_message, fg='white',
                          font=('Comic Sans Ms', 25), bg='DodgerBlue4')
    welcome_label2 = Label(main_menu, text="-- Choose a game from below --",
                           bg='DodgerBlue4', font=('Courier', 18))
    welcome_label.grid(row=0, column=0, columnspan=3, pady=10)
    welcome_label2.grid(row=1, column=0, columnspan=3, pady=10)

    # A function that clears the window except the specified items
    def clear_window(label1, label2, label3, label4):
        keepwidget = [label1, label2, label3, label4]
        for widget in main_menu.winfo_children():
            if widget not in keepwidget:
                widget.destroy()

    # Creating an if condition to specify the user's rank
    if 0 <= int(score) <= 10:
        rank = "Beginner"
    elif 10 < int(score) <= 30:
        rank = "Intermediate"
    else:
        rank = "Experienced"

    # Defining the functions for the three main radiobuttons in the main menu
    # A function that displays the instructions and play button of game 1
    def display_game1():
        global instructions1
        clear_window(welcome_message, game1_button, leaderboard_button,
                     game2_button)
        # A frame is used for a more organized view
        frame1 = Frame(main_menu, bg='DodgerBlue4', bd=2, relief='ridge')
        frame1.grid(row=3, column=0, columnspan=3, pady=10, padx=10,
                    sticky='nsew')
        # Instructions label is placed inside the frame
        instructions = Label(frame1,
                             text="Guess The Definition \n - A definition will "
                                  "be displayed, try to guess the word related"
                                  " to it. Get a point!"
                                  "\n Note: Press (Enter) or (Return) to submit "
                                  "your answer", bg='DodgerBlue4',
                             font=("Comic Sans Ms", 18), wraplength=300)
        instructions.grid(row=3, column=0, columnspan=3, pady=10)
        # Placing a rank label that informs the user about his rank
        rank_label = Label(frame1, text='Your rank is: ' + rank +
                                        "\n Definitions in the game will"
                                        " be based on your rank",
                           bg='DodgerBlue4', font=('Courier', 16))
        rank_label.grid(row=4, column=0, sticky='nsew', padx=10)
        # Placing a play button that launches game 1
        play1_button = Button(main_menu, text="Play (One player)",
                              command=lambda: play_game1(),
                              highlightcolor='white', highlightbackground='white'
                              , font=('Comic Sans Ms', 12), bd=0)
        play1_button.grid(row=5, column=0, columnspan=3, pady=10)
        # Defining the back button that takes the user back to the login window
        back_button = Button(main_menu, text='back', font=('Comic Sans Ms', 12),
                             bg="DodgerBlue4",
                             command=lambda: go_back(main_menu, root),
                             highlightcolor='white', highlightbackground='white',
                             bd=0)
        back_button.grid(row=7, column=1)

    def display_leaderboard():  # A function that displays the leaderboard
        clear_window(welcome_message, game1_button, leaderboard_button,
                     game2_button)
        # Using the treeview method to display the leaderboard
        # Define the tree
        data_tree = ttk.Treeview(main_menu)
        # Define the columns
        data_tree['columns'] = ("Username", "Score", "Level")
        # Format the columns
        data_tree.column('#0', width=0, minwidth=0)
        data_tree.column('Username', width=100, minwidth=20)
        data_tree.column('Score', width=100, minwidth=10)
        data_tree.column('Level', width=100, minwidth=10)
        # Create column headings
        data_tree.heading("#0", text='', anchor='w')
        data_tree.heading("Username", text='Username', anchor='center')
        data_tree.heading("Score", text='Score', anchor='center')
        data_tree.heading("Level", text='Level', anchor='center')
        # Add data to the tree using the write_tree_data function
        write_tree_data(data_tree)
        # incorporate the tree in the screen
        data_tree.grid(row=3, pady=10, columnspan=3, sticky='nsew')
        # Add a back button
        back_button = Button(main_menu, text='Back',
                             font=('Comic Sans Ms', 12),
                             command=lambda: go_back(main_menu, root, ),
                             highlightcolor='white', highlightbackground='white'
                             , bd=0)
        back_button.grid(row=4, columnspan=3, pady=10)

    def display_game2():  # A function that displays game 2 information
        clear_window(welcome_message, game1_button, leaderboard_button,
                     game2_button)
        # Following the same procedure as before, for a uniform theme
        frame1 = Frame(main_menu, bg='DodgerBlue4', bd=2, relief='ridge')
        frame1.grid(row=3, column=0, columnspan=3, pady=10, padx=10,
                    sticky='nsew')
        # A label displaying game 2 instructions
        instructions = Label(frame1, text="Arrange and Categorise \n "
                                          "Scrambled letters are given, arrange "
                                          "them to form a word, and categorise "
                                          "it"
                                          " based on it's type, and earn a point"
                                          "!", bg='DodgerBlue4',
                             font=('Comic Sans Ms', 18), wraplength=300)
        instructions.grid(row=3, column=0, columnspan=3, pady=10)
        # Placing a rank label that informs the user about his rank
        rank_label = Label(frame1, text='Your rank is: ' + rank +
                                        "\n words displayed in the game will"
                                        " be based on your rank",
                           bg='DodgerBlue4', font=('Courier', 16))
        rank_label.grid(row=4, column=0, sticky='nsew', padx=10)
        # Placing the play button that launches game 2
        play2_button = Button(main_menu, text="Play",
                              command=lambda: play_game2(),
                              highlightcolor='white', highlightbackground='white'
                              , font=('Comic Sans Ms', 12), bd=0)
        play2_button.grid(row=4, column=0, columnspan=3, pady=10)
        # Placing a back button to go back to the login window
        back_button = Button(main_menu, text='back', font=('Comic Sans Ms', 12),
                             bg="DodgerBlue4",
                             command=lambda: go_back(main_menu, root),
                             highlightcolor='white', highlightbackground='white',
                             bd=0)
        back_button.grid(row=6, column=1)

    x = IntVar()  # Defining the x variable to be assigned in the radiobuttons
    # Constructing the radiobuttons by using the tkinter Radiobutton function
    # Formatting the buttons and giving them different values to be used later
    game1_button = Radiobutton(main_menu, text="Game 1",
                               value=1,
                               variable=x,
                               indicatoron=False, bg='white', fg='black',
                               command=lambda: display_game1())
    leaderboard_button = Radiobutton(main_menu, text="Leaderboard",
                                     value=2,
                                     variable=x,
                                     indicatoron=False, bg='white', fg='black',
                                     command=lambda: display_leaderboard())
    game2_button = Radiobutton(main_menu, text="Game 2",
                               value=3,
                               variable=x,
                               indicatoron=False, bg='white', fg='black',
                               command=lambda: display_game2())
    # Placing the radiobuttons horizontally to be visible for the user
    game1_button.grid(row=2, column=0, sticky='nsew', padx=20, pady=10)
    leaderboard_button.grid(row=2, column=1, sticky='nsew', padx=20, pady=10)
    game2_button.grid(row=2, column=2, sticky='nsew', padx=20, pady=10)

    # Calling the three pre-defined functions based on the value of x
    # Displaying the relevant information when the relevant button is clicked
    if x.get() == 1:
        display_game1()
    elif x.get() == 2:
        display_leaderboard()
    elif x.get() == 3:
        display_game2()


# Game 1 window is created
game1_window = Tk()
game1_window.withdraw(), game1_window.title('Guess the Definition')


# A function that launches game 1 (guess the definition)
def play_game1():
    # All required variables are defined and globalized to be used later
    global words_list, ingame_score, counter, username, count, play4_button, \
        instructions, main_menu, overall_score, new_score
    ingame_score = 0
    counter = 1
    attempts = 5
    # Assigning the user's overall score to the variable "score"
    score = check_score(username_entry.get())
    # The game 1 window is shown again after being created and hidden
    game1_window.deiconify()
    game1_window.config(bg='DodgerBlue4')  # Formatting the Game 1 window
    # The main menu window is hidden upon entering the game
    main_menu.withdraw()
    # Relevant labels like attempts, round and score labels are created
    attempts_label = Label(game1_window, text='attempts: ' + str(attempts),
                           bg='DodgerBlue4', font=('Courier', 16))
    attempts_label.grid(row=0, column=3, sticky='ne')
    round_label = Label(game1_window, text="Round " + str(counter),
                        bg='DodgerBlue4', font=('Comic Sans Ms', 25))
    round_label.grid(row=1, column=0, columnspan=4, sticky='s', padx=20)
    # Making an adaptive score label where the difficulty changes based on the
    # score number
    score_label = Label(game1_window, text='Score: ' + str(ingame_score),
                        bg='DodgerBlue4', font=('Courier', 16), fg='green2')
    score_label.grid(row=0, column=0, sticky='nw')

    # The difficulty of words chosen is based on the overall user score in
    # the game
    if int(score) <= 10:
        words_list = WordDefinitionSet.easy_words
    elif 10 < int(score) <= 30:
        words_list = WordDefinitionSet.medium_words
    elif int(score) > 30:
        words_list = WordDefinitionSet.hard_words

    # A random word is chosen from the assigned list
    word1 = random.choice(words_list)
    # The definition of the word is shown by using the define_word function
    # created above
    definition_label = Label(game1_window, text=define_word(word1),
                             bg='DodgerBlue4', font=('Comic Sans Ms', 16),
                             wraplength=300)
    definition_label.grid(row=2, column=0, columnspan=4, sticky='s', padx=20)

    # An entry where the user enters his or her answer is created
    user_answer = Entry(game1_window, bg='white', fg='black',
                        font=('Comic Sans Ms', 12))
    user_answer.grid(row=3, column=0, columnspan=4, pady=15)
    # The answer is checked based on the check_answer function below when the
    # 'Enter' key is pressed
    game1_window.bind('<Return>', lambda event: check_answer())

    # Defining the check_answer function
    def check_answer():
        # Global and nonlocal allows the listed variables to be used by this
        # function and the function on a larger scope
        global ingame_score, counter, overall_score, words_list
        nonlocal attempts, word1
        # Checking if the user's entered answer matches the word chosen randomly
        # If it does, the following code is executed
        if user_answer.get().strip().lower() == word1.lower():
            ingame_score += 1  # Score is incremented
            counter += 1  # Counter (round number) is incremented
            # The Score label's colour changes indicating the current game
            # difficulty
            # The word difficulty changes based on the accumulated ingame score
            if 0 < ingame_score <= 10:
                score_label.config(fg='green2')
                words_list = WordDefinitionSet.easy_words
            elif 10 < ingame_score <= 30:
                score_label.config(fg='yellow2')
                words_list = WordDefinitionSet.medium_words
            elif 30 < ingame_score <= 50:
                score_label.config(fg='red2')
                words_list = WordDefinitionSet.hard_words
            # The game ends if the user exceeds 50 correct answers
            elif ingame_score > 50:
                messagebox.showinfo("Game Ended", "You have reached"
                                                  "a score of 50 in a single "
                                                  "game session \n Congrats!")
                go_back(game1_window, main_menu)
            # Score and round labels are configured to write the new score
            # and round number
            score_label.config(text="Score: " + str(ingame_score))
            round_label.config(text='Round ' + str(counter))
            # A new word is chosen randomly
            word1 = random.choice(words_list)
            # A definition is obtained for that word
            definition_label.config(text=define_word(word1))
            # Anything in the entry field is deleted for the user to input
            # something new
            user_answer.delete(0, END)

        else:  # If the user's answer is incorrect the following code is executed
            attempts -= 1  # attempts are decreased by 1
            # Attempts label is configured to write the new attempts number
            attempts_label.config(text='attempts: ' + str(attempts))
            # If the attempts are decreased to 0, the following code executes
            if attempts == 0:
                # A message is shown to inform the user that the attempts
                # have finished
                messagebox.showinfo("Game Over :(",
                                    "You have run out of attempts"
                                    "\n Try playing the game again if you think"
                                    " you can :)")
                # The game is terminated
                exit_game(username_entry.get(), game1_window, main_menu)
            else:  # If the attempts are decreased but not 0, a messagebox
                # showing that a wrong answer was created emerges
                messagebox.showerror("Wrong answer",
                                     "You have entered a wrong answer")

    # Creating a back button that edits the score and takes the user back to the
    # main menu
    back_button = Button(game1_window, text='Back', font=('Comic Sans Ms', 12),
                         command=lambda: exit_game(username_entry.get(),
                                                   game1_window, main_menu),
                         highlightcolor='white', highlightbackground='white',
                         bd=0)
    back_button.grid(row=4, column=0, columnspan=4, pady=10)

    # Creating the game's mainloop
    game1_window.mainloop()


# Creating and configuring the main window of game 2
game2_window = Tk()
(game2_window.config(bg='DodgerBlue4'),
 game2_window.title('Arrange and categorise'))
# Withdrawing and hiding the window so that it appears only when play is clicked
game2_window.withdraw()


def play_game2():
    # Variables counter and main menu are globalised
    global counter, main_menu
    # Game 2 window is shown and main menu window is hidden
    game2_window.deiconify()
    main_menu.withdraw()
    # Assigning the user's overall score to the variable "score"
    score = check_score(username_entry.get())
    # Defining ingame_score, counter and attempts
    ingame_score = 0
    score_label = Label(game2_window, text="Score: " + str(ingame_score),
                        font=('Courier', 12), bg='DodgerBlue4', fg='green2')

    attempts1 = 5
    attempts_label = Label(game2_window, text="attempts: " + str(attempts1),
                           font=('Courier', 12), bg='DodgerBlue4')
    counter = 1
    round_label = Label(game2_window, text="Round " + str(counter),
                        font=('Comic Sans Ms', 20), bg='DodgerBlue4')
    # Placing the labels
    attempts_label.grid(row=0, sticky='nsew', padx=5)
    score_label.grid(row=1, column=0, sticky='nsew', padx=5)
    round_label.grid(row=2, pady=(0, 10))
    # Defining the variable that the radiobuttons' values are assigned to
    z = StringVar()
    # Creating the frame which holds the radio buttons
    frame = Frame(game2_window, bg='DodgerBlue4', bd=2, relief='ridge')
    # Creating a Label which is the title of that frame
    frame_title = Label(frame, text='Word Type', bg='DodgerBlue4',
                        font=('Times New Roman', 16))
    # Creating the three radiobuttons representing the three word types in
    # English language
    button1 = Radiobutton(frame, variable=z, value='Noun', text='Noun',
                          bg='DodgerBlue4', command=lambda: z.set('Noun'))
    button2 = Radiobutton(frame, variable=z, value='Verb', text='Verb',
                          bg='DodgerBlue4', command=lambda: z.set('Verb'))
    button3 = Radiobutton(frame, variable=z, value='Adjective',
                          text='Adjective', bg='DodgerBlue4',
                          command=lambda: z.set('Adjective'))
    # Placing the frame and frame title
    frame.grid(row=5, column=0, pady=5)
    frame_title.grid(row=4, column=0)
    # Placing the three radio buttons
    button1.grid(row=6, padx=10, pady=10)
    button2.grid(row=7, padx=10, pady=10)
    button3.grid(row=8, padx=10, pady=10)

    # Fetching the word and scrambling it based on the user's overall score
    def scramble_word():
        global word, sc_word_label
        if 0 <= int(score) <= 10:
            easy_list = (words.easy_nouns + words.easy_verbs + words.
                         easy_adjectives)
            word = random.choice(easy_list)
            # Convert the word into a list to randomize it
            word_list = list(word)
            # Randomize the word
            random.shuffle(word_list)
            # Join the list into a string
            scrambled_word = ''.join(word_list)
            # 'sc' stands for scrambled
            sc_word_label = Label(game2_window, text=(''.join(scrambled_word)),
                                  font=('Helvetica', 20), bg='DodgerBlue4',
                                  pady=10)
            sc_word_label.grid(row=3, pady=5, padx=10)
        elif 10 < int(score) <= 30:
            medium_list = (words.moderate_nouns + words.moderate_verbs +
                           words.moderate_adjectives)
            word = random.choice(medium_list)
            # Convert the word into a list to randomize it
            word_list = list(word)
            # Randomize the word
            random.shuffle(word_list)
            # Join the list into a string
            scrambled_word = ''.join(word_list)
            # 'sc' stands for scrambled
            sc_word_label = Label(game2_window, text=(''.join(scrambled_word)),
                                  font=('Helvetica', 20), bg='DodgerBlue4',
                                  pady=10)
            sc_word_label.grid(row=3, pady=5, padx=10)
        elif int(score) > 30:
            hard_list = (words.hard_nouns + words.hard_verbs +
                         words.harder_adjectives)
            word = random.choice(hard_list)
            # Convert the word into a list to randomize it
            word_list = list(word)
            # Randomize the word
            random.shuffle(word_list)
            # Join the list into a string
            scrambled_word = ''.join(word_list)
            # 'sc' stands for scrambled
            sc_word_label = Label(game2_window, text=(''.join(scrambled_word)),
                                  font=('Helvetica', 20), bg='DodgerBlue4',
                                  pady=10)
            sc_word_label.grid(row=3, pady=5, padx=10)

    # Call the scramble_word function which was just created
    ingame_score = 0
    scramble_word()

    # Create an entry for the user answer
    user_answer = Entry(game2_window, bg='white', fg='black',
                        font=('Comic Sans Ms', 12))
    user_answer.grid(row=4, padx=10, pady=5)

    # Create a submit button to be clicked when submitting the answer
    # The submit button calls the check_answer function when clicked
    # check_answer function is defined below
    submit_button = Button(game2_window, text='Submit',
                           command=lambda: check_answer(z),
                           highlightcolor='white', highlightbackground='white',
                           bd=0)
    submit_button.grid(row=9, padx=10, pady=5)
    # Create a back button to be clicked when the user wants to exit the game
    back_button = Button(game2_window, text='Back', width=10,
                         command=lambda: exit_game(username_entry.get(),
                                                   game2_window, main_menu),
                         highlightcolor='white', highlightbackground='white',
                         bd=0)
    back_button.grid(row=10)

    # Define the check_answer function
    # Check_answer() is a function that checks the user answer and executes code-
    # -upon that decision
    def check_answer(variable):
        # Variables score, counter, attempts, word and z are globalized
        global counter, attempts1, word, ingame_score
        # If the answer entered in the answer entry is equal to the word chosen
        if user_answer.get().strip().lower() == str(word).lower():
            # The function assigns the word type of the chosen word by checking
            # its presence in the previously classified lists in word.py file
            # The lists were classified as nouns, verbs and adjectives
            if word in words.nouns:
                word_type = 'Noun'
            elif word in words.verbs:
                word_type = 'Verb'
            else:
                word_type = 'Adjective'

            # Upon assigning the word type, the function checks if the word type
            # assigned is equal to the type chosen by the user through the
            # radiobuttons' selection
            if variable.get() == word_type:
                # If the word type and the user choice match, score is
                # incremented, and score label and colour are changed accordingly
                # the round label is also configured
                ingame_score += 1
                counter += 1
                round_label.config(text="Round " + str(counter))
                if 0 < ingame_score <= 10:
                    score_label.config(fg='green2', text=f"Score: "
                                                         f"{str(ingame_score)}")
                elif 10 < ingame_score <= 30:
                    score_label.config(fg='yellow2', text=f'Score:'
                                                          f'{str(ingame_score)}')
                elif 30 < ingame_score < 50:
                    score_label.config(fg='red2', text=f"Score: "
                                                       f"{str(ingame_score)}")
                elif ingame_score >= 50:
                    messagebox.showinfo("Game Ended", "You have reached"
                                                      "a score of 50 in a single"
                                                      " game session"
                                                      " \n Congrats!")
                    exit_game(username_entry.get(), game2_window, main_menu)
                # After updating the round and score labels, anything in the user
                # entry is deleted for the user to start writing again
                user_answer.delete(0, END)
                # Scrambled word label is deleted for a new word to appear
                sc_word_label.destroy()
                # Scramble_word function is called again
                scramble_word()
            # If the word is guessed by the user, but a wrong word type is chosen
            # his answer is considered wrong and attempts are deducted
            # A message box appears to inform him about his incorrect answer
            else:
                messagebox.showerror("Incorrect answer",
                                     "You have entered an incorrect"
                                     " word type")
                attempts1 -= 1
                attempts_label.config(text='Attempts: ' + str(attempts1))
        # If the user guesses the word incorrectly, attempts are deducted
        # A message box appears to inform him about his incorrect answer
        else:
            messagebox.showerror("Incorrect answer",
                                 "You have entered an incorrect"
                                 " answer")
            attempts1 -= 1
            attempts_label.config(text='Attempts: ' + str(attempts1))
        # If the user runs out of attempts, the following code is executed
        if attempts1 == 0:
            # A messagebox informs the user that he has run out of attempts
            messagebox.showerror("Game ended", "You have used all"
                                               " of your available attempts")
            # The game is terminated
            exit_game(username_entry.get(), game2_window, main_menu)
            attempts1 = 5
            ingame_score = 0

    # The game loop is created after creating the game
    game2_window.mainloop()


# Creating the mainloop of the first window
root.mainloop()
