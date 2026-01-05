import argparse
import tokenize as tk

def main() -> None:
    
    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--inputText", type=str, help="Text to train model on")
    parser.add_argument("-f", "--inputTextFile", type=str, help="File to read in a large sum of text for model")


    args = parser.parse_args()


    if args.inputText is None and args.inputTextFile is None:
        raise ValueError("Must supply either a .txt or command line string")
    
    elif args.inputText is not None and args.inputTextFile is not None:
        raise ValueError("Cannot supply both a .txt file and a command line string")

    elif args.inputText is not None:
        text = tk.tokenize(args.inputText)
    elif args.inputTextFile is not None:
        text = tk.parse_file(args.inputTextFile)


    plist = tk.bigram(text)
    stuff = tk.normalize(plist)
    tk.generate(stuff)



if __name__ == "__main__":
    main()