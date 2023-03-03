import binascii as bi

f = open("data/words.bin", "rb")
words = []

while True:
    word = f.readline().strip()
    if not word:
        break
    words.append(word)
f.close()
print("complete1")

i = 0
f = open("data/words.txt", "w")
for word in words:
    i += 1
    word = bi.unhexlify(word).decode()
    if word.find(" ") >= 0:
        print(i)
        continue
    f.write(word)
    f.write("\n")
f.close()
print("complete2")