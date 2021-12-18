import requests

class GitHubUser():

    def __init__(self, name):
        self.name = name
        self.rep_amount = 0
        self.langs = {}
        langs = []
        token = ''
        req = requests.get(f'https://api.github.com/users/{self.name}/repos?access_token={token}')
        for i in req.json():
            self.rep_amount += 1
            langs.append(i["language"])
        for i in list(set(langs)):
           self.langs[i] = langs.count(i)
        req = requests.get(f'https://api.github.com/users/{self.name}?tab=followers')
        self.followers = req.json()["followers"]

    def repos(self):
        token = ''
        req = requests.get(f'https://api.github.com/users/{self.name}/repos?access_token={token}')
        print('the list of repositories:')
        for i in req.json():
            print(f'\t {i["name"]}: {i["description"]}')

    def languages(self):
        print('the list of languages:')
        for i in self.langs.keys():
            print(f'\t {i}: {self.langs[i]}')

def max_rep(*users):
    rep_dict = {}
    for user in users:
        rep_dict[user] = user.rep_amount
    for user in users:
        if rep_dict[user] == max(rep_dict.values()):
            print(f'the user with the highest number of repos: {user.name}')

def pop_lang(*users):
    lang_dict = {}
    for user in users:
        for i in user.langs:
            if i in lang_dict:
                lang_dict[i] += user.langs[i]
            else:
                lang_dict[i] = user.langs[i]
    for i in lang_dict.keys():
        if lang_dict[i] == max(lang_dict.values()):
            print(f'{i} is the most popular programming language among users')

def max_followers(*users):
    followers_dict = {}
    for user in users:
        followers_dict[user.name] = user.followers
    for i in followers_dict.keys():
        if followers_dict[i] == max(followers_dict.values()):
            print(f'{i} has the greatest number of followers')