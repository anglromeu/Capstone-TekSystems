#!/usr/bin/env python3

import openpyxl
import pandas as pd
import xlsxwriter
import xlrd
import os
import csv


#main(excel sheet)
  #Output a sorted excel sheet by platoons (groups), using define parameters (age, sex)
def main():
#Read excel file from generated report
  original = pd.read_excel('list_10.xlsx')
#print (original)

#Convert excel to csv
  original.to_csv('list_10.csv',
                index = None,
                header = True)
  original_csv = pd.DataFrame(pd.read_csv('list_10.csv'))
#print(original_csv)

#Create a one list for each row
  with open("list_10.csv") as f:
    reader = csv.reader(f)
    original_list = list(reader)
#print(original_list)

#Ask user for number of "platoons"
  platoons = int(input('How many Basic Training Platoons?\n'))

#Creat list for each age group
  #thirteen = 13-14
  #fifteen = 15-16
  #seventeen = 17
  thirteen = []
  fifteen = []
  seventeen = []


#Search age column and add each line of infromation from exel to appropriate age group
  #use regex to achive this
  #loop can be use here
  #exit loop after all names on excel sheet are assigned to lists
  #chance to use a while loop

#Search each list for females using regex
  #assign females to a new list
  #if element can be use here

#Iterate through each age group list and randomly assign to each platoon list
  #function should exit once age group and female list are empty
  #considering random.sample()
  #each platoon list should have an aproximate number of people (evenly distrubuted prerred)

#Search female list and add to appropriate age group list (lists should be empty now)

#Iterate through each age group list and randomly assign to each platoon list

#Create a new excel sheet with platoon assignments
  #Considering xlswriter
  #ideally sheet should alphabetize by last name
  #save excel sheet in the same folder as the original




#TODO test scripts for each function need to be created
#TODO ensure PEP8 compliance
  #consider automating this task