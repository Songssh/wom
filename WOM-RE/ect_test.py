

import WOMpro as wom


w = wom.womENV()
for word in w.WORDS:
	if len(word) == 1:
		print(word)







"""import brain

m = brain.manager()
text = type(m.create_new_name())
print(text)"""

"""
import brain

model = brain.manager().model
for i, v in enumerate(model):
    if v["name"] == "íęť":
        v["score"] += 10
#print(model)

t = 19
tt = -t
print(tt)"""
"""
import WOMpro as wom

env = wom.womENV()
start_word = []
for word in env.WORDS:
    if env.get_random_word(word) == None:
        continue
    print(word, "appended")
    start_word.append(word)
with open("data/starts.txt", "w") as f:
    for word in start_word:
        word = word +'\n'
        f.write(word)"""
