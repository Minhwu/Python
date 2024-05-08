from pathlib import Path
path = Path("./learning_python.txt")


# read text
content = path.read_text()
print(content)
print ("=" * 60)
lines = content.splitlines()
for line in lines:
    print(line)
    

# write text
path = Path("./guest_book.txt")
names = ""
user_input = input("Please input username: ")
while user_input != "q":
    names += user_input + "\n"
    user_input = input("Please input username: ")
    
path.write_text(names)