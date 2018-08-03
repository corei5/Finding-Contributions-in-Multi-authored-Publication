
# coding: utf-8

# In[184]:


import nltk
import math
import re
import mmap
#for stemming
#from nltk.stem import PorterStemmer
from porter2stemmer import Porter2Stemmer
#from stemming.porter2 import stem
# for extract_candidate_chunks and extract_candidate_words
import itertools
import string
#end extract_candidate_chunks and extract_candidate_words
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize  
from __future__ import division
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD  

from textblob import TextBlob as tb

import os
import networkx
from nltk.stem.porter import *
#stemmer = PorterStemmer()

#Normal Distribution
import scipy.stats
import statistics
from statistics import mean
from statistics import stdev
import numpy as np
#..............
#ngrams
from nltk import ngrams

from os import walk


#ps = PorterStemmer()
ps = Porter2Stemmer()


import collections


import time

from nltk import ngrams
from nltk.tokenize import RegexpTokenizer

stop_words = set(stopwords.words('english'))


# In[185]:


class Node:       
    def __init__(self,author_name,count): #creat constructor
        self.AuthorName = author_name
        self.Count = count
        self.Impact = 0


# In[186]:


class AuthorImpactFinding:
    def processAuthorList(self,author_name_list,author_information_list, technique):
        for i in range(0,len(author_name_list),1):
            index = self.findAuthorInAuthorInformationList(author_name_list[i],author_information_list)
            if index > -1:
                if technique == 'BOP':
                    author_information_list[index].Count += 1
                elif technique == 'EC':
                    author_information_list[index].Count += (1/len(author_name_list))
                elif technique == 'CBPOS':
                    author_information_list[index].Count += self.calculateCBPOS(i, author_name_list)
            else:
                if technique == 'BOP':
                    author_information_list.append(Node(author_name_list[i],1))
                elif technique == 'EC':
                    author_information_list.append(Node(author_name_list[i],1/len(author_name_list)))
                elif technique == 'CBPOS':
                    author_information_list.append(Node(author_name_list[i],self.calculateCBPOS(i, author_name_list)))
                
    def calculateCBPOS(self, author_pos, author_name_list):
        sum_ = 0
        for i in range(0, len(author_name_list), 1):
            sum_ += 1 / (i + 1)
        
        return (1 / (author_pos+1)) / sum_

    
    def findAuthorInAuthorInformationList(self,author_name,author_information_list):
        for i in range(0,len(author_information_list),1):
            if author_name ==  author_information_list[i].AuthorName:
                return i
        return -1
    
    def displayAuthorInAuthorInformationList(self,author_information_list):
        if len(author_information_list)<1:
            print("List is Empty")
        else:
            for i in range(0,len(author_information_list),1):
                print(author_information_list[i].AuthorName+" "+str(author_information_list[i].Impact))
    
    #
    # This function is created to find out the impact of various authros based on their publications, where position of the 
    # a author in the author list of a paper is not considered.
    # BOP -> Based on papers published by that author in that particular year
    # number_of_papers -> number of papers published in that particular year
    # author_information_list -> a list that contains information of all authors
    #
    
    def findAuthorImpactBOP (self, number_of_papers, author_information_list):
        for i in range(0,len(author_information_list),1):
            author_information_list[i].Impact = author_information_list[i].Count/number_of_papers
            
    def findAuthorImpactBOP (self, number_of_papers, author_information_list):
        for i in range(0,len(author_information_list),1):
            author_information_list[i].Impact = author_information_list[i].Count/number_of_papers
        
    def bubble_sort(self,author_information_list ):
        for i in range(0,len(author_information_list),1):
            for j in range(len(author_information_list)-1-i):
                if author_information_list[j].Impact < author_information_list[j+1].Impact:
                    author_information_list[j], author_information_list[j+1] = author_information_list[j+1], author_information_list[j]     # Swap!


# In[187]:


author_impact_finding = AuthorImpactFinding()

author_name_list = []
author_information_list = []


read_2018 = open("E:/Python/scopus/2015.txt", "r") 
#read_2018 = open("C:/Users/tourist800/python/tf_idf/scopus/2018.txt", "r",encoding="utf8") 

text_2018 = read_2018.read()
#print(text_2018)
text_2018_split = text_2018.split("\n\n")
#print(text_2018_split[0])
for i in range(0,len(text_2018_split),2):
    text_2018_split_name = text_2018_split[i].split("\n")
    author_name_list = text_2018_split_name[0].split(".,")
    
    for j in range(0,len(author_name_list)-1,1):
        author_name_list[j] = str(author_name_list[j]) + "."
    
    
    author_impact_finding.processAuthorList(author_name_list,author_information_list,'CBPOS')


number_of_papers = len(text_2018_split)-(len(text_2018_split)/2)
#author_impact_finding.processAuthorList(author_name_list,author_information_list)
author_impact_finding.findAuthorImpactBOP(number_of_papers,author_information_list)
author_impact_finding.bubble_sort(author_information_list )
author_impact_finding.displayAuthorInAuthorInformationList(author_information_list)

