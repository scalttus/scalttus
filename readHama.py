matrix = [0,3]


source = "Hama.inv"
list = []
with open(source, "r") as f:
    content = f.readline()
    for i in matrix:
        data = content[0:3]
        list.append(data)       
        print(list)