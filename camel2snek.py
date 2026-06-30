from sys import argv

PROGRAM_NAME = "camel2snek.py"

def usage():
    print(f"usage: ./{PROGRAM_NAME} <text>")
    exit(0)

def camel2snek(text: str) -> str:
    new_text = ""
    for (i, c) in enumerate(text):
        if c.isupper() and i > 0:
            new_text += "_"
        new_text += c.lower()

    return new_text

def main():
    argc = len(argv)
    if argc < 2:
        usage()

    print(camel2snek(argv[1]))

if __name__ == "__main__":
    main()
