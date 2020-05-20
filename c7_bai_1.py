imput_file=open('D:/a.txt','r')
for lne in input_file:
    l=len(line)
    s=''
    while(l>=1):
        s=s+line[l-1]
        l=l-1
    print(s)
input_file.close()
