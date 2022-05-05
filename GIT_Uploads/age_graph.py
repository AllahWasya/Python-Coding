import pandas as pd
# Import Data File 

chilla= pd.read_csv("chilla_2.csv")
print(chilla)

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)
########################################################################
# p=sns.countplot(x="Gender",hue="Age",data=chilla)
# plt.show()
#########################################################################
# p=sns.countplot(x="Gender",hue="Time of class (pm)",data=chilla)
# plt.show()

#########################################################################
p=sns.countplot(x="Gender",hue="Age",data=chilla)
plt.show()
