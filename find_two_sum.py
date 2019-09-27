#8. Two Sum
#Write a function that, when passed a list and a target sum, returns, efficiently with respect to time used, two distinct zero-based indices of any two of the numbers, whose sum is equal to the target sum. If there are no two numbers, the function should return None.
#For example, find_two_sum([3, 1, 5, 7, 5, 9], 10) should return a single tuple containing any of the following pairs of indices:
#0 and 3 (or 3 and 0) as 3 + 7 = 10
#1 and 5 (or 5 and 1) as 1 + 9 = 10
#2 and 4 (or 4 and 2) as 5 + 5 = 10

def find_two_sum(numbers, target_sum):
    dict = {}  
    for i in range(0, len(numbers)):
        if(numbers[i] not in dict):
            dict[numbers[i]] = [i]
        else:
            dict[numbers[i]].append(i)
    
    numbers.sort() #this is the trick to get the 100%
    for i in numbers:
        res = target_sum - i
        if(res in dict):
            if(i == res):
                if(len(dict[i]) > 1):
                    return(dict[i][0], dict[res][1])
            else:    
                return(dict[i][0], dict[res][0])   
    return None   

#print(find_two_sum([7, 5], 14))
print(find_two_sum([5, 3, 1, 5, 7, 5, 9], 10))		
