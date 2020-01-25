def get_info_dictonary(x):
    A = datastore["office"].get(x,{})
    print(A)
    A = list(A.keys())
    print(A)
    B = str(A) 
    file = open("output.txt","w")
    file.write(B)
    file.close()

def store_info(x):
    A = datastore["office"]
    print(A)

def change_entry():
    print("inside change entry function")
    spaces = datastore['office']['medical']
    for item in spaces:
        if item.get('use') == "examination" :
           item['price'] = 175

    for item in datastore['office']['medical']: # This loop shows the change is not only in books, but is also in database
        if item.get('use') == "examination" :
            print("The {} rooms now price {}".format(item.get("use"), item.get("price")))
    
            
def get_keys_base(A):
    for k,v in datastore.items():
        if k ==A:
            print(v)

      
def get_value(off,room):
    if datastore[off]:
        for key,value in datastore[off].items():
            for v in value:
                for k,num in v.values():
                    if num==room:
                        print("present:"+str(num))
                    else:
                        pass                            

datastore = {   
            "office":{
                        "medical":
                        [
                            {"room number":100,"use":"reception","sq-ft":50,"price":75},
                            {"room number":101,"use":"waiting","sq-ft":250,"price":75},
                            {"room number":102,"use":"examination","sq-ft":125,"price":150},
                            {"room number":103,"use":"examination","sq-ft":125,"price":150},
                            {"room number":104,"use":"office","sq-ft":150,"price":100}
                        ],  
                        "parking":
                            {"location":"premium","style":"covered","price":750}
                      }
             }
#print(datastore)
'''userinput = input("enter new room number:")
print(replace_room(userinput, BRANDS)
'''
change_entry()
print("to get info of department:")
A = input()
get_info_dictonary(A)
#print(datastore["office"]["medical"].get(0,{}))
#get_value("office",101)
#get_keys_base(A)


