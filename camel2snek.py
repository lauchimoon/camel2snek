from sys import argv

PROGRAM_NAME = "camel2snek.py"

def usage():
    print(f"usage: python3 {PROGRAM_NAME} <text>|--file <filename>")
    exit(0)

def camel2snek(text: str) -> str:
    new_text = ""
    for (i, c) in enumerate(text):
        if c.isupper() and i > 0:
            new_text += "_"
        new_text += c.lower()

    return new_text

def camel2snek_file(filename: str) -> str:
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        print(f"{PROGRAM_NAME}: no such file '{filename}' found")

    text = ""
    for line in f:
        text += camel2snek(line)

    return text

def main():
    argc = len(argv)
    if argc < 2:
        usage()

    if argv[1] == "--file":
        if argc < 3:
            usage()

        print(camel2snek_file(argv[2]))
    else:
        print(camel2snek(argv[1]))

if __name__ == "__main__":
    main()
