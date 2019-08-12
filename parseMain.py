#Justin Lazarski 2019
infile = r"/home/test/Desktop/Parse/input/syslog.txt"

#infile = r"/home/test/Desktop/Parse/input/testLog.txt"

#usrPath = str(input("Input the path of the log file you want to parse: "))
#nfile = r(path)
#print(usrPath)

relevant = []
keywords = []
usrInptLower = ''
usrInptUpper = ''

usrInpt = str(input("Input a keyword to parse the file for: "))

if usrInpt.isupper():
	usrInptLower = usrInpt.lower()
	usrInptUpper = usrInpt

else:
	usrInptUpper = usrInpt.upper()
	usrInptLower = usrInpt



keywords.append(usrInptLower)
keywords.append(usrInptUpper)

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

#exports the array Relevant to a text file
with open("output.txt", "w") as txt_file:
	for line in relevant:
		txt_file.write("".join(line) + "\n")

