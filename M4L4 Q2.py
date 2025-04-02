# allow the program to read the txt file
filename = "learning_python.txt"

print("reading in the entire file:")
# create object to read the whole txt file
with open (filename) as f:
    contents = f.read()
print(contents)

print()
print("looping over the file oject:")
# create object to loop over the file object; 
with open (filename) as f:
    for line in f:
        print(line.strip())

print()
print("storing the lines in a list then working with them outside the with block:")
# create opbject to make the lines in a list then show them in a list
with open (filename) as f:
    lines = [line.rstrip() for line in f]
print(lines)

print("\nreplacing python with PHP:")
# create obejcet that replaces part of the txt file
with open (filename) as f:
    lines = f.readlines()

for line in lines:
    line = line.rstrip()
    print(line.replace("Python", "PHP"))





