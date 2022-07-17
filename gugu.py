# import sys

# sys.stdout = open('./Test.txt','w',encoding='utf-8')
f = open("./Test.txt", "w", encoding='utf-8')
for i in range(2,10):
    for x in range(1,10):
        if i == 8:
            continue
        else:
            lines = (str(i),"X",str(x),"=", str(i*x),"\n")
            f.writelines(lines)
            # f.write("{} x {} = {}\n".format(i,x,i*x))
f.close()
# sys.stdout.close()