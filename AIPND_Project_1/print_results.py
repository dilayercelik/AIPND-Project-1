#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Dilay Fidan Ercelik
# DATE CREATED: 10th of May 2020
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """ 
    # Precises which model's summary statistics are presented
    print("\n\n*** Results Summary for CNN Model Architecture",model.upper(), "***")
    
    # Prints out the Number of images 
    print("{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
    
    # Prints out the Number of dog images
    print("{:20}: {:3d}".format('N Dog Images', results_stats_dic['n_dogs_img']))
    
    # Prints out the Number of NON-dog images
    print("{:20}: {:3d}".format('N NON-Dog Images', results_stats_dic['n_notdogs_img']))
      
    
    # PRINTING PERCENTAGE STATISTICS 
    # Prints all the percentage summary statistics for the model currently running                          
    for key in results_stats_dic:
        
        # Checks that the key in results_stats_dic is a percentage summary statistic                        
        if key[0] == 'p':
        
            print(" {}: {}".format(key, results_stats_dic[key]))
    
                  
    # PRINTING CASES OF MISSCLASSIFICATION       
    # Prints out cases where there are incorrect dog/not-dog classifications, given that parameter 'print_incorrect_dogs' == True           
    if (print_incorrect_dogs) and (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'] != results_stats_dic['n_images']):
        
        print('\nIncorrect Dog/Not-Dog Classifications:')
        
        # Iterates through results_dic                                  
        for key in results_dic:
            
            # if there is NO match between the pet image label and the classifier label:
            # pet image label = dog     and classifier label = not-dog 
            # OR pet image label = not-dog and classifier label = dog                              
            if sum(results_dic[key][3:]) == 1:
            
                print('Pet image label: {} but Classifier label: {}'.format(results_dic[key][0], results_dic[key][1]))
    
   
    # Prints out cases where dog breeds were incorrectly assigned, given that parameter 'print_incorrect_breed' == True
    if (print_incorrect_breed) and (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']):
        
        print('\nIncorrect Breed Assignments:')               
        
        # Iterates through results_dic                                  
        for key in results_dic:
            
            # if pet image label is-of-dog and classifier label is-of-dog but these two labels do not match:      
            if (sum(results_dic[key][3:]) == 2) and (results_dic[key][2] == 0 ):
                  
                  print('Real breed: {} but Classifier label: {}'.format(results_dic[key][0], results_dic[key][1]))
                  
                  
            
                      
