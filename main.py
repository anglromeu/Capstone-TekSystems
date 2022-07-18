#!/usr/bin/env python3

import pandas as pd
import xlsxwriter
import os
import csv
import re
import random
from time import sleep
import xlswriter


#main(excel sheet)
  #Output a sorted excel sheet by platoons (groups), using define parameters (age, sex)
# Create a list for each row
def make_list():
  file_name = input('Enter the xlsx file you want to work with: ')
  # Take xlsx data name, convert to csv to be used in our program
  read_file = pd.read_excel(f"{file_name}.xlsx")

  read_file.to_csv(f"{file_name}.csv",
                index = None,
                header=True)
  # Open and read the csv 
  with open(f"{file_name}.csv") as f:
      reader = csv.reader(f)
      original_list = list(reader)
  return original_list




#TODO test scripts for each function need to be created
#TODO ensure PEP8 compliance
  #consider automating this task