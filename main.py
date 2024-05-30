def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file, "r") as f:
        file_contents = f.read()

    char_count = count_characters(file_contents)
    words = file_contents.split()

    print_report(char_count, len(words), path_to_file)

def count_characters(text):
    text = text.lower()
    char_frequency = {}

    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1

    return char_frequency

def print_report(char_count, word_count, file_path):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

if __name__ == "__main__":
    main()

