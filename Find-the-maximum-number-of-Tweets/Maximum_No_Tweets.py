from collections import defaultdict

#find the key with Maximum Values in the Dictionary
def get_max_value(data):
 d = defaultdict(list)
 for key, value in data.items():
     d[value].append(key)
 return max(d.items())[1]

def Tweet_no(tweet):
 tempset = list(set(tweet))
 dictionary ={}
 for i in range(len(tempset)):
     n = tweet.count(tempset[i])
     dictionary[tempset[i]]=n
 #get Key With the Maximum Value
 max_vall =get_max_value(dictionary)
 #sort the list for alphabetical order
 max_vall.sort()
 #print the user with no.of tweets
 for i in range(len(max_vall)):
  print(max_vall[i]+" " + str(dictionary[max_vall[i]]))

         
Test_cases = int(input()) 
for i in range(Test_cases):
 num = int(input())
 tweet = []
 for j in range(num):
  name = input()
  temp = name.split(" ")
  tweet.append(temp[0])
 Tweet_no(tweet)

 
    
