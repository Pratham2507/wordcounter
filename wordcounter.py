def count_words(text):
   
    words = text.split()
    return len(words)

def get_input():

    user_input = input("Please enter a sentence or paragraph: ")
    return user_input

def display_word_count(word_count):
    print("Word count:", word_count)

def handle_empty_input(text):
    return not text.strip()

def main():
    print("Welcome to the Word Counter!")
    user_input = get_input()

    if handle_empty_input(user_input):
        print("Error: Input cannot be empty.")
        return

    word_count = count_words(user_input)

    display_word_count(word_count)

if __name__ == "__main__":
    main()
