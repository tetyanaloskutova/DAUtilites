"""
This snipped recodes files from encoding_read to encoding_write while splitting them 
in chunks file line_chunk
"""
import pandas as pd
import os
import sys
import io

encoding_read = 'cp860'
encoding_write = 'utf8'
folder = 'C:\\Users\\....\\'
filename_orig = 'GBLGARA'
filename_full = filename_orig + '.csv'
filename_counted = filename_orig+'-converted'
line_chunk = 100000
counter = 1
if not os.path.exists(folder + filename_orig):
    try:
        os.makedirs(folder + filename_orig)
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise
copy = io.open(folder + filename_orig + '\\' + filename_counted + str(counter) + '.csv',"wt",encoding=encoding_write)

with io.open(folder + filename_full,'r', encoding=encoding_read) as f:
    i = 0
    firstline = ''
    for line in f:
        
        if (i>line_chunk): 
            i = 0
            counter += 1
            copy.close()
            copy = io.open(folder + filename_orig + '\\' + filename_counted + str(counter) + '.csv',"wt",encoding=encoding_write)
            copy.write(str(firstline))
        text = line
		# some custome unreadable symbols 
        #text=text.replace('\u2265', 'a').replace('\u2264', 'I')
        #text=text.replace('\u2502', '|').replace('\u03c6','o').replace('\u2562','O').replace('\u03a9','U').replace('\u2593','A').replace('\u2561','A')
        #text=text.replace('\u221a', 'v') .replace('\u2321', 'O')#.replace('\u2554', '-').replace('\u2588','~' )
        #text=text.replace('\u2219','.').replace('\u2261','=').replace('\u255d', 'E').replace('\u2510','`').replace('\u2524' ,'A')
        #text = text.replace('\u2320','N').replace('\u255b', 'E').replace('\u2248','O')
        if (firstline == ''): firstline = text
        copy.write(str(text))
        i = i +1

copy.close()