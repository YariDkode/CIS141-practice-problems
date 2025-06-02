'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a 
song into it. Write a Python program that:
- Reads the file
- Requests 5 inputs from the user: 5 words the user would like to count the frequency of
- Counts how many times each word appears
- Creates a dictionary of the words and their counts
- Print the dictionary to the console
'''
#create a folder with lyrics
with open("song_lyrics.txt", "w") as file:
    file.write("""Her day starts with a coffee and ends with a wine
Takes forever getting ready, so she's never on time for anything
But she gets that come-get-me look in her eyes
It kinda scares me the way that she drives me wild
She’s unpredictable, unforgettable  
It’s unusual, unbelievable  
How I’m such a fool, yeah, I’m such a fool for her """)


# Read lyrics from the file
with open("song_lyrics.txt", "r") as file:
    lyrics = file.read().lower()

# Ask user for 5 words
word_counts = {}
for i in range(5):
    word = input(f"Enter word {i + 1} to count: ").lower()
    count = lyrics.count(word)
    word_counts[word] = count

# Print result
print("\nWord Frequencies:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
