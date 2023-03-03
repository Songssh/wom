import pickle
import datetime


class manager:
    def __init__(self, path="data/models/trained_model.pickle"):
        self.model = self.load_model(path)
    # model update score, count
    def study(self, win: list, lose: list, score: float) -> None:
        def calculate(word, score):
            for data in self.model:
                if data["name"] == word:
                    data["score"] += score
                    data["count"] += 1
        for word in win:
            calculate(word, score)
        for word in lose:
            calculate(word, -score)
    # model update start
    def study_start(self, word, score):
        for data in self.model:
            if data["name"] == word:
                data["start"] += score
    # if you input filepath then read and return list only available .pickle file
    def load_model(self, file_path:str) -> list:
        with open(file_path, "rb") as f:
            return pickle.load(f)
    # 
    def save_model(self) -> None:
        with open(self.create_new_name(), "wb") as f:
            pickle.dump(self.model, f)
    #
    def create_new_name(self) -> str:
        base = "data/models/trained_model_"
        time = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        file = ".pickle"
        name = base + time + file
        return name
    

def transform(observation, result):
    if result:
        win = observation[0::2]
        lose = observation[1::2]
    else:
        lose = observation[0::2]
        win = observation[1::2]
    return win, lose

def who_win(score:float)->bool:
    return True if score >= 0 else False

def create_new_model(word_path="data/words.txt", model_path="data/trained_model.pickle"):
    words = []
    with open(word_path, "r") as f:
        while True:
            word = f.readline().strip()
            if not word:
                break
            words.append(word)


    brain = []
    for word in words:
        template = {
            "name":"",
            "score":0,
            "start":0,
            "count":0,
            "win":0
        }
        template["name"] = word
        brain.append(template)

    with open(model_path, "wb") as f:
        pickle.dump(brain, f)

    with open(model_path, "rb") as f:
        b = pickle.load(f)

    print(b)


def main():
    m = manager()
    text = []
    for w in m.model:
    	if w["count"] > 0:
    		text.append(w)
    print(sorted(text, key = lambda x:x["start"]))

if __name__ == "__main__":
    #create_new_model()
    main()