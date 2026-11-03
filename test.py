arr=[6,4,2,6,8,1]

def sort(left,right):
  result=[]
  i,j=0,0
  n,m=len(left),len(right)
  while(i<n and j<m):
    if left[i]<right[j]:
      result.append(left[i])
      i+=1
    else:
      result.append(right[j])
      j+=1
  if i<n:
    while(i<n):
      result.append(left[i])
      i+=1
  if j<m:
    while(j<m):
      result.append(right[j])
      j+=1
  return result

def merge_sort(arr):
  mid=len(arr)//2
  left_arr=arr[ :mid]
  right_arr=arr[mid: ]
  left=merge_sort(left_arr)
  right=merge_sort(right_arr)
  sort(left,right)

print(arr)
  

  
  
      
  



