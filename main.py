def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_num_char(text)
    list_of_dicts = convert_dict_to_list(char_count)
    sorted_list = sorting_list(list_of_dicts)
    report = get_report(book_path, num_words, sorted_list)
    

def get_report(book_path, num_words, sorted_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    for entry in sorted_list:
        char = entry['char']
        count = entry['count']
        print(f"The '{char}' character was found {count} times")


def sorting_list(list_of_dicts):
    return sorted(list_of_dicts, key=lambda x: x['count'], reverse=True)        

def convert_dict_to_list(char_dict):
    list_of_dicts = []
    for char, count in char_dict.items():
        if char.isalpha():  # Перевіряємо, що це літера
            list_of_dicts.append({"char": char, "count": count})
    return list_of_dicts        
            
def get_num_char(text):
    char_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict

def get_num_words(text):
    words = text.split()
    return len(words)
        
def get_book_text(path):
    with open(path, 'r', encoding='UTF-8') as f:
        return f.read()
            

main()