#! python3

# Import libraries
#import openpyxl
import pandas as pd
#import xlsxwriter
#import xlrd
import os
import csv
import re # regex may not be needed
import random
from time import sleep
import xlsxwriter
#import timeit



# main(excel sheet)
  # Output a sorted excel sheet by platoons (groups), using define parameters (age, sex)

# Create a list for each row and convert file to csv
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
  #print(original_list)    
  return original_list


#  Ask user for number of "platoons"
def divide_into_platoons(thirteen, fifteen, seventeen, females):
  platoon_list = []
    #print(platoon_list)
    
    # Create empty lists for a range of possible platoons. Only need to add more platoons to this list
    # if more is needed.
  platoon_first = []
  platoon_second = []
  platoon_third = []
  platoon_fourth = []
  platoon_fifth = []
  platoon_sixth= []
  platoon_seventh = []
  platoon_eight = []    
    
    # Add any platoons added above to this list as well, keeping the same naming convention and order.
  max_list = [platoon_first, platoon_second, platoon_third, platoon_fourth, platoon_fifth, platoon_sixth, platoon_seventh, platoon_eight]
    
  platoons = int(input('How many Basic Training Platoons?\n'))
    