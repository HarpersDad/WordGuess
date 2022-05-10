import random

words = ["python", "dog", "taco", "Kentucky", "moose", "Berea", "Madison", "pirates", "spoonbread"]
word = ""
guessed_letter = ""
randNum = random.randrange(0,len(words))

word = words[randNum]
guessed_word = ["*"] * len(word)
word_array = [""] * len(word)

tries = len(word) + 3

for i in range(len(word)):
    word_array[i] = word[i]
    guessed_word[i] = "*"

print("Let's guess the secret word.")
print(' '.join(guessed_word))

while(tries > 0):
    if (tries > 1):
        print(f"You have {tries} attempts left!")
    else:
        print(f"You have {tries} attempt left!")
    guessed_letter = input("guess a letter: ")
    
    for i in range(len(word)):
        if(word_array[i] == guessed_letter):
            guessed_word[i] = guessed_letter
    
    tries -= 1
    
    if (guessed_letter == words[randNum]):
        for i in range(len(word)):
            if(word_array[i] == guessed_letter[i]):
                guessed_word[i] = guessed_letter[i]
        print("You guessed the secret word!")
        break
    
    if(guessed_word == word_array):
        print("You guessed the secret word!")
        break
    
    if(tries == 0):
        print("You were unable to guess all the letters for the word!")
        break
    
    print(''.join(guessed_word))
    
print(''.join(guessed_word))