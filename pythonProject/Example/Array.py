data = ['apple','grape','orange','watermelon','pineapple','Banana','Mango','Apricots','Blackberries','Honeydew']
fruits = ""
for i in range(len(data)):
    fruits += " "+data[i]
    if i > 5:
        print(i,fruits)