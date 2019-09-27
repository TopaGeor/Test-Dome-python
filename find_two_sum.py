def find_two_sum(numbers, target_sum):
    dict = {}  
    for i in range(0, len(numbers)):
        if(numbers[i] not in dict):
            dict[numbers[i]] = [i]
        else:
            dict[numbers[i]].append(i)
    
    numbers.sort() 
    for i in numbers:
        res = target_sum - i
        if(res in dict):
            if(i == res):
                if(len(dict[i]) > 1):
                    return(dict[i][0], dict[res][1])
            else:    
                return(dict[i][0], dict[res][0])
  
    
    return None 


def find_two_sum(numbers, target_sum):
    dict = {}  
    for i in range(0, len(numbers)):
        res =  target_sum - numbers[i]
        if(numbers[i] not in dict):
            dict[numbers[i]] = [res, i]
        else:
            dict[numbers[i]].append(i)
        
    print(dict)    
    for i in dict:
        if(i == dict[i][0]):#periptosh pou exei ton idio arithmo, dhladh an yparxoun 2 pente
            if(len(dict[i]) > 2):
                return(dict[i][1], dict[i][2])
        else:
            if(dict[i][0] in numbers):
                return(dict[i][1], numbers.index(dict[i][0]))
        
    
    return None 

def find_two_sum(numbers, target_sum):
    dict = {}
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if(numbers[i] + numbers[j] == target_sum):
                return(i,j)
    return None   
     

#print(find_two_sum([7, 5], 14))
print(find_two_sum([5, 3, 1, 5, 7, 5, 9], 10))
	
def find_two_sum(numbers, target_sum):
    dict = {}
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            res = numbers[i] + numbers[j]
            if res not in dict:
                dict[res] = [(i,j)]
            else:
                dict[res].append((i,j))
        
    print(dict)
    for i in dict:
        if(i == target_sum):
            return(dict[i][0])
    return None   
	
	
	
	
def find_two_sum(numbers, target_sum):
    for i in range(0, len(numbers)):
        res = target_sum - numbers[i]
        if(res in numbers):
            b = numbers.index(res)
            print(b)
            if(i == b):
                if(res in numbers[b+1:]):
                    c = numbers[b+1:].index(res)
                    return(i, i + c + 1)
                else:
                    pass
            else:
                return(i, b)
        
    return None        
	
	def find_two_sum(numbers, target_sum):
    for i in range(0, len(numbers)):
        res = target_sum - numbers[i]
        if(res in numbers):
            b = numbers.index(res)
            if(i == b):
                
                b = [j for j,x in enumerate(numbers[i-1:]) if x==res]
                b = tuple(b)
                if(len(b) > 1):
                    return(b[0], b[1])
                else:
                    pass
            else:
                return(i, b)
        
    return None 
		
def find_two_sum(numbers, target_sum):
    for i in range(0, len(numbers)):
        res = target_sum - numbers[i]
        if(res in numbers):
            b = numbers.index(res)
            print(b)
            if(i == b):
                if(res in numbers[b+1:]):
                    c = numbers[b+1:].index(res)
                    return(i, i + c + 1)
                else:
                    pass
            else:
                return(i, b)
        
    return None        
        
		
def find_two_sum(numbers, target_sum):
    # two point
    nums_index = [(v, index) for index, v in enumerate(numbers)]
    nums_index.sort()
    begin, end = 0, len(numbers) - 1
    while begin < end:
        curr = nums_index[begin][0] + nums_index[end][0]
        if curr == target_sum:
            return (nums_index[begin][1], nums_index[end][1])
        elif curr < target_sum:
            begin += 1
        else:
            end -= 1        
    return None
     

#print(find_two_sum([7, 5], 14))
print(find_two_sum([5, 3, 1, 5, 7, 5, 9], 10))		