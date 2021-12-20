import pickle

class UnigramMorphAnalyzer:

    def train(self):
        pos_dict = {}
        pos_data = []
        with open('pos_data.txt', 'r', encoding="utf-8") as f:
            for line in f:
                for i in range(1, min(len(line.split()[0])+1, 5)):
                    pos_data.append(line)
        pos_statistics = {}

        for token in pos_data:
            for i in range(1, min(len(token.split()[0])+1, 5)):
                if token.split()[0][-i:] in pos_statistics.keys():
                    pos_statistics[token.split()[0][-i:]] += [token.split()[1].strip('/n')]
                else:
                    pos_statistics[token.split()[0][-i:]] = [token.split()[1].strip('/n')]

        for i in pos_statistics:
            pos = {}
            for item in set(pos_statistics[i]):
                pos[item] = list(pos_statistics[i]).count(item)
                pos_dict[i] = pos

        return pos_dict

    def save(self):
        with open('pos_statictics.pickle', 'wb') as f:
            pickle.dump(self.train(), f)

    def load(self):
        with open('pos_statictics.pickle', 'rb') as f:
            return pickle.load(f)

    def predict(self, token):
        pos_data = self.load()
        prob_dict = {}
        token = token[-min(len(token), 4):]
        total = sum(pos_data[token].values())
        for i in pos_data[token]:
            prob = pos_data[token][i]/total
            prob_dict[i] = prob
        print(prob_dict)