print("enter values into dictonary:")
'''indian_batsman = {}
keys = {"type of player",""}
for i in range(len(keys)):
    values = input()
    indian_batsman[keys] = values
    
print(indian_bastman)
'''
players = {
            "Batsman":{"Rohit Sharma":{"Matches":206,"Runs":345688,"Average":47.984,"Highest Score":264},
                       "Virat Kohli":{"Matches":267,"Runs":3456897,"Average":50.984,"Highest Score":183}

                       }

        }
print(players["Batsman"]["Rohit Sharma"]["Average"])
max_average = max(int(i["Runs"]) for i in players.values())
print(max_average)
