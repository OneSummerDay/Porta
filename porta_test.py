
full_text = input()
full_text_1 = full_text.split()
new_arr = []
new_list = ''
uniq = ''

for text in full_text_1:
    for world in sorted(set(text), key=lambda d: text.index(d)):
        if (text.count(world) == 1):
            new_list += world
            new_arr.append(world)
            break 
    
for res in new_arr:
    if (new_list.count(res) == 1 and len(uniq) == 0 ):
        uniq = res
    
print(uniq)