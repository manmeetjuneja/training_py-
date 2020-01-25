def get_info_dictonary(x):
    A = datastore["office"].get(x,{})
    print(A)
    
'''def delete_medical_info(A):
    del datastore["office"]["medical"][A]
    print(datastore[medical])
'''
'''def deep_get(datastore,keys,default="None"):
    assert type(keys) is list
    if datastore is list:
        return default
    if not keys:
        return datastore
    return deep_get(dataframe.get(keys[0]),keys[1:],default)
'''            
def get_keys_base(A):
    for k,v in datastore.items():
        if k ==A:
            print(v)

#def get_value(datastore):
    


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
print("to get info of department:")
A = input()
#get_info_dictonary(A)
#delete_medical_info(A)
#deep_get(datastore,["office"],"room number")
get_keys_base(A)


#https://stackoverflow.com/questions/51788550/parsing-json-nested-dictionary-using-python
