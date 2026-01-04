import argparse
import tokenize as tk

def main() -> None:
    
    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--inputText", type=str, help="Text to train model on")


    args = parser.parse_args()

    text = tk.tokenize(args.inputText)
    plist = tk.bigram(text)
    stuff = tk.normalize(plist)
    tk.generate(stuff)



if __name__ == "__main__":
    main()