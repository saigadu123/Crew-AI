# Employee Data Analysis Report

## Introduction
This report provides a comprehensive analysis of the employee dataset, which includes detailed information about employees in a company. The dataset is structured to aid HR or organizational analysis, focusing on employee skills, roles, and compensation across different departments and locations.

## Data Overview
The dataset includes the following columns:
- **Employee ID**: Unique identifier for each employee.
- **First Name, Last Name, Email**: Personal information.
- **Level, Years of Experience**: Professional experience metrics.
- **Date of Joining (DOJ)**: Date when the employee joined the company.
- **Compensation in USD**: Employee's salary.
- **Primary Skill, Secondary Skill, Role, Department, Education, Organization Entity, Location**: Professional attributes and organizational details.

## Data Analysis

### 1. Missing Values Analysis
- The dataset contains no missing values, ensuring completeness for analysis.

### 2. Data Type Standardization
- **Strings**: Employee ID, First Name, Last Name, Email, Primary Skill, Secondary Skill, Role, Department, Education, Organization Entity, Location.
- **Integers**: Level, Years of Experience.
- **Date**: DOJ (converted from string).
- **Numeric**: Compensation (USD) (converted from string with commas).

### 3. Potential Outliers
- **Compensation**: Ranges from $85,000 to $155,000.
- **Years of Experience**: Ranges from 2 to 18 years.

### 4. Statistical Metrics
- **Compensation (USD)**: 
  - Mean = $117,500
  - Median = $112,500
- **Years of Experience**: 
  - Mean = 8.6 years
  - Median = 7.5 years
- There is a positive correlation between Years of Experience and Compensation.

### 5. Final Data Type Conversion
- DOJ has been converted to date format.
- Compensation (USD) has been converted to numeric format.

## Visualizations

### Histogram of Compensation
![Histogram of Compensation](graphs/compensation_histogram.png)

### Scatter Plot of Years of Experience vs Compensation
![Scatter Plot of Years of Experience vs Compensation](graphs/experience_vs_compensation.png)

### Bar Chart of Average Compensation by Department
![Bar Chart of Average Compensation by Department](graphs/avg_compensation_by_department.png)

### Heatmap of Correlation Between Numeric Features
![Heatmap of Correlation Between Numeric Features](graphs/correlation_heatmap.png)

### Line Plot of Number of Employees Joining Over Time
![Line Plot of Number of Employees Joining Over Time](graphs/employees_joining_over_time.png)

## Conclusion
The analysis of the employee dataset reveals key insights into the distribution of skills and roles within the organization. The positive correlation between years of experience and compensation suggests that experience is a significant factor in determining salary. The visualizations provide a clear depiction of compensation distribution, departmental salary averages, and employee joining trends over time. These insights can aid in workforce planning and talent management strategies.

## Recommendations
- Consider further analysis on the impact of skills and education on compensation.
- Explore potential strategies to address any identified outliers in compensation.
- Utilize the insights for strategic workforce planning and development initiatives.
```