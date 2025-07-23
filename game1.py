import csv
from tkinter import *
from tkinter import messagebox
import WordDefinitionSet
import random

game1_window = Tk()
game1_window.config(bg='DodgerBlue4')
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


welcome_message = Label(game1_window, text='Welcome to "Guess The Definition"',
                    bg="DodgerBlue4", fg='white', font=('Comic Sans Ms', 23))
welcome_message.grid(row=0, column=0, columnspan=3, sticky='s', padx=20)

game1_label = Label(game1_window)



# Function to find a word's definition




global play4_button, \
    instructions
words_list = {}
instructions.destroy()
play4_button.destroy()
welcome_message.destroy()
round_label = Label(game1_window, text="Round " + str(counter),
                    bg='DodgerBlue4', font=('Comic Sans Ms', 25))
round_label.grid(row=0, column=0, columnspan=3, sticky='s', padx=20)

if counter <= 10:
    words_list = WordDefinitionSet.easy_words
elif 10 < counter <= 30:
    words_list = WordDefinitionSet.medium_words
elif 30 < counter <= 50:
    words_list = WordDefinitionSet.hard_words

word = random.choice(words_list)
# Find definition of that word
definition_label = Label(game1_window, text=define_word(word),
                         bg='DodgerBlue4', font=('Comic Sans Ms', 16),
                         wraplength=300)
definition_label.grid(row=1, column=0, columnspan=3, sticky='s', padx=20)

score_label = Label(game1_window, text='Score: ' + str(ingame_score))
score_label.grid(row=2, columnspan=2)

user_answer = Entry(game1_window, bg='white', fg='black',
                    font=('Comic Sans Ms', 12))
user_answer.grid(row=2, column=0, columnspan=3)
game1_window.bind('<Return>', lambda event:
check_answer_one_player(word, user_answer))




def check_answer_one_player(word, user_answer):
    global ingame_score, counter
    if user_answer.get() == word:
        counter += 1
        user_answer.destroy()
    else:
        messagebox.showerror("Wrong answer",
                             "You have entered a wrong answer")



game1_window.mainloop()
