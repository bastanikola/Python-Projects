-------------------------------
### MARKERS AND LINE STYLES ###
-------------------------------
-------------
### LINKS ###
-------------
#https://pandas-datareader.readthedocs.io/en/latest/
#http://eoddata.com/symbols.aspx
#https://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html
#https://www.w3schools.com/cssref/css_colors.asp

---------------
### MATPLOT ###
---------------
plt.figure(figsize=(15,15))

plt.plot(x, y, linestyle='--', marker='o', color='b', lw=1, ls='-', markersize=10, markerfacecolor="orange", markeredgewidth=2, markeredgecolor="blue")
plt.plot(x, y, '--bo')

plt.hist(x, num_bins, facecolor='blue', alpha = 0.5)

plt.scatter(X,Y)

plt.pie(values, colors= colors, labels=labels, explode = explode)

-------------------
### 3D PLOTTING ###
-------------------
plt.scatter(X,Y,Z)

plot_wireframe(X, Y, Z, rstride=20, cstride=10)

plot_surface(X, Y, Z, cmap=cm.coolwarm)

---------------
### SEABORN ###
---------------
sns.pairplot(data, hue = 'target', vars = ['', '', '', '', ''] )
sns.countplot(data['target'], label = "Count")
sns.scatterplot(x = '', y = '', hue = 'target', data = )
sns.heatmap(data, annot=True)
sns.heatmap(data.corr(), annot=True) 
sns.boxplot(x='', y='', data= )
sns.swarmplot(x='', y='',data= )
sns.jointplot(x='', y='', data = )
sns.distplot(data[''], bins = 25, kde= False,color = 'blue')

Reference: https://stackoverflow.com/questions/8409095/matplotlib-set-markers-for-individual-points-on-a-line
