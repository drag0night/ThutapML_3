import csv
import pandas
import matplotlib.pyplot as plt

if __name__ == "__main__":
    data = []
    with open('pokemon.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            #Bỏ đi dòng tiêu đề
            if (row[0] != "#"):
                data.append(row)

    df = pandas.DataFrame(data)
    #Đặt lại tiêu đề cho Data Frame
    df.columns = ['#','Name','Type 1','Type 2','HP','Attack',
                  'Defense','Sp. Atk','Sp. Def','Speed','Generation','Legendary']

    df = df.query("Speed > '80' and Attack > '52'")

    speed = df['Speed']
    attack = df['Attack']

    #Sắp xếp lại các điểm (Speed, Attack) theo thứ tự tăng dần
    x, y = zip(*sorted(zip(speed, attack)))

    plt.plot(x, y, 'bo', markersize=4, alpha=.8)
    plt.xlabel('Speed')
    plt.ylabel('Attack')
    plt.title('Pokemon has Speed > 80 abd Attack > 52')
    plt.show()