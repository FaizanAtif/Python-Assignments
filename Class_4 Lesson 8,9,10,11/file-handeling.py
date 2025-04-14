
def write_to_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)
    return "Text written to file."

def append_to_file(filename, text):
    with open(filename, 'a') as file:
        file.write("\n" + text)
    return "Text appended to file."

def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found!"

# Main execution
if __name__ == "__main__":
    filename = "example.txt"
    
    # Writing to a file
    print(write_to_file(filename, "Hello, this is a test!"))
    
    # Appending to the file
    print(append_to_file(filename, "This is an additional line."))
    
    # Reading from the file
    print("\nFile contents:")
    print(read_from_file(filename))