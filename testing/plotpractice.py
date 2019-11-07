# python -m pip install -U pip
# python -m pip install -U matplotlib
import matplotlib.pyplot as plt

if __name__ == '__main__':
    time = []
    quad = []
    f = open("count_to_1000","w+")
    for i in range(1000):
        time.append(i)
        quad.append((i+1)*(i+1))
        f.write(str(i+1)+"\t"+str((i+1)*(i+1))+"\n")
    f.close()

    plt.plot(time,quad)
    plt.show()
    
    exit()
