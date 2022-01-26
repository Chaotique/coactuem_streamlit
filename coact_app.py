import streamlit as st
import pandas as pd 
import seaborn as sns
from matplotlib import pyplot as plt

#st.set_page_config(layout="wide")


# load sociodem basic data
@st.cache(suppress_st_warning=True) 
def load_answers_basic_sociodem():
    df_sociodem_basic = pd.read_pickle("answers_basic_sociodem.pkl")
    return df_sociodem_basic
df_sociodem_basic = load_answers_basic_sociodem()

st.write("This is the beginning of a beautiful page.")

st.write(str(len(df_sociodem_basic))+" participants already answered the sociodemografic survey (not counting the 7 OS accounts).")

for category in df_sociodem_basic:
    df = df_sociodem_basic
    print(df[category].value_counts().name)
    #x, y = category, "total number"
    fig, ax = plt.subplots()
    sns.barplot(x=df[category].value_counts().index, y=df[category].value_counts(), ax=ax)

    #(df[x].value_counts().pipe((sns.barplot, "data"), ax=ax))  

    st.pyplot(fig)
