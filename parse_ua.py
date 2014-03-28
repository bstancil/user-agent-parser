#!/usr/bin/env python

import httpagentparser
import csv
import json
import sys

def read_table(csv_name,include_header):
    table = []
    
    with open(csv_name, 'Ub') as csvfile:
        f = csv.reader(csvfile, delimiter=',')
        firstline = True
        
        for row in f:
            if firstline == False or include_header == True:
                table.append(tuple(row))
            firstline = False
    
    return table

def write_to_csv(csv_name,array):
    columns = len(array[0])
    rows = len(array)
    
    with open(csv_name, "wb") as test_file:
        file_writer = csv.writer(test_file)
        for i in range(rows):
            file_writer.writerow([array[i][j] for j in range(columns)])

input_file = sys.argv[1]
output_file = sys.argv[2]

file = read_table(input_file,True)

output = []
headers = ('browser','browser_version','platform','platform_version','os','flavor','flavor_version','dist','dist_version')

for i in range(len(file)):
    if i == 0:
        entry = file[i] + headers
    
    else:
        r = file[i]
        result = httpagentparser.detect(r[0])
        
        try:
            browser = result['browser']['name']
            browser_version = result['browser']['version']
        except:
            browser = ''
            browser_version = ''
        
        try:
            platform = result['platform']['name']
            platform_version = result['platform']['version']
        except:
            platform = ''
            platform_version = ''
        
        try:
            os = result['os']['name']
        except:
            os = ''
            
        try:
            flavor = result['flavor']['name']
            flavor_version = result['flavor']['version']
        except:
            flavor = ''
            flavor_version = ''
        
        try:
            dist = result['dist']['name']
            dist_version = result['dist']['version']
        except:
            dist = ''
            dist_version = ''
        
        
        entry = r + (browser,browser_version,platform,platform_version,os,flavor,flavor_version,dist,dist_version)
    
    output.append(entry)

write_to_csv(output_file,output)
    