word ="donkey"
with open("article.txt") as i:
    read = i.read()
    newread = read.replace(word,"######")

with open("article.txt","w") as i:
    i.write(newread)
    