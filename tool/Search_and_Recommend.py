# -*- coding: utf-8 -*-

"""
Updated on Apr 1 2025
Search and Recommend Alg
@author: Devan Thomas
"""

from sklearn.feature_extraction.text import TfidfVectorizer
import re
import pandas as pd
import numpy as np
from math import log
from sklearn.metrics.pairwise import euclidean_distances
import math

raw = pd.read_csv("file-name.csv")
##likes = pd.read_csv("likes.csv")

users = raw["3"]
docs = raw["2"]
users = users.str.replace("b'", '')
users = users.str.replace("'", '')

weights = {}



vectorizer = TfidfVectorizer()

tf_idf = vectorizer.fit_transform(docs)

D = euclidean_distances(tf_idf)

tf_idf = tf_idf.T.toarray()


df = pd.DataFrame(tf_idf, index=vectorizer.get_feature_names_out())

rows = len(df.columns)

##removes twitter link
for i in range(rows):
    docs[i] = re.sub(r"http\S+","",docs[i])

spec_chars = ['b"',"b'","\n","!","#",".","/",":",";","?","@","[","\\","]","^","_",
              "`","{","|","}","~","–",")","("]

for char in spec_chars:
    docs = docs.str.replace(char, ' ')
## 1 letter words seem to not count as words

sim = {}

N = 1

second = 0

top = 0

q_vector = None

qnew = None

qlike_vector = 0

sim_eu = {}

q = None


def get_similar_tweets(querry, df) :
    print("query:", querry)
    
    global q_vector
    global q
    
    q = [querry]

    q_vector = vectorizer.transform(q).toarray().reshape(df.shape[0],)

    q_vector = q_vector + qlike_vector
    
    sub = 0
        
    
    for i in range(rows):
        sim[i] = np.dot(df.loc[:,i].values, q_vector)/np.linalg.norm(df.loc[:, i])*np.linalg.norm(q_vector)

    sim_sorted = sorted(sim.items(), key = lambda x: x[1], reverse = False)
        

    
    for k, v in sim_sorted:         
        if v != 0.0 and v!= None :
            global N 
            N = N + 1
            global second
            second = sub
            global top
            top = k            
            print("Similarity Values: ", v)
            print("User :", users[k])
            print("Post ID: ", k)
            sub = k
            print(docs[k])
            print()
        
    print("-----------------\n")
            
## method is highly ineffecient but theoretically would work with providing the euclidean between all points        
##def euclidean():
##    global q_vector
##    distFrame = pd.DataFrame()
##    dist = 0
##    for p in range(rows):
##        for i in range(rows):
##            for k in range(len(q_vector)-1):        
##                distFrame[p, i] = math.sqrt(np.sum((df.iloc[k, p] - df.iloc[k, i])**2 ))
        
        
##    return distFrame


    

# q1 = input("Enter your search: ")
# get_similar_tweets(q1, df)




def avg_leng():
    avg = 0
    for p in range(rows) :
        avg = avg + len(docs[p])
    avg = avg / len(docs)
    return avg


bmval = {}


def bm25():
    
    avg = avg_leng()

    sub = 0
    
    
    for i in range(rows):
        bmval[i] = ((log(rows/N))*((2.2*sim[i]*len(docs[i]))/((len(docs[i])+2.2)*(0.25+0.75*avg))))
        
    bmval_sorted = sorted(bmval.items(), key = lambda z: z[1], reverse = True)
        

    for d, t in bmval_sorted:         
        if t != 0.0 and t!= None :
            global second
            second = sub
            global top
            top = d   
            print("BM25 Values: ", t)
            print("User :", users[d])
            print("Post ID: ", d)
            sub = d
            print(docs[d])
            print()


def recommend():
    global q_vector
    global qlike_vector
    q_vector = qlike_vector
    
    sub = 0
        
    
    for i in range(rows):
        sim[i] = np.dot(df.loc[:,i].values, q_vector)/np.linalg.norm(df.loc[:, i])*np.linalg.norm(q_vector)

    sim_sorted = sorted(sim.items(), key = lambda x: x[1], reverse = False)
        

    
    for k, v in sim_sorted:         
        if v != 0.0 and v!= None :
            global N 
            N = N + 1
            global second
            second = sub
            global top
            top = k            
            print("Similarity Values: ", v)
            print("User :", users[k])
            print("Post ID: ", k)
            sub = k
            print(docs[k])
            print()
        
    print("-----------------\n")



def recommendsal(Idnum):
    get_similar_tweets(docs[Idnum], df)
        

def recommendpop(num):
    recommendsal(top)
    for i in range(num):
        get_similar_tweets(docs[second], df)

def bmrecommend(Idnum):
    get_similar_tweets(docs[Idnum], df)
    bm25(docs[q])
        

def bmrecommendran(num):
    recommendsal(top)
    bmrecommend(top)
    for i in range(num):
        get_similar_tweets(docs[second], df)
        bm25(docs[second])
        

def recommend_eu():
    global q_vector
    global q
    
    q_vector = vectorizer.transform(q).toarray().reshape(df.shape[0],)
    
    q_vector = q_vector + qlike_vector
    
    for i in range(rows):
        sim_eu[i] = math.sqrt(np.sum((q_vector[i] - df.loc[:,i].values)**2))
    sim_sorted_eu = sorted(sim_eu.items(), key = lambda x: x[1], reverse = True)
    
    for k, v in sim_sorted_eu:         
        if v!= None :           
            print("EU dist: ", v)
            print("User :", users[k])
            print("Post ID: ", k)
            print(docs[k])
            print()

    
def like(IDnum):
    
    global q_vector
    global qnew
    global qlike_vector
    
    qlike = docs[IDnum]
    qlike = [qlike]
    qlike_vector = 0.9 * qlike_vector + 0.1 * vectorizer.transform(qlike).toarray().reshape(df.shape[0],)
    qnew = 1
    
    
# def get():
#     q1 = input("Enter your search: ")
#     get_similar_tweets(q1, df)    
    




## Main Search Prompt


def main():
    while True:
        # Ask for user input
        print("\nOptions: ")
        print("1. Search tweets")
        print("2. Recommend based on last search")
        print("3. BM25 search")
        print("4. Recommend popular posts")
        print("5. Exit")
        print("6. Like a tweet (modify the query based on a liked tweet)")

        choice = input("Enter your choice: ")

        if choice == '1':
            q1 = input("Enter your search: ")
            get_similar_tweets(q1, df) # Main search function, needs input inorder to search

        elif choice == '2':
            recommend()  # Recommend based on the most recent search

        elif choice == '3':
            bm25()  # BM25 function call

        elif choice == '4':
            num = int(input("How many similar posts would you like to see? "))
            recommendpop(num)  # Recommend based on the popularity of posts

        elif choice == '5':
            print("Exiting program.")
            break  # Exit
        
        elif choice == '6':
            tweet_id = int(input("Enter the Post ID to like: "))
            like(tweet_id)  # Modify query based on the liked tweet
            print("Tweet liked! Adjusting your search query.")

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

    
    
    
    