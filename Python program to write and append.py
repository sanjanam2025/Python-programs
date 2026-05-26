file_path="my_file.txt"
content_to_write="Hello,python!\nThis is a new line."
content_to_overwrite="This is the new content."
content_to_append="\nThis is the appended content."
with open(file_path,'a')as file:
    file.write(content_to_append)
    print(f"Content appended to '{file_path}'.")
with open(file_path,"r")as file:
    content=file.read()
    print(f"appended content read from'{file_path}'\n",content)