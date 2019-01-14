# !/usr/bin/env python
# 
#
# Author : 
# Date: May 19 2018
# About: 
from unittest.mock import inplace

'''

https://www.dataquest.io/blog/k-nearest-neighbors-in-python/
https://stackoverflow.com/questions/29530232/python-pandas-check-if-any-value-is-nan-in-dataframe
https://stackoverflow.com/questions/40393663/how-do-i-define-a-dataframe-in-python
https://stackoverflow.com/questions/18689823/pandas-dataframe-replace-nan-values-with-average-of-columns
https://stackoverflow.com/questions/31323499/sklearn-error-valueerror-input-contains-nan-infinity-or-a-value-too-large-for

Tact-id:836

'''

import pandas as pd
import math
import sys
import numpy as np
from scipy.spatial import distance



"""
    This method will find the euclidean distance
"""
'''
def euclidean_distance(row):
    """
    A simple euclidean distance function
    """
    
    inner_value = 0
    for k in columns:
        inner_value += (row[k] - selected_player[k]) ** 2
    return math.sqrt(inner_value)
'''


"""
    This method will find the top similar developers
    max: range
    
"""
def find_top_similar_entitties(max, nba, distance_frame, primary_column):
    
    for i in range(max):
    
        current_farthest = distance_frame.iloc[i]["idx"]
        #print('closest player index: '+str(int(current_farthest)))
        close_to_the_top_founder = nba.loc[int(current_farthest)][primary_column]

        current_distance = distance_frame.iloc[i]["dist"]
        percentile = 100 - (100 / 18.9714833602) * current_distance
        
        current_distance = round(current_distance, 2)
    
        if percentile <0:
            percentile = 0  
            
        percentile = round(percentile, 2)
        
        if(i == 0):
            continue    

        print('similar '+str(i)+' : '+str(close_to_the_top_founder) + ' - distance : '+str(current_distance) + ", Percentile : "+ (str(percentile)))        
        

"""
    This method will find the similar developers using KNN
"""
def find_similar_developers(filepath, columns, primary_column, given_entity_name):
    
    with open(filepath, 'r') as csvfile:
        dev_df = pd.read_csv(csvfile)

    #print the column name
    #print(dev_df.columns.values)
    
    # apply mean on NaN vlaues
    dev_df.fillna(round(dev_df.mean()), inplace=True)
    
    #print(dev_df)    
    
    # remove duplicate index (https://stackoverflow.com/questions/27236275/what-does-valueerror-cannot-reindex-from-a-duplicate-axis-mean)
    #dev_df = dev_df[~dev_df.index.duplicated()] 
    

    selected_player = dev_df[dev_df[primary_column] == given_entity_name].iloc[0]    

    nba_numeric = dev_df[columns] #it select the only numeric column
    #print(nba_numeric)
    
    #print('mean : \n'+str(nba_numeric.mean()))
    
    #abc = nba_numeric - nba_numeric.mean()
    #return


    # the normalization calculation
    nba_normalized = (nba_numeric - nba_numeric.mean()) / nba_numeric.std()
    #print(nba_normalized) #print the value

    # Not sure whether it should be mean or zero (need to verify with ore sources)
    #nba_normalized.fillna(0, inplace=True)
    nba_normalized.fillna(round(nba_normalized.mean()), inplace=True)

    top_founder_normalized = nba_normalized[dev_df[primary_column] == given_entity_name]
    #print(top_founder_normalized)

    euclidean_distances = nba_normalized.apply(lambda row: distance.euclidean(row, top_founder_normalized), axis=1)
    #print(euclidean_distances)
    #return

    distance_frame = pd.DataFrame(data={"dist": euclidean_distances, "idx": euclidean_distances.index})

    distance_frame.sort_values(by=["dist"], inplace=True)

    second_smallest = distance_frame.iloc[1]["idx"]
    most_nearer_entity = dev_df.loc[int(second_smallest)][primary_column]
    
    print('Direct similarity : '+most_nearer_entity)
    
    print('\n')

    print('Top 10 Similar developer to '+given_entity_name)
    find_top_similar_entitties(10, dev_df, distance_frame, primary_column)    
    
    print('\nTop 5 developers Sorted')
    find_top_similar_entitties(5, dev_df, distance_frame, primary_column)

def test_dummy():
    filepath = "developer_score_41_criteria.csv"
    
    columns = [
        'java_score',
        'php_score',
        'javascript_score',
        'rest_api_score',
        'spring_boot_score',
        'cloud_computing_score',
        'ubuntu_score',
        'angular_score',
        'reactjs_score',
        'angularjs_score',
        'exploring_score',
        'team_player_score',
        'solo_player_score',
        'documentation_score',
        'leadership_score',
        'night_owl_score',
        'get_it_done_score',
        'project_score',
        'tact_activity_score',
        'gradual_progress_score',
        'growth_mindset_score',
        'dunning_kruger_score',
        'tact_name_score',
        'public_coding_score',
        'stackoverflow_score',
        'hacker_rank_score',
        'hacker_earth_score',
        'tech_component_score',
        'linkedin_score',
        'admin_score',
        'github_score',
        'explorer_of_the_day_score',
        'interview_question_of_the_day_score',
        'problem_solver_of_the_day_score',
        'kahoot_game_score',
        'volunteer_score',
    ]
    
    primary_column = "name"
    top_developer_name = 'Latha'
    
    find_similar_developers(filepath, columns, primary_column, top_developer_name)

if __name__ == '__main__':
    test_dummy()
    
    
'''
    Variables:    (Target 41)
        name
        java_score
        php_score
        javascript_score
        rest_api_score
        spring_boot_score
        cloud_computing_score
        ubuntu_score
        angular_score
        reactjs_score
        angularjs_score
        exploring_score
        team_player_score
        solo_player_score
        documentation_score
        leadership_score
        night_owl_score
        get_it_done_score
        project_score
        tact_activity_score
        gradual_progress_score
        growth_mindset_score
        dunning_kruger_score
        tact_name_score
        public_coding_score
        stackoverflow_score
        hacker_rank_score
        hacker_earth_score
        tech_component_score
        linkedin_score
        admin_score
        github_score
        explorer_of_the_day_score
        interview_question_of_the_day_score
        problem_solver_of_the_day_score
        kahoot_game_score
        volunteer_score    
        
'''