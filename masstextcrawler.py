import filefunctions
import os
import openpyxl
from fmcapifunctions import getdomainuuid
from fmcapifunctions import searchfmcnwobjects

#----Crawl directory for text files containing string, export results to Excel file-----

#searchstring = raw_input("search string: ")
"""
def search(searchstring):

	directory = "C:/scripts/Config Searcher/Config Files/"
	
	report = filefunctions.createexceldoc("report")

	reportsheet = filefunctions.createexcelsheet(report,"results")

	reportsheet, rowcount = filefunctions.searchdirformultistring(directory,searchstring,reportsheet)

	report.save(filename = "results - %s.xlsx" % searchstring)

#----------------------------------------------------------------------------------------
"""
"""
#----Search FMC for objects related to search string-------------------------------------

#fmcreport = filefunctions.createexceldoc("fmcreport")

#fmcreportsheet = filefunctions.createexcelsheet(report,"results")

domainuuid = getdomainuuid("fmc",
print domainuuid
reportsheet = searchfmcnwobjects("fmc",domainuuid,,reportsheet, searchstring,rowcount)

report.save(filename = "search results - %s.xlsx" % searchstring)
#----------------------------------------------------------------------------------------
"""

hosts = open("searchstrings.txt", "r+")

directory = "C:/scripts/Config Searcher/Config Files/"
	
report = filefunctions.createexceldoc("report")

reportsheet = filefunctions.createexcelsheet(report, "results")

reportsheet, rowcount = filefunctions.searchdirformultistring(directory, hosts, reportsheet)

report.save(filename="results.xlsx")
