def convert(text):
    # Replace :) with 🙂 and :( with 🙁
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    # Prompt the user for input
    user_input = input("Enter your text: ")
    # Convert emoticons to emojis and print the result
    print(convert(user_input))

# Call main function when script is run
if __name__ == "__main__":
    main()
