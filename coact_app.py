import streamlit as st
import pandas as pd 
import seaborn as sns
from matplotlib import pyplot as plt

#st.set_page_config(layout="wide")

reload_data = st.button('Reload Data')
st.write('Click the above button to fetch the latest data (up to one hour old).')
# load sociodem basic data
@st.cache(suppress_st_warning=True) 
def load_answers_basic_sociodem(reload_data=True):
    if reload_data:
        df_sociodem_basic = pd.read_csv("answers_basic_sociodem.csv", usecols = ["genere", "edat", "pp", "p_cuid", "p_prof_si"])
    return df_sociodem_basic
df_sociodem_basic = load_answers_basic_sociodem()

st.write(str(len(df_sociodem_basic))+" participants already answered the sociodemografic survey (not counting the 7 OS accounts).")

for category in df_sociodem_basic:
    df = df_sociodem_basic
    print(df[category].value_counts().name)
    #x, y = category, "total number"
    fig, ax = plt.subplots()
    sns.barplot(x=df[category].value_counts().index, y=df[category].value_counts(), ax=ax)

    #(df[x].value_counts().pipe((sns.barplot, "data"), ax=ax))  

    st.pyplot(fig)
