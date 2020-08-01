# IPL-score-predictor
This project is a part of the [Machine learning](https://iplscorepredictorml.herokuapp.com/) Other DSWG projects can be found at the [main GitHub repo](https://github.com/sfbrigade/data-science-wg).

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
But One-hot encoding categorical variables with high cardinality can cause inefficiency in tree-based ensembles. Continuous variables will be given more importance than the dummy variables by the algorithm which will obscure the order of feature importance resulting in poorer performance means i changing of venue,batting team and bowling team did not affect my final prediction output. So i changed model to Ridge regression.

(Provide more detailed overview of the project.  Talk a bit about your data sources and what questions and hypothesis you are exploring. What specific data analysis/visualization and modelling work are you using to solve the problem? What blockers and challenges are you facing?  Feel free to number or bullet point things here)

## Needs of this project

- frontend developers
- data exploration/descriptive statistics
- data processing/cleaning
- statistical modeling
- writeup/reporting
- etc. (be as specific as possible)

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data is being kept [here](Repo folder containing raw data) within this repo.

    *If using offline data mention that and how they may obtain the data from the froup)*
    
3. Data processing/transformation scripts are being kept [here](Repo folder containing data processing scripts/notebooks)
4. etc...

*If your project is well underway and setup is fairly complicated (ie. requires installation of many packages) create another "setup.md" file and link to it here*  

5. Follow setup [instructions](Link to file)

## Featured Notebooks/Analysis/Deliverables
* [Notebook/Markdown/Slide Deck Title](link)
* [Notebook/Markdown/Slide DeckTitle](link)
* [Blog Post](link)


## Contributing DSWG Members

**Team Leads (Contacts) : [Full Name](https://github.com/[github handle])(@slackHandle)**

#### Other Members:

|Name     |  Slack Handle   | 
|---------|-----------------|
|[Full Name](https://github.com/[github handle])| @johnDoe        |
|[Full Name](https://github.com/[github handle]) |     @janeDoe    |

## Contact
* If you haven't joined the SF Brigade Slack, [you can do that here](http://c4sf.me/slack).  
* Our slack channel is `#datasci-projectname`
* Feel free to contact team leads with any questions or if you are interested in contributing!
