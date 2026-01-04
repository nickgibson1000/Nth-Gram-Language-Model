from itertools import pairwise
import random

def tokenize(text: str) -> list[str]:
    
    text = text.lower() # Lowercase
    text = text.split() # White space delimiter
    return text


def bigram(tokenized_text: list[str]) -> None:
    
    bigram_list = []
    
    for word, next_word in pairwise(tokenized_text):
        
        match = (word, next_word)
        bigram_list.append(match)

    #print(bigram_list)    
    return bigram_list




def normalize(bigram_list) -> None:
    
    probabilities = []
    probability_sequences = {}

    empty = {}

    for entry in bigram_list:
        probability = bigram_list.count(entry) / len(bigram_list)
        empty = {entry: probability}
        
        
        # If entry has already been entered
        #if entry not in probability_sequences:
        #    pass
        #    # Update only the probability value of the dictionary entry
        #    #current_value = probability_sequences[entry]
        #    #probability_sequences[entry] = current_value + probability
        #else:
        #    empty = {entry: probability}
        #    probability_sequences.update(empty)


        if entry not in probability_sequences:
            empty = {entry: probability}
            probability_sequences.update(empty)


    unique_sequences = set(bigram_list)
    #print(probability_sequences)

    # Make sure probabilities add up to 1
    total = 0
    for num in probabilities:
        total += num
    #print(total)
    return probability_sequences

def generate(probability_sequences) -> None:

    word = "<s>"
    sentence = []

    while word != "</s>":
        word = generate_next_word(word, probability_sequences)
        print(word)



def generate_next_word(word: str, probability_sequences):

    #print(probability_sequences)

    possibles = {}

    for key in probability_sequences:

        if key[0] == word:
            new_dict = {key: probability_sequences[key]}
            possibles.update(new_dict)


    #print(possibles)
    items = list(possibles.keys())
    weights = list(possibles.values())
    #print(items)
    #print(weights)
    selected_key = random.choices(items, weights=weights, k=1)
    selected_word = selected_key[0][1] # Element 1, tuple entry 2
    #print(f"Random word: {selected_word}")
    return selected_word

