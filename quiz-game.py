import random
import json

x = 0
y = -1
z = 0
# Kelime listesi (güncel haliyle)
with open('words.json', 'r', encoding="utf-8") as file:
    words_ = json.load(file)
words = eval(str(words_["words"]))
seed = random.randint(2,1000)
random.seed(seed)

def word_game():
    print("Welcome to the Word Guessing Game!")
    print("Type 'quit' to exit the game or 'b' to reveal the answer.")
    global x
    global y
    global z
    
    while True:
        # Rastgele bir kelime seç
        
        english_word, turkish_translation = random.choice(list(words.items()))
        print(f"\nWhat is the meaning of        '{english_word}'      in Turkish?")
        y += 1
        attempts_left = 3  # Her soru için 3 deneme hakkı
        
        while attempts_left > 0:
            guess = input(f"Your guess (Attempts left: {attempts_left}): ").strip().lower()
            
            
            if guess == "quit":
                print("Thanks for playing! Goodbye!")
                z = (x * 100) / y
                print("\nDoğru / Soru "f"\n  {x} / {y}" + f"\t%{int(z)}" )
                return
            
            if guess == "b":
                print(f"The correct answer is: '{turkish_translation}'")
                break
            
            if guess == turkish_translation.lower():
                print("🎉 Correct! You guessed it right.")
                x += 1
                break
            else:
                attempts_left -= 1
                print("❌ Incorrect guess. Try again!")

        if attempts_left == 0:
            print(f"😞 Out of attempts! The correct answer was: '{turkish_translation}'")

# Oyunu başlat
word_game()

