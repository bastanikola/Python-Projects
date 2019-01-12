-------------------------------------
### PROJECT: MOVIE DOMESTIC GROSS ###
-------------------------------------
#import the packages needed to perform the analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline

#import the data
mov = pd.read_csv('Movie_Domestic_Gross', encoding = 'latin1')

#explore the dataset
mov.head()
mov.tail()

#check the summary of the dataframe
mov.describe()
mov.info()
mov.columns

#check the structure of the dataframe
mov.info()
vis1 = sns.factorplot(data = mov, x="Day of Week", kind="count", size=10)

#xplore the categorical variable Studio, used in the assignment
mov.Studio.unique()

#explore the len of categorical variable Studio, used in the assignment
len(mov.Genre.unique()

#filter the dataframe by genre
mov2 = mov[(mov.Genre == 'action') | (mov.Genre == 'adventure') | (mov.Genre == 'animation') | (mov.Genre == 'comedy') | (mov.Genre == 'drama')]

#filter the mov2 dataframe by studio
mov3 = mov2[(mov2.Studio == 'Buena Vista Studios') | (mov2.Studio == 'Fox') | (mov2.Studio == 'Paramount Pictures') | (mov2.Studio == 'Sony') | (mov2.Studio == 'Universal') | (mov2.Studio == 'WB')]

#check how the filters worked
print (mov3.Genre.unique())
print (mov3.Studio.unique())
print (len(mov3))

#define the style
sns.set(style="darkgrid", palette="muted", color_codes=True)

#plot the boxsplots
ax = sns.boxplot(data=mov3, x='Genre', y='Gross % US', orient='v', color='lightgray', showfliers=False)
plt.setp(ax.artists, alpha=0.5)

#add in points to show each observation
sns.stripplot(x='Genre', y='Gross % US', data=mov3, jitter=True, size=6, linewidth=0, hue = 'Studio', alpha=0.7)

ax.axes.set_title('Domestic Gross % by Genre',fontsize=30)
ax.set_xlabel('Genre',fontsize=20)
ax.set_ylabel('Gross % US',fontsize=20)

#define where to place the legend
ax.legend(bbox_to_anchor=(1.05, 1), loc=2)
