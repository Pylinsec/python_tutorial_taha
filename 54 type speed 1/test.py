import random
with open('sentence.txt','r') as file:
    text = file.read()
    text_list = text.split('\n')
    print(text_list)
    text = file.readlines()
    a = random.choice(text)
    print(a , len(a))
    print(len('Stop existing and start living.[:-1]'))
