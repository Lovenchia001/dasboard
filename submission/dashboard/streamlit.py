import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
@st.cache
def load_data():
    data = pd.read_csv("./data/hour.csv")
    return data

hour_df = load_data()

# Set page title
st.title("Bike Rental Dashboard")

# Create a sidebar
st.sidebar.header("Options")

# Show the dataset
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Raw Data")
    st.write(hour_df)

# Display summary statistics
if st.sidebar.checkbox("Display Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(hour_df.describe())

# Show dataset source
st.sidebar.subheader("Dataset Source")
st.sidebar.text("The dataset is sourced from...")

# Visualization - Season-wise Bike Share Count
st.sidebar.subheader("Season-wise Bike Share Count")

# Create a layout with two columns
col1, col2 = st.beta_columns(2)

# Plot season-wise bike share count
with col1:
    st.subheader("Season-wise Bike Share Count")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='season', y='cnt', data=hour_df, estimator='sum', ci=None, palette='muted')
    plt.title('Season-wise Bike Share Count')
    plt.xlabel('Season')
    plt.ylabel('Total Bike Share Count')
    st.pyplot(fig)
