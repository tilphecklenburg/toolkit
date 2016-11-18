import filefunctions
import os
import openpyxl

#----Crawl directory for text files containing string, export results to Excel file-----
directory = raw_input("directory to search: ")
searchstring = raw_input("search string (not case sensitive): ")

report = filefunctions.createexceldoc("report")

reportsheet = filefunctions.createexcelsheet(report,"results")

filefunctions.searchdirforstring(directory,searchstring,reportsheet)

report.save(filename = "results.xlsx")

#----------------------------------------------------------------------------------------