import pandas
import matplotlib
import matplotlib.pylab

d=pandas.read_csv('C:/Users/azzak/Downloads/YouTubeDurationData-master/YouTubeDurationData-master/IndividualLogs_dataTable.csv')

y=d['likeCount']
x=d['death']

matplotlib.pylab.scatter(x,y,c='g',marker='.')
matplotlib.pylab.xlabel("death")
matplotlib.pylab.ylabel("likeCount")
matplotlib.pylab.show()

#le script pour avoir les differents categories
#z=d['category_term']
#y=set()
#exec("for i in range(0,len(z)-1) :y.add(z[i])")

