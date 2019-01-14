#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

@author: raja.raman

source:
        

'''

import random

criteria = 'name,java_score,php_score,javascript_score,rest_api_score,spring_boot_score,cloud_computing_score,ubuntu_score,angular_score,reactjs_score,angularjs_score,exploring_score,team_player_score,solo_player_score,documentation_score,leadership_score,night_owl_score,get_it_done_score,project_score,tact_activity_score,gradual_progress_score,growth_mindset_score,dunning_kruger_score,tact_name_score,public_coding_score,stackoverflow_score,hacker_rank_score,hacker_earth_score,tech_component_score,linkedin_score,admin_score,github_score,explorer_of_the_day_score,interview_question_of_the_day_score,problem_solver_of_the_day_score,kahoot_game_score,volunteer_score'

def main():
    #print(criteria)
    
    cri = criteria.split(',')
    
    for x in cri:
        print("'"+x+"',")    

if __name__ == '__main__':
    main()