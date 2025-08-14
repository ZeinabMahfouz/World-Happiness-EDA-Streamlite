
import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
file_path = 'world-happiness-report-2021.csv'
df = pd.read_csv(file_path)

# Rename columns for convenience
df.rename(columns={
    "Country name": "Country",
    "Regional indicator": "Region",
    "Ladder score": "Happiness",
    "Logged GDP per capita": "GDP",
    "Healthy life expectancy": "Life_Expectancy",
    "Freedom to make life choices": "Freedom",
    "Perceptions of corruption": "Corruption"
}, inplace=True)

# Drop unnecessary columns if they exist
drop_cols = [
    'Standard error of ladder score', 'upperwhisker', 'lowerwhisker',
    'Ladder score in Dystopia', 'Explained by: Log GDP per capita',
    'Explained by: Social support', 'Explained by: Healthy life expectancy',
    'Explained by: Freedom to make life choices', 'Explained by: Generosity',
    'Explained by: Perceptions of corruption', 'Dystopia + residual'
]
df.drop(columns=[col for col in drop_cols if col in df.columns], inplace=True)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select a view:",
    ["Dataset Overview",
     "Region Frequency",
     "Happiness by Region",
     "Correlation Heatmap",
     "GDP vs Happiness",
     "Life Expectancy vs Happiness"]
)

st.title("🌍 World Happiness Report 2021 Dashboard")

if page == "Dataset Overview":
    st.subheader("Dataset Preview")
    st.write(df.head())
    st.markdown(f"**Number of Countries:** {df.shape[0]}")
    st.markdown(f"**Number of Variables:** {df.shape[1]}")

elif page == "Region Frequency":
    st.subheader("Number of Countries per Region")
    fig = px.bar(df['Region'].value_counts().reset_index(),
                 x='count', y='index',
                 labels={'index': 'Region', 'count': 'Number of Countries'},
                 color='index')
    st.plotly_chart(fig, use_container_width=True)

elif page == "Happiness by Region":
    st.subheader("Happiness Scores by Region")
    fig = px.box(df, x='Region', y='Happiness', color='Region')
    st.plotly_chart(fig, use_container_width=True)

elif page == "Correlation Heatmap":
    st.subheader("Correlation Heatmap")
    num_cols = ['Happiness', 'GDP', 'Social support', 'Life_Expectancy', 'Freedom', 'Generosity', 'Corruption']
    corr = df[num_cols].corr()
    fig = px.imshow(corr, text_auto=".2f", color_continuous_scale="RdBu_r")
    st.plotly_chart(fig, use_container_width=True)

elif page == "GDP vs Happiness":
    st.subheader("GDP vs Happiness")
    fig = px.scatter(df, x='GDP', y='Happiness', color='Region', hover_name='Country',
                     trendline='ols')
    st.plotly_chart(fig, use_container_width=True)

elif page == "Life Expectancy vs Happiness":
    st.subheader("Life Expectancy vs Happiness")
    fig = px.scatter(df, x='Life_Expectancy', y='Happiness', color='Region', hover_name='Country',
                     trendline='ols')
    st.plotly_chart(fig, use_container_width=True)
