import random
  

with open('questions.txt','rb') as f:
    question = list()
    for i in f.readlines():
        question.append(i.strip())

print(question)
print('\r\n'+str(random.choice(question)))
