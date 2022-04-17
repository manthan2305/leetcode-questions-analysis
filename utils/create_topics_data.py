""" Generate CSV of all topics with Ids
"""

import pandas as pd
import os

def create_topics_data(data, output_path):

    seen_topics = []
    topics_lst = []

    for _, row in data.iterrows():

        if type(row['Topic Tagged text']) != str:
            continue
        topics = row['Topic Tagged text'].split(',')
        topics_ids = row['Topic Tagged ID'].split(',')

        for topic, id in zip(topics, topics_ids):

            if topic not in seen_topics:
                t_dict = {}
                t_dict['Topic'] = topic
                t_dict['Id'] = id

                seen_topics.append(topic)
                topics_lst.append(t_dict)

    topics_df = pd.DataFrame(topics_lst)
    print(topics_df)
    topics_df.to_csv(output_path, index=False)

    return 

def generate_topics_data():

    DIR_PATH = 'data'
    TOPICS_DATA_PATH = os.path.join(os.getcwd(), DIR_PATH, f'all_topics.csv')

    all_questions_data = pd.read_csv(os.path.join(os.getcwd(), DIR_PATH, 'all_questions_data.csv'))
    
    # if not os.path.exists(TOPICS_DATA_PATH):
    create_topics_data(all_questions_data, TOPICS_DATA_PATH)

