# Dictionary comprehension
# Square = {1:1,2:4,3:9}
square = {f"square of {nums}":nums**2 for nums in  range(1,11)}
# print(square)
# for i , j in square.items():
    # print(f"{i}:{j}")e


name = "ayushpanchal"
counts = {char : name.count(char) for char in name}
# print(counts)

# DC with if else
d = {i:('even'if i %2 == 0 else 'odd') for i in range(1,11)}
print(d)
for ii, j in d.items():
    print(f"{ii}:{j}")