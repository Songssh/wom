import pickle

words = []
with open("data/words.txt", "r") as f:
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
        "count":0
    }
    template["name"] = word
    brain.append(template)

    
brain_path = "data/trained_model.pickle"
with open(brain_path, "wb") as f:
    pickle.dump(brain, f)

with open(brain_path, "rb") as f:
    b = pickle.load(f)

print(b)
