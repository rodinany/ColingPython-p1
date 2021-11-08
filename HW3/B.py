import nltk
import os

class FileReader:

    def __init__(self, path):
        self.path = path

    def __add__(self, other):
        with open('new_file.txt', 'w') as file:
            content = ''
            with open(self.path, 'r') as first_file:
                for line in first_file:
                    content += line
            content += '\n'
            with open(other.path, 'r') as second_file:
                for line in second_file:
                    content += line
            file.write(content)
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
        line_count = 0
        word_count = 0
        with open(self.path, 'r') as file:
            for line in file:
                line_count += 1
                word_count += len(nltk.word_tokenize(line))
        self.line_count = line_count
        self.word_count = word_count
        return f'the amount of lines = {self.line_count}, \nthe amount of words = {self.word_count}'