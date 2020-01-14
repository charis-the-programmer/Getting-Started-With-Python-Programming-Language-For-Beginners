### Breaking out of a Loop

while True:
    line = input(">")
    if line == "done":
        break
    print(line)
print("Done!")