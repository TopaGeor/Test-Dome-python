#1. File Owners
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