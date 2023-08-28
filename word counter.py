def word_count(text):
    words = text.split()
    return len(words)

# Get input from the user
text = input("Enter a sentence or paragraph: ")

# Count the words
num_words = word_count(text)

# Display the word count
print(f"Number of words: {num_words}")
