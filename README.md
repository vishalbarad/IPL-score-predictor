# IPL-score-predictor
This project is a part of the Machine learning see live project by clicking this link https://iplscorepredictorml.herokuapp.com/

#### -- Project Status: [Completed]

## Project Intro/Objective
The purpose of this project is to predict the first inning IPL match score based on Venue, Batting team, Bowling team, Runs, Overs and Wickets etc.

### Methods Used
* Data gathering
* Data preprocessing
* Inferential Statistics
* Machine Learning
* Model evaluation
* Predictive Modeling
* Model deploying

### Technologies
* Python
* Numpy 
* Pandas
* jupyter
* joblib
* HTML
* CSS
* JavaScript
* Flask
* Heroku

## Project Description
This is project based on regression ml algorithm. If you know the venue, current over runs and wickets then you simply predict score by just providing the last 5 over runs and wickets.
Dataset used by this project is 'ipl.csv' downloaded from kaggle. After downloading and importing dataset(in jupyter Notebook) i did data cleaning first like dropping some unnecessary columns, handling missing values, performing one-hot encoding on categorical variables.
After that i just divided my dataset into dependent and independent features. (Independent features=Venue,runs,wickets,etc.. | Dependent feature=total)
After that i just dropped first 5 overs data in every match because first 5 overs are powerplay over ,so i just ignored it.
After that i split data into training data and testing data.
After that i perform model selection in which i chose 'Multiplelinear', 'Ridge', 'Lasso' and 'Decision tree' regression algorithm and count accuracy score so i got

| Model          | Training_accuracy | Testing_accuracy |
| -------------- | ----------------- | ---------------- |
| Linera         | 0.678325          | 0.668358         |
| Ridge          | 0.678321          | 0.668351         |
| Lasso          | 0.678321          | 0.668347         |
| Decision-tree  | 0.999963          | 0.907869         |

As we can saw among all regression Decision tree regression gave the better result so i chose Decision tree for predection
But One-hot encoding categorical variables with high cardinality can cause inefficiency in tree-based ensembles. Continuous variables will be given more importance than the dummy variables by the algorithm which will obscure the order of feature importance resulting in poorer performance means i changing of venue, batting team and bowling team did not affect my final prediction output so this is the difficulty i faced. So i changed model to Ridge regression. After that i saved model using
'joblib' library. After that i creted UI in flask and deployed on 'Heroku'.

## Needs of this project

- frontend developers
- data exploration/descriptive statistics
- data processing/cleaning
- statistical modeling
- writeup/reporting

## Contact
* Feel free to contact me any questions or if you are interested in contributing!

<img src="https://github.com/vishalbarad/IPL-score-predictor/blob/master/ipl.gif" width="100" height="100">

