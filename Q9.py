import pickle
book={"C++":200}
f=open("libary.txt","ab")
pickle.dump(book,f)
f.close()
