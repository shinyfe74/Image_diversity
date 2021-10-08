import numpy as np
import cv2
import time
import matplotlib.pyplot as plt
from collections import Counter
from scipy.optimize import curve_fit


def image_diversity(image_path, fractal_dimension = 5, e_ne_graph=False, fractal_graph=False):
    #read image
    start_time = time.time()
    image = cv2.imread(image_path)
    
    #convert image to 1D array
    image_array = np.reshape(image, (-1, 3))

    #fratal dimension(e)
    fractal = [2**i for i in range(fractal_dimension+1)]
    #result lsit
    N_e = []

    #calculate N(e)
    for i in range(len(fractal)):
        #make fractal box
        fractal_array = (image_array//fractal[i])*fractal[i]

        #count boxes have rgb points
        image_array_of_tuples = map(tuple, fractal_array)
        counter_image_array = Counter(image_array_of_tuples)
        
        #find bgr point
        bgr_points = counter_image_array.keys()

        #N(e)
        N_e.append(len(bgr_points))

        #draw & save rgb graph
        if fractal_graph:
            r = []
            g = []
            b = []
            c = []

            for bgr_point in bgr_points:
                b.append(bgr_point[0])
                g.append(bgr_point[1])
                r.append(bgr_point[2])
                c.append((bgr_point[2]/255, bgr_point[1]/255, bgr_point[0]/255))

                
            fig = plt.figure()
            ax = fig.add_subplot(1,1,1, projection='3d')
            ax.scatter(r, g, b, s=0.5, c=c)
            ax.set_title('e = {}'.format(fractal[i]))
            ax.set_xlabel('R', size=6)
            ax.set_ylabel('G', size=6)
            ax.set_zlabel('B', size=6)
            ax.tick_params(axis='both', which='major', labelsize=6)
            ax.tick_params(axis='both', which='minor', labelsize=6)
            fig.savefig('./{}_fractal.jpg'.format(fractal[i]), dpi=400)


    #find curve my loglog
    def loge_logNe_curve(x, a, b):
        return a*x + b
    popt, pcov = curve_fit(loge_logNe_curve, np.log(fractal[:]), np.log(N_e[:]), maxfev=10000)
    diversity = abs(popt[0])
    
    #draw & save e, Ne graph
    if e_ne_graph:
        newX = np.logspace(0, 2, base=10)
        fig = plt.figure()
        ax = plt.gca()
        ax.scatter(fractal, N_e, c='blue', alpha=0.95, label = 'data')
        ax.set_xlabel("e", size=6)
        ax.set_xscale('log')
        ax.set_ylabel("N(e)", size=6)
        ax.set_yscale('log')
        ax.tick_params(axis='both', which='major', labelsize=6)
        ax.tick_params(axis='both', which='minor', labelsize=6)
        plt.plot(newX, np.exp(loge_logNe_curve(np.log(newX), *popt)), 'r-', label="{0:.3f}*x+{1:.3f})".format(*popt))
        ax.grid(b='on')
        ax.legend(loc='upper right')
        fig.savefig('./diversity.jpg', dpi=400)

    completion_time = time.time() - start_time

    return diversity, N_e, completion_time



print(image_diversity('./Lenna.png', 5, e_ne_graph=True, fractal_graph=True))

