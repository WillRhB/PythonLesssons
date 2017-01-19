
# coding: utf-8

# In[1]:

import sys
import numpy
import matplotlib.pyplot

def analyse (filename, outfile = None): 
        """ Displays  the mean, maxima and minimum value for each weather station.
            Creates a figure of three subplots, showing values for mean, maxima and minimum value with axis = 0, 
            y axis labels, and a tight layout. 
        """
        data = numpy.loadtxt(fname=filename, delimiter =',')
        
        fig = matplotlib.pyplot.figure (figsize= (10.0, 3.0)) 
        subplot1 = fig.add_subplot (1, 3, 1)
        subplot2 = fig.add_subplot (1, 3, 2)
        subplot3 = fig.add_subplot (1, 3, 3)

        subplot1.set_ylabel('average') 
        subplot1.plot(numpy.mean(data, axis = 0))

        subplot2.set_ylabel('max') 
        subplot2.plot(numpy.max(data, axis = 0))

        subplot3.set_ylabel('min') 
        subplot3.plot(numpy.min(data, axis = 0))

#        fig.tight_layout()
        if outfile is None: 
            matplotlib.pyplot.show()
        else: 
            matplotlib.pyplot.savefig(outfile) 
            
def detect_problems (filename):
    """Some of our temperature files have problems, check for these
       This function reads a file(filename argument) and reports on odd looking maxima, 
       and minima that add up to zero. This seems to happen when the sensors break. 
       The function does not return any data. 
    """
    data = numpy.loadtxt(fname=filename, delimiter =',')
    
    if numpy.max (data, axis = 0)[0] and numpy.max(data, axis = 0)[20] ==20:
        print ("Suspicious looking maximum")
    elif numpy.sum(numpy.min(data, axis = 0)) ==0:
        print ("Minima to zero")
    else: 
        print ("Data looks OK")
        
if __name__=="__main__":
        
    print("Running", sys.argv[0])
 
    print (sys.argv[1])
    analyse (sys.argv[1], outfile = sys.argv[2])
    detect_problems (sys.argv[1])


