

source = "Hama.inv"

with open(source, "r") as  f:
    
    size_to_read = 10
    
    f_contents = f.read(size_to_read)
    print(f_contents, end=" ")  
    
    f.seek(0)
    
    f_contents = f.read(size_to_read)
    print(f_contents)  
    
    
    # while len(f_contents) > 0:
    #     print(f_contents, end='*')   
    #     f_contents = f.read(size_to_read)


    
    # for line in f:
    #     print(line, end='')