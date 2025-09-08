import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
import matplotlib.pyplot as plt

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

## Spearman Correlation
corr, p_value = spearmanr(Summarized_Data['Total_Crime'], Summarized_Data['Total_Officers'])
print(f"Spearman Correlation between 'Total_Crime' and 'Total_Officers': {corr:.4f}, P-value: {p_value:.4f}")
##Very strong positive correlation between total crime and total officers

### Test against other variables
corr, p_value = spearmanr(Summarized_Data['Total_Crime'], Summarized_Data['Population'])
print(f"Spearman Correlation between 'Total_Crime' and 'Population': {corr:.4f}, P-value: {p_value:.4f}")

corr, p_value = spearmanr(Summarized_Data['Total_Officers'], Summarized_Data['Population'])
print(f"Spearman Correlation between 'Total_Officers' and 'Population': {corr:.4f}, P-value: {p_value:.4f}")

## Both comparisons still show a strong positive correlaion and the p-values shows strong statistical significance that for all three comparisons the correlation is not random.


### Visual
#### Visual for Officers vs Crime Correlation
#Scatterplot w/regression line
corr, p_value = spearmanr(Summarized_Data['Total_Crime'], Summarized_Data['Total_Officers'])
plt.figure(figsize=(8,8))
sns.regplot(x='Total_Crime', y='Total_Officers', data=Summarized_Data, scatter_kws={'alpha':0.6}, line_kws={'color':'red'})
plt.title('Total Crime vs Total Officers by State (2023)')
plt.xlabel('Total Crime')
plt.ylabel('Total Officers')
plt.show()
