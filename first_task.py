import pandas as pd

f = open('dom.txt', encoding='utf-8-sig')
text = []
p = ',./''?!«»;:…()[]-*""“№\\…”'

for line in f:
    line = line.lower()
    text.extend(line)

for word in text:
    for i in p:
        if word == i:
            text.remove(i)

string = ''.join(text)
string = string.encode(encoding='utf-8-sig', errors='ignore')
string = string.decode()

for i in p:
    while i in string:    
        if i in string:            
            string = string[:string.find(i)] + string[string.find(i)+1:]

parags = string.split('\n')
words = []

for element in parags:
    if element == '':
        parags.remove(element)
    if element == '\t\t  ':
        parags.remove(element)
    element = element.lstrip().rstrip()
    sin_words = element.split()
    words.extend(sin_words)
    
dictionary_df = pd.DataFrame(columns=['лексема', 'кол-во'])
for x in words:
    amount = words.count(x)
    initial = pd.DataFrame({'лексема': [x], 'кол-во': [amount]})
    dictionary_df = dictionary_df.append(initial, ignore_index=True)

print(dictionary_df)
f.close()

dictionary_df.to_csv('Частотный словарь.csv', encoding='utf-8-sig', sep=',', header=False, index=False)
print('DataFrame is written successfully to Excel File.')
