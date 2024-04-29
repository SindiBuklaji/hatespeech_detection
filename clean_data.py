import pandas as pd

data = pd.read_csv("youtube_comments.csv")
print(data.head())

#remove new line characters and spaces
data['Comment'] = data['Comment'].str.replace('\n', ' ').str.strip()