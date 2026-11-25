arr = [100,101,100,102,1010,100]

# for i in range(len(arr)):
#     count= 0 

#     for j in range(len(arr)):

#         if arr[i] == arr[j]:
#             count += 1


# hashing using array (sliding window concept )
# constrain ki max value bhi dekhna hain ( 100 <= arr[i] <= 103 )  note constrain  is important 
## question solve ke lia mujhe array ki max value tak array banan padega 

fre = [0] * 4

for i in arr :
    fre[i-100] += 1 # slide kia index from 100 to 0 visual window backword 

for i in fre :
    print(f"")


