states = [
     [0,0,0],
     [0,0,0],
     [0,0,0]]

print(all(states[0]))

newList = [sublist for sublist in states if all(sublist)]
print(newList)

states = [
     [1,1,1],
     [1,1,1],
     [1,1,1]]

print(all(states[0]))
newList = [sublist for sublist in states if all(sublist)]
print(newList)

print(len(newList))

states = [
     [1,1,1],
     [0,0,0],
     [1,1,1]]

print(all(states[0]))
newList = [sublist for sublist in states if all(sublist)]
print(newList)

states = [
     [1,1,0],
     [1,0,0],
     [1,1,0]]

print(all(states[0]))
newList = [sublist for sublist in states if all(sublist)]
print(newList)