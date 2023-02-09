def search(word):
    try:
        f=open("cities.txt",'rt')
        line_count=0
        for line in f.readlines():
            line_count+=1
            strlist=line.split(" ")
            word_count=0
            for w in strlist():
                word_count+=1
                if word==w:
                    return(line_count,word_count)
            else:
                return None
        f.close()
    except Exception:
        print("file not found")
d=search("delhi")
print(d)
  
