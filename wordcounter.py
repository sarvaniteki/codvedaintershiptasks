def words_counter(data):
    try:
        with open(data, 'r') as file:
            content=file.read()
            words=content.split()
            print(f"Total number of words: {len(words)}")
    except FileNotFoundError:
        print("Error: File not found...plzz check the filename once")
    except Exception as e:
        print(" something went wrong plz try again:", e)
data = input("Enter the name of the file:")
words_counter(data)




