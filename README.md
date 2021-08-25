Team participants: Diana Dmytrashko, Andrii Vedilin

## 1. (team, mandatory, 30 pt) Proof of Concept implementation of your project

![image](https://user-images.githubusercontent.com/76747280/130845738-2d02a497-d43e-4f91-bf6d-923a5d9068a0.png)


## Reddit data processing

The project is designed to process and analyze subreddits. Project has 3 functions: 1 http to event hub, 2 processing data from event hub via text analytics api to detect language, 3 processing data from event hub via text analytics api to find key words.

Data from reddit executes via script that reads .csv file and sends POST Http requests every minute to azure function.
