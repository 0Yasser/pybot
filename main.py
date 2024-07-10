def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    print(f"--- Begin report of {book_path} ---")
        
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

    num_characters = get_num_characters(text)
    sorted_characters = sort_character_nums_dict(num_characters)
    for item in sorted_characters:
        if item['name'].isalpha():
            print(f"The {item['name']} character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    nums = {}
    for c in text:
        c = c.lower()
        nums[c] = nums.get(c, 0) + 1
    return nums
    
def sort_on(dict):
    return dict["num"]

def sort_character_nums_dict(input_dict):
    characters = [{"name": c, "num": input_dict[c]} for c in input_dict]
    characters.sort(reverse=True, key=sort_on)
    return characters

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()