def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")

#This function takes the text and splits it into words and returns the count of words
def get_num_words(text):
    words = text.split()
    return len(words)

#This function orders the list by the character count
def sort_on(d):
    return d["num"]

#This function throws the character dictionary into a list with key value pairs
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

#This function creates a dictionary of all the characters in the text
def get_chars_dict(text):
    chars = {}
    #converts the character to lowercase and counts it
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

#This function locates the book in the directory and opens it up
def get_book_text(path):
    with open(path) as f:
        return f.read()



main()