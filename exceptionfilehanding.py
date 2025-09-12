def write_to_file(Avnishdoc, ai_learning):
    try:
        with open("Avnish.text", "w") as file:
            file.write(Avnishdoc)
            file.write(ai_learning)
            print(f"successfully written to {file.name}")
    except Exception as e:
        print(f"An error occurred: {e}")

def append_to_file(Avnishdoc, ai_learning):
    try:
        with open("Avnish.text", "a") as file:
            file.write(Avnishdoc)
            file.write(ai_learning)
            file.write("\n")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file():
    try:
        with open("Avnish.text", "r") as file:
            data = file.read()
            print("\n" + data)
    except FileNotFoundError:
        print("Avnish.text file not found.")
    except Exception as e:
        print(f"Error while reading the file: {e}")
    finally:
        print("read operation is completed.")
        # ...existing code...

write_to_file("Hello, ", "AI Learning!")
append_to_file("More text.", " Even more learning.")
read_file()