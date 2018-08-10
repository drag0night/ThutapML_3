import numpy as np

def writeToFile(fw, x):
    if (len(x.shape) == 2): #In  ma trận
        for i in range(0, len(x)):
            for j in range(0, len(x[0])):
                s = "\t" + x[i][j].__str__()
                fw.write(s)
            fw.write("\n")
    else: #In mảng 1 chiều
        for i in range(0, len(x)):
            s = "\t" + x[i].__str__()
            fw.write(s)

if __name__ == "__main__":
    X = np.random.randint(0, 101, (100, 100))
    fw = open("output.txt", "w", encoding="utf8")
    fw.write("Dinh thuc cua ma tran: %f\n\n" % (np.linalg.det(X)))

    fw.write("Ma tran chuyen vi: \n")
    writeToFile(fw, X.T)
    fw.write("\n")

    w, v = np.linalg.eig(X)
    fw.write("Tri rieng cua ma tran: \n")
    writeToFile(fw, w)
    fw.write("\n\n")

    fw.write("Vector rieng cua ma tran: \n")
    writeToFile(fw, v)

    fw.close()