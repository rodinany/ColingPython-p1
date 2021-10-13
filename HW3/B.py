import nltk
import os

class FileReader:

    def __init__(self, path):
        self.path = path

    def __add__(self, other):
        with open('new_file.txt', 'w') as file:
            file.write(self.read() + '\n' + other.read())
        return FileReader('new_file.txt')

    def __str__(self):
        return os.path.abspath(self.path)

    def read(self):
        content = ''
        try:
            with open(self.path, 'r') as file:
                for line in file:
                    content += line
            return content
        except FileNotFoundError:
            return content

    def write(self, string):
        with open(self.path, 'w') as file:
             file.write(string)

    def count(self):
        n = 0
        with open(self.path, 'r') as file:
            content = ''
            for line in file:
                n += 1
                content += line
        self.line_count = n
        self.word_count = len(nltk.word_tokenize(content))
        return f'the amount of lines = {self.line_count}, \nthe amount of words = {self.word_count}'