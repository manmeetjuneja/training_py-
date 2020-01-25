import pickle
phonebook = {
                "Chris":"555-1111","Katie":"555-2222","Joanne":"555-3333"

            }
output = open("phonebook.txt","wb")
pb = pickle.dump(phonebook,output)
print(pb)

output = open("phonebook.txt","rb")
s=pickle.load(output)


print(s)
output.close()






