import random

# word bank and variables
words = ["python", "dog", "taco", "kentucky", "horse", "berea", "madison", "pirates", "spoonbread"]
word = ""
guessed_letter = ""

# random number to choose the random word
randNum = random.randrange(0, len(words))

# set random word
word = words[randNum]

# printed word * * * *
guessed_word = ["*"] * len(word)

# guessed word t a c o
word_array = [""] * len(word)

# number of tries
tries = len(word) + 3

# loop that adds the correctly guessed letter to the gussed word array
for i in range(len(word)):
    word_array[i] = word[i]
    guessed_word[i] = "*"

# output to player
print("Let's guess the secret word.")
print(' '.join(guessed_word))

# game loop
while(tries > 0):
    
    # checks if the number of tries has been reached
    if (tries > 1):
        print(f"You have {tries} attempts left!")
    else:
        print(f"You have {tries} attempt left!")
    
    # takes input from player
    guessed_letter = input("guess a letter: ")
    
    # loop that checks if the guessed character is in the hidden word
    for i in range(len(word)):
        if(word_array[i] == guessed_letter):
            guessed_word[i] = guessed_letter
    
    # removes a try from the player
    tries -= 1
    
    # check if the word has been guessed
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
