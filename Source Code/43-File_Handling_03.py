# -------------------------------------
# -- File Handling => Important Info --
# -------------------------------------

file = open(r"e:\mohamed\plain.txt", "a")


# truncate() => to trunc text from a file
file.truncate(10)


# tell() => return the position of the cursor
print(file.tell())


# seek() => adjust cursor postion
file.seek(5)
# print(file.read())

# hint: when writing on the file it will start from the end of the file
file.write("\nThis is new texttt\n")
