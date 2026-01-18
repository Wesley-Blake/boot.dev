from collections import Counter
from pathlib import Path
from string import punctuation, whitespace
from book_bot_errors import FileNotReadable

class BookBot:
    def __init__(self, file: str | Path):
        self.words: list[str]
        with open(file) as f:
            self.words = f.read()
            self.words = self.words.replace('\'s','')
            for c in punctuation:
                self.words = self.words.replace(c,'')
            self.words = self.words.split()

        self.characters = Counter()
        for c in self.words:
            self.characters.update(c.lower())

        self.unique_words =  Counter(self.words)
    def num_words(self):
        return len(self.words)
    def num_unique_words(self):
        return len(self.unique_words.keys())
    def print_characters(self):
        for i in self.characters:
            print(f"{i}:\t{self.characters[i]}")
