""" Generate Data

    Two files will be generated:

    1. Questions List
    2. All Questions data (based on skip & limit)

"""
import os
import json
import pandas as pd

from utils.leetcode_api import get_problemset_api_query, get_problem_details_api_query, call_api
from utils.parser import parse_html_text, parse_html_hints

def create_questions_list(output_path):    

    problemset_query = get_problemset_api_query(skip=0, limit=2238)
    problemset_data = call_api(problemset_query)
    
    problemset = problemset_data['problemsetQuestionList']['questions']
    
    df = pd.DataFrame()
    
    print(f'Generating.. question list ')

    for problem in problemset:

        print(f"processing..{problem['frontendQuestionId']} {problem['titleSlug']}")
        prob_dict = {}
        titleSlug = problem['titleSlug']
        
        # call problem specific api
        query = get_problem_details_api_query(titleSlug)
        data = call_api(query)
        data = data['question']
        
        prob_dict['Question ID'] = data['questionId']
        prob_dict['Question Title'] = data['title']
        prob_dict['Question Slug'] = data['titleSlug']

        # Add related topics
        tags = problem['topicTags']
        prob_dict['Topic Tagged text'] = ",".join([tag['name'] for tag in tags])
        prob_dict['Topic Tagged ID'] = ",".join([tag['id'] for tag in tags])
        
        prob_df = pd.DataFrame.from_dict(prob_dict, orient='index').transpose()
        
        df = df.append(prob_df)
    
    df.to_csv(output_path, index=False)

def create_all_questions_data(skip, limit, output_path):

    ques_df = pd.read_csv('data/questions_list.csv')
    
    print(f'\n\nProcessing data from {skip} - {limit}')
    sl_range_df = ques_df[(ques_df.index >= skip) & (ques_df.index < limit)]

    main_df = pd.DataFrame()
    
    for _, question in sl_range_df.iterrows():

        print(f"Loading.. {question['Question ID']} {question['Question Slug']}")
        q_dict = {}
        q_dict['Question Title'] = question['Question Title']
        q_dict['Question Slug'] = question['Question Slug']
        q_dict['Question ID'] = int(question['Question ID'])

        # Call api
        query = get_problem_details_api_query(question['Question Slug'])
        data = call_api(query)
        data = data['question']

        # parse text
        q_dict['Question Text'] = parse_html_text(data['content'])

        # Topic Tagged Text, ID
        q_dict['Topic Tagged text'] = question['Topic Tagged text']
        q_dict['Topic Tagged ID'] = question['Topic Tagged ID']

        # stats
        q_dict['Difficulty Level'] = data['difficulty']
        stats = json.loads(data['stats'])
        q_dict['Success Rate'] = float(stats['acRate'][:-1])
        q_dict['total submission'] = int(stats['totalSubmissionRaw'])
        q_dict['total accepted'] = int(stats['totalAcceptedRaw'])

        # Company Tag
        q_dict['company tag'] = data['companyTagStats']

        # Likes & Dislikes
        q_dict['Likes'] = data['likes']
        q_dict['Dislikes'] = data['dislikes']

        # Parse hints
        q_dict['Hints'] = parse_html_hints(data['hints'])

        # get similar questions ids, text
        def get_similar_questions_details(ques_df, content):
            que_text_list = []
            que_ids = []
            
            for question in content:
                related_que = ques_df[ques_df['Question Slug'] == question['titleSlug']]

                # if related_que.shape[0] == 0:
                #     continue

                que_id = related_que['Question ID'].item()
                que_text = related_que['Question Title'].item()
                
                que_ids.append(str(que_id))
                que_text_list.append(que_text)

            q_ids = ",".join(que_ids)
            q_text = ",".join(que_text_list)
            

            return q_ids, q_text
                
        similar_ques = json.loads(data['similarQuestions'])
        q_dict['Similar Questions ID'], q_dict['Similar Questions Text'] = get_similar_questions_details(ques_df, similar_ques) 

        # create 1-D DataFrame
        q_df = pd.DataFrame.from_dict(q_dict, orient='index').transpose()
        
        main_df = main_df.append(q_df)
        
    main_df.to_csv(output_path, index=False)


def generate_question_list():

    DIR_PATH = 'data'
    QUE_LIST_PATH = os.path.join(os.getcwd(), DIR_PATH, f'questions_list.csv')

    if not os.path.exists(DIR_PATH):
        os.makedirs(DIR_PATH)
    
    if not os.path.exists(QUE_LIST_PATH):
        create_questions_list(QUE_LIST_PATH)

def generate_all_question_data(skip, limit):

    DIR_PATH = 'data/all_questions_data'
    ALL_DATA_PATH = os.path.join(os.getcwd(), DIR_PATH, f'all_ques_data_{skip}_{limit}.csv')

    if not os.path.exists(DIR_PATH):
        os.makedirs(DIR_PATH)
    
    # if not os.path.exists(ALL_DATA_PATH):
    create_all_questions_data(skip, limit, ALL_DATA_PATH)

def main():

    # Part - 1
    # generate_question_list()

    # Part - 2
    SKIP = 2050
    LIMIT = 2238 # max - 2238

    generate_all_question_data(SKIP, LIMIT)

main()





