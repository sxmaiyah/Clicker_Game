data = open("high_scores.txt", "r")

scores = []


with open("high_scores.txt", "r") as f:
    for line in enumerate(data):
        line = f.readline()
        addMe = line.strip()
        name, score = addMe.split(' - ')
        
        addMe = score + " " + name
        scores.append(addMe)

#scores.sort(key = lambda x: x[1])
#scores.sort()
scores.sort(key=lambda x: int(x.split()[0]))



with open("arrayTest.txt", "w") as file:
    file.write(str(scores))
