import os

def main():
    path = input("Enter the directory path: ")
    abs = os.path.abspath(path)
    print(abs)

if __name__ == "__main__":
    main()