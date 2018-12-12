
# coding: utf-8

# In[36]:


#import time

#start = time.time() # iot calculate the time 

for i in range (20000000):

    J = "aA"
    S = "aAAbbbb"

    count = 0

    for J_el in J:
        for S_el in S:
            if S_el == J_el :
                count += 1

    #print(count)

#end = time.time()
#elapsed = end - start
print(elapsed)


# In[10]:


# second version as Function

J = "aA"
S = "aAAbbbb"
count = 0
def jewel_and_stones (J,S):
    """ You're given strings J representing the types of stones that are jewels, 
    and S representing the stones you have.  Each character in S is a type of stone you have.
    You want to know how many of the stones you have are also jewels.
    The letters in J are guaranteed distinct, and all characters in J and S are letters. 
    Letters are case sensitive, so "a" is considered a different type of stone from "A"."""
    count = 0    
    for J_el in J:
        for S_el in S:
            if S_el == J_el :
                count += 1

    print(count)
    
jewel_and_stones (J,S)


# In[35]:


# Third version

start = time.time()
for i in range (20000000):
    x = sum([1 for J_el in J for S_el in S if J_el == S_el]) 
#print(x)
end = time.time()
elapsed = end - start
print(elapsed)

