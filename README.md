World Happiness Report – EDA & Interactive Dashboard

This project analyzes the World Happiness Report 2021 with Exploratory Data Analysis (EDA) in Jupyter Notebook and an interactive dashboard built using Streamlit and Plotly.
It explores how GDP, life expectancy, freedom, and corruption relate to happiness scores across different regions.

📂 Project Structure
world_happiness_eda.ipynb        # EDA notebook
streamlit_app.py                 # Streamlit dashboard app
world-happiness-report-2021.csv  # Dataset
README.md                        # Documentation

📌 Features
EDA Notebook

Cleaned & renamed dataset columns for clarity

Summary statistics and dataset preview

Visualizations of distributions, relationships, and correlations

Streamlit Dashboard Pages

Dataset Overview – Preview of the dataset and basic stats

Region Frequency – Number of countries per region

Happiness by Region – Boxplots of happiness distribution

Correlation Heatmap – Explore relationships between variables

GDP vs Happiness – Scatter plot with regression line

Life Expectancy vs Happiness – Scatter plot with regression line

📊 Key Insights

Western Europe and North America have the highest average happiness scores.

GDP per capita and Life expectancy are strongly positively correlated with happiness.

Sub-Saharan Africa and South Asia tend to have lower happiness scores.

Freedom to make life choices shows a moderate correlation with happiness, while perception of corruption has a negative correlation.

Economic and health factors play a bigger role in happiness than corruption perception.

📊 Example Visualizations

Bar chart: Countries per region

Boxplot: Happiness score distribution

Heatmap: Correlation between GDP, life expectancy, and happiness

Scatter plots: GDP vs happiness, life expectancy vs happiness

🚀 Setup & Usage
1️⃣ Clone this repository
git clone https://github.com/YourUsername/world-happiness-dashboard.git
cd world-happiness-dashboard

2️⃣ Install dependencies
pip install -r requirements.txt


Example requirements.txt:

pandas
plotly
streamlit

3️⃣ Run the Streamlit app
streamlit run streamlit_app.py

4️⃣ Explore the EDA notebook
jupyter notebook world_happiness_eda.ipynb

📜 Dataset

Source: World Happiness Report 2021

Columns:

Country & Region

Happiness Score

GDP per Capita

Life Expectancy

Freedom Index

Corruption Perception Index
