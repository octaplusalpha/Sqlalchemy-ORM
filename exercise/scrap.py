alphabetic = ['a', 'b', 'c', ' d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']

# i = 1
# for alphabet in alphabetic:
#     with open('grade_arm_slug', 'a') as f:
#         f.writelines(f'{i}. {alphabet}\n')
#         i += 1

# with open('subjects_slug', 'r') as f:
#     result = f.readlines()
#     for i in result:
#         print(i.strip())

fin =[]
with open('subjects_slug', 'r') as f:
    result = f.readlines()
    for r in result:
        fin.append(r.strip())
max_len = len(max(fin))
for f in fin:
    print(f'subject: {f} Length: {len(f)}')

