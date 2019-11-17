'''
You will be provided with a Telephone bill, its a home number. You need to calculate the total cost of the bill.  Looking at all the rules.
Eg.  
Rule- if the call is under 5 minutes its 3c per second charge
Rule- if its more than 5minutes its $1 per min. 
Rule- the longest call you get free. 
'''

def Solution(S):
    aggregator_dict = dict()
    for line in S:
        line.split()