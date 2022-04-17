# leetcode-questions-analysis

Scrape Lettcode questions data using GraphQl API.
Analyse questions and topics.
Predict topics to given questions text or description.

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

### Run Analysis:
```sh
analysis.ipynb
```
### Predict topics:
```sh
predict-topics.ipynb
```

### Analysis

![1](img/1_difficulty_level.png)
![2](img/2_number_of_questions_topicsnewplot.png)
![3](img/3_with_diff_level.png)
![4](img/4_acc_rate.png)
![5](img/5_leading_topic.png)
