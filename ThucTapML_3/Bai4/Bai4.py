import pandas as pd
import matplotlib.pyplot as plt
from threading import Thread
from scipy.spatial.distance import euclidean
import datetime

result = []


class MyThread(Thread):
    def __init__(self, name, group):
        super(MyThread, self).__init__()
        self.name = name
        self.group = group

    def run(self):
        print("Bat dau chay thread %s..." % (self.name))
        global result
        x = toList(self.group)
        d1, d2, m = solution(x, x)
        result.append([self.name, d1, d2, m])
        print("Xong thread %s!" % (self.name))


def toList(group):
    a = list()
    for i, row in group.iterrows():
        x = row["Longtitude"]
        y = row["Latitude"]
        t = datetime.datetime.fromtimestamp(row["UnixTime"]).strftime('%Y-%m-%d')
        a.append([x, y, t])
    return a


def dist(p1, p2):
    return euclidean(p1[:2], p2[:2])


def subtime(d1, d2):
    dateformat = "%Y-%m-%d"
    t1 = datetime.datetime.strptime(d1, dateformat)
    t2 = datetime.datetime.strptime(d2, dateformat)
    return abs(t1 - t2)


def solution(x, y):
    ax = sorted(x, key=lambda x: x[0])  # Presorting x-wise
    ay = sorted(y, key=lambda y: y[1])  # Presorting y-wise
    d1, d2, mi = closest_pair(ax, ay)  # Recursive D&C function
    return d1, d2, mi


def min(d1x, d2x, x, d1y, d2y, y):
    if (x < y):
        return d1x, d2x, x
    else:
        return d1y, d2y, y


def stripClosest(strip, d1, d2, mi):
    i = 0
    while (i < len(strip)):
        j = i + 1
        while (j < len(strip) and abs(strip[j][1] - strip[i][1]) < mi):
            if (subtime(strip[i][2], strip[j][2]).days >= 1 and dist(strip[i], strip[j]) < mi):
                mi = dist(strip[i], strip[j])
                d1 = strip[i][2]
                d2 = strip[j][2]
            j += 1
        i += 1
    return d1, d2, mi


def closest_pair(ax, ay):
    ln_ax = len(ax)  # It's quicker to assign variable
    if ln_ax <= 3:
        return brute(ax)  # A call to bruteforce comparison
    mid = ln_ax // 2  # Division without remainder, need int
    Qx = ax[:mid]  # Two-part split
    Rx = ax[mid:]
    # Determine midpoint on x-axis
    midpoint = ax[mid][0]
    Qy = []
    Ry = []
    for x in ay:  # split ay into 2 arrays using midpoint
        if x[0] <= midpoint:
            Qy.append(x)
        else:
            Ry.append(x)
    # Call recursively both arrays after split
    d1l, d2l, mi1 = closest_pair(Qx, Qy)
    d1r, d2r, mi2 = closest_pair(Rx, Ry)
    # Determine smaller distance between points of 2 arrays
    d1, d2, mi = min(d1l, d2l, mi1, d1r, d2r, mi2)
    strip = []
    for i in range(ln_ax - 1):
        if (abs(ay[i][0] - midpoint) < mi):
            strip.append(ay[i])
    d11, d22, mi2 = stripClosest(strip, d1, d2, mi)
    return min(d1, d2, mi, d11, d22, mi2)


def brute(ax):
    mi = 9999
    d1 = ax[0][2]
    d2 = ax[1][2]
    for i in range(len(ax) - 1):
        for j in range(i + 1, len(ax)):
            if (subtime(ax[i][2], ax[j][2]).days >= 1 and dist(ax[i], ax[j]) < mi):
                mi = dist(ax[i], ax[j])
                d1 = ax[i][2]
                d2 = ax[j][2]
    return d1, d2, mi


if __name__ == "__main__":
    df = pd.read_csv("ZebraBotswana.txt")
    df.columns = ["UnixTime", "Longtitude", "Latitude", "Id"]
    df = df.groupby("Id")[["UnixTime", "Longtitude", "Latitude"]]

    fig, ax = plt.subplots(figsize=(10, 5))
    plt.xlabel("Longtitude")
    plt.ylabel("Latitude")
    color = ["r-", "g-", "b-", "c-", "y-", "k-", "m-"]
    listThread = list()
    i = 0
    for name, group in df:
        plt.plot(group["Longtitude"], group["Latitude"], color[i], linewidth=0.5, label=name)
        i += 1
        thread = MyThread(name, group)
        listThread.append(thread)
        thread.start()
    for t in listThread:
        t.join()
    fw = open("output.txt", "w", encoding="utf8")
    for i in result:
        s = "[%s, %s, %s, %20.20f]\n" % (i[0], i[1], i[2], i[3])
        fw.write(s)
    ax.legend(loc='upper right')
    plt.savefig("plot.jpg")
    plt.show()
