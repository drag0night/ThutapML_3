import numpy as np

def checkMatrixSquare(mat):
    #Tổng của hàng đầu tiên
    temp = np.sum(mat[0])

    #Kiểm tra tổng các hàng
    for ele in mat:
        if (temp != np.sum(ele)):
            return False

    #Kiểm tra tổng các cột
    for ele in mat.T:
        if (temp != np.sum(ele)):
            return False

    #Kiểm tra tổng 2 đường chéo chính
    if (temp != mat[0::].trace() or temp != mat[::-1].trace()):
        return False
    else:
        return True

if __name__ == "__main__":
    mat1 = np.array([[1,2,3],
                    [4,5,6],
                    [9,8,9]])

    mat2 = np.array([[0,1,0],
                     [1,0,0],
                     [0,0,1]])

    print(checkMatrixSquare(mat1))
    print(checkMatrixSquare(mat2))