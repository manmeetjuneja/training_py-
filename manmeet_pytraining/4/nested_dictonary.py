people = {
            1:{"name":"John","age":"27","sex":"Male"},
            2:{"name":"Marie","age":"22","sex":"Female"}
    
        }

print(people[1]["name"])

print("Firts Dictonary:"+str(people[1]))

  #inserting line wise 

people[3] = {}
people[3]["name"] = "Luna"
people[3]["age"] = "27"
people[3]["sex"] = "Female"
people[3]["married"] = "Yes"
print(people[3])
    #inserting line 
people[4] = {
                "name":"John","age":"27","sex":"Male","married":"no"

            }
print(people)

del people[3]["married"]
del people[4]["married"]
print(people[3])
print(people[4])

for p_id, p_info in people.items():
    print("Person ID",p_id)
    for key in p_info:
        print(key+":",p_info[key])
