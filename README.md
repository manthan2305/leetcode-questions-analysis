# leetcode-questions-analysis

Scrape Lettcode questions data.
Analyse questions and topics.
Predict topics to given questions text or description.

### Install:
Python Version > 3.7

```sh
pip install -r requirements.txt
```

### Run:
Scrape all questions data
```sh
python scrape.py
```
Combine data & generate topics file
```sh
python utils/combine_data.py
python utils/create_topics_data.py
```
(All data are already available `data/` folder)

### Analysis and prediction:
`notebooks/` folder constains all analysis and topic prediction notebooks. 

### Analysis

![1](img/1_difficulty_level.png)
![2](img/2_number_of_questions_topicsnewplot.png)
![3](img/3_with_diff_level.png)
![4](img/4_acc_rate.png)
![5](img/5_leading_topic.png)
