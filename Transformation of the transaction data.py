#!/usr/bin/env python
# coding: utf-8

# In[ ]:


data= data[['user_id','upc','paid_time']]
data_groupby_usertime = data.head(100000).groupby(['user_id','paid_time'])['upc'].apply(' '.join).reset_index()
data_list = np.array(data_groupby_usertime,dtype=object)
#To make the UPC of each transaction in to a list
for i in range(0,len(data_list)):
     data_list[i,2] = data_list[i,2].split(" ")
data_list = data_list.tolist()        

#To get the consumption list of each consumer of each time
users =[]
data_lists=[]
for i in range(0,len(data_list )-1):
    user =data_list [i][0]
    if user not in users:
        users.append(user)
        t=users.index (user)
        data_lists.append([])
        data_lists[t].append(data_list[i][2])
        for j in range (i+1,len(data_list)):
                        if data_list[j][0] == data_list[i][0]:
                            data_lists[t].append(data_list[j][2])

