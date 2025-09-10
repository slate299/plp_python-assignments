# Iris Dataset Analysis with Pandas and Matplotlib

## Author

Natasha Hinga

## Project Description

This project demonstrates data analysis and visualization techniques using Python's Pandas library for data manipulation and Matplotlib/Seaborn for creating visualizations. The analysis is performed on the classic Iris flower dataset.

## Objectives

- Load and explore a dataset using Pandas
- Perform basic data analysis and compute statistics
- Create multiple data visualizations to uncover patterns and insights
- Demonstrate proficiency with data science tools and techniques

## Dataset

The Iris dataset contains measurements for 150 flowers from three species of iris:

- Setosa
- Versicolor
- Virginica

For each flower, four features are measured:

- Sepal length (cm)
- Sepal width (cm)
- Petal length (cm)
- Petal width (cm)

## Requirements

- Python 3.6+
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- NumPy
- Jupyter

## Installation

```bash
# Install required packages
pip install -r requirements.txt
```

## Project Structure

```
week_7/
├── data_analysis.ipynb  # Main Jupyter notebook with code
├── README.md            # This file
└── requirements.txt     # Package dependencies
```

## Code Overview

The analysis is organized into three main tasks:

### Task 1: Data Loading and Exploration

- Load the Iris dataset from scikit-learn
- Display dataset structure and first few rows
- Check for missing values and clean data
- Explore data types and basic information

### Task 2: Basic Data Analysis

- Compute descriptive statistics (mean, median, standard deviation)
- Group data by species and calculate averages
- Identify patterns and relationships between variables

### Task 3: Data Visualization

Create multiple visualizations including:

- Line chart comparing sepal and petal length trends
- Bar chart showing average measurements by species
- Histogram of sepal length distribution
- Scatter plot of sepal length vs petal length
- Additional visualizations: box plots, correlation heatmap, and pairplot

## Key Findings

1. **Species Differentiation**: Clear separation between species, especially Setosa which has distinct characteristics
2. **Size Patterns**: Virginica tends to have the largest measurements overall
3. **Correlations**: Strong positive correlation between petal length and petal width
4. **Measurement Patterns**: Sepal width shows less variation across species compared to other features

## How to Run

1. Ensure all required packages are installed
2. Open the Jupyter notebook in VS Code or Jupyter Lab
3. Run all cells sequentially (Click "Run All" or use Shift+Enter for each cell)
4. View the generated outputs and visualizations below each code cell

## Output

The notebook generates:

- Text output with dataset information and statistics
- Multiple visualizations including charts and graphs
- Summary of findings and observations

## Visualizations Included

1. Line Chart - Sepal vs Petal Length Trends
2. Bar Chart - Average Measurements by Species
3. Histogram - Distribution of Sepal Length
4. Scatter Plot - Sepal Length vs Petal Length
5. Box Plots - Measurement Distributions by Species
6. Correlation Heatmap - Relationships between numerical features
7. Pairplot - Comprehensive view of all variable relationships

## Skills Demonstrated

- Data loading and cleaning with Pandas
- Statistical analysis and data aggregation
- Data visualization with Matplotlib and Seaborn
- Exploratory data analysis techniques
- Jupyter notebook workflow
- Documentation and reporting

## References

- Fisher, R. A. (1936). The use of multiple measurements in taxonomic problems
- Scikit-learn: Machine Learning in Python
- Pandas documentation
- Matplotlib documentation
