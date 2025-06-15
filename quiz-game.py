import json
import random

# JSON'dan kelimeleri oku
with open("words.json", "r", encoding="utf-8") as f:
    words_data = json.load(f)

words = list(words_data["words"].items())
random.shuffle(words)

correct = 0
total = 0

print("Çıkmak için 'quit' yazabilirsin.\n")

for english, turkish in words:
    answer = input(f"{english} : ").strip().lower()
    
    if answer == "quit":
        break

    total += 1
    if answer == turkish.lower():
        correct += 1
        print("Doğru!\n")
    else:
        print(f"Yanlış! Doğru cevap: {turkish}\n")

# Sonuçları göster
print("\nOyun Bitti!")
print(f"Doğru Sayısı: {correct}/{total}")
if total > 0:
    print(f"Başarı Oranı: %{correct / total * 100:.2f}")
else:
    print("Hiç cevap verilmedi.")

input("\nÇıkmak için Enter'a basın...")
