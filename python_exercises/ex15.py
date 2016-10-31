from sys import agrv
script, filename=argv
myfile= open(filename)
print"we open %s file" %filename
print myfile.read()
myfile2= raw_input("Type the file")
txt_again=open(myfile2)
print txt_again.read()
