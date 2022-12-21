# Stock-Market-Predictions
Predicting the stock market opening values using Deep learning's Model Recurrent Neural Networks which is a very powerful model.

# Description


# Context
Stock market data can be interesting to analyze and as a further incentive, strong predictive models can have large financial payoff. The amount of financial data on the web is seemingly endless. A large and well structured dataset on a wide array of companies can be hard to come by. Here I provide a dataset with historical stock prices (last 5 years) for all companies currently found on the S&P 500 index.

The script I used to acquire all of these .csv files can be found in this GitHub repository In the future if you wish for a more up to date dataset, this can be used to acquire new versions of the .csv files.

Feb 2018 note: I have just updated the dataset to include data up to Feb 2018. I have also accounted for changes in the stocks on the S&P 500 index (RIP whole foods etc. etc.).

# Content
The data is presented in a couple of formats to suit different individual's needs or computational limitations. I have included files containing 5 years of stock data (in the all_stocks_5yr.csv and corresponding folder).

The folder individual_stocks_5yr contains files of data for individual stocks, labelled by their stock ticker name. The all_stocks_5yr.csv contains the same data, presented in a merged .csv file. Depending on the intended use (graphing, modelling etc.) the user may prefer one of these given formats.

All the files have the following columns: Date - in format: yy-mm-dd

Open - price of the stock at market open (this is NYSE data so all in USD)

High - Highest price reached in the day

Low Close - Lowest price reached in the day

Volume - Number of shares traded

Name - the stock's ticker name

# Acknowledgements
Due to volatility in google finance, for the newest version I have switched over to acquiring the data from The Investor's Exchange api, the simple script I use to do this is found here. Special thanks to Kaggle, Github, pandas_datareader and The Market.

# Inspiration
This dataset lends itself to a some very interesting visualizations. One can look at simple things like how prices change over time, graph an compare multiple stocks at once, or generate and graph new metrics from the data provided. From these data informative stock stats such as volatility and moving averages can be easily calculated. The million dollar question is: can you develop a model that can beat the market and allow you to make statistically informed trades!
