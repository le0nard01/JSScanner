#import faster_than_requests as requests
import concurrent.futures
import requests
from concurrent import futures
#import requests as r 
import re 
import urllib3 
import sys 
import os
import colored
from colored import stylize
urllib3.disable_warnings()

path = input("Path of the file containing the urls: ") 
reg = input("Path of the file containing the regex: ")
list=[] 
file1 = open(path, 'r')
Lines = file1.readlines() 
count = 0
# Strips the newline character

print('-----------------------------//-----------------------')

for line in Lines: 
    ip = line.strip()
    print(colored.fg("white"), ip)
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [
                executor.submit(
                    lambda: requests.get(ip))
            for _ in range(1)
        ]
            

        results = [
            f.result().text
            for f in futures
        ]

        
        
        file2 = open(reg, 'r')
        Lines2 = file2.readlines()
        for line2 in Lines2: 
            regex = line2.strip()
            matches = re.finditer(regex, str(results), re.MULTILINE)
            for matchNum, match in enumerate(matches, start=1):
    
                print (colored.fg("green") ,"Regex: ",regex)
                print(colored.fg("red") , "Match {matchNum} was found at: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()), '\n')
                f = open('out.txt', 'a')
                L = [ip, '\n', "Regex: ", regex, '\n', "Match {matchNum} was found at : {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()),'\n']
                f.writelines(L)
                f.close()
           
    except requests.exceptions.RequestException as e:
        # A serious problem happened, like an SSLError or InvalidURL
        print("Error: {}".format(e))    

print("\n\nYou can see the results in out.txt file")
