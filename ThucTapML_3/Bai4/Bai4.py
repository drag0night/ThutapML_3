import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import cdist


if __name__ == "__main__":
    df = pd.read_csv("ZebraBotswana.txt")
    df.columns = ["UnixTime", "Longtitude", "Latitude", "Id"]
    df = df.groupby("Id")[["UnixTime", "Longtitude", "Latitude"]]

    fig, ax = plt.subplots(figsize=(10, 5))
    plt.xlabel("Longtitude")
    plt.ylabel("Latitude")
    color = ["r-", "g-", "b-", "c-", "y-", "k-", "m-"]

    fw = open("output.txt", "w", encoding="utf8")
    i = 0
    for name, group in df:
        plt.plot(group["Longtitude"], group["Latitude"], color[i], linewidth=0.5, label=name)
        i += 1

        pos = group[["Longtitude", "Latitude"]]
        #Tính khoảng cách giữa các tọa độ
        dist = cdist(pos, pos, metric="euclidean")
        rows = len(dist)
        cols = len(dist[0])
        dist = dist.reshape(rows*cols)
        dist = np.partition(dist, rows*cols-1)
        fw.write("%s: %s\n" % (name, repr(dist[rows+2])))
    fw.close()
    ax.legend(loc='upper right')
    plt.savefig("plot.jpg")
    plt.show()
