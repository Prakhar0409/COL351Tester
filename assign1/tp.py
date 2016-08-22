########!/home/prakhar/Desktop/sem5/COL351/test/tp/bin/python

""" TestingCOL351: Runs tests on your program and matches it with the expected result on the website. Usage: python tp.py 'hw#' """

import urllib2 as ul
import sys
from bs4 import BeautifulSoup
import re
import os

base = 'http://www.cse.iitd.ac.in/~rjaiswal/2016/col351'
headers = { 'User-Agent' : 'Mozilla/5.0' }



def grab(hw):
	req = ul.Request('http://www.cse.iitd.ac.in/~rjaiswal/2016/col351/tc.html',None,headers)
	res = ul.urlopen(req)

	html = res.read()
	res.close()
	#print html
	soup = BeautifulSoup(html,'html.parser')
	inps = []
	outs = []
	for l in soup.find_all('a'):
		x = re.search(hw+"/input",l['href'])	
		if(x):
			inps.append(l['href'])
		x = re.search(hw+"/output",l['href'])
		if(x):
			outs.append(l['href'])	

	os.system('make')
	count = 1
	for (i,o) in zip(inps,outs):
		url = base+i[1:]
	#	print url
		inF=open("input.txt",'w')
		req1 = ul.Request(url,None,headers)
		res1 = ul.urlopen(req1)
		data = res1.read()
		inF.write(data)
		inF.close()
		os.system('make run')
	
		outF=open("output.txt",'r')
		url = base+o[1:]
		req1 = ul.Request(url,None,headers)
		res1 = ul.urlopen(req1)
		data = res1.read()
		d1 = outF.read()
#		print d1
#		print data
		if(d1==data):
			print "Hurray testcase %d passed\n" % count
		else:
			print "testcase %d failed. Check for endlines etc.\n" % count
		count = count +1
		outF.close()
	res.close()

#if(sys.argv<=1):
#	print "You forgot to enter the homework number. Usage: python tp.py 2"
#else:
#	print "Processing request"

a = "HW"
if(sys.argv[-1].isdigit()):
	a = a+sys.argv[-1]
	grab(a)
else:
	print "Usage: python tp.py 1"

