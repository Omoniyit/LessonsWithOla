def ap4(m):
    '''(2D_list) -> 2D_list
    Takes a 2D list and provides the address of the arithmetic progression in the list.

>>> ap4([[0, 10, 1, 1, 0],[1, 7, 2, 2, 1],[4, 4, 3, 5, 2],[9, 1, 4, 10, 3],[16, -2, 5, 17, 4],[25, -5, 6, 26, 5]])
[[0, 1], [1, 1], [2, 1], [3, 1]]
'''
    v=[]
    p=[]
    try:
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j+1]-m[i][j]==m[i][j+2]-m[i][j+1]==m[i][j+3]-m[i][j+2]:
                    for k in range(4):
                        v.append(i)
                        v.append(j+k)
                        p.append(v)
                        n=[]
                    return(p)
    except:
        i+=1
        pass

    try:
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i+1][j]-m[i][j]==m[i+2][j]-m[i+1][j]==m[i+3][j]-m[i+2][j]:
                    for k in range(4):
                        v.append(i+k)
                        v.append(j)
                        p.append(n)
                        v=[]
                    return(p)
    except:
        i+=1
        pass

    try:
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i+1][j-1]-m[i][j]==m[i+2][j-2]-m[i+1][j-1]==m[i+3][j-3]-m[i+2][j-2]:
                    for k in range(4):
                        v.append(i+k)
                        v.append(j-k)
                        p.append(v)
                        v=[]
                    return(p)
    

    except:
        i+=1
        pass
    try:
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i+1][j+1]-m[i][j]==m[i+2][j+2]-m[i+1][j+1]==m[i+2][j+2]-m[i+1][j+1]:
                    for k in range(4):
                        v.append(i+k)
                        v.append(j+k)
                        p.append(v)
                        v=[]
                    return(p)


    except:
        i+=1
        pass
    return (p)
