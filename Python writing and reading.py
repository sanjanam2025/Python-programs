file_path="my_file.txt"
content_to_write="Hello, Python!\nThis is a new line."
content_to_overwrite="This is the new content."
content_to_append="This is the appended content."
with open(file_path,'w')as file:
    file.write(content_to_write)
    print(f"Content written to'{file_path}'.")
with open(file_path,"r")as file:
    content=file.read()
print(f"Content read from '{file_path}'.\n",content)
with open(file_path,'w')as file:
    file.write(content_to_overwrite)
    print(f"Content written to'{file_path}'(overwrite existing content).")
with open(file_path,"r")as file:
    content=file.read()
print(f"overwritten content read from '{file_path}'\n",content)