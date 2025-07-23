import csv
from tkinter import *
from tkinter import messagebox
import WordDefinitionSet
import random

game2_window = Tk()
game2_window.config(bg='DodgerBlue4')
scores = {'q': 0, 'z': 0, 'm': 0, 'p': 0}
ingame_score = 0
counter = 0
count = 0
username = ""







def define_word(word):
    with open('words_definitions.csv', 'r') as definitions_file:
        csv_reader = csv.reader(definitions_file)
        for row in csv_reader:
            if row[0] == word:
                return row[1]

user_answer1 = Entry(game2_window, bg='white', fg='black',
                         font=('Comic Sans Ms', 12), state='disabled')

# Define the main game function

def play_game2():
    global words_list, ingame_score, counter, username, count, play4_button, \
        instructions, scores
    count = 0
    game2_window.config(bg='DodgerBlue4')
    round_label = Label(game2_window, text="Round " + str(counter),
                        bg='DodgerBlue4', font=('Comic Sans Ms', 25))
    round_label.grid(row=0, column=0, columnspan=3, sticky='s', padx=20)

    def define_word(word):
        with open('words_definitions.csv', 'r') as definitions_file:
            csv_reader = csv.reader(definitions_file)
            for row in csv_reader:
                if row[0] == word:
                    return row[1]

    if counter <= 10:
        words_list = WordDefinitionSet.easy_words
    elif 10 < counter <= 30:
        words_list = WordDefinitionSet.medium_words
    elif 30 < counter <= 50:
        words_list = WordDefinitionSet.hard_words

    word = random.choice(words_list)
    # Find definition of that word
    definition_label = Label(game2_window, text=define_word(word),
                             bg='DodgerBlue4', font=('Comic Sans Ms', 16),
                             wraplength=300)
    definition_label.grid(row=1, column=0, columnspan=3, sticky='s', padx=20)
    Q_label = Label(game2_window, text='Q: ' + str(scores['q']),
                    font=('Courier', 16), bg='DodgerBlue4', fg='white')
    Z_label = Label(game2_window, text='Z: ' + str(scores['z']),
                    font=('Courier', 16), bg='DodgerBlue4', fg='white')
    M_label = Label(game2_window, text='M: ' + str(scores['m']),
                    font=('Courier', 16), bg='DodgerBlue4', fg='white')
    P_label = Label(game2_window, text='P: ' + str(scores['p']),
                    font=('Courier', 16), bg='DodgerBlue4', fg='white')
    Q_label.grid(row=3, column=0)
    Z_label.grid(row=3, column=1)
    M_label.grid(row=3, column=2)
    P_label.grid(row=3, column=3, padx=10)

    def reset_labels():
        Q_label.config(fg='white')
        Z_label.config(fg='white')
        M_label.config(fg='white')
        P_label.config(fg='white')

    user_answer = Entry(game2_window, bg='white', fg='black',
                        font=('Comic Sans Ms', 12), state='disabled')

    # Functions when buttons are clicked
    def key_pressed(event):
        global username, words_list
        if username:
            return True
        if event.keysym in ['q', 'z', 'm', 'p']:
            user_answer.config(state='normal')
            user_answer.focus_set()

        if event.keysym == 'q':
            Q_label.config(fg='green')
            username = 'Q'
        elif event.keysym == 'z':
            Z_label.config(fg='green')
            username = 'Z'
        elif event.keysym == 'm':
            M_label.config(fg='green')
            username = 'M'
        elif event.keysym == 'p':
            P_label.config(fg='green')
            username = 'P'




    user_answer.grid(row=2, column=0, columnspan=3, pady=15)
    game2_window.bind('<Key>', key_pressed)
    game2_window.bind('<Return>',
                      lambda event: check_answer_four_players(word, user_answer, username))

    # def clear_window(label1, label2):
    #     keepwidget = [label1, label2]
    #     for widget in game1_window.winfo_children():
    #         if widget not in keepwidget:
    #             widget.destroy()

    def check_answer_four_players(word, user_answer, user):
        global scores, counter
        if user_answer.get() == word:
            scores[user.lower()] += 1
            counter += 1
            round_label.config(text='Round ' + str(counter))
            user_answer.delete(0, END)
            word1 = random.choice(words_list)
            definition_label.config(text=define_word(word1))
            if username.upper() == 'M':
                M_label.config(text='M: ' + str(scores[user.lower()]))
            if username.upper() == 'Q':
                Q_label.config(text='Q: ' + str(scores[user.lower()]))
            if username.upper() == 'Z':
                Z_label.config(text='Z: ' + str(scores[user.lower()]))
            if username.upper() == 'P':
                P_label.config(text='P: ' + str(scores[user.lower()]))
            reset_labels()
            play_game2()
            game2_window.destroy()
        else:
            messagebox.showerror("Wrong answer",
                                 "You have entered a wrong answer")
            reset_labels()

    game2_window.mainloop()



game2_window.mainloop()
