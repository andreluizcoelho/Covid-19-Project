### This repository contains a project that I completed as part of my Ph.D. in Economics coursework at [PIMES/UFPE](https://sites.google.com/view/pimes/principal) in Recife, Brazil. The project was submitted at the end of July 2021 and is quite lengthy. Therefore, on April 5th, 2023, I have decided to break it down into smaller parts. [This](https://github.com/andreluizcoelho/Covid-19-Project/blob/main/covid19project_andreluizcoelho.ipynb) is the first original final project.

## 1. Webscraping 
#### The Covid-19 data is initially webscraped with information such as Total Cases and Death Cases from [World Meters](https://www.worldometers.info/coronavirus/). 


## 2. Covid-19 Vaccines
#### Vaccine data is acquired using url from a [Github](https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv) page.

## 3. Countries Indicators 
### 3.1 Human Development Index
#### The [downloaded](https://hdr.undp.org/data-center/human-development-index#/indicies/HDI) newest HDI is from 2021. On the [first](https://github.com/andreluizcoelho/Covid-19-Project/blob/main/covid19project_andreluizcoelho.ipynb) original final project the newest HDI was from 2019. So, some details in the code had to change.
#### The [ISO](https://www.iso.org/standards.html) from each country is generated in this section
### 3.2 World Bank Data
#### 3.2.1 Growth Domestic Product (GDP) per capita
#### The GDP per capita data can be downloaded [here](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD), and for direct [download](https://api.worldbank.org/v2/en/indicator/NY.GDP.PCAP.CD?downloadformat=excel)
#### GDP per capita is also for 2021, where in the original final project it was from 2019. 
#### 3.2.2 Growth Domestic Product (GDP) 
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
