import pickle
f=open("libary.txt","rb")
s=pickle.load(f)
for key in s:
    print(s[key])
f.close()