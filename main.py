from collections import Counter



def main():
    book_path = "books/CrimeAndPunishment.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lower_text = text.lower()
    num_chars = count_characters(lower_text)
    num_char_sorted = dictToSortedList(num_chars)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for item in num_char_sorted:

        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def dictToSortedList(num_chars_dict):
    sort_list = []
    for ch in num_chars_dict:
      sort_list.append({"char": ch, "num": num_chars_dict[ch]})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list 


def count_characters(text):
    """Count frequency of each character in the text and return as dictionary."""
    # Use Counter to count all characters
    char_count = Counter(text)
    
    # Convert to dictionary with special character handling
    frequency_dict = {}
    for char, count in char_count.items():
        # Handle special characters for readability
        if char == '\n':
            key = '\\n'
        elif char == '\t':
            key = '\\t'
        elif char == ' ':
            key = 'SPACE'
        else:
            key = char
            
        frequency_dict[key] = count
    
    return frequency_dict



def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
