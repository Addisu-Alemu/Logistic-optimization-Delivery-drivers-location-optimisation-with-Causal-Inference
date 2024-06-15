# Logistic-optimization-with-Causal-Inference

# Business Need

The business need is to use data analysis and optimization techniques to identify the causes of unfulfilled delivery requests and develop solutions that recommend optimal driver placement to increase the completion rate of orders, thereby improving client satisfaction and growing Gokada's business.

# Causal inference

Causal inference is a crucial field within statistics and machine learning that delves into understanding and quantifying the causal relationships between variables. It goes beyond simply identifying correlations and seeks to answer fundamental questions about cause and effect. For instance, causal inference aims to determine the effect of a specific intervention or treatment on an outcome, whether changing one variable directly causes a change in another, and the extent to which a specific factor contributes to a particular outcome.

# Steps used to perform causal inference

## Data Enrichment: Expanding the data parameters
Think about factors like weather (rain or no rain), time of year (holiday or not), day of the week (weekday or weekend), and even things like the speed of a motorbike, or the distance of a trip.

## Exploratory Data Analysis (EDA): Cleaning and Preparing the Data 

Cleaning: Fix any errors or inconsistencies in the data. This makes sure your analysis is based on reliable information.
Normalizing: Put all the data on a similar scale (like 0 to 1). This helps algorithms work better and compare different variables fairly.
Identifying Outliers: Look for unusual data points that might be mistakes or represent special situations.

## Using CausalNex: Building and Analyzing a Causal Model

### Prepare Data for Structure Learning: 
    Make sure all the data is in a format that the algorithms can understand (usually numeric).
### Apply NOTEARS Algorithm:
    This algorithm helps discover the causal relationships hidden within the data. 
### Visualize the Graph:
    Create a diagram that shows how the variables are connected. This makes it easier to understand the causal relationships.
