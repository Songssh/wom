import random
import pickle

class womENV:
    def __init__(self):
        self.dataset_path = "data/words.txt"
        self.WORDS = []
    
    def load_words(self):
        with open(self.dataset_path, "r") as f:
            while True:
                word = f.readline().strip()
                if not word:
                    break
                self.WORDS.append(word)
    
    def show(self):
        print(self.WORDS)
    
    def get_last_char(self, word):
        try:
        	return word[(len(word) - 1)]
        except IndexError:
            return word
        except:
            pass
    
    def get_score(self, word):
        return len(word) / 10
    
    def get_random_word(self, word):
        words = []
        for w in self.WORDS:
            if self.get_last_char(word) == w[0]:
                words.append(w)
        return random.choice(words) if len(words) > 0 else None


class wom_train(womENV):
    def __init__(self):
        self.reset()
        model_path = "data/trained_model.pickle"
        self.model = self.load_model(model_path)
    
    def reset(self):
        self.observation = []
        self.score = 0
        self.action_space = []
        self.turn = 0
        self.done = False
        self.stw = False
        return self.observation
    
    def begin(self):
        pass
    
    def load_model(self, path):
        with open(path, "rb") as f:
            return pickle.load(f)
    
#        


    
    def step(self, action):
        next_word = self.get_random_word(action)
        self.observation.append(next_word)
        self.done = self.check_end()
        self.stw = self.check_is_first()
        if not self.done:
            pass
        
        return self.done
        
        
    
        
    
    def render(self):
        print(self.observation)
        print(self.score)
    
    def check_end(self):
        return True if self.observation[-1] == None else False
    
    def select_first_user(self):
        c = [True, False]
        return random.choice(c)
    
    def check_is_first(self):
        return True if self.turn == 0 else False
    
    def check_next(self, word):
        return True if self.get_random_word(word) == None else False
    
if __name__ == "__main__":
    env = wom_train()
    text = env.model
    print(text)