from glob import glob
import scipy.misc
import matplotlib.pyplot as plt
path = glob('./dataset/%s/%s/*' % ('weed_maize', 'train'))
print (path)
for image in path:
    image = scipy.misc.imread(image)
    plt.imshow(image)
    plt.show()
