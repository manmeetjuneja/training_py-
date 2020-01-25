'''from collections import Counter
def remove_duplicates(stirng):
    string = string.split(" ")
    for i in range(0, len(string)): 
        string[i] = "".join(string[i])
    UniqW = Counter(string)
    s = " ".join(UniqW.keys()) 
    print (s)'''
string=[n for n in input("enter a sequence of words:").split(' ')]
string.sort()
print(" ".join(string))
print("Final list:")
#remove_duplicates(string)   


