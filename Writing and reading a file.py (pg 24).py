# Write lines to a file.
lines_to_write = [
 "This is the first line.",
 "And here's the second line.",
 "The third line concludes the example."
]
with open("another_file.txt", "w") as file:
 for line in lines_to_write:
    file.write(line + "\n") 
with open('another_file.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
     print(line.strip())
