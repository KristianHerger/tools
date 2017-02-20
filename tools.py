import requests  # http://docs.python-requests.org/en/latest/
import csv
import os


def removeFile(name):
	try:
		os.remove(name)
	except OSError:
		pass


def fetchHTML(_url, _allow_redirects=False, _print=False, _verify=True):

	r = requests.get(_url, allow_redirects=_allow_redirects, verify = _verify)

	if _print == True:
		print('tools.fetchHTML: ' + _url)

	if (r.encoding != 'utf8') and (r.encoding != None):
		st = r.content.decode(r.encoding)

	else:
		st = r.text


	return str(st)


def getStatus(_url, _print = True):

	r = requests.get(_url, allow_redirects=False)
	if _print is True:
		print (_url + ': ' + str(r.status_code))	

	return r.status_code

def getR(_url, _print = True, _verify = True):

	try:
		r = requests.get(_url, verify = _verify)
	
	except:
		r = False

	if _print is True:
		print (_url)	

	return r

def appendLine(where, lineArr, _delimiter=';', _encoding='utf8'):
	with open(where, 'a', encoding=_encoding, newline='') as csvfile:
		csvwriter = csv.writer(csvfile, delimiter = _delimiter, quotechar='|', quoting=csv.QUOTE_MINIMAL)
		csvwriter.writerow(lineArr)


# def readCSV(where, _delimiter=';', _quotechar='|', ):

# 	with open(where, newline='') as csvfile:
# 		r = csv.reader(csvfile, delimiter = _delimiter, quotechar = _quotechar)
# 		

# 		for row in r:


