import pandas as pd
import streamlit as st
import seaborn as sns

# Define function to load CSV file
@st.cache_resource
def load_data(file):
    data = pd.read_csv(file)
    return data


file = st.file_uploader("Upload CSV file", type=["csv"])
if file is not None:
    data = load_data(file)

# Define function to display rows
def display_rows(data):
    rows = st.slider("Select number of rows to display", 1, len(data))
    st.write(data.head(rows))


if st.button("Display Rows"):
    display_rows(data)

@st.cache_resource
def load_data(file):
    data = pd.read_csv(file)
    return data



# Define function to remove missing values
def remove_missing_values(data):
    data = data.dropna()
    return data

# Add button to remove missing values
if st.button("Remove Missing Values"):
    data = remove_missing_values(data)
    st.write("Missing values removed.")


def visualize_data(data):
    sns.set(style="ticks", color_codes=True)
    g = sns.pairplot(data)
    st.pyplot(g.fig)

# Add button to visualize data
if st.button("Visualize Data"):
    visualize_data(data)