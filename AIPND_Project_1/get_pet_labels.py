#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Dilay Fidan Ercelik
# DATE CREATED: 6th of May 2020                                 
# REVISED DATE: 10th of May 2020
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Creates list of files in directory
    in_files = listdir(image_dir)
    
    # Creates an empty dictionary results_dic
    results_dic = {}
    
    # Scrolls through each jpg file in the list in_files that contains files of the image directory (image_dir)
    for index in range(0, len(in_files), 1):
            
            # Check if the jpg file at index = index is 'appropriate'
            if in_files[index][0] != '.':
                
                # Creates a string pet_label variable and fills it for the jpg file at index = index
                pet_label = ""
                
                # Creates a list containing each word in the file's name (at index = index) 
                list_words_in_a_label = in_files[index].lower().split('_')
                
                # Iterates through the words in the list_words_in_a_label list 
                for word in list_words_in_a_label:
                    # To check if the pet label is made of alphabetic characters only
                    if word.isalpha(): # if true, append the word to the pet label, each word in list_words_in_a_label separated by a space
                        pet_label += word + ' '
                
                # Get rid of starting and trailing whitespaces
                pet_label = pet_label.strip()
                
                # If the file at index = index in the in_files list is not already a key of the results_dic: add it as a key to the
                # dictionnary
                if in_files[index] not in results_dic:
                    
                    results_dic[in_files[index]] = [pet_label]
                    
                # if the file at index = index is already a key of results_dic: this is a duplicate file
                else: 
                    
                    print('There is a duplicate file in the image directory {}'.format(in_files[index]))
                    
                
                   
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
