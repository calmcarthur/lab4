import sys

# search(pattern, file_name)
#
# Inputs: text pattern (string), file name (file.txt)
# Outputs: None
#
# This function prints all lines from a file that contain the given pattern.
def search(pattern, file_name):
    try:
        file = open(file_name, 'r')
        line_number = 0

        for line in file:
            line_number += 1
            
            if pattern in line:
                # Print the line number and content
                print("Line", line_number, ":", line.strip())
        
        file.close()

    # Exception handling
    except FileNotFoundError:
        print("Error: File '" + file_name + "' not found.")
    except Exception as e:
        print(f"An error occurred with pattern ({pattern}) and ({file_name}):", str(e))

    return None

def main():
    # Input checking
    if (
        len(sys.argv) != 4 
        or sys.argv[1] != "search" 
        or not isinstance(sys.argv[2], str) 
        or not isinstance(sys.argv[3], str) 
        or not sys.argv[3].endswith(".txt")):
        print("Usage: python script.py search <pattern> <filename.txt>")
        return
    
    pattern = sys.argv[2]
    file_path = sys.argv[3]
    search(pattern, file_path)

if __name__ == "__main__":
    main()