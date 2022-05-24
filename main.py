import random
import hangman_art
import hangman_words
from replit import clear

print(hangman_art.logo)
lives=6
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)
#print(chosen_word)

answer = ['_']*len(chosen_word)
print(answer)
flag=0
while flag==0 :
  if '_' in answer:
    guess= input("make a guess : ").lower()
    clear()
    if guess in answer:
        print(f"You've already guessed {guess}")
    if guess not in chosen_word:
      print(f"You guessed {guess}, that's not in the word. You lose a life." )
      lives=lives-1
    for i in range(0,len(chosen_word)):
      if chosen_word[i] == guess:
        if answer[i]=='_':
          answer[i]= guess 
    print(f"{' '.join(answer)}")
    #print(answer)
    print(hangman_art.stages[lives])
    if lives==0:
      print("you loose")
      flag=1
  else:
    print("you win")
    flag=1
    
