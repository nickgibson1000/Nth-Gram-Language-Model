import argparse
import tokenize as tk

def main() -> None:
    
    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--inputText", type=str, help="Text to train model on")


    args = parser.parse_args()

    text = tk.tokenize(args.inputText)
    list = tk.bigram(text)
    tk.normalize(list)



if __name__ == "__main__":
    main()