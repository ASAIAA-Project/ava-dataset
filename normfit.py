import numpy as np
import pickle
from scipy.stats import norm, skewnorm, truncnorm
import matplotlib.pyplot as plt

def sample():
    # Generate some data for this demonstration.
    data = norm.rvs(10.0, 2.5, size=500)
    print(data)

    # Fit a normal distribution to the data:
    mu, std = norm.fit(data)

    # Plot the histogram.
    plt.hist(data, bins=25, density=True, alpha=0.6, color='g')

    # Plot the PDF.
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
    plt.title(title)

    plt.show()

def findskew():
    with open('train.pickle', 'rb') as handle:
        annotations = pickle.load(handle)

    for i, anno in enumerate(annotations):
        if anno[12] > 8:
            print(i, anno[12])

def fitsome():
    idx = np.arange(1,11,1)
    idy = np.arange(0,1,0.01)
    with open('AVA/AVA_corrected.txt', 'r') as handle:
        orig = [sum([int(l) for l in line.split()[1:]][1:11]) for line in handle]
    with open('train.pickle', 'rb') as handle:
        annotations = pickle.load(handle)
    xmin, xmax = 0, 11

    def fitone(img_id): # untruncated
        annotation = annotations[img_id][2:12]
        score = annotations[img_id][12]
        data = []
        # Recover votes
        for i in range(10):
            cnt = int(annotation[i]*orig[img_id])
            data += [i+1 for _ in range(cnt)]
        plt.plot(idx, annotation, 'x')
        mu, std = norm.fit(data)
        a, l, s = skewnorm.fit(data)
        print(a, l, s)
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mu, std)
        p = skewnorm.pdf(x, a, l, s)
        plt.plot(x, p, 'k', linewidth=2)
        plt.plot([mu for _ in range(100)], idy, 'k--')
        plt.plot([score for _ in range(100)], idy, 'r--')
        title = "(%d) mu = %.2f,  std = %.2f, diff_s = %.4f" % (img_id, mu, std, score-mu)
        plt.title(title)
        return score

    fitone(0)
    plt.show()
    # exit()
    fitone(48633)
    plt.show()
    fitone(101783)
    plt.show()
    fitone(156972)
    plt.show()

    fitone(1156)
    plt.show()
    fitone(6534)
    plt.show()
    fitone(7099)
    plt.show()

    return None
    for i in range(10000):
        s = fitone(i)
        print(s)
        if s < 3:
            plt.show()
        plt.close()
        

if __name__ == "__main__":
    #findskew()
    fitsome()
    # sample()