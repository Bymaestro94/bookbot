def main():
	path_name = "books/frankenstein.txt"

	with open(path_name, 'r', encoding='utf-8') as f:
		file_content = f.read()

	word_count = count_words(file_content)
	character_count = count_character(file_content)

	print_report(word_count, character_count)

def count_words(text):
	words = text.split()

	return len(words)

def count_character(character):
	text = character.lower()

	char_counts = {}


	for char in text:
		if char.isalpha():
			if char in char_counts:
				char_counts[char] += 1
			else:
				char_counts[char] = 1

	return char_counts

def print_report(word, character):

	print("--- Begin report of books/frankenstein.txt ---")
	print(f"{word} words found in the document")

	sorted_char_count = sorted(character.items(), key=lambda x: x[1], reverse=True)

	for char, count in sorted_char_count:
		print(f"The {char} was found {count} times")

	print(f"--- End report ---")

if __name__ == "__main__":
	main()
#bookbot