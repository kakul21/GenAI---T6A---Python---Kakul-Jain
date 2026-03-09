# Email Domain Analysis

class Solution:
    def count_company_emails(self, emails):
        count = 0
        for i in emails:
            if i.endswith("@company.com"):
                count+=1
        return count
    
# Username Validation System

class Solution:

    def get_valid_usernames(self, usernames):
        valid_usernames = []
        for i in usernames:
            if i.startswith("user") and i[4:].isdigit() and len(i)>6:
                valid_usernames.append(i)

        return valid_usernames


'''Problem Description
A bank monitors daily transactions of a user. If 3 or more consecutive transactions exceed ₹10,000, the system should flag the account as "Fraud Alert".

You are given a list of transaction amounts.

The system must scan the transactions sequentially and determine whether such a suspicious pattern exists.

If detected, return "Fraud Alert", otherwise return "Safe".'''

# Solution
class Solution:
    def detect_fraud(self, transactions):
        cnt = 0
        for i in transactions:
            if i>10000:
                cnt+=1
        if cnt>=3:
            return "Fraud Alert"
        else:
            return "Safe"
        pass


# Smart Parking Fee Calculator
class Solution:
    def parking_fee(self, hours):
        fee = 0
        #write your code here
        if hours<=5:
            fee = (hours-2 )*20
        else:
            fee = 3*20 + (hours-5)*50
        if hours>12:
            fee+=200
        return fee

# Online Quiz Result Analyzer

class Solution:
    def quiz_score(self, student, correct):
        score = 0
        #write your code here
        for i in range(len(student)):
            if student[i]=="X":
                score+=0
            elif student[i]==correct[i]:
                score+=5
            else:
                score-=2
        total = len(correct)*5
        if score>0.7*total:
            score+=10
        return score

