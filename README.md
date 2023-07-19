### This repository contains a project that I completed as part of my Ph.D. in Economics coursework at [PIMES/UFPE](https://sites.google.com/view/pimes/principal) in Recife, Brazil. The project was submitted at the end of July 2021 and is quite lengthy. Therefore, on April 5th, 2023, I have decided to break it down into smaller parts. [This](https://github.com/andreluizcoelho/Covid-19-Project/blob/main/covid19project_andreluizcoelho.ipynb) is the first original final project. The project is a descriptive analysis which uses Covid data and many Economic data. It begins with webscraping and it ends with machine learning application, besides including many data visualizations after several merges between the data.  

## Data Science Covid-19 Project Overview 

* In this Data Science Covid-19 Project, I conducted a comprehensive analysis of the pandemic's impact on various countries using a wide range of data sources and statistical methods. The project can be outlined as follows:
* Collected Covid-19 data from world meters using Python's web scraping techniques. Additionally, acquired vaccine data to correlate with Covid-19 cases and death rates.
* Merged the Covid-19 data and vaccine data with country indicators such as the Human Development Index, Gross Domestic Product (GDP), GDP per capita, unemployment rate, inflation rate, and annual GDP growth.
* To provide a comprehensive visual representation, I created various graphs such as scatter plots, bar graphs, pie charts, tree maps, trendlines, as well as world maps with shapefiles using latitude and longitude data. I utilized libraries such as Plotly, Matplotlib, Geopandas, and others to enhance the visual aspect of the analysis.
* Statistical tests were employed to assess the significance between different variables.
* For the econometric analysis, I utilized a diverse set of models including linear regression, multivariate regression, tested for endogeneity, two-stage least squares, Hausman test, OLS (Ordinary Least Squares), Regression Discontinuity Design (RDD), and Difference-in-Difference (Dif-in-Dif). I also employed Logit regression and quantile regression to explore correlations and causal relationships between variables such as GDP per capita and Covid-19 cases or fatalities, and the potential impact of unemployment rates on the number of Covid-19 cases. Many other variables were also tested.
* Spatial Econometrics was used to analyze spatial autocorrelation, both global and local, to understand how Covid-19 cases and fatalities might affect neighboring countries.
* Machine learning techniques, including Support Vector Classifier (SVC), Logistic Regression, Decision Trees, and Random Forests, were applied for prediction purposes. For instance, I predicted Covid-19 mortality rates based on whether a country falls into the high income group, upper middle income group, lower middle income group, or lower income group.
* The project is divided into separate sections, each focusing on specific analyses and methodologies. I have made the data and relevant links available for download or web scraping for further exploration.
* By conducting this comprehensive analysis, we aimed to gain valuable insights into the correlations and impacts of various factors related to Covid-19, contributing to a deeper understanding of the pandemic's effects on different countries and populations.


## 1. Webscraping 
#### The Covid-19 data is initially webscraped with information such as Total Cases and Death Cases from [World Meters](https://www.worldometers.info/coronavirus/). 


## 2. Covid-19 Vaccines
#### Vaccine data is acquired using url from a [Github](https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv) page.

## 3. Countries Indicators 
### 3.1 Human Development Index
#### The [downloaded](https://hdr.undp.org/data-center/human-development-index#/indicies/HDI) newest HDI is from 2021. On the [first](https://github.com/andreluizcoelho/Covid-19-Project/blob/main/covid19project_andreluizcoelho.ipynb) original final project the newest HDI was from 2019. So, some details in the code had to change.
#### The [ISO](https://www.iso.org/standards.html) from each country is generated in this section
### 3.2 World Bank Data
#### 3.2.1 Gross Domestic Product (GDP) per capita
#### The GDP per capita data can be downloaded [here](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD), and for direct [download](https://api.worldbank.org/v2/en/indicator/NY.GDP.PCAP.CD?downloadformat=excel)
#### GDP per capita is also for 2021, where in the original final project it was from 2019. 
#### 3.2.2 Gross Domestic Product (GDP) 
#### The GPD data can be downloaded [here](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD), and for direct [download](https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD?downloadformat=excel)
#### GDP is also for 2021, where in the original final project it was from 2019 
#### 3.2.3 Unemployment Rate 
#### The Unemployment Rate data can be downloaded [here](https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS), and for direct [download](https://api.worldbank.org/v2/en/indicator/SL.UEM.TOTL.ZS?downloadformat=excel)
#### The Unemployment data is for 2021, where in the original final project it was from 2020.
#### 3.2.4 Inflation Rate 
#### The Inflation Rate data can be downloaded [here](https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG), and for direct [download](https://api.worldbank.org/v2/en/indicator/FP.CPI.TOTL.ZG?downloadformat=excel)
#### The Inflation data is for 2021, where in the original final project it was from 2019.
#### 3.2.5 GDP Growth (Annual %) 
#### The GDP growth data can be downloaded [here](https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG), for direct [download](https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.KD.ZG?downloadformat=excel)
#### The GDP Growth data is for 2021, where in the original final project it was from 2019.
## 4. Merging the datas
#### Merging World Indicators Data (World Bank (GDP, GDP per capita, GDP growth, unemployment rate, inflation rate) & United Nations (HDI)) with Covid Vaccines and then with Covid Cases/Deaths
### 4.1 Merging World Bank Data (GDP, GDP per capita, GDP growth, unemployment rate, inflation rate)
#### 4.1.1 Merging GDP with GDP per capita
#### 4.1.2 Merging GDP growth with gdppercapitagdp (the merge between GDP with GDP per capita)
#### 4.1.3 Merging between Unemployment rate and Inflation Rate
#### 4.1.4 Merging between GDPs (gdp, gdp per capita and gdp growth) with unemploymentinflationrate (unemployment rate and inflation rate)
### 4.2 Merging World Bank Data (GDP, GDP per capita, GDP growth, unemployment rate, inflation rate) & United Nations (HDI)
### 4.3 Merging Economic Indicator (World Bank Data with United Nations (HDI)) with Covid Vaccines
### 4.4 Merging the (Economic Indicators and Covid Vaccines) with Covid Cases/Deaths
## 5. Data Visualization
#### OBS: Unfortunately, the graphs from Plotly are not rendered on the GitHub page when the ipynb file is opened. While many of these graphs are interactive, only a static image with the 'fig.show('svg')' code is displayed, although some maps still will not show up, and some will show up less nicely and not interactive. Without this code, nothing will appear when opening the ipynb file. To experience the full interactivity of the Plotly graphs, please run the code on your own machine without the 'fig.show('svg')' code. That's why there are two versions uploaded for Part 5 - '5. Data Visualization' which is interactive and '5. Data Visualization Static' which can be displayed on the GitHub page.
### 5.1 Mapping
#### 5.1.1 Globe
#### 5.1.2 World Map
### 5.2 Graphs
#### 5.2.1 Scatter Plots
#### 5.2.2 Bar Graphs
#### 5.2.3 Pie Chart
#### 5.2.4 Tree Map
#### 5.2.5 Trendline
### 5.3 Maps with Shapefiles
#### obs: There are two very common ways to work with map plotting:
#### 1.From latitude and longitude finding a point to plot over the shapefile OR 2.Merging the shapefile with the data, not plotting the point over it
#### 5.3.1 From latitude and longitude finding a point to plot over the shapefile
#### 5.3.2 Merging the shapefile with the data, not plotting the point over it
### 5.4 More Maps, Bubble Chart and Boxplot with Plotly
## 6. Statistics
## 7. Econometrics
### 7.1 Linear Regression
### 7.2 Multivariate Regression Model
### 7.3 Endogeneity
#### 7.3.1 Two-stage least squares (2SLS) regression
##### 7.3.1.1 First Stage
##### 7.3.1.2 Second Stage
#### 7.3.2 Hausman Test
### 7.4 The OLS parameter 𝛽 estimated using matrix algebra and numpy
### 7.5 Regression Discontinuity Design (RDD)
### 7.6 Difference-in-Difference (Dif-in-Dif)
### 7.7 More OLS 
#### 7.7.1 Robust Linear Regression
### 7.8 Logit Regression
### 7.9 Quantile Regression
## 8. Spatial Econometrics
### 8.1 Spatial Autocorrelation
#### 8.1.1 Spatial Similarity
#### 8.1.2 Attribute Similarity
### 8.2 Global Spatial Autocorrelation
#### 8.2.1 Join Counts
#### 8.2.2 Continous Case
### 8.3 Local Autocorrelation: Hot Spots, Cold Spots, and Spatial Outliers
## 9. Machine Learning
### 9.1 Support Vector Classifier (SVC)
### 9.2 Logistic Regression, Decision Tree, and Random Forest 
