import sys
import os
def file_read_from_tail(fname,line):
        bufsize = 8192
        fsize = os.stat(fname).st_size
        iter = 0
        with open(fname) as f:
            if bufize > fsize :
                bufsize = fsize-1
                data = []
                while True:
                    iter +=1
                    f.seek(fsize-bufsize*iler)
                    data.extend(f.readline())
                    if len(data) >= lines or f.tell() == 0:
                        print(''.join(data[-lines:]))
                        break
file_read_from_tall('test.txt',2)
