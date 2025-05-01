f = open("11.txt", "r") #text file name 11.txt

fr = f.read()

inr = int(input("Enter the word length you want: "))
s = fr.split()
lenght = [word for word in s if len(word) == inr]
print(f"Total {inr}-letter words in file: {len(lenght)}")

print(f"{inr}-letter words: {lenght}")

#11.txt file 
#The old lighthouse keeper swore he saw a singing walrus on the rocks.
#Turns out, it was just the foghorn and a very enthusiastic seal.
