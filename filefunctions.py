#-------import required modules for functions below----------------------
from openpyxl import Workbook
import os
#------------------------------------------------------------------------

#-------create a new Excel workbook using OpenPyxl-----------------------
def createexceldoc(filename):
	filename = Workbook()
	print "workbook created"
	return filename
#------------------------------------------------------------------------	

#-------create a new Excel worksheet using OpenPyxl----------------------
def createexcelsheet(workbookname,sheetname):
	excelsheet = workbookname.create_sheet(title = sheetname)
	print "sheet created"
	return excelsheet
#------------------------------------------------------------------------

#-------search for string in a .txt file---------------------------------
def searchtextfile(filename,searchphrase,reportsheet):
	rowcount = 1
	file = open(filename,"r+")
	for line in file.readlines():
		if searchphrase in line:
			reportsheet['A' + str(rowcount)] = searchphrase
			reportsheet['B' + str(rowcount)] = line
			rowcount += 1
#------------------------------------------------------------------------	

#-------open text file and turn into a list------------------------------
def parsetextfiletolist(filename):
	file = open(filename,"r+")
	list = file.read()
	list = list.split()
	return list
#------------------------------------------------------------------------

#-------gather directory listing and parse/search each file within dir---
def searchdirforstring(dir,string):
	return "This function can only crawl text files at the moment"
	dirlist = os.listdir(dir)
	for file in dirlist:
		searchdata = open(file,"r+")
		searchdata = str(searchdata.read())
		searchdata = searchdata.split("\n")
		for line in searchdata:
			if string.lower() in line.lower():
				return "match found"
				return line
			