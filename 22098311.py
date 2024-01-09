# -*- coding: utf-8 -*-
"""
Created on Fri Jan 9 18:10:28 2024

@author: Amarnath Sandana Sevanan
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Reading data from csv file
df = pd.read_csv("22098311.csv")

# Set the font scale and colors for seaborn plots
sns.set(font_scale=1.5, rc={'axes.facecolor': 'white', 'figure.facecolor': 'white'})

# Define the grid for the subplots and give title
fig = plt.figure(figsize=(20, 16), constrained_layout=True, facecolor='#f4f4f4')
fig.suptitle("The distribution of salaries within the field of Data Science\n", fontweight='bold', fontsize=35, color='#0066cc')

gs = fig.add_gridspec(nrows=4, ncols=2)

# Title
ax1 = fig.add_subplot(gs[0, 0:2])
plt.text(0.3, 0.9, "Data Handling and Visualisation", fontsize=35, color='#0066cc')
plt.text(0.4, 0.7, "Infographics Project", fontsize=35, color='#0066cc')
plt.text(0.001, 0.3, "Name: Amarnath Sandana Sevanan", fontsize=30, color='#333333')
plt.text(0.8, 0.3, "Student ID: 22098311", fontsize=30, color='#333333')
plt.axis('off')

# Subplot1
ax4 = fig.add_subplot(gs[1, 0])
top_company = df['company_location'].value_counts().nlargest(5).index.tolist()
df_top_company = df[df['company_location'].isin(top_company)]
sns.histplot(x='salary_in_usd', hue='company_location', multiple='stack', alpha=0.9,
             edgecolor='#cfd0d4', bins=50, data=df_top_company, palette='viridis')
plt.title('Company Location-based Salary Distribution in USD', fontsize=25, color='#0066cc')

# Subplot2
ax3 = fig.add_subplot(gs[1, 1])
sns.lineplot(y='salary_in_usd', x='work_year', data=df,
             color='#0066cc', alpha=1)
plt.title('Yearly Salary (USD) Distribution', fontsize=25, color='#0066cc')



# Subplot3
ax5 = fig.add_subplot(gs[2, 0])
experience_levels = df['experience_level'].value_counts().index
#colors = ['#ffcc00', '#ff6666', '#66ff66', '#6666ff']
colors = sns.color_palette('pastel')[0:4]

df['experience_level'].value_counts().plot(kind='pie', autopct='%.0f%%', colors=colors)

#plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')

plt.legend(labels=experience_levels,
           bbox_to_anchor=(1.0, 0.45), fontsize=15)
plt.title('Salary Distribution Across Experience Levels', fontsize=25, color='#0066cc')

# Subplot4
ax6 = fig.add_subplot(gs[2, 1])
sns.violinplot(x='salary_in_usd', y='company_size', data=df, palette='viridis')
plt.title('Salary (USD) Distribution Based on Company Size', fontsize=25, color='#0066cc')

# Set the aspect ratio
aspect_ratio = 2/1

# Textbox
ax7 = fig.add_subplot(gs[3, :])
plt.text(0.0, 0.8,"This dashboard illustrates the growth in data science job\n"+
"salaries from 2020 to 2023 and explores the factors influencing salary distribution.\n"+ 
"The histogram highlights that individuals employed by companies in the United States\n"+ 
"receive higher salaries than those in other countries, underscoring the significance of location.\n"+ 
"Additionally, company size, evident in the violin plot, plays a role in salary discrepancies.\n"+ 
"The pie chart indicates that the most experienced employees command the highest salaries.\n"+
"In summary, factors such as location, company size, and experience level collectively contribute\n"+
"to the variation in salary levels.", fontsize=25, color='#333333')
plt.axis('off')

plt.savefig("22098311.png", dpi=300, bbox_inches='tight', facecolor='#f4f4f4')
plt.show()

#Github link: https://github.com/Amarnathsandana/Infographics_Project
