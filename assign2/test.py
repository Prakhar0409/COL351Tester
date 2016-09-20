
inp = [line.rstrip('\n') for line in open('input.txt')]
outp = [line.rstrip('\n') for line in open('output.txt')]

#print outp
if(len(outp[0])==1 and outp[0][0]=='0'):
	print "Havent checked for invalid cases :("
	exit()
rows = inp[1].split(",")   
cols = inp[2].split(",")

flag = True
vals = [[x for x in r.split(",")] for r in outp[1:]] 

tmp =0
for i in range(0,int(inp[0])):
	tmp = 0
	for j in range(0,int(inp[0])):
		tmp = tmp + int(vals[i][j])
	if(tmp!=int(rows[i])):
		flag = False
		print "you fucked up in %dth row sum. Expected: %d You get: %d" % (i,int(rows[i]),tmp)



tmp =0
for i in range(0,int(inp[0])):
	tmp = 0
	for j in range(0,int(inp[0])):
		tmp = tmp + int(vals[j][i])
	if(tmp!=int(cols[i])):
		flag = False
		print "you fucked up in %dth col sum. Expected: %d You get: %d" % (i,int(cols[i]),tmp)

if flag == True:
	print "Hurray u passed the test case"
