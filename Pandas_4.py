# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:50:34 2019

@author:Sarveswara Rao Kanduri
"""
#==========================PANDAS===================================
import numpy as np
import pandas as pd

#==========================Series===================================
#Empty Series
s=pd.Series()

s1=pd.Series((10,20,30))

#Create series from n-Dimensional array
data=np.array(['a','b','c','d','e'])
s=pd.Series(data)
print(s)

#Create a series from dictionary
data={'a':0,'b':1,'c':2,'d':3}
s=pd.Series(data)
print(s)   
print(s['c'])

data={'a':0,'b':1,'c':2}
pd.Series(data,index=['a','b','c'])

#Create Series from Scalar
pd.Series(5,index=[0,1,2,3])

#Retrieve single element using index labelvalues
s=pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])
s[4]
s['e']

#Retrieve Multiple elements using index label
s=pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])
s[['a','c','d']

#Series: It fetches one column with same datatype
ser=pd.Series(np.random.rand(1))
print(ser) #Gives a series from 0-33.
type(ser)

#Series is a datastructure of pandas. It creates indexes on its own which is helpful in searching
#========================End of Series==================================

#==========================DataFrame====================================

dict1={
       "name":['harry','rohan','chetan','Kiran'],
       "marks":[82,92,77,86],
       "city":['Delhi','Bangalore','Mangalore','Hubli']
       }

#Create a dataframe
df=pd.DataFrame(dict1)

#To read a csv file.
data=pd.read_csv(r"C:\Users\Sarveswara Rao K\Desktop\data\Dataframe.csv")
print(data)
#import xlrd
#data=pd.read_excel(r'‪C:\Users\Chetan Shetty\Desktop\abc.xlsx')

data=pd.read_csv(r"C:\Users\Sarveswara Rao K\Desktop\data\cancer_dataset.txt")
print(data)

#Shows the first 5 rows.
#data.head(-3)
data.head()

#Shows the last 5 rows.
data.tail()

#To get summary of a numeric column
data.describe()

#Fetch particular column
data['patient_id']
data['clump_thickness']

#To print certain rows using range
data[:3]
data[2:4]
#Negative index range
data[-3:]


#Fetch a particular value
data['patient_id'][0] #[column][row]

#Update the value
data['patient_id'][0]=50

 
##Change index values to some name 
#data.index=['First','Second','Third','Fourth']

newdf=pd.DataFrame(np.random.rand(334,5),index=np.arange(334)) #334 rows and 5 columns.
type(newdf)

newdf.describe()
newdf.dtypes

#If data is string it becomes object.
#This 
newdf[0][0]="Chetan"
newdf.dtypes

newdf[0][0]=0.32
newdf.index #Get total indexes


#Warning when you assign a value to a particular location in Dataframe.
    #Error is because assignment is not sure if its view or copy. 
        #Solution is to use iloc.

#loc --> Selects the element based on row index and column index.
#iloc --> Selects the element based on row and column name.

newdf.iloc[0,0]=0.45 #[row,column]. if row index is name then use name instead of number.
#To get specific rows and columns
newdf.iloc[[1,2],[1,2]] #No new df is created.

#To get all the rows
newdf.iloc[:,[1,2]]

#To get all the columns
newdf.iloc[[1,2],:]

#To get the entire dataframe.
newdf.iloc[:,:]

#To write query or to put condition
newdf=newdf.rename(columns={0:'A',1:'B',2:'C',3:'D',4:'E'})
newdf.loc[(newdf['A']<0.3) & (newdf['C']>0.1)] #inner expression will give a boolean output



#To transpose a dataframe
newdf.T

#Sort dataframe by index #By default it wil be sorted in ascending order.
newdf.sort_index(axis=0,ascending=False) #Row sorting
newdf.sort_index(axis=1,ascending=False) #Column sorting

#The type of it is "Series".
type(newdf[0])

#View (reference)
df2=newdf #updating one will change the another
#Creates a Copy.
df2=newdf.copy() #seperate independent copy is created 

#To drop a column
newdf=newdf.drop(0,axis=1)

#Drop a row from Dataframe
newdf.drop([5]).reset_index(drop=True)

#Code will have some error  here
#Drop a column from Dataframe
newdf.drop([0],axis=1)
newdf.drop(['A','C'],axis=1) #Item is not dropped as it is not assigned.
newdf=newdf.drop(['A','C'],axis=1)
newdf.drop(['A','C'],axis=1,inplace=True) #Drops the column without assignment.
newdf.drop([1,5],axis=0,inplace=True) #Drops the rows without assignment.

#To reset the index
newdf.reset_index() #This adds the index column
newdf.reset_index(drop=True,inplace=True) #'drop=True' Removes the added index column

#To remove rows which has NA in dataframe
newdf.dropna()

#Drop rows where all elements are missing
#import xlrd
newdf2=pd.read_csv('munging1.csv')

newdf2.dropna(how='all',axis=1,inplace=True) # To drop all the empty values from margin1 and margin2 columns
newdf2.isna().sum() # count of NA values in every column
newdf2.drop_duplicates(subset=['R&D Spend'])#Drop duplicates from dataframe
newdf2.drop_duplicates(subset=['R&D Spend'],keep='first')#Keeps first element
newdf2.drop_duplicates(subset=['R&D Spend'],keep='last')#Keeps last element
newdf2.drop_duplicates(subset=['R&D Spend'],keep=False)

#Rename column names.
newdf2.rename(columns={'R&D Spend':'R&D_Spend','Administration':'Admin'},inplace=True)

#Write content to the file. 
newdf2.to_excel("data1.xlsx",index=False)

#Write to a csv file.
df.to_csv("Dataframe.csv")

#If you dont want index to be written to excel file then use index=False.
df.to_csv("Dataframe.csv",index=False)

#Read an excel file
data=pd.read_excel('data.xlsx',sheet_name='Sheet2')

#To write to excel 
#pip install openpyxl 
data.to_excel('data.xlsx',sheet_name='Sheet2')

newdf2.mean()
newdf2.median()
newdf2.min()
newdf2.max()
newdf2.corr() #gives the corelation between the values
newdf2.count()
newdf2.std()
#==========================End Of Dataframe===============================



