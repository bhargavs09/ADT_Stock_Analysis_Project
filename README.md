# Stock-Prediction-Analysis

Stock prediction analysis predicts the efficient stock among the provided stocks. The objects which extracted in this project are real-time data. The data is used to predict the efficient stock using statistical analysis.

**Problem Statement**: 
        Now-a-days, many people are showing interest towards organizational capital value(stock) market and millions of dollars are being invested in stocks for better growth. People are facing difficulties to predict the growing stocks and losing huge amount of money. In modern trends these stock markets are highly volatile and unpredictable, even the top stable stocks are also facing sudden decrease in the value (dip). 
  
**Motivation**: This project will help a lot of people who shows interest towards investing in the stock market. The daily trends in the Stock market are becoming unpredictable and people are puzzled on selecting the stocks to invest among multiple stock exchange options which makes it more challenging to predict the uptrends of stocks. Our targeted users are the members who shows greater interests towards investing in stocks. 

**Proposed Approach**: In this project, the larger amount of historical data is required to predict the stock analysis. Apache spark is suitable to processing the enormous volume of data due to its performance which was 100 times faster than the Hadoop. All the data processing techniques which require to predict the stock analysis will be achieved through Apache Spark. Recent Study: Stock market is one of the major fields that investors are dedicated to, thus stock market trend prediction is always a hot topic for researchers from both financial and technical domains. In this research, our objective is to build a predictive solution which displays the statistics of data till current date. The other similar kind of projects related to prediction analysis displays the data of past years for five years only. 

**Model Workflow and Analysis**:

Following are the main tasks in our project and discussed briefly on it.
* Data Extraction
* Data Selection
* Data Transformation
* Business logic 
* Statistical prediction analysis

The spark session is created at the beginning of the project using spark builder, data extraction process starts after the spark session begins by inputting the stock symbol. For Instance, AAPL is the stock symbol for apple. The historical real-time data is extracted based on the provided stock symbol from January 1,2001 to today’s date.

The extracted historical data is stored in the spark data frames and temp views are created for spark SQL selection and transformation activities. In data selection, the required attributes are selected and stored in the spark data frames. The row numbers are added as a new attribute to the selected data. 

The new previous_adjacent_close attribute is created in data transformations to access the previous day adjacent close data using lag functions. Before applying the lag function, the data is partitioned and sorted based on the provided attributes.

The business logic is applied to find the returns of stocks based on the adjacent_close attribute and previous_adjacent_close attribute. The resultant returns of the stocks are stored as a new attribute named returns in the spark data frame.

After data transformations, the statistical prediction analysis is applied by defining the mean, variance and standard deviation. After calculating the mean, variance and standard deviation for provided stocks with the resultant spark data frame. 

The stock daily returns are predicted based on these statistical analysis. The analysis predicts which stocks is better among the provided stocks and it also provides the prediction analysis of stock daily returns at 99.3% of time, 95.5% of time and 68.3% of time. The daily returns, 68.3% of time gives the shorter range than other percentages of time. The 95.5% of time daily returns gives the wider range than 68.3% of time. The 99.3% of time gives the wider range than 68.3% of time and 95.5% of time. 

For instance, If the 68.3% of time gives daily returns range between 0.0216 and 0.0247 then 95.5% of time gives daily returns range between 0.0201 and 0.0262 then 99.3% of time gives the daily returns range between 0.0186 and 0.0278. The analysis results are integrated with the dashboards to improve the productivity and visibility.

**Discussion and Conclusion**: In stock prediction analysis projects, complex algorithms are used to solve the problems which results in time consuming, understanding and applying advanced algorithms are difficult, and not every tasks are easy to deal with the algorithms. In our stock prediction analysis project, the solutions are achieved based on the statistical analysis. Without the complex algorithm techniques, the statistics will assist in identifying trends that might otherwise go unnoticed. Achieving the results through statistical analysis will be quick, efficient, and productive. 

All in all, the statistical analysis is used to predict the outcome of two stock values over a large period of time I.e 2001 to current date. The results will also provides information regarding the daily return of the stock and represent them in the form of graph for better understanding for the users.
