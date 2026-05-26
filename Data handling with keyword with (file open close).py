with open("python.txt","w") as file:
    file.write("My name is Sanjana")
with open("python.txt","r") as file:
    content=file.read()
    print(content)
file.close()