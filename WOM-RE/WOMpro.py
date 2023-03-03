import random

class womENV:
    def __init__(self):
        self.dataset_path = "data/words.txt"
        self.WORDS = self.load_words(self.dataset_path)
        self.start_words = self.load_words("data/starts.txt")
    
    def load_words(self, path:str) -> list:
        words = []
        with open(path, "r") as f:
            while True:
                word = f.readline().strip()
                if not word:
                    break
                words.append(word)
        return words
    
    # input word or char then will return char
    def get_last_char(self, word):
        try:
        	return word[(len(word) - 1)]
        except IndexError:
            return word
        except:
            pass
    # calculate the word's score and return score
    def get_score(self, word):
        return len(word) / 10
    
    # if you input word, will return the word that use next time
    def get_random_word(self, word, used = []):
        words = []
        for w in self.WORDS:
            if self.get_last_char(word) == w[0]:
                if w in used:
                	continue
                words.append(w)
        return random.choice(words) if len(words) > 0 else None


class wom_train(womENV):
    def __init__(self):
        super().__init__()
        self.reset()
    
    def reset(self):
        self.observation = []
        self.observation.append(random.choice(self.start_words))
        self.score = self.get_score(self.observation[-1])
        self.turn = False
        #self.action_space = []
        return self.observation
    
    def step(self, action):
        self.observation.append(action)
        done = self.check_end(self.observation)
        if done:
            if self.turn:
                self.score -= 0.4
            else:
                self.score += 0.4
            reward = self.score
        else:
            reward = self.get_score(self.observation[-1])
            if self.turn:
                self.turn = False
                self.score += reward
            else:
                self.turn = True
                self.score -= reward
        self.score = round(self.score, 3)
        info = "No information"
        return self.observation, round(reward, 3), done, info
    
    def check_end(self, ob:list) -> bool:
        return True if ob[-1] == None else False
    
if __name__ == "__main__":
    env = wom_train()
    observation = env.reset()
    action = env.get_random_word(observation[-1])
    print(env.step(action))