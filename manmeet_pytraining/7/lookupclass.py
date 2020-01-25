#function to look up in the dictonary 
def look():
    for key in dic.keys():
        print('name of Users: {}'.format(key, dic[key]))


# function to add into the dictonary
def add(U_name,name,sname):
    dic[U_name] = {"name":name,"surname":sname}
    print(dic)
    print("user added")
# function to change an exixting
def change(U_name,name,sname):
    print()
    print("add user name to change:")
    dic[U_name] = {"name":name,"surname":sname}
    print(dic)
    print("user details changed):")

#function to delete a contact
def delete(dic,name):
    dic.pop(name)
    print(dic)

#function to quit the progam 
dic = {
            "user1":
            {
                 "name":"Gikas",
                  "Surname":"Goyal"
            },
            "user2":
            {
                "name":"Bhuvan",
                "Surname":"Bam"

            }

        }
look()
U_name = str(input("add user as(user(1-20): "))
name = str(input("enter name: "))
sname = str(input("enter surnname: "))
add(U_name,name,sname)
#change(u_name,name,sname)
#delete(dic,name)

