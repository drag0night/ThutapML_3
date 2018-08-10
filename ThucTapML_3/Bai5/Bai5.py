import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    x = np.arange(0, 10.02, 0.02)

    fx = np.exp(-x/10.0)*np.sin(np.pi*x)
    gx = x*np.exp(-x/3.0)

    fig, ax = plt.subplots(figsize=(8,4))
    plt.title("Đồ thị hàm số")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x, fx, "b-", label='f(x)=(e^(−x/10))*sin(πx)')
    plt.plot(x, gx, "r-", label="g(x)=x*e^(−x/3)")
    ax.legend(loc='upper right')
    plt.savefig("plot.jpg")
    plt.show()