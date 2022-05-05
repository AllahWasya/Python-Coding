import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
# Import Data File 
d= pd.read_excel("Book1.xlsx")
# print(d)
sns.barplot(y="Total Acre",x="Education",data=d)
plt.show()
d.head()
x=sns.boxplot(x=d["Own Acres"], showmeans=True)
plt.show()