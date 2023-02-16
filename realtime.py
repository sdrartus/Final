# remove question marks, special char with re
import re
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

import nltk
from nltk.corpus import words

nltk.download("words")

class wordChecker:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x500")

        self.text = ScrolledText(self.root, font = ("Arial", 14))

        # check after releasing spacebar
        self.text.bind("<KeyRelease>", self.check)
        self.text.pack()

        # initial number of spaces, if it changes, check the validity of the text
        self.old_spaces = 0

        self.root.mainloop()


    # 1.0 initial character
    def check (self, event):
        content = self.text.get("1.0", tk.END)
        space_count = content.count(" ")
        
        
        for tag in self.text.tag_names():
            self.text.tag_delete(tag)


        if space_count != self.old_spaces:
            self.old_spaces = space_count
            for word in content.split(" "):
                # lower case of the word and remove all special characters
                if re.sub(r"[^\w]", "", word.lower()) not in words.words():
                    #if not valid get position of particular invalid word
                    position = content.find(word)
                    self.text.tag_add(word, f"1.{position}", f"1.{position + len(word)}")
                    self.text.tag_config(word, foreground="red")

wordChecker()