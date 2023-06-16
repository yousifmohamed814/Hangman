import random
words='''apple banana mango strawberry
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''
#len(words)
words=['apple',
 'banana',
 'mango',
 'strawberry',
 'orange',
 'grape',
 'pineapple',
 'apricot',
 'lemon',
 'coconut',
 'watermelon',
 'cherry',
 'papaya',
 'berry',
 'peach',
 'lychee',
 'muskmelon']
word=random.choice(words)
guessed_letters = []
guessed_word = ["_"]*len(word)
tries=len(word)+2
while tries>0:
    print(f"{' '.join(guessed_word)}")
    print(f"tries lift{tries}")
    gusse_letter=input("Gusse a letter: ")
    if gusse_letter in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue
    guessed_letters.append(gusse_letter)
    if gusse_letter in word:
        print("Good Gusse")
        for i,letter in enumerate(word):
            if gusse_letter==letter:
                guessed_word[i]=gusse_letter
    else:
        print("Sorry,That letter is not in the word.")
        tries-=1
    if ''.join(guessed_word)==word:
        print(f"Congratulations! You suggested the {word}")
        break 
print(f"Game over. The word was {word}.")