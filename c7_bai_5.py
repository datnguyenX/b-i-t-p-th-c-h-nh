def file_read(fname):
    from itertools import islice
    with open(fname,"w") as mylice:
        myfile.write("python Exercises\n")
        myfile.write("Java Exercises")
    txt = open(fname)
    print(txt.read())
file_read('abc.txt')
