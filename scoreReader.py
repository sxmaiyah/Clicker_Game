data = open("high_scores.txt", "r")

scores = []


with open("high_scores.txt", "r") as f:
    for line in enumerate(data):
        line = f.readline()
        addMe = line.strip()
        name, score = addMe.split(' - ')
        
        addMe = score + " - " + name
        scores.append(addMe)

#scores.sort(key = lambda x: x[1])
#scores.sort()


scores.sort(key=lambda x: int(x.split()[0]))

if len(scores) > 10:
    scores.pop(0)

with open("high_scores.txt", "w") as file:
    for element in scores:
        score, name = element.split('-')
        writeMe = name + " - " + score + '\n'
        file.write(writeMe)


#with open("arrayTest.txt", "w") as file:
    #file.write(str(scores))
