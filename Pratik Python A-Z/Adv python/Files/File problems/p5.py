#first just make a list of removed words 
words = ["monkey","bad","ganda","dog"]
with open("article.txt","r") as i:
        content = i.read()
for word in words:
        if word in content:
           content = content.replace(word,len(word)*"#")
with open("article.txt","w") as j:
      j.write(content)
with open("article.txt") as j:
      print(j.read())