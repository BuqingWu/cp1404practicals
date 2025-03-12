"""
Estimate: 30 minutes
Actual: 65 minutes
"""
def main():
    count_words(text)

def count_words(text):
    words = text.split()
    word_counts = {}

# Count the number of occurrences of each word
    for word in words:
        word = word.lower()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

# Sorting a dictionary
    sorted_word_counts = dict(sorted(word_counts.items()))

# Find the length of the longest word and adjust the output alignment
    max_word_length = max(len(word) for word in sorted_word_counts)
    for word, count in sorted_word_counts.items():
        print(f"{word:{max_word_length}} : {count}")

text = input("Enter a string: ")
main()