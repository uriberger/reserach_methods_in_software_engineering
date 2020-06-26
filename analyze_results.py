import csv
import numpy as np
import matplotlib.pyplot as plt
scores_file_name = 'scores.csv'

def create_db():
    scores_db = []
    
    with open(scores_file_name, newline='', encoding='utf8') as f:
        reader = csv.reader(f)
        first = True
        line_counter = 0
        for row in reader:
            line_counter += 1
            
            # Skip the first line (contains headers)
            if first:
                first = False
                continue
            
            # If the first column is empty, we reached the end
            if row[0] == '':
                break
            
            if row[0] == '':
                print('Line ' + str(line_counter) + ': No question id')
                assert(False)
            if row[2] == '':
                print('Line ' + str(line_counter) + ': No time record')
                assert(False)
            if row[6] == '':
                print('Line ' + str(line_counter) + ': No final score record')
                assert(False)
                
            # Fill the database
            scores_db.append((int(row[0]),float(row[2]),int(row[6])))
            
    return scores_db

def cdf(my_list):
    res_cdf = []
    for grade in range(11):
        num_up_to_cur_grade = len([y for y in my_list if y <= grade])
        res_cdf.append(num_up_to_cur_grade)
        
    return res_cdf

def analyze_cdfs_of_grades(scores_db, question_pairs):
    for question_1,question_2,question_str in question_pairs:
        all_question_1_grades = [x[2] for x in scores_db if x[0] == question_1]
        all_question_2_grades = [x[2] for x in scores_db if x[0] == question_2]
        
        question_1_cdf = cdf(all_question_1_grades)
        question_2_cdf = cdf(all_question_2_grades)
        
        plt.plot(range(11),question_1_cdf)
        plt.plot(range(11),question_2_cdf)
        plt.legend(['Long version','Short version'])
        plt.title(question_str)
        plt.xlabel('Grade')
        plt.ylabel('Number of answers up to this grade')
        plt.show()

def produce_scatter_plot(scores_db, question_pairs):
    for question_1,question_2,question_str in question_pairs:
        all_question_1_grades = [x[2] for x in scores_db if x[0] == question_1]
        all_question_1_times = [x[1]/1000 for x in scores_db if x[0] == question_1]
        all_question_2_grades = [x[2] for x in scores_db if x[0] == question_2]
        all_question_2_times = [x[1]/1000 for x in scores_db if x[0] == question_2]
                
        plt.scatter(all_question_1_grades,all_question_1_times,s=10)
        plt.scatter(all_question_2_grades,all_question_2_times,s=10)
        plt.legend(['Long version','Short version'])
        plt.title(question_str)
        plt.xlabel('Grade')
        plt.ylabel('Time (seconds)')
        plt.show()

scores_db = create_db()
'''analyze_cdfs_of_grades(scores_db, [
    (1,2,'decimal to other base'),
    (3,4,'count chars'),
    (5,6,'bubble sort'),
    (7,8,'string insertion'),
    ])'''
produce_scatter_plot(scores_db, [
    (1,2,'decimal to other base'),
    (3,4,'count chars'),
    (5,6,'bubble sort'),
    (7,8,'string insertion'),
    ])