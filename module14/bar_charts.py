import pandas as pd
import matplotlib as plit


df = pd.read_csv("avgIQpercountry.csv")


filtered_df = df[df["Average IQ"] >= 100]