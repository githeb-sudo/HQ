import pandas
import matplotlib
import matplotlib.pylab

d=pandas.read_csv('C:/Users/azzak/Downloads/YouTubeDurationData-master/YouTubeDurationData-master/IndividualLogs_dataTable.csv')

category=['Music', 'Shows', 'Gaming', 'Sports', 'Trailers', 'Pets & Animals', 'Science & Technology', 'Travel & Events', 'Education', 'Entertainment', 'Autos & Vehicles', 'People & Blogs', 'Film & Animation', 'Howto & Style', 'News & Politics', 'Comedy', 'Nonprofits & Activism']
cat=['Music', 'Shows', 'Gaming', 'Sports', 'Trailers', 'Animals', 'SciTec', 'Events', 'Educ', 'Enterta', 'Autos','Blogs', 'Film ', 'Howto', 'News ', 'Comedy', 'Nonprofits']

l=[0]*len(category)
m=[0]*len(category)

a=d['averageViewDuration']
b=d['duration']
y=[c/d for c,d in zip(a,b)]
x=d['category_term']

for i in range (0,len(y)-1):
   for j in range (0,len(category)-1):
      if (x[i]==category[j]) :
          l[j]=l[j]+y[i]
          m[j]=m[j]+1

for j in range (0,len(category)-1):
    l[j]=l[j]/m[j]
    
matplotlib.pylab.scatter(cat,l,c='blue',marker='.')
matplotlib.pylab.xlabel("category")
matplotlib.pylab.ylabel("la moyenne des pourcentages des temps regardés des videos  par rapport aux longeurs totals")
matplotlib.pylab.title("la moyenne des pourcentages des temps regardés des videos  par rapport aux longeurs totals par categorie")
matplotlib.pylab.show()

#le script pour avoir les differents categories
#z=d['category_term']
#y=set()
#exec("for i in range(0,len(z)-1) :y.add(z[i])")

