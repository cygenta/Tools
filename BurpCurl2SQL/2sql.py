# _______           _______  _______  _       _________ _______ 
#(  ____ \|\     /|(  ____ \(  ____ \( (    /|\__   __/(  ___  )
#| (    \/( \   / )| (    \/| (    \/|  \  ( |   ) (   | (   ) |
#| |       \ (_) / | |      | (__    |   \ | |   | |   | (___) |
#| |        \   /  | | ____ |  __)   | (\ \) |   | |   |  ___  |
#| |         ) (   | | \_  )| (      | | \   |   | |   | (   ) |
#| (____/\   | |   | (___) || (____/\| )  \  |   | |   | )   ( |
#(_______/   \_/   (_______)(_______/|/    )_)   )_(   |/     \|
# 2014                                                               



import re
import sys

kommand = "sqlmap.py -o -a --batch -t c2s.txt --proxy='http://127.0.0.1:8080' "

header = ""
cookie = ""
data = ""
url = ""


def welcomescreen():
	print "welcome"

def curl_split(usercommand):
	global cookie
	global header
	global data
	global url
	print "processing curl command"
	patternsplit = re.compile(r'\\')
	patternfindH = re.compile(r' -H \'(.+?)\'')
	patternfindb = re.compile(r' -b \'(.+?)\'')
	patternfinddata = re.compile(r' --data-binary \$\'(.+?)\'')
	patternURL = re.compile(r'\'(.+?)\'$')

	for split in re.split(patternsplit,usercommand):
		for findH in re.findall(patternfindH,split):
			if header == "":
				header = findH
			else:
				header = header+"\\n"+findH
		
	        for findb in re.findall(patternfindb,split):
			cookie = findb
		for finddata in re.findall(patternfinddata,split):
			data = finddata
		for findURL in re.findall(patternURL,split):
			 url = findURL
	
	print kommand, "-u "+url, "--cookie='"+cookie+"'", "--data='"+data+"'", "--headers=\""+header+"\""

def paste_curlcommand():
	print "input your curl command here"
	#grab user input and fling to the next function
	print "paste here and then press ctrl+d twice"
	foob = sys.stdin.read()
	curl_split(foob)


welcomescreen()
paste_curlcommand()
