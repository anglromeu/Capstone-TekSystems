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
    
    # Our pattern matching for platoon numbers
  match platoons:
    case 1:
      platoon_list.append(platoon_first)
    case 2:
      for i in range(0, 2):
        platoon_list.append(max_list[i])
    case 3:
      for i in range(0, 3):
        platoon_list.append(max_list[i])
    case 4:
      for i in range(0, 4):
        platoon_list.append(max_list[i])
    case 5:
      for i in range(0, 5):
        platoon_list.append(max_list[i])
    case 6:
      for i in range(0, 6):
        platoon_list.append(max_list[i])
    case 7:
      for i in range(0, 7):
        platoon_list.append(max_list[i])
    case 8:
      for i in range(0, 8):
        platoon_list.append(max_list[i])
    #case 9:
      #for i in range(0, 9):
        #platoon_list.append(max_list[i])
    #case 10:
      #for i in range(0, 10):
        #platoon_list.append(max_list[i])
    case _:
      print('Number not supported, try again.')
      #print(max_list)
    
    # Iterate through current ages and assign the males to the platoons, clearing list as we go.
    #Ryan Bradley assisted with this portion.  Thanks Ryan!!
    #  print('Males...')
  while thirteen != []:
    try:
      if thirteen == []:
        pass
      else:
        for set_platoon in platoon_list:
          set_platoon.append(thirteen[0])
          thirteen.pop(0)
    except:
      pass
  while fifteen != []:
    try:
      if fifteen == []:
        pass
      else:
        for set_platoon in platoon_list:
          set_platoon.append(fifteen[0])
          fifteen.pop(0)
    except:
      pass
  while seventeen != []:
    try:
      if seventeen == []:
        pass
      else:
        for set_platoon in platoon_list:
          set_platoon.append(seventeen[0])
          seventeen.pop(0)
    except:
        pass

    # Redo the lists, this time with the females
    # Iterate through each row, and add to the appropriate lists
    for row in females:
      if row[2] == 'Age':
        pass
      elif int(row[2]) == 13 or int(row[2]) == 14:
        thirteen.append(row)
      elif int(row[2]) == 15 or int(row[2]) == 16:
        fifteen.append(row)
      elif int(row[2]) == 17:        
        seventeen.append(row)
        
      # Redo platoon assignment for the females
      # Reshuffle to add more randomness
      random.shuffle(thirteen)
      random.shuffle(fifteen)
      random.shuffle(seventeen)

     # Iterate through each age list. When a name is put into a platoon, remove it from the list
    while thirteen != []:
      try:
        if thirteen == []:
          pass
        else:
          for set_platoon in platoon_list:
            set_platoon.append(thirteen[0])
            thirteen.pop(0)
      except:
        pass
      
    while fifteen != []:
      try:
        if fifteen == []:
          pass
        else:
          for set_platoon in platoon_list:
            set_platoon.append(fifteen[0])
            fifteen.pop(0)
      except:
        pass
      
    while seventeen != []:
      try:
        if seventeen == []:
          pass
        else:
          for set_platoon in platoon_list:
            set_platoon.append(seventeen[0])
            seventeen.pop(0)
      except:
        pass
   
    #print(females)  
    return platoon_list

#Advise the user if max capacity for females is reached
#Return a count of how many female bunks are needed  
def female_count():
    female_bunks = str(len(females))
    if int(female_bunks) > 100:
      print("Max capacity reached at 100")
    else:        
      print("Female bunks needed at Eagle's Landing: " + female_bunks)
    
  


# Main script area
if __name__ == "__main__":
    # Use previously created function to make the rows lists
    result = make_list()
    #print(result)
    result.pop(0)
    print(f"Number of Candidates dividing: {len(result)}")
    
    # Creat list for each age group
    # thirteen = 13-14
    # fifteen = 15-16
    # seventeen = 17
    thirteen = []
    fifteen = []
    seventeen = []
    females = []
  
    for row in result:
      if row[3] == 'Female':
        females.append(row)

    for row in females:
      if row[3] == 'Female':
        result.remove(row)
        
    female_count()       
    # Iterate through each row, and add to the appropriate lists
    for row in result:
      if row[2] == 'Age' or row[2] == 'age':
        pass
      elif int(row[2]) == 13 or int(row[2]) == 14:
        thirteen.append(row)
      elif int(row[2]) == 15 or int(row[2]) == 16:
        fifteen.append(row)
      elif int(row[2]) == 17:        
        seventeen.append(row)
      
      #print(result) 
          
    # Shuffle our lists prior to dividing
    random.shuffle(thirteen)
    random.shuffle(fifteen)
    random.shuffle(seventeen)
    random.shuffle(females)
    platoon_list = divide_into_platoons(thirteen, fifteen, seventeen, females)
    
    #print(platoon_list)
    # Write to xlsx, dividing the lists into their own sheets.
    with xlsxwriter.Workbook('Platoon List.xlsx') as workbook:
      for platoon in platoon_list:
          worksheet = workbook.add_worksheet()
          
          for row_num, data in enumerate(platoon):
            worksheet.write_row(row_num, 0, data)
    print(f'Job is done! Look for a file named "Platoon List.xlsx" inside the folder containing the original file. ')
   