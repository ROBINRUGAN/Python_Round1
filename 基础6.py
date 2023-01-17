
def find_num_of_mew(meww):
    a = {}
    for i in meww:
        if i not in a:
            a[i]=1
        else:
            a[i]+=1
    return a
mew = [1,1,1,2,3,4,4,4,4,5,6,7,7,7,7,7,8]
print(find_num_of_mew(mew))