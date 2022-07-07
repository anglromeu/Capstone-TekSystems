"""
#Github help

  # the git command (may have to specify "/usr/bin/git" for example)
git: git

# the temp directory that sync will use for cloning
tmp: tmp-sync

# set to true to stop subsequent cloning upon failing to clone any repository 
abort-on-failure: false

# the list of repositories to clone, in the order provided
repositories:

# this will clone the specified repo with the branch dev into the working directory
- url: git@github.com:thekeenant/repo1.git
  branch: master
  target: ./

# this will clone the specified repo with the branch dev into ./repo2-copy
- url: git@github.com:thekeenant/repo2.git
  branch: dev
  target: ./repo2-copy
"""


#import pandas
#import xlswriter
#import os

#main(excel sheet)
  #Output a sorted excel sheet by platoons (groups), using define parameters (age, sex)

#Read excel sheet from generated report
  #use pandas library to import file and read excel file

#Ask user for number of "platoons"
  #input("How many platoons? ")
  #assign a list variable based on int input
  #Platoon 1, Platoon 2, Platoon 3, etc

#create age group empty list
  #group ie 13-14, 15-16, 17

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




#TODO Create excel sheet data with names, age and sex
  #considering mockaroo.com
#TODO test scripts for each function need to be created
#TODO ensure PEP8 compliance
  #consider automating this task