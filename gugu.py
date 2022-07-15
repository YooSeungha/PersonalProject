

f = open("./Test.txt", "w")
for i in range(2,10):
    for x in range(1,10):
        if i == 8:
            continue
        lines = (str(i),"X",str(x),"=", str(i*x),"\n")
        f.writelines(lines)
f.close()
