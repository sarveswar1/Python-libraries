# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:24:29 2020

@author: Sarveswara Rao Kanduri
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 10:22:32 2019

@author: Sarveswara Rao Kanduri
"""
#=================Python Plots============================================

#In anaconda type: pip install numpy
import numpy as np

#Array creation methods in numpy: 5 Methods
#1. Conversion fom other python structures (lists,tuples)
myarr=np.array([3,6,32,7]) #always list or tuple should be passed as input to a array

myarr=np.array([32,65,32,32771],np.uint16)

myarr=np.array([32,65,321232,71],np.int8) #Bigger number gets garbage value.

#1-D Array
myarr=np.array([32,65,321232,71],np.int32)
myarr[1]

#2-D Array
myarr=np.array([[32,65,321232,71]],np.int8)
print(myarr)
myarr[0,1]

#myarr.shape #Array has 1-row and 4-columns

#update the element
myarr[0,2]=45



#dtype=object is not the efficient way of computation try to stay away from this.
ar=np.array((22,23,34),dtype=np.int32)

#Similar to range functionin python
rng=np.arange(15) #Creates an array of 15 elements from 0-14.

#To get linearly spaced 12 elements
lspace=np.linspace(1,5,12)#Between 1-5 it will give 12 equally spaced elements.

#To create identity matrix
ide=np.identity(6) #Creates a 6*6 matrix.

list1=[[1,2,3],[4,5,6],[7,8,9]]
ar=np.array(list1)
#listarray.size
   
np.sqrt(ar) #Gives square root of each element. 
ar.sum()
ar.max()
ar.min()
np.size(28)
#To find an element.
np.where(ar>5)

np.count_nonzero(ar) #Gives the number of nonzero elements.
np.nonzero(ar) #Gives the index of all nonzero elements.

#How numpy takes less space.
import sys
python_list=[0,4,55,2]
numpy_array=np.array(python_list)

sys.getsizeof(1)*len(python_list) #Get sizeof each element * number of elements #112

numpy_array.itemsize*numpy_array.size #16

numpy_array.tolist() #converts numpy array to list

#------------------------------Plots---------------------------------------
#Importing matplotlib:
from matplotlib import pyplot as plt
%matplotlib qt
#Or
#import matplotlib.pyplot as plt 

#1. Line Plot 
# x-axis values 
x = [1, 2, 3, 4, 5] 
  
# Y-axis values 
y = [10, 5, 8, 4, 2] 

 # Function to line plot 
plt.hist(x)   
# function to show the plot 
plt.show()


#2.Bar plot :
plt.bar(x,y) 
plt.show() 

#3. Histogram
# Function to plot histogram 
plt.hist(x) 
plt.show() 

#4. Scatter Plot
plt.scatter(x, y)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.suptitle("Sarveswar PLOT")
plt.show() 

#5.
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

#Subplots creates all grphs in 1-Space
plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()

#6.
#Pie Chart
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

#Scatter Plot
import numpy as np
import matplotlib.pyplot as plt

# Create data
N = 20
x = np.random.rand(N)
y = np.random.rand(N)
colors = (1,0,0) #RGB

# Plot
plt.scatter(x, y,  c=colors, alpha=1,s=20,marker='2') #Alpha determines transparency 1-Opaque 0-Transparent.
plt.title('Scatter plot')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#==============================================================================================================
                                        #PYTHON PLOTS
#==============================================================================================================
#pip install matplotlib                  

from matplotlib import pyplot as plt
x=np.random.rand(30)
y=np.random.rand(30)
plt.scatter(x,y,s=150) #s is for global size

plt.scatter(x,y,s=150,c='Red')                                        
plt.scatter(x,y,s=150,c='Red',alpha=0.5)

#Setting bubble shape
plt.scatter(x,y,s=150,marker='*') #>,<,D,*,8

#Setting the edges for bubbles charts
plt.scatter(x,y,s=150,c="Red",alpha=0.4,linewidth=7)

plt.scatter(x,y,s=150,c="beige",linewidth=7,edgecolors='brown')

#------------------------------------END OF PYTHON PLOTS------------------------------------------------------------
