class Contact:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email

    '''def set_name(self):
        self.name = name
    def set_phone(self):
        self.phone = phone
    def set_email(self):
        self.email = email'''
    
    def get_name(self):
        return f'Name is:{self.name}'
    def get_phone(self):
        return f'Phone number is:{self.phone}'
    def get_email(self):
        return f'Email is"{self.email}'

def listToString(s):   
    str1 = " "    
    return (str1.join(s))      
  

def main():
    A = str(input("enter name"))
    B = str(input("enter contact number"))
    C = str(input("enter E mail"))
    C1 = Contact(A,B,C)
    list = [A,B,C]
    print(list)
    
    Stng = listToString(list)
    
    print(listToString(list))
    
    file = open("Contact.txt","w")
    file.write(Stng)
    print(C1.get_name())
    print(C1.get_phone())
    print(C1.get_email())
    
main()
