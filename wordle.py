logo = '''
 __    __   ___   ____   ___    _        ___ 
|  |__|  | /   \ |    \ |   \  | |      /  _]
|  |  |  ||     ||  D  )|    \ | |     /  [_ 
|  |  |  ||  O  ||    / |  D  || |___ |    _]
|  `  '  ||     ||    \ |     ||     ||   [_ 
 \      / |     ||  .  \|     ||     ||     |
  \_/\_/   \___/ |__|\_||_____||_____||_____|
'''
import random
from nltk.corpus import words
allwords = set(words.words())
f = open("C:\\Users\\shash\\OneDrive\\Documents\\wordlist.txt",'r')
word_list = []
for x in f:
    if x == '\n':
        pass
    else:
        word_list.append((x.replace("\n","")))
def calculate_stats(word,guess):
    stats= ""
    for i in range(0,5):
        if guess[i] == word[i]:
            stats += '\033[92m' + guess[i].upper() +'\033[0m'+"  "
        elif guess[i] in word:
            stats += '\033[93m' + guess[i].upper() +'\033[0m'+"  "
        else:
            stats += guess[i].upper() + "  "
    return stats
play = True
while play:
    print(logo)
    lives = 6
    print('__ __ __ __ __\n' * lives)
    word = random.choice(word_list).lower()
    print(word)
    guessed_words = []
    stats_list = []
    while lives != 0:
        guess = input('guess the word : ')
        if guess not in allwords or len(guess) != 5:
            print("not valid")
            continue
        guessed_words.append(guess)
        stats_list.append(calculate_stats(word,guess))
        for i in range(len(stats_list)):
            print(stats_list[i])
        print('__ __ __ __ __\n'* (lives-1))
        if guess == word:
            print("congrats you won")
            break
        lives -= 1
    if lives == 0:
        print(f"YOU LOSE the word was {word} \nbetter luck next time")
    x = int(input("do you want to play again....\n 1 to continue \n0 to end : "))
    if x==0:
        play = False
