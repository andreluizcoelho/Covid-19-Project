#!/usr/bin/env python
# coding: utf-8

# I worked on this project for a Python elective course during my doctoral studies in economics at PIMES for approximately three months. The project required the inclusion of at least one section on web scraping and data visualization. While many sections of the project were not covered in the course, particularly the libraries I utilized, there were also other course sections that were not included in the project. I selected Covid-19 as the theme for this project, and the data was scraped from the web on April 5th 2023 (the data on covid19project_andreluizcoelho.ipynb on the same repository was scraped on July 30th, 2021). Any data analyzed can be downloaded using the links provided throughout the project.

# # Covid-19 

# ## 1. Webscraping Covid-19 Total and Death Cases

# In[1]:


#importing libraries


# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[3]:


#defining the url


# In[4]:


url = 'https://www.worldometers.info/coronavirus/'


# In[5]:


url


# In[6]:


#get request to get the raw html content


# In[7]:


html_content = requests.get(url).text


# In[8]:


html_content


# In[9]:


#parsing the html code for the entire site


# In[10]:


soup = BeautifulSoup(html_content, 'lxml')


# In[11]:


#print the parsed data of html


# In[12]:


print(soup.prettify())


# In[13]:


#picking the id of the table to scrape and extract html for only the specific table


# In[14]:


covid_table = soup.find('table', attrs = {'id': 'main_table_countries_today'})


# In[15]:


#head will form the columns


# In[16]:


head = covid_table.thead.find_all('tr') 
#the <table> tag defines an HTML table 
#each table row is defined with a <tr> tag
#A <tr> element contains one or more <th> or <td> elements
#each table data/cell is defined with a <td> tag
#The <th> tag defines a header cell in an HTML table


# In[17]:


head #headers are inside this html code


# In[18]:


#extracting headers from html to a list


# In[19]:


headings = []
for th in head[0].find_all('th'):
    #removing newlines and extra spaces from left and right
    print(th.text)
    headings.append(th.text.replace('\n','').strip())
print(headings)


# In[20]:


#extracting the rest of rows with tbody element


# In[21]:


body = covid_table.tbody.find_all('tr')


# In[22]:


body


# In[23]:


body[0] #the first row for example


# In[24]:


#appending the values of rows into a list, since there are lists inside a list here
#declaring empty list data that'll hold all rows data


# In[25]:


data = []
for r in range(1, len(body)):
    row = [] #empty list to hold one row data
    for tr in body[r].find_all('td'):
        row.append(tr.text.replace('\n','').strip())
        #appending row data to row after removing newlines escape and triming unnecessary spaces
    data.append(row)


# In[26]:


data


# In[27]:


row


# In[28]:


#data contains all the rows excluding header
#row contains data for one row


# In[29]:


#passing the values on the body as the data and headings as the columns 
#to a DataFrame


# In[30]:


#with headings as the columns


# In[31]:


df = pd.DataFrame(data, columns = headings)


# In[32]:


df


# In[33]:


df.shape


# In[34]:


df.head()


# In[35]:


df.head(10)


# In[36]:


df.tail()


# In[37]:


#to end up with the data only from today, it's needed to remove duplicates, because the data is kept up to three days on the website


# In[38]:


data=df[df['#']!=''].reset_index(drop=True)


# In[39]:


#the data points with # value are the contries while data points with null values for # columns are features like continents, totals, etc


# In[40]:


data


# In[41]:


data = data.drop_duplicates(subset = ['Country,Other'])


# In[42]:


#because the worldmeter reports data for up to three days, counting today to two days back, there's a need to drop duplicates
#when duplicates are removed, the values for the last two days are removed, while today´s values are kept


# In[43]:


data.head()


# In[44]:


#if some columns are wished to be dropped, as the ones below


# In[45]:


cols = ['#', 
        'Tot\xa0Cases/1M pop',
        'Deaths/1M pop',
        'Tests/1M pop', 
        '1 Caseevery X ppl',
        '1 Deathevery X ppl',
        '1 Testevery X ppl']


# In[46]:


cols


# In[47]:


data_final = data.drop(cols, axis=1)


# In[48]:


data_final.head()


# In[49]:


data_final.tail()


# In[50]:


data_final


# In[51]:


pd.set_option('display.max_rows', None)


# In[52]:


data_final


# In[53]:


pd.set_option('display.max_rows', 100)


# In[54]:


data_final


# In[55]:


data_final.to_excel('covidcasesdeaths_April5th2023.xlsx', index=False) #index=False saves the file without the first "Unnamed: 0" column, otherwise, there's the need to drop this column every time after openning the file


# ### Continue on part 2 Covid-19 Vaccines

# # 2. Covid-19 Vaccines

# In[1]:


import pandas as pd 


# In[2]:


url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv'


# In[3]:


df = pd.read_csv(url)


# In[4]:


df


# In[5]:


df = df.groupby('location')['total_vaccinations', 'iso_code', 'date', 'people_vaccinated', 'people_fully_vaccinated', 'daily_vaccinations_raw', 'daily_vaccinations', 'total_vaccinations_per_hundred', 'people_vaccinated_per_hundred', 'people_fully_vaccinated_per_hundred', 'daily_vaccinations_per_million'].max().reset_index()


# In[6]:


df.head()


# In[7]:


pd.set_option('display.max_rows', None)


# In[8]:


df


# In[9]:


pd.set_option('display.max_rows', 100)


# In[10]:


df.to_excel('covidvaccinationsApril5th2023.xlsx', index = False)


# ### Continue on part 3 Countries Indicators

# # 3. Countries Indicators

# ## 3.1 Human Development Index

# The HDI data can be downloaded [here](https://hdr.undp.org/data-center/human-development-index#/indicies/HDI), and for direct download [here](https://hdr.undp.org/sites/default/files/2021-22_HDR/HDR21-22_Statistical_Annex_HDI_Table.xlsx)

# ![](https://hdr.undp.org/sites/default/files/styles/original/public/images/2022-03/hdiRoadMap.png?itok=_Q5mwWs0)

# In[1]:


import pandas as pd


# In[2]:


hdiranking2021 = pd.read_excel('C:/Users/andre/Documents/Programming Languages/Python/pimespython/Project/Ajusting the Final Project from 31-07-2021 now April 4th 2023/HDR21-22_Statistical_Annex_HDI_Table.xlsx', sheet_name='Table 1')


# In[3]:


hdiranking2021 


# In[4]:


hdiranking2021.shape


# In[5]:


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns',None)


# In[6]:


hdiranking2021


# In[7]:


hdiranking2021.drop(hdiranking2021.index[0:3], inplace = True)


# In[8]:


hdiranking2021


# In[9]:


hdiranking2021.drop(hdiranking2021.index[196:], inplace = True)


# In[10]:


hdiranking2021


# In[11]:


hdiranking2021.drop(['Unnamed: 3','Unnamed: 5','Unnamed: 7','Unnamed: 9'], axis=1, inplace = True) 


# In[12]:


hdiranking2021


# In[13]:


hdiranking2021.drop(hdiranking2021.columns[7:],axis=1, inplace = True)


# In[14]:


hdiranking2021


# In[15]:


hdiranking2021.reset_index(drop=True, inplace=True)


# In[16]:


hdiranking2021


# In[17]:


hdiranking2021.drop(hdiranking2021.index[[3,70,120,165]], axis=0, inplace = True)


# In[18]:


hdiranking2021


# In[19]:


hdiranking2021.reset_index(drop=True, inplace=True)


# In[20]:


hdiranking2021


# In[21]:


hdiranking2021.rename(columns=hdiranking2021.iloc[0], inplace = True)


# In[22]:


hdiranking2021


# In[23]:


hdiranking2021.drop(hdiranking2021.index[0:3], inplace = True)


# In[24]:


hdiranking2021


# In[25]:


hdiranking2021.reset_index(drop=True, inplace=True)


# In[26]:


hdiranking2021


# In[27]:


hdiranking2021.set_axis(['HDI rank', 'Country', 'Human Development Index (HDI)','Life expectancy at birth','Expected years of schooling','Mean years of schooling', 'Gross national income (GNI) per capita'], axis=1, inplace = True)


# In[28]:


hdiranking2021


# In[29]:


pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)


# In[30]:


hdiranking2021


# I need the country's iso code 3 to merge with the other data, if merging by Country name many information will be lost

# In[31]:


print(hdiranking2021['Country'].tolist())


# In[32]:


#pip install country-converter


# In[33]:


import country_converter as coco
some_names = ['Switzerland', 'Norway', 'Iceland', 'Hong Kong, China (SAR)', 'Australia', 'Denmark', 'Sweden', 'Ireland', 'Germany', 'Netherlands', 'Finland', 'Singapore', 'Belgium', 'New Zealand', 'Canada', 'Liechtenstein', 'Luxembourg', 'United Kingdom', 'Japan', 'Korea (Republic of)', 'United States', 'Israel', 'Malta', 'Slovenia', 'Austria', 'United Arab Emirates', 'Spain', 'France', 'Cyprus', 'Italy', 'Estonia', 'Czechia', 'Greece', 'Poland', 'Bahrain', 'Lithuania', 'Saudi Arabia', 'Portugal', 'Latvia', 'Andorra', 'Croatia', 'Chile', 'Qatar', 'San Marino', 'Slovakia', 'Hungary', 'Argentina', 'Türkiye', 'Montenegro', 'Kuwait', 'Brunei Darussalam', 'Russian Federation', 'Romania', 'Oman', 'Bahamas', 'Kazakhstan', 'Trinidad and Tobago', 'Costa Rica', 'Uruguay', 'Belarus', 'Panama', 'Malaysia', 'Georgia', 'Mauritius', 'Serbia', 'Thailand', 'Albania', 'Bulgaria', 'Grenada', 'Barbados', 'Antigua and Barbuda', 'Seychelles', 'Sri Lanka', 'Bosnia and Herzegovina', 'Saint Kitts and Nevis', 'Iran (Islamic Republic of)', 'Ukraine', 'North Macedonia', 'China', 'Dominican Republic', 'Moldova (Republic of)', 'Palau', 'Cuba', 'Peru', 'Armenia', 'Mexico', 'Brazil', 'Colombia', 'Saint Vincent and the Grenadines', 'Maldives', 'Algeria', 'Azerbaijan', 'Tonga', 'Turkmenistan', 'Ecuador', 'Mongolia', 'Egypt', 'Tunisia', 'Fiji', 'Suriname', 'Uzbekistan', 'Dominica', 'Jordan', 'Libya', 'Paraguay', 'Palestine, State of', 'Saint Lucia', 'Guyana', 'South Africa', 'Jamaica', 'Samoa', 'Gabon', 'Lebanon', 'Indonesia', 'Viet Nam', 'Philippines', 'Botswana', 'Bolivia (Plurinational State of)', 'Kyrgyzstan', 'Venezuela (Bolivarian Republic of)', 'Iraq', 'Tajikistan', 'Belize', 'Morocco', 'El Salvador', 'Nicaragua', 'Bhutan', 'Cabo Verde', 'Bangladesh', 'Tuvalu', 'Marshall Islands', 'India', 'Ghana', 'Micronesia (Federated States of)', 'Guatemala', 'Kiribati', 'Honduras', 'Sao Tome and Principe', 'Namibia', "Lao People's Democratic Republic", 'Timor-Leste', 'Vanuatu', 'Nepal', 'Eswatini (Kingdom of)', 'Equatorial Guinea', 'Cambodia', 'Zimbabwe', 'Angola', 'Myanmar', 'Syrian Arab Republic', 'Cameroon', 'Kenya', 'Congo', 'Zambia', 'Solomon Islands', 'Comoros', 'Papua New Guinea', 'Mauritania', "Côte d'Ivoire", 'Tanzania (United Republic of)', 'Pakistan', 'Togo', 'Haiti', 'Nigeria', 'Rwanda', 'Benin', 'Uganda', 'Lesotho', 'Malawi', 'Senegal', 'Djibouti', 'Sudan', 'Madagascar', 'Gambia', 'Ethiopia', 'Eritrea', 'Guinea-Bissau', 'Liberia', 'Congo (Democratic Republic of the)', 'Afghanistan', 'Sierra Leone', 'Guinea', 'Yemen', 'Burkina Faso', 'Mozambique', 'Mali', 'Burundi', 'Central African Republic', 'Niger']
standard_names = coco.convert(names=some_names, to='ISO3')
print(standard_names)


# In[34]:


isocode3 = ['CHE', 'NOR', 'ISL', 'HKG', 'AUS', 'DNK', 'SWE', 'IRL', 'DEU', 'NLD', 'FIN', 'SGP', 'BEL', 'NZL', 'CAN', 'LIE', 'LUX', 'GBR', 'JPN', 'KOR', 'USA', 'ISR', 'MLT', 'SVN', 'AUT', 'ARE', 'ESP', 'FRA', 'CYP', 'ITA', 'EST', 'CZE', 'GRC', 'POL', 'BHR', 'LTU', 'SAU', 'PRT', 'LVA', 'AND', 'HRV', 'CHL', 'QAT', 'SMR', 'SVK', 'HUN', 'ARG', 'TUR', 'MNE', 'KWT', 'BRN', 'RUS', 'ROU', 'OMN', 'BHS', 'KAZ', 'TTO', 'CRI', 'URY', 'BLR', 'PAN', 'MYS', 'GEO', 'MUS', 'SRB', 'THA', 'ALB', 'BGR', 'GRD', 'BRB', 'ATG', 'SYC', 'LKA', 'BIH', 'KNA', 'IRN', 'UKR', 'MKD', 'CHN', 'DOM', 'MDA', 'PLW', 'CUB', 'PER', 'ARM', 'MEX', 'BRA', 'COL', 'VCT', 'MDV', 'DZA', 'AZE', 'TON', 'TKM', 'ECU', 'MNG', 'EGY', 'TUN', 'FJI', 'SUR', 'UZB', 'DMA', 'JOR', 'LBY', 'PRY', 'PSE', 'LCA', 'GUY', 'ZAF', 'JAM', 'WSM', 'GAB', 'LBN', 'IDN', 'VNM', 'PHL', 'BWA', 'BOL', 'KGZ', 'VEN', 'IRQ', 'TJK', 'BLZ', 'MAR', 'SLV', 'NIC', 'BTN', 'CPV', 'BGD', 'TUV', 'MHL', 'IND', 'GHA', 'FSM', 'GTM', 'KIR', 'HND', 'STP', 'NAM', 'LAO', 'TLS', 'VUT', 'NPL', 'SWZ', 'GNQ', 'KHM', 'ZWE', 'AGO', 'MMR', 'SYR', 'CMR', 'KEN', 'COG', 'ZMB', 'SLB', 'COM', 'PNG', 'MRT', 'CIV', 'TZA', 'PAK', 'TGO', 'HTI', 'NGA', 'RWA', 'BEN', 'UGA', 'LSO', 'MWI', 'SEN', 'DJI', 'SDN', 'MDG', 'GMB', 'ETH', 'ERI', 'GNB', 'LBR', 'COD', 'AFG', 'SLE', 'GIN', 'YEM', 'BFA', 'MOZ', 'MLI', 'BDI', 'CAF', 'NER']


# In[35]:


isocode3


# In[36]:


dfisocode3 = pd.DataFrame(isocode3)


# In[37]:


dfisocode3


# In[38]:


dfisocode3.rename({0:"Country Code"}, axis = 'columns', inplace=True)  


# In[39]:


dfisocode3


# In[40]:


dfisocode3.join(hdiranking2021)


# In[41]:


pd.set_option('display.max_rows', None)


# In[42]:


dfisocode3.join(hdiranking2021)


# In[43]:


hdiranking2021 = dfisocode3.join(hdiranking2021)


# In[44]:


hdiranking2021


# In[45]:


pd.set_option('display.max_rows', 100)


# In[46]:


hdiranking2021


# In[47]:


hdiranking2021.rename({'Human Development Index (HDI)':'Human Development Index 2021 (HDI)'}, axis = 'columns', inplace = True)


# In[48]:


hdiranking2021


# In[49]:


hdiranking2021.to_excel('hdiranking2021.xlsx', index = False)


# ## 3.2 World Bank Data

# ### 3.2.1 Growth Domestic Product (GDP) per capita

# The GDP per capita data can be downloaded [here](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD), and for direct [download](https://api.worldbank.org/v2/en/indicator/NY.GDP.PCAP.CD?downloadformat=excel)

# In[50]:


gdppercapita2021 = pd.read_excel('C:/Users/andre/Documents/Programming Languages/Python/pimespython/Project/Ajusting the Final Project from 31-07-2021 now April 4th 2023/API_NY.GDP.PCAP.CD_DS2_en_excel_v2_5358450.xls', sheet_name = 'Data')


# In[51]:


gdppercapita2021


# In[52]:


gdppercapita2021.shape


# In[53]:


gdppercapita2021.head()


# In[54]:


gdppercapita2021.tail()


# In[55]:


gdppercapita2021['Unnamed: 64'].isna().sum()


# In[56]:


gdppercapita2021['Unnamed: 65'].isna().sum()


# In[57]:


gdppercapita2021['Unnamed: 63'].isna().sum()


# In[58]:


gdppercapita2021['Unnamed: 62'].isna().sum()


# In[59]:


gdppercapita2021regiongroup = pd.read_excel('C:/Users/andre/Documents/Programming Languages/Python/pimespython/Project/Ajusting the Final Project from 31-07-2021 now April 4th 2023/API_NY.GDP.PCAP.CD_DS2_en_excel_v2_5358450.xls', sheet_name = 'Metadata - Countries')


# In[60]:


gdppercapita2021regiongroup


# In[61]:


gdppercapita2021.head()


# In[62]:


gdppercapita2021.drop(gdppercapita2021.columns[2:65],axis=1)


# In[63]:


gdppercapita2021.drop(gdppercapita2021.columns[2:65],axis=1, inplace = True)


# In[64]:


gdppercapita2021.drop(gdppercapita2021.index[0:2], inplace = True)


# In[65]:


gdppercapita2021.rename(columns=gdppercapita2021.iloc[0], inplace = True)


# In[66]:


gdppercapita2021


# In[67]:


gdppercapita2021.rename({2021.0:'GDP per capita 2021 (US$)'}, axis = 'columns', inplace=True)


# In[68]:


gdppercapita2021


# In[69]:


gdppercapita2021.reset_index(drop=True,inplace=True)


# In[70]:


pd.set_option('display.max_rows', None)


# In[71]:


gdppercapita2021


# In[72]:


gdppercapita2021 = gdppercapita2021.dropna()


# In[73]:


gdppercapita2021 = gdppercapita2021[1:]


# In[74]:


gdppercapita2021


# In[75]:


gdppercapita2021.reset_index(drop=True,inplace=True)


# In[76]:


gdppercapita2021


# In[77]:


gdppercapita2021regiongroup


# In[78]:


gdppercapita2021 = gdppercapita2021.merge(gdppercapita2021regiongroup, how='inner',on='Country Code', indicator=True)


# In[79]:


gdppercapita2021


# In[80]:


gdppercapita2021.drop(['SpecialNotes', 'TableName', '_merge'], axis = 1, inplace = True)


# In[81]:


gdppercapita2021 = gdppercapita2021.dropna()


# In[82]:


gdppercapita2021.reset_index(drop=True, inplace=True)


# In[83]:


gdppercapita2021


# In[84]:


pd.set_option('display.max_rows', 100)


# In[85]:


gdppercapita2021.to_excel('gdppercapita2021.xlsx', index = False)


# ### 3.2.2 Growth Domestic Product (GDP) 

# The GDP data can be downloaded [here](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD), and for direct [download](https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD?downloadformat=excel)

# In[86]:


gdp2021 = pd.read_excel('C:/Users/andre/Documents/Programming Languages/Python/pimespython/Project/Ajusting the Final Project from 31-07-2021 now April 4th 2023/API_NY.GDP.MKTP.CD_DS2_en_excel_v2_5358382.xls', sheet_name = 'Data')


# In[87]:


gdp2021


# In[88]:


gdp2021regiongroup = pd.read_excel('C:/Users/andre/Documents/Programming Languages/Python/pimespython/Project/Ajusting the Final Project from 31-07-2021 now April 4th 2023/API_NY.GDP.MKTP.CD_DS2_en_excel_v2_5358382.xls', sheet_name = 'Metadata - Countries')


# In[89]:


gdp2021regiongroup


# In[90]:


gdp2021


# In[91]:


gdp2021.drop(gdp2021.columns[2:65],axis=1)


# In[92]:


gdp2021.drop(gdp2021.columns[2:65],axis=1, inplace = True)


# In[93]:


gdp2021.drop(gdp2021.index[0:2], inplace = True)


# In[94]:


gdp2021


# In[95]:


gdp2021.rename(columns=gdp2021.iloc[0], inplace = True)


# In[96]:


gdp2021


# In[97]:


gdp2021.rename({2021.0:'GDP 2021 (US$)'}, axis = 'columns', inplace=True)


# In[98]:


gdp2021


# In[99]:


gdp2021.reset_index(drop=True, inplace=True)


# In[100]:


pd.set_option('display.max_rows',None)


# In[101]:


gdp2021


# In[102]:


gdp2021 = gdp2021.dropna()


# In[103]:


gdp2021 = gdp2021[1:]


# In[104]:


gdp2021


# In[105]:


gdp2021.reset_index(drop=True, inplace=True)


# In[106]:


gdp2021


# In[107]:


gdp2021regiongroup


# In[108]:


gdp2021= gdp2021.merge(gdp2021regiongroup, how = 'inner', on = 'Country Code', indicator = True)


# In[109]:


gdp2021


# In[110]:


gdp2021.drop(['SpecialNotes', 'TableName', '_merge'], axis = 1, inplace = True)


# In[111]:


gdp2021


# In[112]:


gdp2021 = gdp2021.dropna()


# In[113]:


gdp2021.reset_index(drop=True, inplace=True)


# In[114]:


gdp2021


# In[115]:


pd.set_option('display.max_rows', 100)


# In[116]:


gdp2021.to_excel('gdp2021.xlsx', index = False)


# ### 3.2.3 Unemployment Rate

# The Unemployment Rate data can be downloaded [here](https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS), and for direct [download](https://api.worldbank.org/v2/en/indicator/SL.UEM.TOTL.ZS?downloadformat=excel)

# In[117]:


unemploymentrate2021 = pd.read_excel('C:/Users/andre/Documents/Programming Languages/Python/pimespython/Project/Ajusting the Final Project from 31-07-2021 now April 4th 2023/API_SL.UEM.TOTL.ZS_DS2_en_excel_v2_5358380.xls', sheet_name = 'Data')


# In[118]:


unemploymentrate2021 


# In[119]:


unemploymentrate2021regiongroup = pd.read_excel('C:/Users/andre/Documents/Programming Languages/Python/pimespython/Project/Ajusting the Final Project from 31-07-2021 now April 4th 2023/API_SL.UEM.TOTL.ZS_DS2_en_excel_v2_5358380.xls', sheet_name = 'Metadata - Countries')


# In[120]:


unemploymentrate2021regiongroup


# In[121]:


unemploymentrate2021.head()


# In[122]:


unemploymentrate2021.drop(unemploymentrate2021.columns[2:65],axis=1,inplace=True)


# In[123]:


unemploymentrate2021


# In[124]:


unemploymentrate2021.drop(unemploymentrate2021.index[0:2], inplace = True)


# In[125]:


unemploymentrate2021.rename(columns = unemploymentrate2021.iloc[0], inplace = True)


# In[126]:


unemploymentrate2021


# In[127]:


unemploymentrate2021 = unemploymentrate2021[1:]


# In[128]:


unemploymentrate2021


# In[129]:


unemploymentrate2021 = unemploymentrate2021.dropna()


# In[130]:


unemploymentrate2021


# In[131]:


unemploymentrate2021.reset_index(drop=True, inplace=True)


# In[132]:


unemploymentrate2021


# In[133]:


unemploymentrate2021.rename({2021.0:'Unemployment Rate 2021 (%)'}, axis = 'columns', inplace=True)


# In[134]:


unemploymentrate2021


# In[135]:


unemploymentrate2021regiongroup


# In[136]:


unemploymentrate2021 = unemploymentrate2021.merge(unemploymentrate2021regiongroup, how='inner', on = 'Country Code', indicator = True)


# In[137]:


unemploymentrate2021


# In[138]:


unemploymentrate2021.drop(['SpecialNotes','TableName','_merge'], axis = 1, inplace = True)


# In[139]:


unemploymentrate2021


# In[140]:


unemploymentrate2021 = unemploymentrate2021.dropna()


# In[141]:


unemploymentrate2021


# In[142]:


unemploymentrate2021.reset_index(drop=True, inplace=True)


# In[143]:


unemploymentrate2021


# In[144]:


unemploymentrate2021.to_excel('unemploymentrate2021.xlsx', index = False)


# ### 3.2.4 Inflation Rate

# The Inflation Rate data can be downloaded [here](https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG), and for direct [download](https://api.worldbank.org/v2/en/indicator/FP.CPI.TOTL.ZG?downloadformat=excel)

# In[145]:


inflationrate2021 = pd.read_excel('C:/Users/andre/Documents/Programming Languages/Python/pimespython/Project/Ajusting the Final Project from 31-07-2021 now April 4th 2023/API_FP.CPI.TOTL.ZG_DS2_en_excel_v2_5358556.xls', sheet_name = 'Data')


# In[146]:


inflationrate2021


# In[147]:


inflationrate2021regiongroup = pd.read_excel('C:/Users/andre/Documents/Programming Languages/Python/pimespython/Project/Ajusting the Final Project from 31-07-2021 now April 4th 2023/API_FP.CPI.TOTL.ZG_DS2_en_excel_v2_5358556.xls', sheet_name = 'Metadata - Countries')


# In[148]:


inflationrate2021regiongroup


# In[149]:


inflationrate2021.drop(inflationrate2021.columns[2:65], axis = 1, inplace=True)


# In[150]:


inflationrate2021


# In[151]:


inflationrate2021.drop(inflationrate2021.index[0:2], inplace = True)


# In[152]:


inflationrate2021.rename(columns = inflationrate2021.iloc[0], inplace = True)


# In[153]:


inflationrate2021


# In[154]:


inflationrate2021 = inflationrate2021[1:]


# In[155]:


inflationrate2021


# In[156]:


inflationrate2021 = inflationrate2021.dropna()


# In[157]:


inflationrate2021


# In[158]:


inflationrate2021.reset_index(drop=True, inplace=True)


# In[159]:


inflationrate2021


# In[160]:


inflationrate2021.rename({2019.0:'Inflation Rate 2021 (%)'}, axis = 'columns', inplace = True)


# In[161]:


inflationrate2021


# In[162]:


inflationrate2021.drop(inflationrate2021.index[0:2], inplace = True)


# In[163]:


inflationrate2021


# In[164]:


inflationrate2021.reset_index(drop=True, inplace=True)


# In[165]:


inflationrate2021regiongroup


# In[166]:


inflationrate2021= inflationrate2021.merge(inflationrate2021regiongroup, how = 'inner', on = 'Country Code', indicator = True)


# In[167]:


inflationrate2021


# In[168]:


inflationrate2021.rename({2021.0:'Inflation Rate 2021 (%)'}, axis = 'columns', inplace = True)


# In[169]:


inflationrate2021 = inflationrate2021.iloc[:, [0,1,2,3,4]]


# In[170]:


inflationrate2021 = inflationrate2021.dropna()


# In[171]:


inflationrate2021.reset_index(drop = True, inplace = True)


# In[172]:


inflationrate2021


# In[173]:


inflationrate2021.to_excel('inflationrate2021.xlsx', index = False)


# ### 3.2.5 GDP Growth (Annual %)

# The GDP growth data can be downloaded [here](https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG), for direct [download](https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.KD.ZG?downloadformat=excel)

# In[174]:


gdpgrowth2021 = pd.read_excel('C:/Users/andre/Documents/Programming Languages/Python/pimespython/Project/Ajusting the Final Project from 31-07-2021 now April 4th 2023/API_NY.GDP.MKTP.KD.ZG_DS2_en_excel_v2_5358368.xls', sheet_name = 'Data')


# In[175]:


gdpgrowth2021


# In[176]:


gdpgrowth2021regiongroup = pd.read_excel('C:/Users/andre/Documents/Programming Languages/Python/pimespython/Project/Ajusting the Final Project from 31-07-2021 now April 4th 2023/API_NY.GDP.MKTP.KD.ZG_DS2_en_excel_v2_5358368.xls', sheet_name = 'Metadata - Countries')


# In[177]:


gdpgrowth2021regiongroup


# In[178]:


gdpgrowth2021.head()


# In[179]:


gdpgrowth2021 = gdpgrowth2021.iloc[:,[0,1,65]]


# In[180]:


gdpgrowth2021 


# In[181]:


gdpgrowth2021.drop(gdpgrowth2021.index[0:2], inplace = True)


# In[182]:


gdpgrowth2021


# In[183]:


gdpgrowth2021.rename(columns = gdpgrowth2021.iloc[0], inplace = True)


# In[184]:


gdpgrowth2021


# In[185]:


gdpgrowth2021.rename({2021.0:'GDP growth 2021 (annual %)'}, axis = 'columns', inplace = True)


# In[186]:


gdpgrowth2021


# In[187]:


gdpgrowth2021 = gdpgrowth2021.dropna()


# In[188]:


gdpgrowth2021 = gdpgrowth2021[1:]


# In[189]:


gdpgrowth2021.reset_index(drop = True, inplace = True)


# In[190]:


gdpgrowth2021


# In[191]:


gdpgrowth2021regiongroup


# In[192]:


gdpgrowth2021 = gdpgrowth2021.merge(gdpgrowth2021regiongroup, how = 'inner', on = 'Country Code', indicator = True)


# In[193]:


gdpgrowth2021


# In[194]:


gdpgrowth2021 = gdpgrowth2021.iloc[:,[0,1,2,3,4]]


# In[195]:


gdpgrowth2021


# In[196]:


gdpgrowth2021 = gdpgrowth2021.dropna()


# In[197]:


gdpgrowth2021


# In[198]:


gdpgrowth2021.reset_index(drop = True, inplace = True)


# In[199]:


gdpgrowth2021


# In[200]:


gdpgrowth2021.to_excel('gdpgrowth2021.xlsx', index = False)


# ## 4. Merging the datas

# Merging World Indicators Data (World Bank (GDP, GDP per capita, GDP growth, unemployment rate, inflation rate) & United Nations (HDI)) with Covid Vaccines and then with Covid Cases/Deaths

# #### 4.1 Merging World Bank Data (GDP, GDP per capita, GDP growth, unemployment rate, inflation rate)
# #### 4.2 Merging World Bank Data (GDP, GDP per capita, GDP growth, unemployment rate, inflation rate) & United Nations (HDI)
# #### 4.3 Merging Economic Indicators (World Bank Data with United Nations (HDI)) with Covid Vaccines
# #### 4.4 Merging the (Economic Indicators and Covid Vaccines) with Covid Cases/Deaths

# #### 4.1 Merging World Bank Data (GDP, GDP per capita, GDP growth, unemployment rate, inflation rate)

# ##### 4.1.1 Merging GDP with GDP per capita

# In[1]:


import pandas as pd


# In[2]:


gdp2021 = pd.read_excel('gdp2021.xlsx')


# In[3]:


gdp2021


# In[4]:


gdppercapita2021 = pd.read_excel('gdppercapita2021.xlsx')


# In[5]:


gdppercapita2021


# In[6]:


gdppercapitagdp = gdp2021.merge(gdppercapita2021, on = ['Country Name','Country Code'], how='inner', indicator = True)


# In[7]:


gdppercapitagdp


# In[8]:


gdppercapitagdp = gdppercapitagdp.iloc[:,[0,1,2,3,4,5]]


# In[9]:


gdppercapitagdp


# In[10]:


gdppercapitagdp = gdppercapitagdp[gdppercapitagdp.columns[[0,1,2,5,3,4]]]


# In[11]:


gdppercapitagdp 


# In[12]:


gdppercapitagdp.rename({'Region_x':'Region','IncomeGroup_x':'IncomeGroup'}, axis = 'columns', inplace = True)


# In[13]:


gdppercapitagdp


# #### 4.1.2 Merging GDP growth with gdppercapitagdp (the merge between GDP with GDP per capita)

# In[14]:


gdpgrowth2021 = pd.read_excel('gdpgrowth2021.xlsx')


# In[15]:


GDPs = gdpgrowth2021.merge(gdppercapitagdp, on = ['Country Code', 'Country Name'], how='inner', indicator = '_merge1')


# In[16]:


GDPs


# In[17]:


GDPs = GDPs.iloc[:, [0,1,2,3,4,5,6]]


# In[18]:


GDPs.rename({'Region_x':'Region', 'IncomeGroup_x': 'IncomeGroup'}, axis = 1, inplace = True)


# In[19]:


GDPs


# In[20]:


GDPs = GDPs[GDPs.columns[[0,1,5,6,2,3,4]]]


# In[21]:


GDPs


# #### 4.1.3 Merging between Unemployment rate and Inflation Rate

# In[22]:


inflationrate2021 = pd.read_excel('inflationrate2021.xlsx')


# In[23]:


inflationrate2021


# In[24]:


unemploymentrate2021 = pd.read_excel('unemploymentrate2021.xlsx')


# In[25]:


unemploymentrate2021


# In[26]:


unemploymentinflationrate = inflationrate2021.merge(unemploymentrate2021, on = ['Country Code', 'Country Name'], how='inner', indicator = '_merge2')


# In[27]:


unemploymentinflationrate.head()


# In[28]:


unemploymentinflationrate = unemploymentinflationrate.iloc[:, [0,1,2,3,4,5]]


# In[29]:


unemploymentinflationrate.rename({'Region_x':'Region','IncomeGroup_x':'IncomeGroup'}, axis = 'columns', inplace = True)


# In[30]:


unemploymentinflationrate = unemploymentinflationrate[unemploymentinflationrate.columns[[0,1,2,5,3,4]]]


# In[31]:


unemploymentinflationrate


# #### 4.1.4 Merging between GDPs (gdp, gdp per capita and gdp growth) with unemploymentinflationrate (unemployment rate and inflation rate)

# In[32]:


worldbankeconomicindicators = GDPs.merge(unemploymentinflationrate, on = ['Country Code', 'Country Name'], how='inner', indicator = '_merge3')


# In[33]:


worldbankeconomicindicators.head(3)


# In[34]:


worldbankeconomicindicators.drop(['Region_y','IncomeGroup_y','_merge3'], axis = 1, inplace = True)


# In[35]:


worldbankeconomicindicators.head()


# In[36]:


worldbankeconomicindicators.rename({'Region_x':'Region', 'IncomeGroup_x':'IncomeGroup'}, axis = 'columns', inplace = True)


# In[37]:


worldbankeconomicindicators.head(3)


# In[38]:


worldbankeconomicindicators = worldbankeconomicindicators[worldbankeconomicindicators.columns[[0,1,2,3,4,7,8,5,6]]]


# In[39]:


worldbankeconomicindicators


# ### 4.2 Merging World Bank Data (GDP, GDP per capita, GDP growth, unemployment rate, inflation rate) & United Nations (HDI)

# In[40]:


hdiranking2021 = pd.read_excel('hdiranking2021.xlsx')


# In[41]:


hdiranking2021


# In[42]:


economicindicators = hdiranking2021.merge(worldbankeconomicindicators, on = ['Country Code'], how='inner', indicator = '_merge4')


# In[43]:


economicindicators


# In[44]:


economicindicators.drop({'Country Name', '_merge4'}, axis = 'columns', inplace = True)


# In[45]:


economicindicators.head(3)


# In[46]:


economicindicators = economicindicators[economicindicators.columns[[0,2,1,3,4,5,6,7,8,9,10,11,12,13,14]]]


# In[47]:


economicindicators


# In[48]:


economicindicators.to_excel('economicindicators2021.xlsx', index = False)


# ### 4.3 Merging Economic Indicator (World Bank Data with United Nations (HDI)) with Covid Vaccines

# ####  merging economicindicators with covid19vaccinations first because it has isocode, then do the final merge with covid cases/deaths

# In[49]:


covidvaccinations = pd.read_excel('covidvaccinationsApril5th2023.xlsx')


# In[50]:


covidvaccinations


# In[51]:


economicindicatorsvaccines = economicindicators.merge(covidvaccinations, left_on = ['Country Code'], right_on = ['iso_code'], how='inner', indicator = True)


# In[52]:


economicindicatorsvaccines


# In[53]:


economicindicatorsvaccines.drop({'location', 'iso_code','_merge'}, axis = 'columns', inplace = True)


# In[54]:


economicindicatorsvaccines.head(3)


# #### finding the iso code 3 first for covid cases/deaths before the merge

# In[55]:


covidcasesdeaths = pd.read_excel('covidcasesdeaths_April5th2023.xlsx')


# In[56]:


covidcasesdeaths


# #### if the merge were to be done by country name, a lot of information would be lost; that's why finding the iso code 3 is so important to do the merge 

# In[57]:


print(covidcasesdeaths['Country,Other'].tolist()) 


# In[58]:


import country_converter as coco
some_names = ['USA', 'India', 'France', 'Germany', 'Brazil', 'Japan', 'S. Korea', 'Italy', 'UK', 'Russia', 'Turkey', 'Spain', 'Vietnam', 'Australia', 'Taiwan', 'Argentina', 'Netherlands', 'Iran', 'Mexico', 'Indonesia', 'Poland', 'Colombia', 'Austria', 'Greece', 'Portugal', 'Ukraine', 'Chile', 'Malaysia', 'Israel', 'Belgium', 'DPRK', 'Thailand', 'Czechia', 'Canada', 'Peru', 'Switzerland', 'Philippines', 'South Africa', 'Romania', 'Denmark', 'Hong Kong', 'Sweden', 'Serbia', 'Iraq', 'New Zealand', 'Singapore', 'Hungary', 'Bangladesh', 'Slovakia', 'Georgia', 'Jordan', 'Ireland', 'Pakistan', 'Norway', 'Finland', 'Kazakhstan', 'Slovenia', 'Lithuania', 'Bulgaria', 'Morocco', 'Croatia', 'Guatemala', 'Lebanon', 'Costa Rica', 'Bolivia', 'Tunisia', 'Cuba', 'Ecuador', 'UAE', 'Uruguay', 'Panama', 'Mongolia', 'Nepal', 'Belarus', 'Latvia', 'Saudi Arabia', 'Azerbaijan', 'Paraguay', 'Bahrain', 'Sri Lanka', 'Kuwait', 'Dominican Republic', 'Cyprus', 'Myanmar', 'Palestine', 'Moldova', 'Estonia', 'Venezuela', 'Egypt', 'Libya', 'Qatar', 'Ethiopia', 'Réunion', 'Honduras', 'Armenia', 'Bosnia and Herzegovina', 'Oman', 'North Macedonia', 'Zambia', 'Kenya', 'Albania', 'Botswana', 'Luxembourg', 'Montenegro', 'Brunei', 'Algeria', 'Nigeria', 'Zimbabwe', 'Uzbekistan', 'Mozambique', 'Martinique', 'Laos', 'Afghanistan', 'Iceland', 'Kyrgyzstan', 'Guadeloupe', 'El Salvador', 'Trinidad and Tobago', 'Maldives', 'Ghana', 'Namibia', 'Uganda', 'Jamaica', 'Cambodia', 'Rwanda', 'Cameroon', 'Malta', 'Barbados', 'Angola', 'Channel Islands', 'French Guiana', 'DRC', 'Senegal', 'Malawi', 'Ivory Coast', 'Suriname', 'New Caledonia', 'French Polynesia', 'Eswatini', 'Guyana', 'Belize', 'Fiji', 'Madagascar', 'Sudan', 'Mauritania', 'Cabo Verde', 'Bhutan', 'Syria', 'Burundi', 'Seychelles', 'Gabon', 'Andorra', 'Papua New Guinea', 'Curaçao', 'Aruba', 'Tanzania', 'Mayotte', 'Mauritius', 'Togo', 'Guinea', 'Isle of Man', 'Bahamas', 'Lesotho', 'Faeroe Islands', 'Haiti', 'Mali', 'Cayman Islands', 'Saint Lucia', 'Benin', 'Somalia', 'Micronesia', 'Congo', 'Solomon Islands', 'San Marino', 'Timor-Leste', 'Burkina Faso', 'Liechtenstein', 'Gibraltar', 'Grenada', 'Bermuda', 'Nicaragua', 'South Sudan', 'Tajikistan', 'Equatorial Guinea', 'Tonga', 'Samoa', 'Monaco', 'Marshall Islands', 'Dominica', 'Djibouti', 'CAR', 'Gambia', 'Saint Martin', 'Vanuatu', 'Greenland', 'Yemen', 'Caribbean Netherlands', 'Sint Maarten', 'Eritrea', 'Niger', 'St. Vincent Grenadines', 'Guinea-Bissau', 'Antigua and Barbuda', 'Comoros', 'Liberia', 'Sierra Leone', 'Chad', 'British Virgin Islands', 'Cook Islands', 'Saint Kitts and Nevis', 'Turks and Caicos', 'Sao Tome and Principe', 'Palau', 'St. Barth', 'Nauru', 'Kiribati', 'Anguilla', 'Macao', 'Saint Pierre Miquelon', 'Wallis and Futuna', 'Tuvalu', 'Saint Helena', 'Falkland Islands', 'Montserrat', 'Niue', 'Diamond Princess', 'Vatican City', 'Western Sahara', 'MS Zaandam', 'Tokelau', 'China']
standard_names = coco.convert(names=some_names, to='ISO3')
print(standard_names)


# In[59]:


covidcasesdeaths['Country,Other'].str.replace('UK','United Kingdom')


# In[60]:


covidcasesdeaths['Country,Other'] = covidcasesdeaths['Country,Other'].str.replace('UK','United Kingdom')
covidcasesdeaths['Country,Other'] = covidcasesdeaths['Country,Other'].str.replace('UAE','ARE')
covidcasesdeaths['Country,Other'] = covidcasesdeaths['Country,Other'].str.replace('DRC','COD')
covidcasesdeaths['Country,Other'] = covidcasesdeaths['Country,Other'].str.replace('CAR','CAF')


# In[61]:


covidcasesdeaths['Country,Other']


# In[62]:


print(covidcasesdeaths['Country,Other'].tolist()) 


# In[63]:


import country_converter as coco
some_names = ['USA', 'India', 'France', 'Germany', 'Brazil', 'Japan', 'S. Korea', 'Italy', 'United Kingdom', 'Russia', 'Turkey', 'Spain', 'Vietnam', 'Australia', 'Taiwan', 'Argentina', 'Netherlands', 'Iran', 'Mexico', 'Indonesia', 'Poland', 'Colombia', 'Austria', 'Greece', 'Portugal', 'Ukraine', 'Chile', 'Malaysia', 'Israel', 'Belgium', 'DPRK', 'Thailand', 'Czechia', 'Canada', 'Peru', 'Switzerland', 'Philippines', 'South Africa', 'Romania', 'Denmark', 'Hong Kong', 'Sweden', 'Serbia', 'Iraq', 'New Zealand', 'Singapore', 'Hungary', 'Bangladesh', 'Slovakia', 'Georgia', 'Jordan', 'Ireland', 'Pakistan', 'Norway', 'Finland', 'Kazakhstan', 'Slovenia', 'Lithuania', 'Bulgaria', 'Morocco', 'Croatia', 'Guatemala', 'Lebanon', 'Costa Rica', 'Bolivia', 'Tunisia', 'Cuba', 'Ecuador', 'ARE', 'Uruguay', 'Panama', 'Mongolia', 'Nepal', 'Belarus', 'Latvia', 'Saudi Arabia', 'Azerbaijan', 'Paraguay', 'Bahrain', 'Sri Lanka', 'Kuwait', 'Dominican Republic', 'Cyprus', 'Myanmar', 'Palestine', 'Moldova', 'Estonia', 'Venezuela', 'Egypt', 'Libya', 'Qatar', 'Ethiopia', 'Réunion', 'Honduras', 'Armenia', 'Bosnia and Herzegovina', 'Oman', 'North Macedonia', 'Zambia', 'Kenya', 'Albania', 'Botswana', 'Luxembourg', 'Montenegro', 'Brunei', 'Algeria', 'Nigeria', 'Zimbabwe', 'Uzbekistan', 'Mozambique', 'Martinique', 'Laos', 'Afghanistan', 'Iceland', 'Kyrgyzstan', 'Guadeloupe', 'El Salvador', 'Trinidad and Tobago', 'Maldives', 'Ghana', 'Namibia', 'Uganda', 'Jamaica', 'Cambodia', 'Rwanda', 'Cameroon', 'Malta', 'Barbados', 'Angola', 'Channel Islands', 'French Guiana', 'COD', 'Senegal', 'Malawi', 'Ivory Coast', 'Suriname', 'New Caledonia', 'French Polynesia', 'Eswatini', 'Guyana', 'Belize', 'Fiji', 'Madagascar', 'Sudan', 'Mauritania', 'Cabo Verde', 'Bhutan', 'Syria', 'Burundi', 'Seychelles', 'Gabon', 'Andorra', 'Papua New Guinea', 'Curaçao', 'Aruba', 'Tanzania', 'Mayotte', 'Mauritius', 'Togo', 'Guinea', 'Isle of Man', 'Bahamas', 'Lesotho', 'Faeroe Islands', 'Haiti', 'Mali', 'Cayman Islands', 'Saint Lucia', 'Benin', 'Somalia', 'Micronesia', 'Congo', 'Solomon Islands', 'San Marino', 'Timor-Leste', 'Burkina Faso', 'Liechtenstein', 'Gibraltar', 'Grenada', 'Bermuda', 'Nicaragua', 'South Sudan', 'Tajikistan', 'Equatorial Guinea', 'Tonga', 'Samoa', 'Monaco', 'Marshall Islands', 'Dominica', 'Djibouti', 'CAF', 'Gambia', 'Saint Martin', 'Vanuatu', 'Greenland', 'Yemen', 'Caribbean Netherlands', 'Sint Maarten', 'Eritrea', 'Niger', 'St. Vincent Grenadines', 'Guinea-Bissau', 'Antigua and Barbuda', 'Comoros', 'Liberia', 'Sierra Leone', 'Chad', 'British Virgin Islands', 'Cook Islands', 'Saint Kitts and Nevis', 'Turks and Caicos', 'Sao Tome and Principe', 'Palau', 'St. Barth', 'Nauru', 'Kiribati', 'Anguilla', 'Macao', 'Saint Pierre Miquelon', 'Wallis and Futuna', 'Tuvalu', 'Saint Helena', 'Falkland Islands', 'Montserrat', 'Niue', 'Diamond Princess', 'Vatican City', 'Western Sahara', 'MS Zaandam', 'Tokelau', 'China']
standard_names = coco.convert(names=some_names, to='ISO3')
print(standard_names)


# #### erase the 3 "not found" cases by hand

# In[64]:


isocode3 = ['USA', 'IND', 'FRA', 'DEU', 'BRA', 'JPN', 'KOR', 'ITA', 'GBR', 'RUS', 'TUR', 'ESP', 'VNM', 'AUS', 'TWN', 'ARG', 'NLD', 'IRN', 'MEX', 'IDN', 'POL', 'COL', 'AUT', 'GRC', 'PRT', 'UKR', 'CHL', 'MYS', 'ISR', 'BEL', 'PRK', 'THA', 'CZE', 'CAN', 'PER', 'CHE', 'PHL', 'ZAF', 'ROU', 'DNK', 'HKG', 'SWE', 'SRB', 'IRQ', 'NZL', 'SGP', 'HUN', 'BGD', 'SVK', 'GEO', 'JOR', 'IRL', 'PAK', 'NOR', 'FIN', 'KAZ', 'SVN', 'LTU', 'BGR', 'MAR', 'HRV', 'GTM', 'LBN', 'CRI', 'BOL', 'TUN', 'CUB', 'ECU', 'ARE', 'URY', 'PAN', 'MNG', 'NPL', 'BLR', 'LVA', 'SAU', 'AZE', 'PRY', 'BHR', 'LKA', 'KWT', 'DOM', 'CYP', 'MMR', 'PSE', 'MDA', 'EST', 'VEN', 'EGY', 'LBY', 'QAT', 'ETH', 'REU', 'HND', 'ARM', 'BIH', 'OMN', 'MKD', 'ZMB', 'KEN', 'ALB', 'BWA', 'LUX', 'MNE', 'BRN', 'DZA', 'NGA', 'ZWE', 'UZB', 'MOZ', 'MTQ', 'LAO', 'AFG', 'ISL', 'KGZ', 'GLP', 'SLV', 'TTO', 'MDV', 'GHA', 'NAM', 'UGA', 'JAM', 'KHM', 'RWA', 'CMR', 'MLT', 'BRB', 'AGO', 'GUF', 'COD', 'SEN', 'MWI', 'CIV', 'SUR', 'NCL', 'PYF', 'SWZ', 'GUY', 'BLZ', 'FJI', 'MDG', 'SDN', 'MRT', 'CPV', 'BTN', 'SYR', 'BDI', 'SYC', 'GAB', 'AND', 'PNG', 'CUW', 'ABW', 'TZA', 'MYT', 'MUS', 'TGO', 'GIN', 'IMN', 'BHS', 'LSO', 'FRO', 'HTI', 'MLI', 'CYM', 'LCA', 'BEN', 'SOM', 'FSM', 'COG', 'SLB', 'SMR', 'TLS', 'BFA', 'LIE', 'GIB', 'GRD', 'BMU', 'NIC', 'SSD', 'TJK', 'GNQ', 'TON', 'WSM', 'MCO', 'MHL', 'DMA', 'DJI', 'CAF', 'GMB', 'MAF', 'VUT', 'GRL', 'YEM', 'BES', 'SXM', 'ERI', 'NER', 'VCT', 'GNB', 'ATG', 'COM', 'LBR', 'SLE', 'TCD', 'VGB', 'COK', 'KNA', 'TCA', 'STP', 'PLW', 'BLM', 'NRU', 'KIR', 'AIA', 'MAC', 'SPM', 'WLF', 'TUV', 'SHN', 'FLK', 'MSR', 'NIU', 'VAT', 'ESH', 'TKL', 'CHN']


# In[65]:


isocode3


# In[66]:


dfisocode3 = pd.DataFrame(isocode3)


# In[67]:


dfisocode3


# In[68]:


dfisocode3.rename({0:'Country Code'}, axis = 'columns', inplace=True) 


# In[69]:


dfisocode3  


# In[70]:


covidcasesdeaths


# In[71]:


pd.set_option('display.max_rows', None)


# In[72]:


dfisocode3.join(covidcasesdeaths)


# In[73]:


#129 is wrong GGY - Channel Islands


# In[74]:


covidcasesdeaths[covidcasesdeaths['Country,Other'] != 'Channel Islands']


# In[75]:


covidcasesdeaths = covidcasesdeaths[covidcasesdeaths['Country,Other'] != 'Channel Islands']


# In[76]:


covidcasesdeaths.reset_index(inplace=True,drop=True)


# In[77]:


covidcasesdeaths


# In[78]:


dfisocode3.join(covidcasesdeaths)


# In[79]:


#224 wrong Diamond Princess


# In[80]:


covidcasesdeaths = covidcasesdeaths[covidcasesdeaths['Country,Other'] != 'Diamond Princess']


# In[81]:


covidcasesdeaths.reset_index(inplace=True,drop=True)


# In[82]:


covidcasesdeaths


# In[83]:


dfisocode3.join(covidcasesdeaths)


# In[84]:


#226 MS Zaandam wrong


# In[85]:


covidcasesdeaths = covidcasesdeaths[covidcasesdeaths['Country,Other'] != 'MS Zaandam']


# In[86]:


covidcasesdeaths.reset_index(inplace=True,drop=True)


# In[87]:


dfisocode3.join(covidcasesdeaths)


# In[88]:


covidcasesdeathsisocode = dfisocode3.join(covidcasesdeaths)


# In[89]:


covidcasesdeathsisocode


# ### 4.4 Merging the (Economic Indicators and Covid Vaccines) with Covid Cases/Deaths

# #### final merge covidcasesdeathsisocode with economicindicatorsvaccines

# In[90]:


covid = economicindicatorsvaccines.merge(covidcasesdeathsisocode, on = 'Country Code', indicator = '_merge1')


# In[91]:


covid


# In[92]:


covid.shape


# In[93]:


covid = covid.drop(['_merge1'], axis=1)


# In[94]:


covid


# In[95]:


covid.to_excel('covidApril5th2023.xlsx', index = False)


# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


covid = pd.read_excel('covidApril5th2023.xlsx')


# In[3]:


covid


# In[4]:


covid.shape


# In[5]:


pd.set_option('display.max_columns',None)


# In[6]:


covid.head(3)


# In[7]:


plt.plot(covid['Human Development Index 2021 (HDI)'])
plt.show()


# In[8]:


covid.describe()


# In[9]:


covid.isnull().sum()


# In[10]:


covid['TotalDeaths'].value_counts()


# In[11]:


covid.nunique()


# In[12]:


#There's the need to find lat and long for all countries to put it on the map 


# In[13]:


url = 'https://gist.githubusercontent.com/tadast/8827699/raw/f5cac3d42d16b78348610fc4ec301e9234f82821/countries_codes_and_coordinates.csv'
countrylatlong = pd.read_csv(url)
countrylatlong


# In[14]:


countrylatlong.drop(['Numeric code', 'Alpha-2 code'], axis = 1, inplace = True)


# In[15]:


countrylatlong


# In[16]:


countrylatlong.rename({'Alpha-3 code': 'Country Code', 'Latitude (average)':'Latitude', 'Longitude (average)':'Longitude'}, axis=1, inplace=True)


# In[17]:


countrylatlong


# In[18]:


countrylatlong['Country Code'] = countrylatlong['Country Code'].str.strip('" "')
countrylatlong['Latitude'] = countrylatlong['Latitude'].str.strip('" "')
countrylatlong['Longitude'] = countrylatlong['Longitude'].str.strip('" "')


# In[19]:


countrylatlong


# In[20]:


covid


# In[21]:


covidlatlong = countrylatlong.merge(covid, on= 'Country Code', how = 'inner', indicator = True)


# In[22]:


covidlatlong


# In[23]:


covidlatlong = covidlatlong.drop_duplicates(subset=['Country Code'])


# In[24]:


covidlatlong


# In[25]:


covidlatlong.reset_index(drop=True, inplace = True)


# In[26]:


covidlatlong


# In[27]:


covidlatlong = covidlatlong.drop(['Country_y','_merge'], axis = 1)


# In[28]:


covidlatlong


# In[29]:


covidlatlong.rename({'Country_x': 'Country'}, axis=1, inplace=True)


# In[30]:


covidlatlong


# In[31]:


covidlatlong.to_excel('covidlatlongApril5th2023.xlsx', index = False)


# ### 5.1 Mapping

# In[32]:


covidlatlong = pd.read_excel('covidlatlongApril5th2023.xlsx')


# In[33]:


covidlatlong.head(3)


# In[34]:


covidlatlong.shape


# In[35]:


covidlatlong.dtypes


# #### 5.1.1 Globe

# In[36]:


import geopandas as gpd
from mpl_toolkits.basemap import Basemap 
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[37]:


covidlatlong.shape


# In[38]:


sns.color_palette('Set1',149)


# In[39]:


country = list(covidlatlong['Country'].unique())
c = sns.color_palette('Set1',149)
label = country


# In[40]:


country


# In[41]:


c


# In[42]:


for i, j, k in zip(country,c,country):
    print(i,j,k)


# In[43]:


m3 = Basemap(projection='ortho', resolution=None, lat_0=50, lon_0=10,urcrnrlat=80,llcrnrlat=-80)

plt.figure(figsize=(8,8))

country = list(covidlatlong['Country'].unique())
c       = sns.color_palette('Set1',149)
#label   = country

def function(country,c,label):
    lat = list(covidlatlong[covidlatlong['Country'] == country].Latitude) 
    lon = list(covidlatlong[covidlatlong['Country'] == country].Longitude)
    x,y = m3(lon,lat)
    m3.plot(x,y,'go',markersize=15,color=c,alpha=.8,label=label)

for i,j in zip(country,c): # zip: aggregates elements based on the elements
    function(i,j,i)

m3.bluemarble(scale=0.5)
#plt.legend(loc='lower right',frameon=True,prop={'size':8}).get_frame().set_facecolor('white')
plt.title('Country Labels')
plt.show()


# In[44]:


list(covidlatlong[covidlatlong['Country']=='Brazil'].Latitude)


# In[45]:


list(covidlatlong['Country'].unique())


# In[46]:


country


# In[47]:


print(country)


# #### 5.1.2 World Map

# In[48]:


# Create a world map to show distributions of users 
import folium
from folium.plugins import MarkerCluster
#empty map
world_map= folium.Map(tiles='cartodbpositron')
marker_cluster = MarkerCluster().add_to(world_map)
#for each coordinate, create circlemarker of user percent
for i in range(len(covid)):
        lat = covidlatlong.iloc[i]['Latitude']
        long = covidlatlong.iloc[i]['Longitude']
        radius=5
        popup_text = """Country : {}<br>
                    Fully Vaccinated : {}<br>"""
        popup_text = popup_text.format(covidlatlong.iloc[i]['Country'],
                                   covidlatlong.iloc[i]['people_fully_vaccinated_per_hundred']
                                   )
        folium.CircleMarker(location = [lat, long], radius=radius, popup= popup_text, fill =True).add_to(marker_cluster)
#show the map
world_map


# In[49]:


covidlatlong.head(3)


# ### 5.2 Graphs

# In[50]:


covidvisual = covidlatlong.copy()


# In[51]:


covidvisual.shape


# In[52]:


covidvisual.head(3)


# In[53]:


covidvisual.dtypes


# In[54]:


covidvisual['TotalDeaths'] = covidvisual['TotalDeaths'].replace(',','', regex=True)


# In[55]:


covidvisual['Population']=covidvisual['Population'].replace(',','', regex=True)


# In[56]:


covidvisual.head(2)


# In[57]:


covidvisual['TotalDeaths'] = covidvisual['TotalDeaths'].astype(float)
covidvisual['Population'] = covidvisual['Population'].astype(float)


# In[58]:


covidvisual.dtypes


# In[59]:


covidvisual['covid_mortality_rate (per 100000)'] = (covidvisual['TotalDeaths']/covidvisual['Population']*100000)


# In[60]:


covidvisual.dtypes


# In[61]:


covidvisual.head(3)


# In[62]:


covidvisual['Country'].tolist()


# In[63]:


replacers = {'Bolivia, Plurinational State of':'Bolivia', 
             'Iran, Islamic Republic of':'Iran',
             'Korea, Republic of':'South Korea',
             "Lao People's Democratic Republic":'Laos',
             'Macedonia, the former Yugoslav Republic of':'Macedonia',
             'Moldova, Republic of':'Moldova',
             'Palestinian Territory, Occupied':'Palestinian territories',
             'Tanzania, United Republic of':'Tanzania'} 
covidvisual['Country']=covidvisual['Country'].replace(replacers)


# In[64]:


covidvisual['Country'].tolist()


# In[65]:


covidvisual.to_excel('covidvisualApril5th2023.xlsx', index = False)


# #### 5.2.1 Scatter Plots

# In[66]:


import plotly_express as px


# In[67]:


covidvisual = pd.read_excel('covidvisualApril5th2023.xlsx')


# In[68]:


covidvisual.head(3)


# In[69]:


covidvisual.shape


# In[70]:


fig = px.scatter(covidvisual, x = 'people_fully_vaccinated_per_hundred', y ='Country', title = 'People Fully Vaccinated (per 100) by Country', color = 'Country')
fig.update_layout(
    title={
        'text': 'People Fully Vaccinated (per 100) by Country',
        'y':0.85,
        'x':0.44,
        'xanchor': 'center',
        'yanchor': 'top'},
    xaxis_title='People Fully Vaccinated per Hundred')


# In[71]:


fig = px.scatter(covidvisual, x = 'GDP per capita 2021 (US$)', y = 'people_fully_vaccinated_per_hundred', marginal_x = 'box', marginal_y = 'violin', color = 'GDP per capita 2021 (US$)')
fig.update_layout(
    title={
        'text': 'People Fully Vaccinated (per 100) by GDP per capita 2021',
        'y':0.95,
        'x':0.34,
        'xanchor': 'center',
        'yanchor': 'top'},
    yaxis_title='People Fully Vaccinated per Hundred')


# In[72]:


fig = px.scatter(covidvisual, x = 'Human Development Index 2021 (HDI)', y = 'people_fully_vaccinated_per_hundred', marginal_x = 'box', marginal_y = 'violin', color = 'Country')
fig.update_layout(
    title={
        'text': 'People Fully Vaccinated (per 100) by Countries HDI',
        'y':0.95,
        'x':0.3,
        'xanchor': 'center',
        'yanchor': 'top'},
    yaxis_title='People Fully Vaccinated per Hundred')


# In[73]:


fig = px.scatter(covidvisual, x = 'GDP per capita 2021 (US$)', y = 'people_fully_vaccinated_per_hundred', marginal_x = 'box', marginal_y = 'violin', color = 'Country', trendline = 'ols')
fig.update_layout(
    title={
        'text': 'People Fully Vaccinated (per 100) by GDP per capita',
        'y':0.95,
        'x':0.3,
        'xanchor': 'center',
        'yanchor': 'top'},
    yaxis_title='People Fully Vaccinated per Hundred')


# #### 5.2.2 Bar Graphs

# In[74]:


fig = px.bar(covidvisual, x = 'Country', y = 'people_fully_vaccinated_per_hundred', color = 'Country')
fig.update_layout(
    title={
        'text': 'People Fully Vaccinated (per 100) by Country',
        'y':0.95,
        'x':0.4,
        'xanchor': 'center',
        'yanchor': 'top'},
    yaxis_title='People Fully Vaccinated per Hundred')


# In[75]:


fig = px.bar(covidvisual, x = 'people_fully_vaccinated_per_hundred', y = 'Country', color = 'Country', orientation='h')
fig.update_layout(
    title={
        'text': 'People Fully Vaccinated (per 100) by Country',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
 xaxis_title='People Fully Vaccinated per Hundred')


# In[76]:


fig = px.bar(covidvisual, x='people_fully_vaccinated_per_hundred', y='Country', color='Country', orientation='h',
             hover_data=['Human Development Index 2021 (HDI)', 'TotalDeaths'],
             height=400)
fig.update_layout(
    title={
        'text': 'People Fully Vaccinated (per 100) by Country with HDI and Total Deaths',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
 xaxis_title='People Fully Vaccinated per Hundred')


# In[77]:


fig = px.scatter(covidvisual, x='Country', y='people_fully_vaccinated_per_hundred', color='Continent')
fig.update_layout(
    title={
        'text': 'People Fully Vaccinated (per 100) by Country and Continent',
        'y':0.95,
        'x':0.45,
        'xanchor': 'center',
        'yanchor': 'top'},
 yaxis_title='People Fully Vaccinated per Hundred')


# #### 5.2.3 Pie Chart

# In[78]:


covidvisual1 = covidvisual.sort_values(by='TotalDeaths', ascending = False)


# In[79]:


covidvisual1.head()


# In[80]:


covidvisual1['TotalDeaths'][0:19]


# In[81]:


covidvisual1.loc[covidvisual1['TotalDeaths']< 100000, 'Country'] ='Other Countries Total Deaths'
fig = px.pie(covidvisual1, values='TotalDeaths', names='Country', title='Total Deaths by Country')
fig.update_layout(
    title={
        'text': 'Countries with Highest Deaths',
        'y':0.9,
        'x':0.45,
        'xanchor': 'center',
        'yanchor': 'top'})


# In[82]:


covidvisual1


# In[83]:


covidvisual2 = covidvisual.sort_values(by='covid_mortality_rate (per 100000)', ascending = False)


# In[84]:


covidvisual2


# In[85]:


covidvisual2.loc[covidvisual2['covid_mortality_rate (per 100000)']<180, 'Country'] = 'Other countries Death Rate'
fig = px.pie(covidvisual2, values='covid_mortality_rate (per 100000)', names='Country')
fig.update_layout(
    title={
        'text': 'Countries with Highest Mortality Rate',
        'y':0.98,
        'x':0.4,
        'xanchor': 'center',
        'yanchor': 'top'})


# In[86]:


fig = px.pie(covidvisual2, values='covid_mortality_rate (per 100000)', names='Country',
             hover_data=['Human Development Index 2021 (HDI)'], labels={'HDI':'Human Develpment Index'})
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(
    title={
        'text': 'Countries with Highest Covid Death Rate and HDI',
        'y':0.95,
        'x':0.37,
        'xanchor': 'center',
        'yanchor': 'top'})
fig.show()


# #### 5.2.4 Tree Map

# In[87]:


covidvisual.head()


# In[88]:


covidvisual.isnull().sum()


# In[89]:


covidvisual.shape


# In[90]:


fig = px.treemap(covidvisual, path=['Continent', 'Country'], values='people_fully_vaccinated_per_hundred',
                  color='covid_mortality_rate (per 100000)', hover_data=['Country Code'],
                labels={'covid_mortality_rate (per 100000)': 'COVID Mortality Rate (per 100,000)'})
fig.update_layout(
    title={
        'text': 'Treemap of People Fully Vaccinated (per 100) by Country',
        'y':0.95,
        'x':0.44,
        'xanchor': 'center',
        'yanchor': 'top'})


# #### 5.2.5 Trendline

# In[91]:


fig = px.scatter(covidvisual, x='covid_mortality_rate (per 100000)', y='people_fully_vaccinated_per_hundred', trendline='ols')
fig.update_layout(
    title={
        'text': 'People Fully Vaccinated (per 100) by Covid Death Rate OLS',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
 xaxis_title='Covid Mortality Rate (per 100,000)',
 yaxis_title='People Fully Vaccinated (per 100)')


# In[92]:


fig = px.scatter(covidvisual, x='Human Development Index 2021 (HDI)', y='people_fully_vaccinated_per_hundred', trendline='ols')
fig.update_layout(
    title={
        'text': 'People Fully Vaccinated (per 100) and HDI OLS',
        'y':0.95,
        'x':0.47,
        'xanchor': 'center',
        'yanchor': 'top'},
yaxis_title='People Fully Vaccinated (per 100)')


# In[93]:


fig = px.scatter(covidvisual, x='Human Development Index 2021 (HDI)', y='people_fully_vaccinated_per_hundred', trendline='ols', color = 'Country')
fig.update_layout(
    title={
        'text': 'People Fully Vaccinated (per 100) and HDI by Country',
        'y':0.95,
        'x':0.37,
        'xanchor': 'center',
        'yanchor': 'top'},
yaxis_title='People Fully Vaccinated (per 100)')


# In[94]:


px.scatter(covidvisual, x='Human Development Index 2021 (HDI)', y='people_fully_vaccinated_per_hundred', trendline='ols', color = 'Continent')
fig.update_layout(
    title={
        'text': 'People Fully Vaccinated (per 100) vs HDI by Continent Color',
        'y':0.95,
        'x':0.38,
        'xanchor': 'center',
        'yanchor': 'top'})


# In[95]:


fig = px.scatter(covidvisual, x='Inflation Rate 2021 (%)', y='people_fully_vaccinated_per_hundred', trendline='ols')
fig.update_layout(
    title={
        'text': 'People Fully Vaccinated (per 100) vs Inflation Rate (%)',
        'y':0.95,
        'x':0.47,
        'xanchor': 'center',
        'yanchor': 'top'},
yaxis_title='People Fully Vaccinated (per 100)')


# In[96]:


fig = px.scatter(covidvisual, x='Unemployment Rate 2021 (%)', y='covid_mortality_rate (per 100000)', trendline='ols')
fig.update_layout(
    title={
        'text': 'Covid Death Rate (per 100000) vs Unemployment Rate (%)',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
yaxis_title='Covid Mortality Rate (per 100,000)')


# In[97]:


covidvisual.columns


# In[98]:


sns.set(
    style="white", 
    palette="muted", 
    color_codes=True
)
sns.pairplot(
    covidvisual[[
        'Human Development Index 2021 (HDI)', 'GDP per capita 2021 (US$)',
       'Region', 'Inflation Rate 2021 (%)','Unemployment Rate 2021 (%)', 'total_vaccinations_per_hundred', 'people_fully_vaccinated_per_hundred',
       'TotalCases','TotalDeaths','Population','Continent', 'covid_mortality_rate (per 100000)'
    ]].dropna(), 
    hue='people_fully_vaccinated_per_hundred'
)


# ### 5.3 Maps with Shapefiles

# #### 5.3.1 From latitude and longitude finding a point to plot over the shapefile

# In[99]:


import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon


# In[100]:


covidvisual = pd.read_excel('covidvisualApril5th2023.xlsx')


# In[101]:


covidvisual


# In[102]:


covidvisual.shape


# In[103]:


covidvisual.head(3)


# In[104]:


covidvisual['Country'].tolist()


# In[105]:


#'naturalearth_lowres' is a shapefile dataset from geopandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world.head(3)


# In[106]:


fig, ax = plt.subplots(figsize = (15,15))
world.plot(ax=ax)


# In[107]:


crs = {'init':'epsg:4326'}
geometry = [Point(xy) for xy in zip(covidvisual['Longitude'], covidvisual['Latitude'])]
geometry[:5]


# In[108]:


geodataframe = gpd.GeoDataFrame(covidvisual, crs = crs, geometry = geometry)
geodataframe.head()


# In[109]:


#plot confirmed cases world map 
#plotting the points from latitude and longitude over a shapefile
fig, ax = plt.subplots(figsize = (15,15))
world.plot(ax=ax, alpha = 0.4, color = 'grey')
geodataframe.plot(ax = ax, column='TotalCases', scheme="quantiles",
           figsize=(25, 20),
           legend=True,cmap='coolwarm')
plt.title('Confirmed Case Amount in Different Countries',fontsize=15)
# add countries names and numbers 
for i in range(0,30):
    plt.text(float(geodataframe.Longitude[i]),float(geodataframe.Latitude[i]),"{}\n{}".format(geodataframe.Country[i],geodataframe.TotalCases[i]),size=8)
plt.show()


# ### 5.3.2 Merging the shapefile with the data, not plotting the point over it

# In[110]:


covidvisual = pd.read_excel('covidvisualApril5th2023.xlsx')


# In[111]:


covidvisual.shape


# In[112]:


covidvisual['Country'].tolist()


# In[113]:


covidvisual.head(3)


# In[114]:


world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))


# In[115]:


world.head()


# In[116]:


world.drop(['pop_est', 'continent', 'gdp_md_est'], axis = 1, inplace = True)


# In[117]:


world.rename({'iso_a3':'Country Code'}, axis = 1, inplace = True)


# In[118]:


world.head(3)


# In[119]:


worldmerge = world.merge(covidvisual, how = 'inner', on ='Country Code', indicator = True)


# In[120]:


worldmerge.head(3)


# In[121]:


worldmerge.plot(column='TotalCases', scheme="quantiles",
           figsize=(25, 20),
           legend=True,cmap='coolwarm')
plt.title('Confirmed Case Amount in Different Countries',fontsize=25)
for i in range(0,20):
    plt.text(float(worldmerge.Longitude[i]),float(worldmerge.Latitude[i]),"{}\n{}".format(worldmerge.name[i],worldmerge.TotalCases[i]),size=10)
plt.show()


# ### 5.4 More Maps, Bubble Chart and Boxplot with Plotly

# In[122]:


import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# In[123]:


covidvisual = pd.read_excel('covidvisualApril5th2023.xlsx')


# In[124]:


covidvisual.isna().sum()


# In[125]:


covidvisual.shape


# In[126]:


covidvisual.head(3)


# In[127]:


fig = px.scatter_geo(covidvisual, locations='Country Code', color='Continent',title = 'Total Deaths per Country',
               hover_name='Country', size='TotalDeaths')
fig.update_layout(
    title={
        'text':'Total Deaths per Country and Continent',
        'y':0.85,
        'x':0.47,
        'xanchor': 'center',
        'yanchor': 'top'})


# In[128]:


fig = px.scatter_geo(covidvisual,
                    lat=covidvisual.Latitude,
                    lon=covidvisual.Longitude,
                    hover_name='Country')
fig.update_layout(
    title={
        'text':'Countries Coordinates',
        'y':0.94,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})


# In[129]:


fig = px.choropleth(covidvisual, locations='Country Code',
                    color='covid_mortality_rate (per 100000)',
                    hover_name='Country',
                    color_continuous_scale=px.colors.sequential.Plasma,
                   labels={'covid_mortality_rate (per 100000)': 'COVID Mortality Rate (per 100,000)'})
fig.update_layout(
    title={
        'text':'Covid Death Rate by Country',
        'y':0.88,
        'x':0.44,
        'xanchor': 'center',
        'yanchor': 'top'})


# In[130]:


fig = go.Figure(data=go.Choropleth(
    locations = covidvisual['Country Code'],
    z = covidvisual['people_fully_vaccinated_per_hundred'],
    text = covidvisual['Country'],
    colorscale = 'Blues',
    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    #colorbar_tickprefix = '$',
    colorbar_title = '%',
    
))

fig.update_layout(
    title={'text':'People Fully Vaccinated by Country','y':0.89,'x':0.5,'xanchor': 'center','yanchor': 'top'},
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    annotations = [dict(
        x=0.5,
        y=0.1,
        xref='paper',
        yref='paper',
        text='World Map',
        
        showarrow = False
    )]
)

fig.show()


# In[131]:


fig = px.scatter(covidvisual, x='Human Development Index 2021 (HDI)', y='people_fully_vaccinated_per_hundred', size='TotalDeaths', color='Continent',
           hover_name='Country', log_x=True, size_max=60)
fig.update_layout(
    title={
        'text':'Fully Vaccinated People (per 100) vs HDI by Continent and Total Deaths',
        'y':0.95,
        'x':0.44,
        'xanchor': 'center',
        'yanchor': 'top'},
    yaxis_title='People Fully Vaccinated (per 100)')


# In[132]:


fig = px.box(covidvisual, y='covid_mortality_rate (per 100000)', color = 'IncomeGroup', title = 'Covid Death Rate by Income Group',
labels={'IncomeGroup': 'Income Group'})
fig.update_layout(
    title={
        'text': 'Covid Death Rate per Continent',
        'y':0.88,
        'x':0.44,
        'xanchor': 'center',
        'yanchor': 'top'},
    yaxis_title='Covid Mortality Rate (per 100,000)',
xaxis_title='Income Group')


# In[133]:


fig = px.box(covidvisual, y='covid_mortality_rate (per 100000)', color = 'Continent')
fig.update_layout(
    title={
        'text': 'Covid Death Rate per Continent',
        'y':0.95,
        'x':0.44,
        'xanchor': 'center',
        'yanchor': 'top'}, font_family='Arial',font_color='blue', title_font_family='Times New Roman',title_font_color='black',
    legend_title_font_color='green',  font=dict(family='Courier New, monospace',size=15,color='RebeccaPurple'
    ),
    yaxis_title='Covid Mortality Rate (per 100,000)',
xaxis_title='Continent')


# In[ ]:





# In[1]:


import pandas as pd


# In[2]:


covidvisual = pd.read_excel('covidvisualApril5th2023.xlsx')


# In[3]:


covidvisual


# In[4]:


covidvisual.shape


# In[5]:


covidvisual.columns


# In[6]:


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# In[7]:


covidvisual


# In[8]:


import plotly.express as px


# In[9]:


fig = px.scatter(covidvisual, x='Human Development Index 2021 (HDI)', y='people_fully_vaccinated_per_hundred', color='Continent', trendline='ols')
fig.update_layout(
    title={
        'text': 'People Fully Vaccinanted (per 100) vs HDI by Continent OLS ',
        'y':0.95,
        'x':0.44,
        'xanchor': 'center',
        'yanchor': 'top'},
yaxis_title='People Fully Vaccinanted (per 100)')
fig.show()

results = px.get_trendline_results(fig)
print(results)

results.px_fit_results.iloc[0].summary()


# In[10]:


fig = px.scatter(covidvisual, x='Human Development Index 2021 (HDI)', y='people_fully_vaccinated_per_hundred', trendline='ols', hover_name='Country')
fig.update_layout(
    title={
        'text': 'People Fully Vaccinated (per 100) vs HDI OLS',
        'y':0.94,
        'x':0.47,
        'xanchor': 'center',
        'yanchor': 'top'},
yaxis_title='People Fully Vaccinanted (per 100)')
fig.show()

results = px.get_trendline_results(fig)
print(results)

results.px_fit_results.iloc[0].summary()


# In[11]:


fig = px.scatter(covidvisual, x='Human Development Index 2021 (HDI)', y='covid_mortality_rate (per 100000)', trendline='ols', hover_name='Country')
fig.update_layout(
    title={
        'text': 'Covid Death Rate (per 100000) vs HDI OLS',
        'y':0.94,
        'x':0.48,
        'xanchor': 'center',
        'yanchor': 'top'},
yaxis_title='Covid Mortality Rate (per 100,000)')
fig.show()

results = px.get_trendline_results(fig)
print(results)

results.px_fit_results.iloc[0].summary()


# In[12]:


fig = px.scatter(covidvisual, x='people_fully_vaccinated_per_hundred', y='covid_mortality_rate (per 100000)', trendline='ols', hover_name='Country')
fig.update_layout(
    title={
        'text': 'Covid Death Rate vs People Fully Vaccinated (per 100) OLS',
        'y':0.95,
        'x':0.48,
        'xanchor': 'center',
        'yanchor': 'top'},
yaxis_title='Covid Mortality Rate (per 100,000)')
fig.show()

results = px.get_trendline_results(fig)
print(results)

results.px_fit_results.iloc[0].summary()


# In[13]:


import numpy as np 
import matplotlib.pyplot as plt
import itertools
import seaborn as sns


# In[14]:


cols  = ['covid_mortality_rate (per 100000)','people_fully_vaccinated_per_hundred','Human Development Index 2021 (HDI)','daily_vaccinations_per_million']
length = len(cols)
c = ['b','r','k','c']
plt.figure(figsize=(13,10))

for i,j,k in itertools.zip_longest(cols,range(length),c):
    plt.subplot(2,2,j+1)
    sns.distplot(covidvisual[i],color=k)
    plt.axvline(covidvisual[i].mean(),color = 'k',linestyle = 'dashed',label='mean')
    plt.legend(loc='best')
    plt.title(i)
    plt.xlabel('')

plt.show()


# In[15]:


plt.figure(figsize=(13,6))
sns.heatmap(covidvisual[['people_fully_vaccinated_per_hundred', 'Human Development Index 2021 (HDI)','Inflation Rate 2021 (%)','Unemployment Rate 2021 (%)']].describe()[1:].transpose(),annot=True,fmt='f',linecolor='white',linewidths=2) # fmt: String formatting code to use when adding annotations
plt.title('Covid-19 Rates by Country')
plt.show()


# In[16]:


corr = covidvisual.corr()
ax = sns.heatmap(
    corr, 
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
);
plt.title('Correlation Heatmap')


# In[17]:


fig = px.imshow(covidvisual.corr())
fig.update_layout(
    title={
        'text': 'Correlation Heatmap',
        'y':0.92,
        'x':0.48,
        'xanchor': 'center',
        'yanchor': 'top'})
fig.show()


# In[18]:


import string
letters = string.ascii_uppercase[0:15]
covidvisual.corr()


# In[19]:


corr = covidvisual.corr()


# In[20]:


corr.style.background_gradient(cmap='coolwarm')


# In[21]:


corr.style.background_gradient(cmap='coolwarm').set_precision(2) 


# In[22]:


corr = covidvisual.corr() 
c1 = corr.unstack()
c1.sort_values(ascending = False)


# In[23]:


corr = covidvisual.corr() 
c1 = corr.abs().unstack()
c1.sort_values(ascending = False)


# In[24]:


corr = covidvisual.corr()
kot = corr[corr>=.9]
plt.figure(figsize=(12,8))
sns.heatmap(kot, cmap='Reds')
plt.title('Variables with Correlation > .9');


# In[25]:


dfCorr = covidvisual.corr()
filteredDf = dfCorr[((dfCorr >= .5) | (dfCorr <= -.5)) & (dfCorr !=1.000)]
plt.figure(figsize=(25,10))
sns.heatmap(filteredDf, annot=True, cmap='coolwarm')
plt.title('Variables with Correlation > .5 or <.-5 and not equal to 1',
          size=20, verticalalignment='bottom')
plt.show()


# In[ ]:





# # 7. Econometrics

# In[1]:


import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.sandbox.regression.predstd import wls_prediction_std
from statsmodels.api import add_constant, OLS
from statsmodels.iolib.summary2 import summary_col
from numpy import NaN
from sklearn import linear_model
from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from linearmodels.iv import IV2SLS


# In[2]:


covidvisual = pd.read_excel('covidvisualApril5th2023.xlsx')


# In[3]:


covidvisual


# In[4]:


covidvisual.shape


# In[5]:


dfCorr = covidvisual.corr()
filteredDf = dfCorr[((dfCorr >= .5) | (dfCorr <= -.5)) & (dfCorr !=1.000)]
plt.figure(figsize=(25,10))
plt.title('Variables with Correlation > .5 or <.-5 and not equal to 1',
          size=20, verticalalignment='bottom')
sns.heatmap(filteredDf, annot=True, cmap='Greens')
plt.show()


# In[6]:


pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', None)


# In[7]:


covidvisual.head(3)


# In[8]:


covidvisual.sort_values(by=['covid_mortality_rate (per 100000)'], ascending = False).head(3)


# In[9]:


plt.style.use('seaborn')
covidvisual.plot(x='Human Development Index 2021 (HDI)', y='covid_mortality_rate (per 100000)', kind='scatter')
plt.ylabel('Covid Mortality Rate (per 100,000)')
plt.show()


# In[10]:


#correlating the hdi with covid_mortality_rate, as control population, latitude can be used, income group (or gpd per capita);
#for an instrument, a variable that correlates with hdi but not directly to covid mortality rate, gdp per capita for example


# ## 7.1 Linear Regression

# $$ 
# Coviddeathrate_{i} = \beta_{0} + \beta_{1}HDI_{i} + u_{i}
# $$

# In[11]:


# Dropping NA's is required to use numpy's polyfit
df1_subset = covidvisual.dropna(subset=['covid_mortality_rate (per 100000)', 'Human Development Index 2021 (HDI)'])

# Use only 'base sample' for plotting purposes
#df1_subset = df1_subset[df1_subset['baseco'] == 1]

X = df1_subset['Human Development Index 2021 (HDI)']
y = df1_subset['covid_mortality_rate (per 100000)']
labels = df1_subset['Country Code']

# Replace markers with country labels
fig, ax = plt.subplots()
ax.scatter(X, y, marker='')

for i, label in enumerate(labels):
    ax.annotate(label, (X.iloc[i], y.iloc[i]))

# Fit a linear trend line
ax.plot(np.unique(X),
         np.poly1d(np.polyfit(X, y, 1))(np.unique(X)),
         color='black')

#ax.set_xlim([0,1])
#ax.set_ylim([0,300])
ax.set_xlabel('HDI')
ax.set_ylabel('Covid Death Rate')
ax.set_title('Figure 2: OLS relationship between HDI and Covid Death Rate')
plt.show()


# In[12]:


#it might seem counterintuitive at first, as HDI increases Covid Death Rate increases
#it could be because of countries with higher HDI has higher mobility, or something else, let's find out


# In[13]:


#adding a constant term prevents overall bias by forcing the residual mean to equal zero
#it's like moving the regression line up or down to the point where the residual mean equals zero
#that's why a constant term is usually added into a linear regression
#bias exists if the residuals have an overall positive or negative mean, the model makes predicitons that are too high or too low
#the constant term prevents overall bias by forcing the residual mean to equal zero


# In[14]:


covidvisual['const'] = 1


# In[15]:


covidvisual.head(3)


# In[16]:


#building the model
reg1 = sm.OLS(endog=covidvisual['covid_mortality_rate (per 100000)'], exog=covidvisual[['const', 'Human Development Index 2021 (HDI)']],     missing='drop')
type(reg1)


# ##### obtainning the parameter estimates 
# $$ 
# Coviddeathrate_{i} = \hat\beta_{0} + \hat\beta_{1}HDI_{i} + u_{i}
# $$

# In[17]:


results = reg1.fit()
type(results)


# In[18]:


print(results.summary())


# The intercept $ \hat\beta_{0} = -238.60 $ \
# The slope $ \hat\beta_{1} = 513.93 $ \
# The positive $ \hat\beta_{1} $ parameter estimate implies that HDI has a positive effect on covid death rate, that is the higher HDI, higher covid death rate \
# The p-value of 0.000 for $ \hat\beta_{1} $ implies that the effect of HDI on covid death rate is statistically significant
# (using p<0.05 as a rejection rule). \
# The R-squared value of 0.294 indicates that around 29% of variation in covid death rate is explained by HDI

# In[19]:


#using the parameter estimates


# $$
# \widehat{Coviddeathrate_{i}} = -238.60 + 513.93HDI_{i}
# $$

# In[20]:


#the equation above describes the line that best fits the data shown in Figure 2
#the equation can be used to predict the level of covid death rate for a value of HDI


# In[21]:


mean_hdi = np.mean(df1_subset['Human Development Index 2021 (HDI)'])
mean_hdi


# In[22]:


predicted_coviddeathrate = -238.60 + 513.93 * 0.74
predicted_coviddeathrate


# In[23]:


#for a country with HDI value of 0.74 (the average for the dataset), the predicted level of covid death rate is 141.70


# In[24]:


#there's another way to do it, it's easier and more accurate, using predict(), setting constant = 1 and hdii = mean_hdi


# In[25]:


results.predict(exog=[1, mean_hdi])


# In[26]:


#plotting the predicted values hdi and observed values covid death rate


# In[27]:


# Drop missing observations from whole sample

df1_plot = covidvisual.dropna(subset=['covid_mortality_rate (per 100000)', 'Human Development Index 2021 (HDI)'])

# Plot predicted values

fix, ax = plt.subplots()
ax.scatter(df1_plot['Human Development Index 2021 (HDI)'], results.predict(), alpha=0.5,
        label='predicted')

# Plot observed values

ax.scatter(df1_plot['Human Development Index 2021 (HDI)'], df1_plot['covid_mortality_rate (per 100000)'], alpha=0.5,
        label='observed')

ax.legend()
ax.set_title('OLS predicted values')
ax.set_xlabel('HDI')
ax.set_ylabel('Covid Death Rate')
plt.show()


# ## 7.2 Multivariate Regression Model

# In[28]:


#that are many factors that influence covid death rate, and leaving out variables that affect it, will result in omitted variable bias
#yielding biased and inconsistent parameter estimates
#adding other factors will extend the linear regression model into multivariate regression model


# In[29]:


#Factos such as:
#the effect on climate on covid death rate, latitude is used as a proxy
#(Latitude)
#population, in general it's harder to control countries with higher population, and the higher population more people can trasmit the virus
#(Population)
#people fully vaccinated per hundred, people who received all doses are less likely to die from the virus
#(people_fully_vaccinated_per_hundred)
#incomegroup, lower income groups are more likely to die from the virus cause the lack of resources, worse sanitation such as sewage treatment, 
#less access to treated water, and the lower income group are also more likely to share rooms with the same household, increasing the chance of transmitting the virus
#(IncomeGroup)-> since income group is categorical it won't be used in the regression


# In[30]:


covidvisual.head()


# In[31]:


#lists of variables to be used in each regression
X1 = ['const', 'Human Development Index 2021 (HDI)']
X2 = ['const', 'Human Development Index 2021 (HDI)', 'Latitude']
X3 = ['const', 'Human Development Index 2021 (HDI)', 'Latitude','Population']
X4 = ['const', 'Human Development Index 2021 (HDI)', 'Latitude','Population','people_fully_vaccinated_per_hundred']
#X5 = ['const', 'Human Development Index 2019 (HDI)', 'Latitude','Population','people_fully_vaccinated_per_hundred','IncomeGroup']
#estimating an OLS regression for each set of variables
reg1 = sm.OLS(covidvisual['covid_mortality_rate (per 100000)'], covidvisual[X1], missing='drop').fit()
reg2 = sm.OLS(covidvisual['covid_mortality_rate (per 100000)'], covidvisual[X2], missing='drop').fit()
reg3 = sm.OLS(covidvisual['covid_mortality_rate (per 100000)'], covidvisual[X3], missing='drop').fit()
reg4 = sm.OLS(covidvisual['covid_mortality_rate (per 100000)'], covidvisual[X4], missing='drop').fit()
#reg5 = sm.OLS(covidvisual['covid_mortality_rate (per 100000)'], covidvisual[X5], missing='drop').fit()


# In[32]:


info_dict={'R-squared' : lambda x: f"{x.rsquared:.2f}",
           'No. observations' : lambda x: f"{int(x.nobs):d}"}

results_table = summary_col(results=[reg1,reg2,reg3, reg4],
                            float_format='%0.2f',
                            stars = True,
                            model_names=['Model 1',
                                         'Model 2',
                                         'Model 3',
                                         'Model 4'],
                            info_dict=info_dict,
                            regressor_order=['const',
                                             'Human Development Index 2021 (HDI)',
                                             'Latitude',
                                             'Population',
                                             'people_fully_vaccinated_per_hundred'])

results_table.add_title('Table 2 - OLS Regressions')

print(results_table)


# In[33]:


#population and people fully vaccinated did not show significant 
#as for HDI, it showed statistically significant throghout all models  for p<.01, meaning that higher HDI impacts into higher covid death rate
#Latitude was not significant 
#latitude ranges from -90 to 90, at the equator is 0, above is positve until 90 and below is negative until 90


# ## 7.3 Endogeneity

# In[34]:


#OLS models are likely to suffer from endogeneity issues, resulting in biased and inconsistent model estimates
#there's likely a two-way relationship between HDI and covid death rate

#higher covid death rate can be because of higher mobility, richer people can afford to travel more, in and out of the country
#variables that affect covid death rate may also be correlated with HDI

#to deal with endogeneity, two-stage least squares (2SLS) regression, an extension of OLS regression, can be used


# ### 7.3.1 Two-stage least squares (2SLS) regression

# In[35]:


#this method requires replacing the endogenous variable HDIi, with a variable that is:
#1. correlated with HDIi
#2. not correlated with the error term (ie. it should not directly affect the dependent variable (in this case covid death rate),
#otherwise it would be correlated with ui due to omitted variable bias)

#the new set of regressor is called an intrument, which aims to remove endogeneity in our HDI variable


# In[36]:


# an option for an instrument could be inflation rate or unemployment rate, each one is correlated with HDI,
#because countries that have lower unemployment rate tend to have a higher HDI
#and also countries that have lower inflation rate tend to have a higher HDI
#both, inflation rate nor unemployment rate is correlated dirrectly to covid death rate
#let's find out which one would be a better instrument


# In[37]:


covidvisual.head(3)


# In[38]:


plt.style.use('seaborn')
covidvisual.plot(x='Inflation Rate 2021 (%)', y='covid_mortality_rate (per 100000)', kind='scatter')
plt.ylabel('Covid Mortality Rate (per 100,000)')
plt.show()


# In[39]:


plt.style.use('seaborn')
covidvisual.plot(x='Unemployment Rate 2021 (%)', y='covid_mortality_rate (per 100000)', kind='scatter')
plt.ylabel('Covid Mortality Rate (per 100,000)')
plt.show()


# In[40]:


#both inflation rate nor unemployment rate shows correlation with covid death rate, which is a good sign for the instrument
#it has to be correlated with the independent variable HDI and not with the dependent variable covid death rate


# In[41]:


px.scatter(covidvisual, x='Inflation Rate 2021 (%)', y='Human Development Index 2021 (HDI)', trendline='ols')


# In[42]:


fig = px.scatter(covidvisual, x='Inflation Rate 2021 (%)', y='Human Development Index 2021 (HDI)', trendline='ols')
fig.show('svg')


# In[43]:


px.scatter(covidvisual, x='Unemployment Rate 2021 (%)', y='Human Development Index 2021 (HDI)', trendline='ols')


# In[44]:


fig = px.scatter(covidvisual, x='Unemployment Rate 2021 (%)', y='Human Development Index 2021 (HDI)', trendline='ols')
fig.show('svg')


# In[45]:


#inflation rate will be used as instrument because it shows a correlation (negative) with HDI
#a country with a higher inflation rate tends to present a lower HDI, 
#meanwhile inflation rate is not directly correlated with covid death rate


# In[46]:


# Dropping NA's is required to use numpy's polyfit
df1_subset2 = covidvisual.dropna(subset=['Inflation Rate 2021 (%)', 'Human Development Index 2021 (HDI)'])

X = df1_subset2['Inflation Rate 2021 (%)']
y = df1_subset2['Human Development Index 2021 (HDI)']
labels = df1_subset2['Country Code']

# Replace markers with country labels
fig, ax = plt.subplots()
ax.scatter(X, y, marker='')

for i, label in enumerate(labels):
    ax.annotate(label, (X.iloc[i], y.iloc[i]))

# Fit a linear trend line
ax.plot(np.unique(X),
         np.poly1d(np.polyfit(X, y, 1))(np.unique(X)),
         color='black')

#ax.set_xlim([1.8,8.4])
#ax.set_ylim([3.3,10.4])
ax.set_xlabel('Inflation Rate 2021 (%)')
ax.set_ylabel('HDI')
ax.set_title('Figure 3: First-stage relationship between inflation rate     and HDI')
plt.show()


# #### 7.3.1.1 First Stage

# In[47]:


#the first stage involves regressing the endogenous variable (HDIi) on the instrument
#the instrument is the set of all exonegous variables in the model (not just the variable replaced)
#on model 1, the instrument is a constant and inflation rate
#thus, the first-stage regression estimated is


# $$ 
# HDI_{i} = \delta_{0} + \delta_{1}inflationrate_{i} +v_{i}
# $$

# In[48]:


covidvisual.head(3)


# In[49]:


# Fit the first stage regression and print summary
results_fs = sm.OLS(covidvisual['Human Development Index 2021 (HDI)'],
                    covidvisual[['const', 'Inflation Rate 2021 (%)']],
                    missing='drop').fit()
print(results_fs.summary())


# #### 7.3.1.2 Second Stage

# There's the need to retrieve the predicted values of HDIi using .predict()
# then replace the endogenous variable HDIi with the predicted values $ \widehat{HDI_i} $ in the original linear model
# the second stage regression is the following:

# $$ 
# Coviddeathrate_{i} = \beta_{0} + \beta_{1}\widehat{HDI_i} + u_{i}
# $$

# In[50]:


covidvisual['predicted_HDI'] = results_fs.predict()

results_ss = sm.OLS(covidvisual['covid_mortality_rate (per 100000)'],
                    covidvisual[['const', 'predicted_HDI']], missing = 'drop').fit()
print(results_ss.summary())


# In[51]:


#the second stage results in a p-value that is not statistically significant
#indicating the second-stage regression results does not give an unbiased and conssitent estimate of the effect of 
#HDI on covid death rate, the inflation rate is not a good instrument, and HDI is not endogenous according to the 
#Hausman Test used after the IV2SLS 


# In[52]:


covidvisual.head(3)


# In[53]:


iv = IV2SLS(dependent=covidvisual['covid_mortality_rate (per 100000)'],
            exog=covidvisual['const'],
            endog=covidvisual['Human Development Index 2021 (HDI)'],
            instruments=covidvisual['Inflation Rate 2021 (%)']).fit(cov_type='unadjusted')

print(iv.summary)


# In[54]:


#the p value is not significant meaning the estimates are not consistent nor unbiased, but if it were interpreting the results
#there's the marginal effect of 484.88 to calculate the difference in the hdi index implies difference in covid death rate


# #### 7.3.2 Hausman Test

# In[55]:


#besides identifying endogeneity by thinking about the data and model, there's a test for endogeneity, it's called Hausman test
#to test the correlation between the endogenous variable, HDIi, and the errors, ui


# $$
# H_{0}: Cov({HDI_i},u_{i}) = 0 \ (no \ endogeneity) \\
# H_{1}: Cov({HDI_i},u_{i}) \neq 0 \ (endogeneity)
# $$

# In[56]:


#the test is run in two stages
#first regressing the independent variable (HDIi) on the instrument (inflationratei)


# $$ 
# HDI_{i} = \pi_{0} + \pi_{1}inflationrate_{i} +v_{i}
# $$

# second retrieving the residuals $ \hat{v_{i}} $ and including them in the original equation

# $$ 
# Coviddeathrate_{i} = \beta_{0} + \beta_{1}{HDI_i} + \alpha\hat{v_i} + u_{i}
# $$

# If $\alpha$ is statistically significant (with a p-value < 0.05), then we reject the null hypothesis and conclude that $HDI_{i}$ is endogenous.
# Estimating the Hausman Test and interpreting the results

# In[57]:


# Estimate the first stage regression
reg1 = sm.OLS(endog=covidvisual['Human Development Index 2021 (HDI)'],
              exog=covidvisual[['const', 'Inflation Rate 2021 (%)']],
              missing='drop').fit()

# Retrieve the residuals
covidvisual['resid'] = reg1.resid

# Estimate the second stage residuals
reg2 = sm.OLS(endog=covidvisual['covid_mortality_rate (per 100000)'],
              exog=covidvisual[['const', 'Human Development Index 2021 (HDI)', 'resid']],
              missing='drop').fit()

print(reg2.summary())


# In[58]:


#the output shows that the coefficient on the residuals is not statistically significant, 
#indicating HDIi is not endogenous

#if the coefficient on the residuals were statistically significant, HDIi would be endogenous


# ### 7.4 The OLS parameter 𝛽 estimated using matrix algebra and numpy

# In[59]:


#the linear equation to estimate written in matrix form is 


# y = X$\beta$ + u

# In[60]:


#to solve the unknown parameter B, we want to minimize the sum of squared residuals


# ${\displaystyle\min_\hat{\beta}} \ \hat{u}' \ \hat{u}$

# In[61]:


#isolating u on the first equation and substituting into the second equation


# ${\displaystyle\min_\hat{\beta}} \ (Y - X \hat{\beta})'(Y - X \hat{\beta})$

# optimizing the problem gives the solution for the  $\hat{\beta}$ coefficients

# $\hat{\beta} = (X'X)^{-1}X'y$

# computing $\hat{\beta}$ from the model using numpy, the results should be the same as using statsmodels

# In[62]:


df1 = covidvisual.dropna(subset=['covid_mortality_rate (per 100000)', 'Human Development Index 2021 (HDI)'])
# Define the X and y variables
y = np.asarray(df1['covid_mortality_rate (per 100000)'])
X = np.asarray(df1[['const', 'Human Development Index 2021 (HDI)']])

# Compute β_hat
β_hat = np.linalg.solve(X.T @ X, X.T @ y)

# Print out the results from the 2 x 1 vector β_hat
print(f'β_0 = {β_hat[0]:.2}')
print(f'β_1 = {β_hat[1]:.2}')


# In[63]:


#exactly the same results


# In[64]:


reg1 = sm.OLS(endog=covidvisual['covid_mortality_rate (per 100000)'], exog=covidvisual[['const', 'Human Development Index 2021 (HDI)']],     missing='drop')
type(reg1)

results = reg1.fit()
type(results)

print(results.summary())


# The intercept $ \hat\beta_{0} = -238.60 $ \
# The slope $ \hat\beta_{1} = 513.93 $ 

# ### 7.5 Regression Discontinuity Design (RDD)

# In[65]:


covidvisual = pd.read_excel('covidvisualApril5th2023.xlsx')


# In[66]:


covidvisual


# In[67]:


covidvisual.shape


# In[68]:


covidvisual.sort_values(by = 'people_fully_vaccinated_per_hundred', ascending = False)


# In[69]:


covidvisual['people_fully_vaccinated_per_hundred'].mean()


# In[70]:


covidvisual['people_fully_vaccinated_per_hundred'].median()


# In[71]:


covidvisual['people_fully_vaccinated_per_hundred'].isna().sum()


# In[72]:


covidvisual['IncomeGroup'].value_counts()


# In[73]:


covidvisual['people_fully_vaccinated_per_hundred'].mean()


# In[74]:


covidvisual.groupby(['IncomeGroup'])['people_fully_vaccinated_per_hundred'].mean()


# In[75]:


covidvisual.groupby(['IncomeGroup'])['people_fully_vaccinated_per_hundred'].median()


# In[76]:


covidvisual[covidvisual['IncomeGroup']=='High income']


# In[77]:


len(covidvisual[covidvisual['IncomeGroup']=='High income'])


# In[78]:


#in order to use RDD let's get the cut off to be around the median of 74 for High Income Group 
#since there's a higher number of observations the high income group, this group will be used cause it has similar characteristics


# In[79]:


covidhighincomerdd = covidvisual[covidvisual['IncomeGroup']=='High income']


# In[80]:


covidhighincomerdd.head(3)


# In[81]:


covidhighincomerdd.shape


# In[82]:


covidhighincomerdd = covidhighincomerdd.sort_values(by ='people_fully_vaccinated_per_hundred', ascending = False)


# In[83]:


covidhighincomerdd = covidhighincomerdd.dropna(subset=['people_fully_vaccinated_per_hundred'])


# In[84]:


covidhighincomerdd.shape


# In[85]:


covidhighincomerdd['people_fully_vaccinated_per_hundred'].median()


# In[86]:


len(covidhighincomerdd[covidhighincomerdd['people_fully_vaccinated_per_hundred'] < 74.75])


# In[87]:


len(covidhighincomerdd[covidhighincomerdd['people_fully_vaccinated_per_hundred'] > 74.75])


# In[88]:


#to ilustrate a RDD application the cuttoff will be 74.75 (median) for people fully vaccinated per hundred
#it would be interesting to use the date in which countries started applying the vaccine, but this information in the data 
#is not available, the vaccine application ordered by the government would be an exogenous fact


# In[89]:


covidhighincomerdd


# In[90]:


plt.figure(figsize=(8,8))
ax = plt.subplot(3,1,1)
covidhighincomerdd.plot.scatter(x='people_fully_vaccinated_per_hundred', y='covid_mortality_rate (per 100000)', ax=ax)
plt.xlabel('People Fully Vaccinated per 100')
plt.ylabel('Covid Mortality Rate (per 100,000)')

plt.title('Covid Death Rate vs People Fully Vaccinated');


# In[91]:


covidhighincomerdd.rename({'covid_mortality_rate (per 100000)':'coviddeathrate'}, axis = 'columns', inplace = True)


# In[92]:


rdd_df = covidhighincomerdd.assign(threshold=(covidhighincomerdd['people_fully_vaccinated_per_hundred'] > 74.75).astype(int))

model = smf.wls('coviddeathrate~people_fully_vaccinated_per_hundred*threshold', rdd_df).fit()

model.summary().tables[1]


# In[93]:


#covid death rate increases by 47.22(threshold) points with more people fully vaccinated
#people fully vaccinated increases the chance of death by 47%
#the p-value is not below 0.01, so it's not statistically significant
#and the right interpretation that would make total sense would be 47% decrease in death rate by people fully vaccinated per hundred above the threshold (74.75)


# In[94]:


ax = covidhighincomerdd.plot.scatter(x='people_fully_vaccinated_per_hundred', y='coviddeathrate', color='C0')
covidhighincomerdd.assign(predictions=model.fittedvalues).plot(x='people_fully_vaccinated_per_hundred', y='predictions', ax=ax, color='C1')
plt.xlabel('People Fully Vaccinated per 100')
plt.ylabel('Covid Mortality Rate (per 100,000)')
plt.title('Regression Discontinuity');


# In[95]:


#a slight discontinuity around the threshold is observed


# In[96]:


#another way of doing it would be 


# In[97]:


# Create binned peoplefullyvaccinated values
covidhighincomerdd['peoplefullyvaccinated_bin'] = pd.qcut(covidhighincomerdd['people_fully_vaccinated_per_hundred'],10)
covidhighincomerdd['peoplefullyvaccinated_bin'].value_counts()

covidhighincomerdd['over74'] = 0
covidhighincomerdd.loc[covidhighincomerdd['people_fully_vaccinated_per_hundred']>=74.75,'over74'] = 1 
covidhighincomerdd['over74'].value_counts()

# Plot
plt.figure(num=None, figsize=(6, 4), dpi=80, facecolor='w', edgecolor='k')

sns.set(style='whitegrid')
a = sns.boxplot(x='peoplefullyvaccinated_bin', y='coviddeathrate',
              color='b',  data=covidhighincomerdd)
plt.xlabel('People Fully Vaccinated per 100 Bin')
plt.ylabel('Covid Mortality Rate (per 100,000)')
a.set_xticklabels(a.get_xticklabels(), rotation=45, horizontalalignment='right');


# In[98]:


re = smf.ols(formula = 'coviddeathrate ~ over74', data = covidhighincomerdd).fit()
print(re.summary())


# In[99]:


#the p-value is actually significant, meaning the RDD is a good choice is this case


# In[100]:


plt.figure(num=None, figsize=(6, 4), dpi=80, facecolor='w', edgecolor='k')
plt.scatter(covidhighincomerdd['people_fully_vaccinated_per_hundred'],covidhighincomerdd['coviddeathrate'], color='blue')
l=covidhighincomerdd.loc[covidhighincomerdd['over74']==0,'over74'].count()
plt.plot(covidhighincomerdd['people_fully_vaccinated_per_hundred'][0:(l-1)], re.predict()[0:(l-1)], '-', color='r')
plt.plot(covidhighincomerdd['people_fully_vaccinated_per_hundred'][l:], re.predict()[l:], '-', color='r')
plt.title('Regression Discontinuity: Before and After the Cutoff', fontsize='14')


# In[101]:


#a discontinuity is shown and it's statistically significant
#since it is significant, now it makes sense to say 
#there is a 47% decrease in death rate by people fully vaccinated per hundred 
#above the threshold of 74.75 fully vaccinated people per 100 individuals


# ## 7.6 Difference-in-Difference

# The idea behind DiD is the following: 
# The difference in the mean of the outcome between the two groups, treatment group and control group, in the "before" period (A) 
# The difference in the mean of the outcome between the two groups, treatment group and control group, in the "after" period (B)
# The "second difference", the difference between (A) and (B), which would be (C)
# It measures how the change in outcome differs between the two groups, the average effect of treatment on the treated (ATT)
# This difference is attributed to the causal effect of the intervention, difference-in-differences (DiD)
# 
# So, 
# 1. The difference in the mean of the outcome between the treatment group and control group
# before the intervention (A)
# 2. The difference in the mean of the outcome between the treatment group and control group
# after the intervention (B)
# 3. The difference between (A) and (B), which is the "second difference", DiD estimate
# 
# To do this there are some assumptions that need to be met when designing the treatment and control groups, they are:
# 
# 1. Parallel trends: the treatment and control groups have parallel trends in the outcome. 
# Meaning that in the absence of the intervention, the difference between the treatment and control group is constant over time. 
# To see this, a good way is to plot and visually inspect if the parallel trends hold.
# 2. No spillover effects.
# 3. The characteristics of the treatment and control groups are stable over the study period.

# In[102]:


covidvisual = pd.read_excel('covidvisualApril5th2023.xlsx')


# In[103]:


covidvisual.shape


# In[104]:


covidvisual.head(3)


# to ilustrate a DiD, the best idea would be to have two different periods in time, for example when the vaccines started being 
# applied. The period would be before the vaccines were applied and after, the treatment group the countries that received 
# the vaccines and the control group the countries that did not receive vaccines. For a good counterfactual countries within 
# the same income group could be chosen as treatment group (the ones that received that vaccines) and the control group 
# the ones that did not receive the vaccines, in this case differences-in-differences-in-differences could be used, since 
# the income groups would be interacted, or just differences-in-dinfferences with a dummy variable for income
# but this is not the case, the data does not have two periods, so to apply the method I'll use 
# the median date, how it is affecting the covid death rate

# In[105]:


#there's the need to create the dummies and interaction


# In[106]:


covidvisual.sort_values('date', ascending = False)


# In[107]:


covidvisual['date'].max()


# In[108]:


covidvisual['date'].min()


# In[109]:


covidvisual['date'].astype('datetime64[ns]').quantile(0.5, interpolation='midpoint')


# In[110]:


covidvisual.dtypes


# In[111]:


#covidvisual['date'] = pd.to_datetime(covidvisual['date']) it's better not to convert to timestamp


# In[112]:


covidvisual['date'].describe()


# In[113]:


#covidvisual['date'].median() #this works when converted to timestamp 
#the median Timestamp('2023-03-17 00:00:00') will change when the code is run again with the data updated


# In[114]:


covidvisual['people_fully_vaccinated_per_hundred'].describe()


# In[115]:


covidvisual['date']


# In[116]:


len(covidvisual[covidvisual['date'] < '2023-03-17'])


# In[117]:


len(covidvisual[covidvisual['date'] > '2023-03-17'])


# In[118]:


len(covidvisual[covidvisual['date'] == '2023-03-17'])


# In[119]:


len(covidvisual[covidvisual['IncomeGroup']=='Low income'])


# I'll choose two periods, before 2023-03-17 and after, for treatment and control 
# in the low income group the treatment for the countries who received the vaccines (16 countries), and as control 
# the countries who did not receive the vaccines

# In[120]:


covidvisual['IncomeGroup']


# In[121]:


(covidvisual[covidvisual['IncomeGroup']=='Low income']).isna().sum()


# In[122]:


covidlowincome = covidvisual[covidvisual['IncomeGroup']=='Low income']


# In[123]:


covidlowincome.head(3)


# In[124]:


covidlowincome['people_fully_vaccinated_per_hundred'].fillna(0).apply(np.ceil).astype(int)


# In[125]:


covidlowincome['people_fully_vaccinated_per_hundred']=covidlowincome['people_fully_vaccinated_per_hundred'].fillna(0).apply(np.ceil).astype(int)


# In[126]:


covidlowincome['people_fully_vaccinated_per_hundred']


# In[127]:


covidlowincome.head(3)


# In[128]:


covidlowincome['Continent'].unique()


# In[129]:


covidvisualdummies = pd.get_dummies(covidlowincome, columns=['IncomeGroup', 'Continent']) #drop_first = True)


# In[130]:


covidvisualdummies.shape


# In[131]:


covidvisualdummies.head(3)


# In[132]:


covidvisualdummies.sort_values('date', ascending = False)


# In[133]:


covidvisualdummies.dtypes


# In[134]:


covidvisualdummies['date'] = covidvisualdummies['date'].str.replace('-','')


# In[135]:


covidvisualdummies


# In[136]:


covidvisualdummies.sort_values(by = 'date', ascending = False, inplace = True)


# In[137]:


covidvisualdummies


# In[138]:


len(covidvisualdummies['date'])//2


# In[139]:


covidvisualdummies['date'].iloc[8]


# In[140]:


covidvisualdummies['date'] = covidvisualdummies['date'].astype(int)


# In[141]:


covidvisualdummies[covidvisualdummies['date'] < 20230319] 


# In[142]:


covidvisualdummies.loc[covidvisualdummies['date'] < 20230319, 'date'] = 0
covidvisualdummies.loc[covidvisualdummies['date'] >= 20230319, 'date'] = 1 


# In[143]:


covidvisualdummies


# In[144]:


#now there's a need for an interaction term


# In[145]:


covidvisualdummies['people_fully_vaccinated_per_hundred']


# In[146]:


covidvisualdummies['date']


# In[147]:


covidvisualdummies['date*people_fully_vaccinated_per_hundred']=covidvisualdummies['date']*covidvisualdummies['people_fully_vaccinated_per_hundred']


# In[148]:


covidvisualdummies.head(3)


# In[149]:


covidvisualdummies.rename({'covid_mortality_rate (per 100000)':'coviddeathrate', 'IncomeGroup_Low income':'lowincomegroup'}, axis = 'columns', inplace = True)


# In[150]:


#covidvisualdummies.rename({'Continent_North America':'continent_northamerica'}, axis = 'columns', inplace = True)


# In[151]:


model = smf.ols(formula = 'coviddeathrate ~ date*people_fully_vaccinated_per_hundred + Continent_Africa                 + lowincomegroup', data = covidvisualdummies).fit()
print(model.summary())


# The 'date:people_fully_vaccinated_per_hundred' is not statistically significant, meaning that vaccines after the date meantioned has no impact on coviddeathrate, as compared with the date before.

# In[152]:


# People Fully Vaccinated in the low income group Before and after the middle date
peoplefullyvaccinated_before = covidvisualdummies.loc[(covidvisualdummies['people_fully_vaccinated_per_hundred']==1) & (covidvisualdummies['date']!=1),'coviddeathrate'].mean()
peoplefullyvaccinated_after  = covidvisualdummies.loc[(covidvisualdummies['people_fully_vaccinated_per_hundred']==1) & (covidvisualdummies['date']==1),'coviddeathrate'].mean()

# People Not Fully Vaccinated in the low income group Before and after the middle date
peoplenotfullyvaccinated_before = covidvisualdummies.loc[(covidvisualdummies['people_fully_vaccinated_per_hundred']!=1) & (covidvisualdummies['date']!=1),'coviddeathrate'].mean()
peoplenotfullyvaccinated_after  = covidvisualdummies.loc[(covidvisualdummies['people_fully_vaccinated_per_hundred']!=1) & (covidvisualdummies['date']==1),'coviddeathrate'].mean()

# People Fully Vaccinated in the low income group Before and after the middle date counterfactual (if no treatment)
peoplefullyvaccinated_counterfactual = peoplefullyvaccinated_before + ( peoplefullyvaccinated_before - peoplenotfullyvaccinated_before )

[peoplefullyvaccinated_before, peoplefullyvaccinated_after,
 peoplenotfullyvaccinated_before,peoplenotfullyvaccinated_after,peoplefullyvaccinated_before,peoplefullyvaccinated_counterfactual]

#it'll present the covid death rate of peoplefullyvaccinated (before and after), peoplenotfullyvaccinated(before and after) and peoplefullyvaccinated counterfactual


# In[153]:


plt.figure(num=None, figsize=(4, 3), dpi=80, facecolor='w', edgecolor='k')
fig, ax = plt.subplots()
linepeoplefullyvaccinated, = ax.plot(['0', '1'], [peoplefullyvaccinated_before, peoplefullyvaccinated_after],color='blue',label='peoplefullyvaccinated before and after')
linepeoplenotfullyvaccinated, = ax.plot(['0', '1'], [peoplenotfullyvaccinated_before, peoplenotfullyvaccinated_after],color = 'red',label = 'peoplenotfullyvaccinated before and after')
linepeoplefullyvaccinated0, = ax.plot(['0', '1'], [peoplefullyvaccinated_before, peoplefullyvaccinated_counterfactual],color = 'blue',linestyle='dashed',label='peoplefullyvaccinated counterfactual')
ax.legend()
plt.ylim(0, 15)  
plt.title("Difference-in-difference: Before and After", fontsize="14");


# In[154]:


#the blue line and dotted lines are not showned because of the dates chosen, it had some NaN values when making the counterfactural
#with other dates it will show


# ### 7.7 More OLS

# In[155]:


covidvisual = pd.read_excel('covidvisualApril5th2023.xlsx')


# In[156]:


covidvisual


# In[157]:


covidvisual.shape


# In[158]:


covidvisual.head(3)


# In[159]:


covidvisual.columns


# In[160]:


X = covidvisual[['people_fully_vaccinated_per_hundred', 'Human Development Index 2021 (HDI)', 'Unemployment Rate 2021 (%)', 'Inflation Rate 2021 (%)', 'GDP per capita 2021 (US$)', 'GDP 2021 (US$)', 'HDI rank']]
y = covidvisual['covid_mortality_rate (per 100000)']
X = sm.add_constant(X)


# In[161]:


model = sm.OLS(y, X, missing='drop')
results = model.fit()
predictions = results.predict(X)
results.summary()


# In[162]:


covidvisual.isnull().sum()


# In[163]:


fig = plt.figure(figsize=(15,8))
plt.plot(range(0,len(y)), y.tolist(), 'b')
plt.plot(range(0,len(y)), predictions.tolist(), 'r--')
plt.show()


# In[164]:


covidvisual = pd.read_excel('covidvisualApril5th2023.xlsx')


# In[165]:


covidvisual.head(2)


# In[166]:


covidvisuallm = covidvisual.loc[:, ['people_fully_vaccinated_per_hundred','covid_mortality_rate (per 100000)']]


# In[167]:


covidvisuallm


# In[168]:


covidvisuallm = covidvisuallm.dropna(subset=['people_fully_vaccinated_per_hundred','covid_mortality_rate (per 100000)'])


# In[169]:


covidvisuallm


# In[170]:


X = covidvisuallm['people_fully_vaccinated_per_hundred']
y = covidvisuallm['covid_mortality_rate (per 100000)']


# In[171]:


lm = linear_model.LinearRegression()
model = lm.fit(X.values.reshape(-1,1),y)


# In[172]:


lm.coef_


# In[173]:


lm.intercept_


# In[174]:


lm.score(X.values.reshape(-1,1),y)


# In[175]:


predictions = lm.predict(X.values.reshape(-1,1))
print(predictions[0:5])


# #### 7.7.1 Robust Linear Regression

# In[176]:


X = covidvisuallm['people_fully_vaccinated_per_hundred']
y = covidvisuallm['covid_mortality_rate (per 100000)']


# In[177]:


model = sm.RLM(y, X, missing='drop', M=sm.robust.norms.HuberT())
results = model.fit()
results.summary()


# In[178]:


X = covidvisuallm['people_fully_vaccinated_per_hundred']
y = covidvisuallm['covid_mortality_rate (per 100000)']
X = sm.add_constant(X)


# In[179]:


res = sm.OLS(y, X).fit()
print(res.params)


# In[180]:


resrlm = sm.RLM(y, X).fit()
print(resrlm.params)


# ### 7.8 Logit Regression

# y must be 0 or 1

# In[181]:


covidvisual = pd.read_excel('covidvisualApril5th2023.xlsx')


# In[182]:


covidvisual


# In[183]:


covidvisual['IncomeGroup']


# In[184]:


#y = covidvisual['IncomeGroup']
covidvisualdum = covidvisual.drop('IncomeGroup',1)


# In[185]:


covidvisualdum.head(2)


# In[186]:


dummie_incomegroup = pd.get_dummies(covidvisual['IncomeGroup'],prefix='dum')


# In[187]:


dummie_incomegroup.head(3)


# In[188]:


coviddummies = pd.concat([covidvisualdum, dummie_incomegroup], axis = 1)


# In[189]:


coviddummies.head(3)


# In[190]:


coviddummies1 = coviddummies.loc[:, ['people_fully_vaccinated_per_hundred','covid_mortality_rate (per 100000)','dum_High income']]


# In[191]:


coviddummies1.head(3)


# In[192]:


coviddummies1 = coviddummies1.dropna()
#coviddummies1= covidvisuallm.dropna(subset=['people_fully_vaccinated_per_hundred','covid_mortality_rate (per 100000)','dum_High income'])


# In[193]:


coviddummies1.head(3)


# In[194]:


coviddummies1.shape


# In[195]:


Y = coviddummies1['dum_High income']


# In[196]:


Y.head(3)


# In[197]:


X = coviddummies1[['covid_mortality_rate (per 100000)', 'people_fully_vaccinated_per_hundred']]


# In[198]:


X.head(3)


# In[199]:


X = sm.add_constant(X)


# In[200]:


X.head(3)


# In[201]:


logit_mod = sm.Logit(Y,X)


# In[202]:


logit_res = logit_mod.fit()
logit_res.summary()


# In[203]:


logit_res.summary2()


# In[204]:


logit_res.get_margeff(at='overall', method='dydx').summary()


# ### 7.9 Quantile Regression

# In[205]:


covidvisual = pd.read_excel('covidvisualApril5th2023.xlsx')


# In[206]:


covidvisual.head(3)


# In[207]:


covidvisual.rename({'covid_mortality_rate (per 100000)':'coviddeathrateper100k'}, axis='columns', inplace = True)


# In[208]:


covidvisual.rename({'Human Development Index 2021 (HDI)':'hdi'}, axis='columns', inplace = True)


# In[209]:


covidvisual


# In[210]:


mod = smf.quantreg('coviddeathrateper100k ~ hdi', covidvisual)
res = mod.fit(q=.5)
res.summary()


# In[211]:


quantiles = np.arange(.05, .96, .1)
def fit_model(q):
    res = mod.fit(q=q)
    return [q, res.params['Intercept'], res.params['hdi']] +             res.conf_int().loc['hdi'].tolist()

models = [fit_model(x) for x in quantiles]
models = pd.DataFrame(models, columns=['q', 'a', 'b', 'lb', 'ub'])

ols = smf.ols('coviddeathrateper100k ~ hdi', covidvisual).fit()
ols_ci = ols.conf_int().loc['hdi'].tolist()
ols = dict(a = ols.params['Intercept'],
           b = ols.params['hdi'],
           lb = ols_ci[0],
           ub = ols_ci[1])

print(models)
print(ols)


# In[212]:


x = np.arange(covidvisual.hdi.min(), covidvisual.hdi.max(), 50)
get_y = lambda a, b: a + b * x

fig, ax = plt.subplots(figsize=(8, 6))

for i in range(models.shape[0]):
    y = get_y(models.a[i], models.b[i])
    ax.plot(x, y, linestyle='dotted', color='grey')

y = get_y(ols['a'], ols['b'])

ax.plot(x, y, color='red', label='OLS')
ax.scatter(covidvisual.hdi, covidvisual.coviddeathrateper100k, alpha=.3)
ax.set_xlim((0.5, 1))
ax.set_ylim((0, 250))
legend = ax.legend()
ax.set_xlabel('hdi', fontsize=16)
ax.set_ylabel('coviddeathrateper100k', fontsize=16);


# In[213]:


n = models.shape[0]
p1 = plt.plot(models.q, models.b, color='black', label='Quantile Reg.')
p2 = plt.plot(models.q, models.ub, linestyle='dotted', color='black')
p3 = plt.plot(models.q, models.lb, linestyle='dotted', color='black')
p4 = plt.plot(models.q, [ols['b']] * n, color='red', label='OLS')
p5 = plt.plot(models.q, [ols['lb']] * n, linestyle='dotted', color='red')
p6 = plt.plot(models.q, [ols['ub']] * n, linestyle='dotted', color='red')
plt.ylabel(r'Covid Death Rate (per 100000)')
plt.xlabel('Quantiles of the conditional HDI distribution')
plt.legend()
plt.show()


# The graph displays estimated coefficients as a function of quantile using a black line, with the OLS estimate of the coefficients shown by the horizontal line. For most of the estimated coefficients in the quantiles, the upper and lower bounds (at a 95% confidence interval) do not fall within the OLS estimate. 
# This suggests a notable difference between the OLS estimates and the quantile regression estimates. As a result, it is logical to analyze the Covid death rate by quantiles of the conditional HDI distribution rather than just relying on a regular OLS estimate.

# # 8. Spatial Econometrics

# In[1]:


import esda
import pandas as pd
import geopandas as gpd
from geopandas import GeoDataFrame
import libpysal as lps
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


covidvisual = pd.read_excel('covidvisualApril5th2023.xlsx')


# In[3]:


covidvisual.head(3)


# In[4]:


covidvisual.shape


# In[5]:


covidvisual.columns


# In[6]:


import shapely
shapely.speedups.disable()


# In[7]:


world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))


# In[8]:


world


# In[9]:


world.drop(['pop_est', 'continent', 'gdp_md_est'], axis = 1, inplace = True)


# In[10]:


world.head(3)


# In[11]:


covidvisual.head(3)


# In[12]:


world.rename({'iso_a3':'Country Code'}, axis = 1, inplace = True)


# In[13]:


worldmerge = world.merge(covidvisual, how = 'inner', on ='Country Code', indicator = True) 
#in order to preserve the map and to avoid empty spaces on the map, the merge is how='left'


# In[14]:


worldmerge.head(3)


# In[15]:


worldmerge.drop('_merge', axis = 1, inplace = True)


# In[16]:


worldmerge


# In[17]:


worldmerge.plot(column='covid_mortality_rate (per 100000)')


# In[18]:


fig, ax = plt.subplots(figsize=(14,10), subplot_kw={'aspect':'equal'})
worldmerge.plot(column='covid_mortality_rate (per 100000)', scheme='Quantiles', k=5, cmap='GnBu', legend=True, ax=ax);
leg = ax.get_legend()
leg.set_bbox_to_anchor((0., 0., 1.15, 1.0))
#ax.set_xlim(150000, 160000)
#ax.set_ylim(208000, 215000)


# ### 8.1 Spatial Autocorrelation

# Sometimes, we observe visually-clustered patterns, 
# but often there are no discernible statistical patterns, 
# thus requiring testing. 
# Spatial autocorrelation pertains to the combination of two types of similarity - spatial and attribute similarity.

# #### 8.1.1 Spatial Similarity

# In[19]:


#queen contiguity for spatial weights is defined
#w = Queen.from_dataframe(df, idVariable='name')
#knn1 = lps.weights.KNN.from_dataframe(df)
#queen = lps.weights.Queen.from_dataframe(df)

#symm_knn = lps.weights.WSP((knn1.sparse + knn1.sparse.T)>0).to_W()

#fully_connected = lps.weights.w_union(symm_knn, queen)


# In[20]:


worldmerge


# In[21]:


df = worldmerge
wq =  lps.weights.Queen.from_dataframe(df, idVariable = 'Country Code')
wq.transform = 'r'


# In[22]:


df = worldmerge
wq =  lps.weights.Queen.from_dataframe(df)
wq.transform = 'r'


# In[23]:


worldmerge


# In[24]:


worldmerge.drop(worldmerge.index[[0, 13, 32, 56, 58, 65, 70, 104, 105, 106, 107, 112, 115, 122, 125, 135]], axis = 0, inplace = True)


# In[25]:


worldmerge.reset_index(drop=True, inplace = True)


# In[26]:


df = worldmerge
wq =  lps.weights.Queen.from_dataframe(df, idVariable = 'Country Code')
wq.transform = 'r'


# #### 8.1.2 Attribute Similarity

# The spatial weight between neighborhoods i and j indicates if the two are neighbors. 
# The spatial lag is a derived variable that is a measure of attribute of similarity that pairs up with the concept of spatial similarity.
# The spatial lag for neighborhood i is as showed in the equation below.

# $$ 
# ylag_{i} = \sum_{j}w_{i,j}y_{j}
# $$

# In[27]:


#so, the spatial lag = average of the neighbors 


# In[28]:


y = df['covid_mortality_rate (per 100000)']
ylag = lps.weights.lag_spatial(wq, y)


# In[29]:


ylag


# In[30]:


import mapclassify as mc
ylagq5 = mc.Quantiles(ylag, k=5)


# In[31]:


f, ax = plt.subplots(1, figsize=(9, 9))
df.assign(cl=ylagq5.yb).plot(column='cl', categorical=True,         k=5, cmap='GnBu', linewidth=0.1, ax=ax,         edgecolor='white', legend=True)
ax.set_axis_off()
leg = ax.get_legend()
leg.set_bbox_to_anchor((0., 0., 1.1, 1.0))
plt.title('Spatial Lag Covid Mortality Rate (100000) (Quintiles)')

plt.show()


# In[32]:


#the quintile map for the spatial lag makes us think there's similarity in space


# In[33]:


df['lag_coviddeathrate'] = ylag
f,ax = plt.subplots(1,2,figsize=(4.16*4,4))
df.plot(column='covid_mortality_rate (per 100000)', ax=ax[0], edgecolor='k',
        scheme='quantiles',  k=5, cmap='GnBu')
ax[0].axis(df.total_bounds[np.asarray([0,2,1,3])])
ax[0].set_title('Covid Mortality Rate')
df.plot(column='lag_coviddeathrate', ax=ax[1], edgecolor='k',
        scheme='quantiles', cmap='GnBu', k=5)
ax[1].axis(df.total_bounds[np.asarray([0,2,1,3])])
ax[1].set_title('Spatial Lag Covid Mortality Rate')
ax[0].axis('off')
ax[1].axis('off')
plt.show()


# In[34]:


#on the left are the values of covid mortality rate and neighbors
#on the right are weighted average of covid death rates' neighbors, which is the spatial lag


# ### 8.2 Global Spatial Autocorrelation

# In[35]:


#converting the attribute to a binary case to see it easily 


# In[36]:


y.median()


# In[37]:


yb = y > y.median()
sum(yb)


# In[38]:


sum(y < y.median())


# In[39]:


#there are 60 neighborhoods with covid death rate above the median and 60 (120-60=60) below the median


# In[40]:


y


# In[41]:


yb = y > y.median()
labels = ['0 Low', '1 High']
yb = [labels[i] for i in 1*yb] 
df['yb'] = yb


# In[42]:


fig, ax = plt.subplots(figsize=(12,10), subplot_kw={'aspect':'equal'})
df.plot(column='yb', cmap='binary', edgecolor='grey', legend=True, ax=ax)


# #### 8.2.1 Join Counts

# In[43]:


# a join is a way to formalize a test for spatial autocorrelation in a binary attribute, it also exists for each 
#neighbor pair of observations, and the joins are reflected in the binary spatial weights object wq
#each unit can take either Black (B) or White (W), there are three type of joins, BB (black black), WW (white white), BW (black white or white black)
#finding out what is the number of BB joins if the 65 black polygons were randomly assingned on the map


# In[44]:


import esda 
yb = 1 * (y > y.median()) # convert back to binary
wq =  lps.weights.Queen.from_dataframe(df)
wq.transform = 'b'
np.random.seed(12345)
jc = esda.join_counts.Join_Counts(yb, wq)


# In[45]:


jc.bb


# In[46]:


jc.ww


# In[47]:


jc.bw


# In[48]:


jc.bb + jc.ww + jc.bw #all possibilites


# In[49]:


wq.s0 / 2 #unique number of joins in the spatial weights object


# In[50]:


jc.bb #there are 92 BB joins


# In[51]:


jc.mean_bb #The average number of BB joins from the synthetic realizations is


# In[52]:


#less than the observed count, but is it enought to reject the null of complete spatial randomness(CSR)


# In[53]:


jc.p_sim_bb #the pseudo p-value summarizes that the observed value is extremely high, it'a bellow 1%, rejecting null of CSR, 
#meaning there's autocorrelation in covid death rate


# #### 8.2.2 Continous Case

# In[54]:


#transforming the weights to be row-standardized from the current binary state


# In[55]:


wq.transform = 'r'


# In[56]:


y = df['covid_mortality_rate (per 100000)']


# In[57]:


#Moran's I is a test for global autocorrelation for a continuous attribute


# In[58]:


np.random.seed(12345)
mi = esda.moran.Moran(y, wq)
mi.I


# In[59]:


import seaborn as sbn
sbn.kdeplot(mi.sim, shade=True)
plt.vlines(mi.I, 0, 1, color='r')
plt.vlines(mi.EI, 0,1)
plt.xlabel('Moran\'s I')


# In[60]:


mi.p_sim


# ### 8.3 Local Autocorrelation: Hot Spots, Cold Spots, and Spatial Outliers

# In[61]:


#local Moran statistic


# In[62]:


np.random.seed(12345)
import esda


# In[63]:


wq.transform = 'r'
lag_coviddeathrate = lps.weights.lag_spatial(wq, df['covid_mortality_rate (per 100000)'])


# In[64]:


df.rename({'covid_mortality_rate (per 100000)':'coviddeathrate'}, axis = 1, inplace = True)


# In[65]:


df.head(3)


# In[66]:


#df = df[df.coviddeathrate != 0]
#df = df[df.lag_coviddeathrate !=0]
df = df.dropna(axis=0, subset=['coviddeathrate','lag_coviddeathrate'])


# In[67]:


df['coviddeathrate'].values.reshape(-1,1) #when plotting the graph below there was an error expected x and y to have same length
#that's why the need to reshape, but this would be 2d, it has to be 1d, many errors where found when doing the plotting below
#what worked was reshaping x and y to 1d with values.reshape(-1)


# In[68]:


df['coviddeathrate'].values.reshape(-1)


# In[69]:


df


# In[70]:


coviddeathrate = df['coviddeathrate'].values.reshape(-1)
lag_coviddeathrate = df['lag_coviddeathrate'].values.reshape(-1)
b, a = np.polyfit(coviddeathrate, lag_coviddeathrate, 1)
f, ax = plt.subplots(1, figsize=(9, 9))

plt.plot(coviddeathrate, lag_coviddeathrate, '.', color='firebrick')

 # dashed vert at mean of the price
plt.vlines(coviddeathrate.mean(), lag_coviddeathrate.min(), lag_coviddeathrate.max(), linestyle='--')
 # dashed horizontal at mean of lagged price 
plt.hlines(lag_coviddeathrate.mean(), coviddeathrate.min(), coviddeathrate.max(), linestyle='--')

# red line of best fit using global I as slope
plt.plot(coviddeathrate, a + b*coviddeathrate, 'r')
plt.title('Moran Scatterplot')
plt.ylabel('Spatial Lag of Covid Mortality Rate')
plt.xlabel('Covid Mortality Rate')
plt.show()


# In[71]:


#instead of a single I statistic, there's an array of local Ii statistics, stored in the .Is attribute, and p-value from the simulation are in p_sim


# In[72]:


#there might be spatial autocorrelation according to the graph,
#the positive slope means that neighbors of locations with large values have high values, and neighbors of locations
#with small values have small values


# In[73]:


li = esda.moran.Moran_Local(y, wq)


# In[74]:


li.q


# In[75]:


#using conditional random permutations (different distributions for each focal location)


# In[76]:


(li.p_sim < 0.05).sum()


# In[77]:


#distinguishing the specific type of local spatial association reflected in the four quadrants of the Moran Scatterplot above:


# In[78]:


sig = li.p_sim < 0.05
hotspot = sig * li.q==1
coldspot = sig * li.q==3
doughnut = sig * li.q==2
diamond = sig * li.q==4


# In[79]:


spots = ['n.sig.', 'hot spot']
labels = [spots[i] for i in hotspot*1]


# In[80]:


df = df
from matplotlib import colors
hmap = colors.ListedColormap(['red', 'lightgrey'])
f, ax = plt.subplots(1, figsize=(9, 9))
df.assign(cl=labels).plot(column='cl', categorical=True,         k=2, cmap=hmap, linewidth=0.1, ax=ax,         edgecolor='white', legend=True)
ax.set_axis_off()
leg = ax.get_legend()
leg.set_bbox_to_anchor((0., 0., 1.1, .8))
plt.show()


# In[81]:


spots = ['n.sig.', 'cold spot']
labels = [spots[i] for i in coldspot*1]


# In[82]:


df = df
from matplotlib import colors
hmap = colors.ListedColormap(['blue', 'lightgrey'])
f, ax = plt.subplots(1, figsize=(9, 9))
df.assign(cl=labels).plot(column='cl', categorical=True,         k=2, cmap=hmap, linewidth=0.1, ax=ax,         edgecolor='white', legend=True)
ax.set_axis_off()
leg = ax.get_legend()
leg.set_bbox_to_anchor((0., 0., 1.1, .8))
plt.show()


# In[83]:


spots = ['n.sig.', 'doughnut']
labels = [spots[i] for i in doughnut*1]


# In[84]:


df = df
from matplotlib import colors
hmap = colors.ListedColormap(['lightblue', 'lightgrey'])
f, ax = plt.subplots(1, figsize=(9, 9))
df.assign(cl=labels).plot(column='cl', categorical=True,         k=2, cmap=hmap, linewidth=0.1, ax=ax,         edgecolor='white', legend=True)
ax.set_axis_off()
leg = ax.get_legend()
leg.set_bbox_to_anchor((0., 0., 1.1, .8))
plt.show()


# In[85]:


spots = ['n.sig.', 'diamond']
labels = [spots[i] for i in diamond*1]


# In[86]:


df = df
from matplotlib import colors
hmap = colors.ListedColormap(['pink', 'lightgrey'])
f, ax = plt.subplots(1, figsize=(9, 9))
df.assign(cl=labels).plot(column='cl', categorical=True,         k=2, cmap=hmap, linewidth=0.1, ax=ax,         edgecolor='white', legend=True)
ax.set_axis_off()
leg = ax.get_legend()
leg.set_bbox_to_anchor((0., 0., 1.1, .8))
plt.show()


# In[87]:


sig = 1 * (li.p_sim < 0.05)
hotspot = 1 * (sig * li.q==1)
coldspot = 3 * (sig * li.q==3)
doughnut = 2 * (sig * li.q==2)
diamond = 4 * (sig * li.q==4)
spots = hotspot + coldspot + doughnut + diamond
spots


# In[88]:


spot_labels = [ '0 ns', '1 hot spot', '2 doughnut', '3 cold spot', '4 diamond']
labels = [spot_labels[i] for i in spots]


# In[89]:


from matplotlib import colors
hmap = colors.ListedColormap([ 'lightgrey', 'red', 'lightblue', 'blue', 'pink'])
f, ax = plt.subplots(1, figsize=(9, 9))
df.assign(cl=labels).plot(column='cl', categorical=True,         k=2, cmap=hmap, linewidth=0.1, ax=ax,         edgecolor='white', legend=True)
ax.set_axis_off()
leg = ax.get_legend()
leg.set_bbox_to_anchor((0., 0., 1.1, .8))
plt.show()


# # 9. Machine Learning

# ![](https://www.datacatchup.com/wp-content/uploads/2019/05/image.png)
# ![](https://static.javatpoint.com/tutorial/machine-learning/images/difference-between-supervised-and-unsupervised-learning.jpg)
# ![](https://miro.medium.com/max/1400/1*6iDmbHflsN6NULBLpVHA6A.png)
# ![](https://scikit-learn.org/stable/_static/ml_map.png)

# In[1]:


import os
import pandas as pd

from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

import matplotlib.pyplot as plt

from pandas.plotting import scatter_matrix
from sklearn.metrics import confusion_matrix


# In[2]:


#the model used below is classification, a subset of supervised learning 


# ## 9.1 Support Vector Classifier (SVC)

# In[3]:


covidvisual = pd.read_excel('covidvisualApril5th2023.xlsx')


# In[4]:


covidvisual.shape


# In[5]:


covidvisual.head(3)


# In[6]:


covidvisual.isnull().sum()


# In[7]:


covidvisual.columns


# In[8]:


dataset = covidvisual.loc[:, ['total_vaccinations_per_hundred',
                              'daily_vaccinations_per_million','covid_mortality_rate (per 100000)',
                              'Human Development Index 2021 (HDI)','GDP per capita 2021 (US$)',
                              'IncomeGroup']]


# In[9]:


dataset.head(3)


# In[10]:


dataset = dataset.dropna()


# In[11]:


dataset


# In[12]:


len(dataset)


# In[13]:


dataset.shape


# In[14]:


dataset.describe()


# In[15]:


print(dataset.groupby('IncomeGroup').size())


# In[16]:


dataset.drop(dataset.loc[dataset['IncomeGroup']=='Low income'].index, inplace=True)


# In[17]:


print(dataset.groupby('IncomeGroup').size())


# In[18]:


dataset=dataset.groupby('IncomeGroup', as_index=False, group_keys=False).apply(lambda x: x.sample(n=39))


# In[19]:


print(dataset.groupby('IncomeGroup').size())


# In[20]:


len(dataset)


# In[21]:


dataset


# In[22]:


#datasetrand = dataset.sample(frac=1)
#The frac keyword argument specifies the fraction of rows to return in the random sample, so frac=1 means return all rows (in random order)
#but in order to work in my case it needs to be in order like it is and not shuffled, otherwise it won't run later


# In[23]:


import statsmodels.api as sm
import statsmodels.formula.api as smf


# In[24]:


dummie_class = pd.get_dummies(dataset['IncomeGroup'],prefix='IncomeGroup')


# In[25]:


dummie_class


# In[26]:


Y = dummie_class['IncomeGroup_High income']


# In[27]:


Y.sample(n=10) # 1 is high income, 0 it's not


# In[28]:


X = dataset[['total_vaccinations_per_hundred',
            'daily_vaccinations_per_million',
             'covid_mortality_rate (per 100000)',
            'Human Development Index 2021 (HDI)','GDP per capita 2021 (US$)']] 
X = sm.add_constant(X)


# In[29]:


X


# In[30]:


probit_mod = sm.Probit(Y, X)


# In[31]:


probit_res = probit_mod.fit()


# In[32]:


print(probit_res.summary2())


# In[33]:


print(probit_res.get_margeff(at='overall', method='dydx').summary())


# In[34]:


X.head(3)


# In[35]:


predictions = probit_res.predict(X)
print(predictions[15:30])


# In[36]:


Y[15:30]


# In[37]:


dataset.plot(kind='box', subplots=True, layout=(3,2), sharex=False, sharey=False, figsize=(7, 7))
plt.show()


# In[38]:


dataset.hist(figsize=(8, 8))
plt.show()


# In[39]:


scatter_matrix(dataset, figsize=(15,15))
plt.show()


# In[40]:


dataset


# In[41]:


dataset.values


# In[42]:


array = dataset.values


# In[43]:


array


# In[44]:


X = array[:,0:5]


# In[45]:


X


# In[46]:


Y = array[:,5]


# In[47]:


Y


# In[48]:


validation_size = 0.2 #it sets 80% to train 20% to test, the default is 75% train 25% test
seed = 8
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)


# In[49]:


X_train[0:5]


# In[50]:


Y_train[0:5]


# In[51]:


len(X_train)


# In[52]:


len(X_validation)


# In[53]:


len(Y_train)


# In[54]:


len(Y_validation)


# In[55]:


X[0:5]


# In[56]:


Y[0:5]


# In[57]:


print('Training')
print('    X_training size:', len(X_train))
print('    Y_training size:', len(Y_train))
print('Validation')
print('    X_validation size:', len(X_validation))
print('    Y_validation size:', len(Y_validation))


# In[58]:


svm = SVC(probability=True) #training the model
#svm = SVC()
svm.fit(X_train, Y_train)


# In[59]:


svm


# In[60]:


predictions = svm.predict(X_validation) #making the predictions
print(predictions)


# In[61]:


print(Y_validation) #what the true outcome is


# In[62]:


#comparing the true outcome (validation) with the predictions
print(accuracy_score(Y_validation, predictions)) 


# In[63]:


dataset.head(3)


# In[64]:


dataset.max()


# In[65]:


dataset.min()


# In[66]:


dataset.describe() 


# In[67]:


svm.predict([[6.0, 600 , 60, 0.6, 6000]])


# In[68]:


svm.predict_proba([[6.0, 600 , 60, 0.6, 6000]])


# In[69]:


dataset.IncomeGroup


# In[70]:


labels = ['High income','Lower Middle income','Upper middle income']
cm = confusion_matrix(Y_validation, predictions)
print(cm)


# In[71]:


fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
cax = ax.matshow(cm)
plt.title('Confusion Matrix do Classifier')
fig.colorbar(cax)
ax.set_xticklabels([''] +labels)
ax.set_yticklabels([''] + labels)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()


# In[72]:


probs = svm.predict_proba(X_validation)
print(probs)
#probability associated to each observation


# In[73]:


#it's possible to make one prediction 


# In[74]:


Data = [[7.0, 578 , 55, 0.6, 5000]]
pred_data = svm.predict(Data)
print(pred_data)


# In[75]:


#or many at once


# In[76]:


Data = [[5.5, 550, 80, 0.59, 15000], [6.4, 400, 60, 0.57, 9500]]
pred_data = svm.predict(Data)
print(pred_data)


# In[77]:


dataset.describe() 


# ## 9.2 Logistic Regression, Decision Tree and Random Forest

# In[78]:


#making predictions in a different ways, this will also be classification, but not SVC


# In[79]:


covidvisual = pd.read_excel('covidvisualApril5th2023.xlsx')


# In[80]:


covidvisual


# In[81]:


covidvisual.head(3)


# In[82]:


covidvisual.shape


# In[83]:


covidvisual.isna().sum()


# In[84]:


import missingno as msno


# In[85]:


msno.bar(covidvisual)


# In[86]:


covidvisual.nunique()


# In[87]:


covidvisual.dtypes


# In[88]:


type(covidvisual)


# In[89]:


type(covidvisual['IncomeGroup'])


# In[90]:


covidvisual['IncomeGroup'].value_counts()


# In[91]:


covidvisual['IncomeGroup'].value_counts(normalize=True)


# In[92]:


import seaborn as sns


# In[93]:


sns.countplot(data=covidvisual, y = 'IncomeGroup')


# In[94]:


covidvisual.describe()


# In[95]:


covidvisual['covid_mortality_rate (per 100000)'].hist(grid=False, bins=50);


# In[96]:


sns.histplot(data=covidvisual, x = 'covid_mortality_rate (per 100000)', hue='IncomeGroup');


# In[97]:


sns.kdeplot(data=covidvisual,x='covid_mortality_rate (per 100000)', hue='IncomeGroup');


# In[98]:


pd.crosstab(covidvisual['Continent'], covidvisual['IncomeGroup'], margins=True)


# In[99]:


pd.crosstab(covidvisual['Continent'], covidvisual['IncomeGroup'], normalize='index')


# In[100]:


sns.heatmap(pd.crosstab(covidvisual['Continent'], covidvisual['IncomeGroup']), annot=True, fmt='.5g', cmap='viridis');


# In[101]:


covidvisual = covidvisual.dropna(subset=['daily_vaccinations_per_million','covid_mortality_rate (per 100000)'])


# In[102]:


incomegroupdummies = pd.get_dummies(covidvisual['IncomeGroup'], prefix='IncomeGroup')


# In[103]:


incomegroupdummies 


# In[104]:


covidvisual.shape


# In[105]:


covidvisual.isna().sum()


# In[106]:


covidvisual.head(3)


# In[107]:


from sklearn.model_selection import train_test_split


# In[108]:


x = covidvisual[['total_vaccinations_per_hundred',
            'daily_vaccinations_per_million',
             'covid_mortality_rate (per 100000)',
            'Human Development Index 2021 (HDI)','GDP per capita 2021 (US$)']]
y = incomegroupdummies['IncomeGroup_High income']


# In[109]:


x.head(3)


# In[110]:


x.isna().sum()


# In[111]:


y.head(10) #1 it's in the high income group, 0 it's not in the high income group


# In[112]:


x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=8) #by default from the library train is 75% test is 25%


# In[113]:


x_train.shape, x_test.shape


# In[114]:


from sklearn.linear_model import LogisticRegression


# In[115]:


lr = LogisticRegression(solver='liblinear')


# In[116]:


lr.fit(x_train, y_train)


# In[117]:


from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

def classification_results(classifier, x_test, y_test, cmap='Blues'):
    print('Model Results:', classifier.__class__.__name__)
    
    y_pred = classifier.predict(x_test)
    
    print(classification_report(y_test, y_pred))
    
    cm = confusion_matrix(y_test, y_pred)
    cmd = ConfusionMatrixDisplay(cm, display_labels=classifier.classes_)
    cmd.plot(cmap=cmap);


# In[118]:


classification_results(lr, x_test, y_test)
plt.grid(False)


# In[119]:


from sklearn.tree import DecisionTreeClassifier


# In[120]:


dt = DecisionTreeClassifier()


# In[121]:


dt.fit(x_train, y_train)


# In[122]:


from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

def classification_results(classifier, x_test, y_test, cmap='Blues'):
    print('Model Results:', classifier.__class__.__name__)
    
    y_pred = classifier.predict(x_test)
    
    print(classification_report(y_test, y_pred))
    
    cm = confusion_matrix(y_test, y_pred)
    cmd = ConfusionMatrixDisplay(cm, display_labels=classifier.classes_)
    cmd.plot(cmap=cmap);


# In[123]:


classification_results(dt, x_test, y_test)
plt.grid(False)


# In[124]:


from sklearn.ensemble import RandomForestClassifier


# In[125]:


rf = RandomForestClassifier()
rf.fit(x_train, y_train)
classification_results(rf, x_test, y_test, cmap='Oranges')
plt.grid(False)

