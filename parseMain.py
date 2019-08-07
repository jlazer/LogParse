#Justin Lazarski 2019
infile = r"/home/test/Desktop/Parse/input/testLog.txt"

important = []
keep_phrases = [ "test","important","keep me","error"]

with open(infile) as f:
	f = f.readlines()

for line in f:
	for phrase in keep_phrases:
		if phrase in line:
			important.append(line)
			break
print(important)



