lines_to_write = [
  "First line of text.\n",
  "Second line with more information.\n",
  "Third and final line."
]
with open("my_file.txt", "w") as file:
 file.writelines(lines_to_write)
with open("my_file.txt", "r") as file:
 line1 = file.readline()
 line2 = file.readline(10)
print(f"First line: {line1.strip()}") 
print(f"Second line: {line2.strip()}")
