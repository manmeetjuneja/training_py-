matrix = [ [1,2,3],
            [4,5,9,7],
           [6,7,8,9]
        ]
flatten_matrix = []
for a in matrix:
    for b in a:
        flatten_matrix.append(b)

print(flatten_matrix)


# flatten in one line
f_m = [va for sb in matrix for va in sb]
print(f_m)

#nested list in if condition
planets = [
                    ["mercury","venus","earth"],
                    ["mars","jupiter","saturn"],
                    ["uranus","neptune","pluto"]
                ]
fla_p = [planets for sublist in planets for planets in sublist if len(planets)<6] 
print(fla_p)
