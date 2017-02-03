from threading import Thread,active_count,Lock

class MultiplicationMatrix():

    product = []
    
    def __check_size(self,matrix_1,matrix_2):
        if len(matrix_1) != len(matrix_2):
            return False
        for row1,row2 in zip(matrix_1, matrix_2):
            if len(row1) != len(row2):
                return False
        else:
            return True        
            
    
    def __init__(self, nb_threads, matrix_1, matrix_2):
        MultiplicationMatrix.product=[]
        if not isinstance(nb_threads,int):
            raise Exception("nb_threads is not an integer")
        if not all(len(matrix_1) == len(row) for row in matrix_1):
            raise Exception("matrix_1 is not a square matrix")
        if not all(len(matrix_2) == len(row) for row in matrix_2):
            raise Exception("matrix_2 is not a square matrix")
        if not self.__check_size(matrix_1,matrix_2):
            raise Exception("matrix_1 and matrix_2 don't have the same size")
        n = len(matrix_1)
        for x in range(n):
            MultiplicationMatrix.product.append([0]*n)
        chunk = int(n*n/nb_threads)
        coords = []
        m = 1
        for i in range(n):
            for j in range(n):
                if (m <= (nb_threads-1)*chunk):
                    m +=1
                    coords.append([i,j])
                    thread = MultiplicationMatrixThread(i,j,matrix_1[i],zip(*matrix_2)[j])
                    thread.start()
                else:
                    break
        for i in range(n):
            for j in range(n):
                if [i,j] not in coords:
                    thread = MultiplicationMatrixThread(i,j,matrix_1[i],zip(*matrix_2)[j])
                    thread.start()

    def isComputing(self):
       if active_count() == 1:
           return False
       return True
       

    def __str__(self):
        with Lock():
            return str(tuple(MultiplicationMatrix.product))


class MultiplicationMatrixThread(Thread):

    def __init__(self, x, y, row_matrix_1, column_matrix_2):
        if not isinstance(x,int) or not isinstance(y,int):
            raise Exception("x or y is not a integer")
        if not all(isinstance(number,int) for number in row_matrix_1):
            raise Exception("row_matrix_1 is not an array of integers")
        if not all(isinstance(number,int) for number in column_matrix_2):
            raise Exception("column_matrix_2 is not an array of integers")
        self.__x = x
        self.__y = y
        self.__r = row_matrix_1
        self.__c = column_matrix_2
        Thread.__init__(self)

    def run(self):
        with Lock():
            for x in range(len(self.__r)):
                MultiplicationMatrix.product[self.__x][self.__y] += (self.__r[x]*self.__c[x])
                        
        
        
