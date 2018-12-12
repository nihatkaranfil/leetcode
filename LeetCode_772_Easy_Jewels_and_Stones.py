
# coding: utf-8

# In[2]:


J = "aA"
S = "aAAbbbb"
count = 0

for J_el in J:
    for S_el in S:
        if S_el == J_el :
            count += 1

print(count)



# In[ ]:


J = "aA"
S = "aAAbbbb"
count = 0
def Jewel_num_finder (J,S):
    for J_el in J:
        for S_el in S:
            if S_el == J_el :
                count += 1

    print(count)

