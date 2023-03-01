import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def correlations_heatmap(data, figsiz=(15,15)):
    corr = data.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    fig, ax = plt.subplots(figsize=figsiz)
    ax = sns.heatmap(corr, annot=True,
                     vmin=-1, vmax=1,
                     fmt=".2f", annot_kws={'size':8},
                     mask=mask,
                     center=0,
                     cmap="coolwarm")
    plt.title(f"Correlation Heatmap\n")
    plt.show()
