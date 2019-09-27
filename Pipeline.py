#Pipeline

def pipeline(*funcs): 
    def helper(arg):
        x = arg
        for i in funcs:
            x = i(x)
        return(x)
    
    return helper
            
fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3)) #should print 5.0