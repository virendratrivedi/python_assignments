#!/usr/bin/env python
# coding: utf-8

# ## 1. Write a Python Program to find sum of array?

# In[5]:


#a=[1,3,5,8,4,6,77]
#print(sum(a))
def sum_of_array(array):
  sum = 0
  for element in array:
    sum += element
  return sum


if __name__ == "__main__":
  array = [1, 2, 30, 4, 5]
  print(sum_of_array(array))


# ## 2. Write a Python Program to find largest element in an array?

# In[11]:


#aa=[1,3,5,8,4,6,77]
#print(max(aa))
def largest_element_in_array(array):
  largest_element = 0
  for element in array:
    if element > largest_element:
      largest_element = element
  return largest_element


if __name__ == "__main__":
  array = [1, 20,0, 3, 44, 5]
  print(largest_element_in_array(array))


# ## 3. Write a Python Program for array rotation?

# In[12]:


def rotate_array(array, rotation_count):
  rotated_array = []
  for i in range(len(array)):
    new_index = (i + rotation_count) % len(array)
    rotated_array.append(array[new_index])
  return rotated_array


if __name__ == "__main__":
  array = [1, 2, 3, 4, 5]
  rotation_count = 2
  rotated_array = rotate_array(array, rotation_count)
  print(rotated_array)


# ## 4. Write a Python Program to Split the array and add the first part to the end?
# 

# In[18]:


def split_and_add(array, n):
    if len(array) < n:
        return array

    new_array = array[n:]  # Second part of the array
    new_array.extend(array[:n])  # First part of the array added to the end

    return new_array

# Test the function
array = [int(x) for x in input("Enter the elements of the array (space-separated): ").split()]
n = int(input("Enter the split index: "))

new_array = split_and_add(array, n)

print("Array after splitting and adding the first part to the end:", new_array)



# ## 5. Write a Python Program to check if given array is Monotonic?
# 

# In[15]:


def is_monotonic(array):
  increasing = True
  decreasing = True
  for i in range(1, len(array)):
    if array[i] > array[i - 1]:
      increasing = False
    elif array[i] < array[i - 1]:
      decreasing = False
  return increasing or decreasing


if __name__ == "__main__":
  array = [1, 2, 3, 4, 5]
  print(is_monotonic(array))

  array = [1, 2, 3, 2, 1]
  print(is_monotonic(array))

  array = [4,3,2,1,11]
  print(is_monotonic(array))


# In[ ]:




