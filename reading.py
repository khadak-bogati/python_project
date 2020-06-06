f = open("demofile.txt", "r")
print(f.read())
print(f.name)
print(f.mode)
FileContent = f.read()
print(FileContent)
f.close()



output
.........................
This is file 1
this is file 2
this is file 3

demofile.txt
r


ex======================2
example1 = "demofile.txt"
file1 = open(example1, "r")

with open(example1, "r") as demofile:
	FileCOntent = demofile.read()
	print(FileCOntent)
print(FileCOntent)

output
..................
This is file 1
this is file 2
this is file 3

This is file 1
this is file 2
this is file 3



ex================================3
example1 = "demofile.txt"
file1 = open(example1, "r")

with open(example1, "r") as demofile:
	print(demofile.read(4))
	print(demofile.read(8))
	print(demofile.read(12))
	print(demofile.read(15))
  
  output
  .........................
  This
 is file
 1
this is f
ile 2
this is f




ex===========================4
example1 = "demofile.txt"
file1 = open(example1, "r")

with open(example1, "r") as demofile:
	print("first line " + demofile.readline())
  
  output
  ....................
  first line This is file 1
  
  
  ex=======================5
  print("We can use a loop to iterate through each line:")
example1 = "demofile.txt"
file1 = open(example1, "r")

with open(example1, "r") as demofile:
	i = 0;
	for line in demofile:
		print("iteration", str(i), ":", line)
		i = i +1;
    
    output
    We can use a loop to iterate through each line:
iteration 0 : This is file 1

iteration 1 : this is file 2

iteration 2 : this is file 3


ex=============================6
print("We can use the method readlines() to save the text file to a list:")
example1 = "demofile.txt"
file1 = open(example1, "r")

with open(example1, "r") as demofile:
	FileasList = demofile.readlines()
	print("Each element of the list corresponds to a line of text:")
	print(FileasList[0])
	print(FileasList[1])
	print(FileasList[2])
  
  output
  ...................
  We can use the method readlines() to save the text file to a list:
Each element of the list corresponds to a line of text:
This is file 1

this is file 2

this is file 3


ex============================7
print("Write line to file:")
example1 = "demofile2.txt"
file1 = open(example1, "w")

with open(example1, "w") as writefile:
	writefile.write("This is line A \n")
	writefile.write("This is line B \n")
	writefile.write("This is line C \n")
	
with open(example1, 'r') as testwritefile:
	print(testwritefile.read())
  
  
  output
  .................
  Write line to file:
This is line A
This is line B
This is line C


ex=======================8
print("Write line to file:")
example1 = "demofile2.txt"
file1 = open(example1, "w")

lines = ["This is line A\n", "This is line B\n", "This is line C\n"]

with open('demofile2.txt', 'w') as writefle:
	for line in lines:
		print(line)
		writefle.write(line)
	
	
with open(example1, 'r') as testwritefile:
	print(testwritefile.read())


with open('demofile2.txt', 'r') as readfile:
	with open('demofile3', 'w') as writefile:
		for line in readfile:
			writefile.write(line)
with open('demofile3', 'r') as testwritefile:
	print(testwritefile.read())
  
  
  output
  ...................
This is line A
This is line B
This is line C


