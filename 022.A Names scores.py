with open("p022_names.txt", mode="r") as file:
  text = file.read()

names = [name[1:-1] for name in text.split(",")]
names.sort()

score = [l for l in range(1, 27)]
key = [chr(l) for l in range(97, 123)]
ref_dict = dict(zip(key,score))

def word_score(word):
  word_score = 0
  for l in word:
    word_score += ref_dict[l.lower()]
  return word_score

rank = 1
total_score = 0
for name in names:
  total_score += rank * word_score(name)
  rank += 1

print(total_score)
  
