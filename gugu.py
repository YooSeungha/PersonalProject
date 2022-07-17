# import sys

# sys.stdout = open('./gugu.txt','w',encoding='utf-8')
f = open("./Test.txt", "w")
for i in range(2,10):
    for x in range(1,10):
        if i == 8:
            continue
        lines = (str(i),"X",str(x),"=", str(i*x),"\n")
        f.writelines(lines)
f.close()
# f.sys.stdout.close()
