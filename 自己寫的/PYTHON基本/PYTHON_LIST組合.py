abc=['1','2','3']
cde2=['1','2','3']
cde3=['1','2','3']

cde=[abc,abc]
print(cde)
cde2.append(abc)
print(cde2)
cde3.extend(abc)
print(cde3)

#result
#[['1', '2', '3'], ['1', '2', '3']]
#['1', '2', '3', ['1', '2', '3']]
#['1', '2', '3', '1', '2', '3']