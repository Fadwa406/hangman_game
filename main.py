import random
hangman_stages = [
    """
     ------
     |    |
     |
     |
     |
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    ---
    """
]

# guessed word
words = ["good", "bad", "ugly"]
chosen_word = random.choice(words)
display = ["_"] * len(chosen_word)
print(" ".join(display))
attempts = 6
guessed_letters = []
print(hangman_stages[0])

#check for the guessing and add the guess to the list
while "_" in display and attempts > 0:
  guessed_word = input("\nPlease guess a letter! ").lower()
  
  #has the letter already been guessed?
  if guessed_word in guessed_letters:
    print("You have already chosen this letter already!")
    print(f"You have {attempts} attempts left!")
    continue
    
#if that letter is wrong
  if guessed_word not in chosen_word:
    attempts -=1 
    print(f"You have {attempts} attempts left!")
    print(hangman_stages[6-attempts])
    
  for position in range(len(chosen_word)):
    if chosen_word[position] == guessed_word:
      display[position] = guessed_word
  print(" ".join(display))
  print(f"You have {attempts} attempts left!")

if attempts == 0:
  print("""
  ***
Yos lost!
  ***
  """)
  print(hangman_stages[-1])
  
else:
  print("""

  ***
You WIN!!!
  ***
  
  """)


