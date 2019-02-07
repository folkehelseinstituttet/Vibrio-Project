"""
This python module contains all the reusable sub-functions  
"""
from os import listdir
import os
import fnmatch

"""
This function will list all the files in a folder
"""
def list_paird_end_files(file_location):
    
    fastq_files = [f for f in listdir(file_location)]
    
    """
    Sort the files to pick the paird end files
    """
    fastq_files.sort()
    
    return fastq_files


"""
This function will list "type" of the files you want in a directory
"""
def list_paired_end_files_with_pattern(file_location,pattern):
    fastq_files = []
    list_of_files = os.listdir(file_location)
    for entry in list_of_files:  
        if fnmatch.fnmatch(entry, pattern):
            fastq_files.append(entry)
    """
    Sort the files to pick the paird end files
    """
    fastq_files.sort()
        
    return fastq_files
