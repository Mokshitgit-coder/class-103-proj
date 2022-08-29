import pandas as pd
import plotly.express as px

df=pd.read_csv("data.csv")
#fig=px.bar(df,x="Country",y="InternetUsers")
fig=px.scatter(df,x="Population",y="Per capita",color="Country",size="Percentage",size_max=60)
fig.show()