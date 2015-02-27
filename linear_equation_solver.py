# Mat=[[1, 2 ,3],[3, 4, 5],[1, 8, 6]]
# size=len(a[0])
import sys
def determinant(mat,size):
    s=1
    det=0
    b=[[0 for x in range(size)] for x in range(size)]
    if(size==1):
        return mat[0][0]
    else:
        det=0
        for c in xrange(size):
            m=0
            n=0
            for i in xrange(size):
                for j in xrange(size):
                    b[i][j]=0
                    if(i!=0 and j!=c):
                        b[m][n]=mat[i][j]
                        if (n<(size-2)):
                            n=n+1
                        else:
                            n=0
                            m=m+1
            det=det+s*(mat[0][c]*determinant(b,size-1))
            s=-1*s
    return det

def cofactor(mat,size):
    b=[[0 for x in range(size)] for x in range(size)]
    fac=[[0 for x in range(size)] for x in range(size)]
    for q in xrange(size):
        for p in xrange(size):
            m=0
            n=0
            for i in xrange(size):
                for j in xrange(size):
                    if (i!=q and j!=p):
                        b[m][n]=mat[i][j]
                        if(n<(size-2)):
                            n=n+1
                        else:
                            n=0
                            m=m+1
            fac[q][p]=((-1)**(q+p))*determinant(b,size-1)
    return fac
    #transpose(mat,fac,size)

def transpose(mat,fac,size):
    b=[[0 for x in range(size)] for x in range(size)]
    transpose=[[0 for x in range(size)] for x in range(size)]

    for i in xrange(size):
        for j in xrange(size):
            b[i][j]=fac[j][i]
    d=determinant(mat,size)
    for i in xrange(size):
        for j in xrange(size):
            transpose[i][j]=float(b[i][j])/float(d)
    return transpose
    #mat_multiplication(inverse,)
    
def mat_multiplication(inverse_mat,column_mat):

    final_mat=[[0 for x in range(len(column_mat[0]))] for x in range(len(inverse_mat))]
    for i in xrange(len(inverse_mat)):
        for j in xrange(len(column_mat[0])):
            for k in xrange(len(column_mat)):
                final_mat[i][j]+= inverse_mat[i][k]*column_mat[k][j]
    return final_mat

if __name__ == '__main__':
    mat=[[1,10,4,12],[5,12,2,40],[8,5,9,1422],[2,21,3,1]]
    column_mat=[[1],[4],[10],[13]]
    size=len(mat[0])
    d=determinant(mat,size)
    if d==0 :
        print "Inverse not possible"
        sys.exit()
    fac=cofactor(mat,size)
    trans=transpose(mat,fac,size)
    mat_mul=mat_multiplication(trans,column_mat)
    print mat_mul



