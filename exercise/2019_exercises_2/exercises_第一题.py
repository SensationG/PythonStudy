# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 09:36:01 2019

@author: hhw
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 10:56:18 2018

@author: User
"""
stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]


def toplen_word(l_word):
    len_dict={} #记录长度   
    for i in l_word: #记录每个单词长度
        word_len = len(i)
        len_dict[i]=word_len        
    len_dict=sorted(len_dict.items(), key=lambda x: x[1], reverse=True)
    print('字母最長的5個單字：')
    for k,v in len_dict[:5]:
        print(k,v)

def topcount_word(c_word):
    words={} #记录不重复的所有单词 /统计每个单词重复次数
    for n in c_word:
        if n not in words:
            words[n]=1
        else:
            words[n]+=1
    
    #print(words)
    words=sorted(words.items(), key=lambda x: x[1], reverse=True)
    print()
    print('最常出現的5個單字：')
    for k,v in words[:5]:
        print(k,v)
        
def open_file(): #读取文本文件
   a=''
   with open('s4_read.txt', 'r', encoding='utf-8') as r:
    for line in r:      
        a+=line
   return a

def main():
    s=open_file()#第三题 从外部读取s
    s_word = s.split()  #  \r\n
    n_word = [] #纯净的单词表  
    for x,i in enumerate(s_word):# 剔除标点 并记录在n_word
        i=i.replace(',','')
        i=i.replace('.','')
        n_word.append(i)
    print(n_word)
    print('--------第一题---------')
    toplen_word(n_word)
    topcount_word(n_word)
    print('--------第二题---------') 
    s_word=[] #记录去除stopwords的结果
    for i in n_word:
        if i not in stopwords:
            s_word.append(i)
    toplen_word(s_word)
    topcount_word(s_word)
    
main()

          
