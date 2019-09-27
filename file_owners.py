#1. File Owners
#Implement a group_by_owners function that:
#Accepts a dictionary containing the file owner name for each file name.
#Returns a dictionary containing a list of file names for each owner name, in any order.
#For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners
#function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.
def group_by_owners(files):
    dict = {}
    for i in files:
        if(files[i] in dict):
            dict[files[i]].append(i)           
        else:
            dict[files[i]] = [i]
    return dict
    
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy',
    'yes.txt': 'Randy',
}   
print(group_by_owners(files))
