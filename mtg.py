import random
from nltk import corpus

class MarkovChain:
    def __init__(self):
        """
        Initialize our dictionary
        """
        self.dictionary = {}

    def learn_character(self, key, value):
        """
        Input: Key of the dictionary, value of the key
        Output: Dictionary of each word as a key and value as a list of words that follow it
        Description: Append values to keys. If the key is not in the dictionary, add the key. 
        """
        if key not in self.dictionary:
            self.dictionary[key] = []
        self.dictionary[key].append(value)

    def learn(self, text):
        """
        Training the model
        Input: Corpus text
        Description: Split the corpus into tokens, create a trigram of words. For each trigram in trigram list, run learn_character()
        """
        dicti = ' '.join(text)
        sentence = dicti.split()
        N = 3
        trigrams = [sentence[i:i+N] for i in range(len(sentence)-N+1)]
        for trigram in trigrams:
            self.learn_character(trigram[0], trigram[1])

    def find_next_word(self, current_word):
        """
        Input: current word
        Description: Randomly select the next word that is most likely to follow the last word in n-gram(current word). If no word exists, pick randomly(stupid backoff)
        Output: randomly selected word
        """
        # deterministic
        next_word = self.dictionary.get(current_word)
        # stupid backoff
        if not next_word:
            next_word = self.dictionary.keys()

        return random.sample(next_word, 1)[0]

    def finish_sentence(self, amount, state=''):
        """
        Input: number of words in sentence, string to add onto
        Output is a string of n words, where n is amount
        Description: return a sentence
        """
        if not amount:
            return state

        next_word = self.find_next_word(state)
        return state + ' ' + self.finish_sentence(amount - 1, next_word)

if __name__ == "__main__":
    # words = corpus.gutenberg.words('austen-emma.txt')
    words = ["But", "her", "death", "which", "happened", "ten", "years", "before", "his", "own" "," ,"produced", "a", "great", 'alteration', 'in', 'his', 'home' ,';' 'for', 'to', 'supply',
'her', 'loss', ',' 'he', 'invited', 'and', 'received', 'The', 'family', 'of', 'Dashwood', 'had' ,'long', 'been', "settled", 'in', "Sussex.",
"Their", "estate" , 'was', 'huge' , ',', 'and' ,'their', 'residence', 'was', 'at', 'Norland', 'Park']
    markov = MarkovChain()
    markov.learn(words)
    print(markov.finish_sentence(15))
    