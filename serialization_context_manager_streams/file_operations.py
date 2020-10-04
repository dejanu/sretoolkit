
import os
import sys

# File_object exposes API for sockets, on-disk File, in-memory buffer)
# File_object types: raw_binary, buffered binary, text(on-disk files)

# Create a file
s = "This is a sample text which need to be put in a file , on each line"

print(f"Current dir {os.getcwd()}")


##open file clasic way

##f = open('clasic_file.txt','w')
##try:
##    f.write("first line \n")
##    f.write("second line \n")
##finally:
##    f.close()
    

# open(file,mode) returns a STREAM (e.g: _io.TextIOWrapper)

# Stream classes:
# BytesIO - expects binary-like obj and produces bytes objects
# StringIO - expects str obj and produces str obj

f = open("ex.txt","w")
for w in s.split(" "):
    f.write(w+"\r\n")
f.close()

#default beahaviour for reading
with open("ex.txt","r") as f:
    for line in f:
        print(line)

#context manager and read 4 chars 
with open("ex.txt","r") as f:

    # no of chars
    size_to_read = 4

    # returns 0 if reaches EOF
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end="**")
        f_contents = f.read(size_to_read)

        
