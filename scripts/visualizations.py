import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew


def numerical_distribution(df, numerical_columns, style='whitegrid', nrows=2, ncols=5, figsize=(18, 12), bins=30):
    # Set the style
    sns.set_style(style)

    # Create subplots
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
    axes = axes.flatten()

    # Plot histograms
    for i, column in enumerate(numerical_columns):
        sns.histplot(df[column], kde=True, ax=axes[i], bins=bins)
        axes[i].set_title(f"Distribution of {column}")
        axes[i].set_xlabel(column)
        axes[i].set_ylabel('Frequency')
        axes[i].grid(True)

    # Remove any empty subplots
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    
    # Adjust layout and show plot
    plt.tight_layout()
    plt.show()

def correlation_analysis(df, numeric_columns):
    # Task 5: Correlation Analysis
    corr_matrix = df[numeric_columns].corr()
    f, ax = plt.subplots(figsize=(10,8))
    sns.heatmap(corr_matrix, square=True, annot=True, linewidth=0.8, cmap='RdBu')
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.title('Correlation Matrix')
    plt.xlabel('Features')
    plt.ylabel('Features')
    plt.show()


def outlier_detection(df, numeric_columns, style='whitegrid', nrows=4, ncols=3, figsize=(15,8), bins=30):
    # Set the style 
    sns.set_style(style)
    palette = sns.color_palette("Set2")
    
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
    axes = axes.flatten()

    # Create a box plot for each numeric column
    for i, column in enumerate(numeric_columns):  # Use enumerate to get both index and value
        sns.boxplot(ax=axes[i], data=df[column], color=palette[i % len(palette)])  # Use the axes from the subplot
        axes[i].set_title(f'Box Plot for {column}')

    # Remove any empty subplots
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    # Adjust layout and show plot 
    plt.tight_layout()
    plt.show()



def detect_skewness(df, numeric_columns, threshold=0.5):
    """
    Computes skewness for numerical columns and highlights those with high skewness.
    """
    skewness_values = df[numeric_columns].apply(lambda x: skew(x.dropna()))
    skewed_features = skewness_values[abs(skewness_values) > threshold]
    
    print("Skewness of numerical features:")
    print(skewness_values.sort_values(ascending=False))
    
    if not skewed_features.empty:
        print("\nHighly skewed features:")
        print(skewed_features)
    else:
        print("\nNo highly skewed features detected.")
    
    return skewed_features

# def univariate_analysis(df, numeric_columns, style='whitegrid', nrows=3, ncols=4, figsize=(18, 12)):
#     """
#     Performs univariate analysis by plotting histograms and boxplots for numerical features.
#     """
#     sns.set_style(style)
#     fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
#     axes = axes.flatten()
    
#     for i, column in enumerate(numeric_columns):
#         sns.histplot(df[column], kde=True, ax=axes[i])
#         axes[i].set_title(f'Distribution of {column}')
    
#     plt.tight_layout()
#     plt.show()

def univariate_analysis(df, numeric_columns, style='whitegrid', nrows=3, ncols=4, figsize=(18, 12), bins=20, kde=False):
    """
    Performs univariate analysis by plotting histograms and boxplots for numerical features.
    """
    sns.set_style(style)
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
    axes = axes.flatten()
    
    # Limit the number of rows if numeric_columns are more than the number of axes
    numeric_columns = numeric_columns[:len(axes)]

    for i, column in enumerate(numeric_columns):
        sns.histplot(df[column], kde=kde, ax=axes[i], bins=bins)
        axes[i].set_title(f'Distribution of {column}')
    
    plt.tight_layout()
    plt.show()



def bivariate_analysis(df, numeric_columns, target_column, style='whitegrid', nrows=3, ncols=4, figsize=(18, 12)):
    """
    Performs bivariate analysis by plotting scatter plots of numerical features against the target variable.
    """
    sns.set_style(style)
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
    axes = axes.flatten()
    
    for i, column in enumerate(numeric_columns):
        if column != target_column:
            sns.scatterplot(x=df[column], y=df[target_column], ax=axes[i])
            axes[i].set_title(f'{column} vs {target_column}')
    
    plt.tight_layout()
    plt.show()
