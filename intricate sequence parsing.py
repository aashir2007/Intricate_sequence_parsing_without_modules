#%% super compressed in dict comprehension
target = 'AUG'
with open('file.txt', 'r') as fhand:
    result = {f'line_{n} has {target} at' : [i for i in range(len(line)) if line.startswith(target, i)]
              for n, line in enumerate(fhand, start=1)} # didnt want to add the else value if target not found
print(result)
#%% more elaborate (to make up for NOT FOUND value as else)
target = 'AUG'
result = {}
with open('file.txt', 'r') as fhand:
    for n, line in enumerate(fhand, start=1):
        indices = [i for i in range(len(line)) if line.startswith(target, i)]
        if indices:
            result[f'line_{n} has {target} at'] = [indices]
        else:
            result[f'at line_{n} {target}'] = ['not found']
print(result)
