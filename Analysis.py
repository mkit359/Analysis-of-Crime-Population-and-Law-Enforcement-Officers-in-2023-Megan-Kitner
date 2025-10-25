import pandas as pd
import seaborn as sns
import numpy as np
from scipy.stats import spearmanr
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Pull in the datasets to utilize for analysis
Crime_Data_State = pd.read_csv('Crime_Data_State.csv')
Officer_Data_State = pd.read_csv('Officer_Data_State.csv')
Overall_Data = pd.read_csv('Overall_Data.csv')
Summarized_Data = pd.read_csv('Summarized_Data.csv')

# Ensure they pulled in properly and compare their shapes to main
print(f"Crime_Data_State shape: {Crime_Data_State.shape}")
print(f"Officer_Data_State shape: {Officer_Data_State.shape}")
print(f"Overall_Data shape: {Overall_Data.shape}")
print(f"Summarized_Data shape: {Summarized_Data.shape}")

# Create a subset to analyze
  ## Sub grouping will be used for Spearman correlation where outliers are not as impactful
  ### Sub per 100k will be used for Pearson correlation where outliers would have a larger impact
sub = Summarized_Data[['Total_Crime', 'Total_Officers', 'Population']]
sub_per_100k = Summarized_Data[['Crime_per_100k', 'Officers_per_100k', 'Population']]

## Pearson Correlation Coefficient

corr, p_value = pearsonr(Summarized_Data['Crime_per_100k'], Summarized_Data['Officers_per_100k'])
print(f"Pearson Correlation between 'Crime_per_100k' and 'Officers_per_100k': {corr:.4f}, P-value: {p_value:.4f}")
## Correlation is 0.2667, indicting a weak, but positive correlation (more officers per 100k, has more crime per 100k); p-value of 0.0585 suggesting the relationship is not statistically significant

## Visual for Pearson Correlation
sns.regplot(
    x = 'Officers_per_100k',
    y = 'Crime_per_100k',
    data = Summarized_Data,
    scatter_kws={'s': 60, 'alpha':0.6},
    line_kws={'color':'red'}
)

plt.title('Crime vs Officers by State (2023)')
plt.xlabel('Officers per 100k')
plt.ylabel('Crime per 100k')
plt.text(
    x = Summarized_Data['Officers_per_100k'].min() + 50,
    y = Summarized_Data['Crime_per_100k'].max() - 500,
    s = f'Pearson r: {corr:.4f}\nP-value: {p_value:.4f}',
    fontsize = 10,
    bbox=dict(facecolor='white', edgecolor='gray', boxstyle ='round,pad=0.4')
)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

pearson_100k = sub_per_100k.corr(method='pearson')
print("Pearson Correlation Matrix (Per 100k Values):\n", pearson_100k)

## Spearman Correlations

corr, p_value = spearmanr(Summarized_Data['Total_Crime'], Summarized_Data['Population'])
print(f"Spearman Correlation between 'Total_Crime' and 'Population': {corr:.4f}, P-value: {p_value:.4f}")
## Correlation is 0.9489, indicating a strong positive correlation; p-value of 0.0000 suggesting the correlation is statistically significant; not necessary
##  but wanted to include for completeness

corr, p_value = spearmanr(Summarized_Data['Total_Officers'], Summarized_Data['Population'])
print(f"Spearman Correlation between 'Total_Officers' and 'Population': {corr:.4f}, P-value: {p_value:.4f}")
## Correlation is 0.9618, indicating a strong positive correlation; p-value of 0.0000 suggesting the correlation is statistically significant; not necessary
##  but wanted to include for completeness

corr, p_value = spearmanr(Summarized_Data['Total_Officers'], Summarized_Data['Total_Crime'])
print(f"Spearman Correlation between 'Total_Officers' and 'Total_Crime': {corr:.4f}, P-value: {p_value:.4f}")
## Correlation is 0.9206, indicating a strong positive correlation; p-value of 0.0000 suggesting the correlation is statistically significant

## All three comparisons show a strong positive correlaion and the p-values shows strong statistical significance that for those comparing crime and officer
# amounts directly to population, as well as crime to officer. These values do no explicity account for population size, which is why the next comparison is important.

corr, p_value = spearmanr(Summarized_Data['Officers_per_100k'], Summarized_Data['Crime_per_100k'])
print(f"Spearman Correlation between 'Officers_per_100k' and 'Crime_per_100k': {corr:.4f}, P-value: {p_value:.4f}")


# Matrix for analyzing three at a time
spearman_matrix = sub.corr(method = 'spearman')
sub_100_spearman_matrix = sub_per_100k.corr(method = 'spearman')

### Outputs for Matrices
print("Spearman Correlation Matrix (Total Values):\n", spearman_matrix, "\n")
print("Spearman Correlation Matrix (100k Values):\n", sub_100_spearman_matrix, "\n")


### Visuals
#### Scatterplots
## Utilizing the normalized rates to get an accurate depiction of correlation
sns.pairplot(sub, kind = 'reg', diag_kind = 'kde', plot_kws={'line_kws':{'color':'red'}})
plt.suptitle('Matrix of Total Crime, Total Officers, and Population', y = 1)
plt.show()

#### Visual for Officers vs Crime Correlation
#Scatterplot w/regression line
# corr, p_value = spearmanr(Summarized_Data['Total_Crime'], Summarized_Data['Total_Officers'])
# plt.figure(figsize=(8,8))
# sns.regplot(x='Total_Crime', y='Total_Officers', data=Summarized_Data, scatter_kws={'alpha':0.6}, line_kws={'color':'red'})
# plt.title('Total Crime vs Total Officers by State (2023)')
# plt.xlabel('Total Crime')
# plt.ylabel('Total Officers')
# plt.show()
#
# corr, p_value = spearmanr(Summarized_Data['Total_Crime'], Summarized_Data['Population'])
# plt.figure(figsize=(8,8))
# sns.regplot(x='Total_Crime', y='Population', data=Summarized_Data, scatter_kws={'alpha':0.6}, line_kws={'color':'red'})
# plt.title('Total Crime vs Population by State (2023)')
# plt.xlabel('Total Crime')
# plt.ylabel('Population')
# plt.show()


# corr, p_value = spearmanr(Summarized_Data['Crime_per_100k'], Summarized_Data['Officers_per_100k'])
# plt.figure(figsize=(8,8))
# sns.regplot(x='Crime_per_100k', y='Officers_per_100k', data=Summarized_Data, scatter_kws={'alpha':0.6}, line_kws={'color':'red'})
# plt.title('Crime vs Officers by State per 100k (2023)')
# plt.xlabel('Crime per 100k')
# plt.ylabel('Officers per 100k')
# plt.show()

sns.regplot(
    x = 'Officers_per_100k',
    y = 'Crime_per_100k',
    data = Summarized_Data,
    scatter_kws={'s': 60, 'alpha':0.6},
    line_kws={'color':'red'}
)

plt.title('Spearman Crime vs Officers by State per 100k (2023)')
plt.xlabel('Officers per 100k')
plt.ylabel('Crime per 100k')
plt.text(
    x = Summarized_Data['Officers_per_100k'].min() + 50,
    y = Summarized_Data['Crime_per_100k'].max() - 500,
    s = f'Spearman ρ: {corr:.4f}\nP-value: {p_value:.4f}',
    fontsize = 10,
    bbox=dict(facecolor='white', edgecolor='gray', boxstyle ='round,pad=0.4')
)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
