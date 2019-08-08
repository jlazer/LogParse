#Justin Lazarski 2019
infile = r"/home/test/Desktop/Parse/input/syslog.txt"

#infile = r"/home/test/Desktop/Parse/input/testLog.txt"

#usrPath = str(input("Input the path of the log file you want to parse: "))
#nfile = r(path)
#print(usrPath)

relevant = []
keywords = []

usrInpt = str(input("Input a keyword to parse the file for: "))

keywords.append(usrInpt)
print(keywords)

with open(infile) as f:
	#f = f.readlines()
	for line in f:
		for phrase in keywords:
			if phrase in line:
				relevant.append(line)
				break

print("Relevant Lines: ")
print(relevant)
