# Change_point_analysis
### Task 1: Defining the Data Analysis Workflow and Understanding the Model and Data

#### 1.1 Defining the Data Analysis Workflow

**Steps and Processes:**
1. **Data Collection:** Gather historical Brent oil prices data from reliable sources such as the U.S. Energy Information Administration (EIA), International Energy Agency (IEA), or Bloomberg.
2. **Data Preprocessing:** Clean the data to handle missing values, outliers, and inconsistencies. Normalize or standardize the data if necessary.
3. **Exploratory Data Analysis (EDA):** Perform initial analysis to understand data distributions, trends, and correlations. Use visualizations like line charts, histograms, and scatter plots.
4. **Model Selection:** Choose appropriate time series models (e.g., ARIMA, GARCH) based on the data characteristics.
5. **Model Training:** Split the data into training and testing sets. Train the selected models on the training set.
6. **Model Evaluation:** Evaluate model performance using metrics like RMSE, MAE, and R-squared. Validate the model using out-of-sample testing.
7. **Insight Generation:** Interpret model outputs to derive actionable insights and recommendations.
8. **Communication:** Present findings to stakeholders using reports, dashboards, and visualizations.

**Data Generation and Sampling:**
- Understand how Brent oil prices are recorded (e.g., daily, weekly, monthly) and the factors influencing these prices.
- Ensure the data is representative and free from biases.

**Model Inputs, Parameters, and Outputs:**
- Inputs: Historical price data, economic indicators, technological changes, political factors.
- Parameters: Model-specific parameters (e.g., ARIMA parameters p, d, q).
- Outputs: Forecasted prices, volatility measures, trend analysis.

**Assumptions and Limitations:**
- Assumptions: Stationarity of time series, linear relationships, no external shocks.
- Limitations: Model accuracy, data quality, unforeseen market events.

**Communication Channels:**
- Reports, presentations, interactive dashboards, emails, meetings.

#### 1.2 Understanding the Model and Data

**Key Concepts and Models:**
- **ARIMA (AutoRegressive Integrated Moving Average):** Suitable for univariate time series data, capturing trends and seasonality.
- **GARCH (Generalized Autoregressive Conditional Heteroskedasticity):** Models volatility clustering in financial time series.
- **VAR (Vector Autoregression):** For multivariate time series, capturing interdependencies between variables.
- **LSTM (Long Short-Term Memory):** A type of recurrent neural network for capturing long-term dependencies in sequential data.

**Purpose and Application:**
- **ARIMA:** Predict future prices based on past trends and seasonality.
- **GARCH:** Model and predict volatility, useful for risk management.
- **VAR:** Analyze the impact of multiple economic indicators on oil prices.
- **LSTM:** Capture complex, non-linear patterns in price movements.

**Data Generation Processes:**
- Prices are influenced by supply-demand dynamics, geopolitical events, and economic indicators.
- Models aim to capture these influences through statistical and machine learning techniques.

**Expected Outputs and Limitations:**
- Outputs: Forecasted prices, volatility measures, trend analysis.
- Limitations: Model assumptions, data quality, external shocks.

### Task 2: Analyzing Brent Oil Prices

#### 2.1 Applying Time Series Analysis

**Historical Data Analysis:**
- Use ARIMA and GARCH models to analyze historical Brent oil prices.
- Identify trends, seasonality, and volatility patterns.

**Advanced Models:**
- **VAR:** Analyze the impact of GDP, inflation, and exchange rates on oil prices.
- **Markov-Switching ARIMA:** Capture different market regimes (e.g., high volatility vs. low volatility).
- **LSTM:** Model complex, non-linear dependencies in price data.

#### 2.2 Exploring Influencing Factors

**Economic Indicators:**
- **GDP:** Analyze correlation with oil prices.
- **Inflation Rates:** Examine impact on oil demand.
- **Unemployment Rates:** Investigate relationship with oil consumption.
- **Exchange Rates:** Assess effect of USD fluctuations on prices.

**Technological Changes:**
- **Extraction Technologies:** Study impact of fracking and deep-sea drilling on supply.
- **Renewable Energy:** Analyze effect on oil demand.
- **Efficiency Improvements:** Evaluate impact on consumption.

**Political and Regulatory Factors:**
- **Environmental Regulations:** Investigate impact on production and prices.
- **Trade Policies:** Study effect of tariffs and embargoes on markets.

#### 2.3 Adapting the Model to New Scenarios

**Different Scenarios:**
- Extend analysis to natural gas or coal markets.
- Compare factors influencing different energy markets.

**New Variables:**
- Integrate macroeconomic variables and indices.
- Include data on technological advancements and regulatory changes.

**Model Validation:**
- Backtest models using historical data.
- Conduct out-of-sample testing.
- Use cross-validation techniques.

### Task 3: Developing an Interactive Dashboard

#### 3.1 Backend (Flask)

**APIs:**
- Develop APIs to serve analysis results, model outputs, and performance metrics.
- Handle requests for different datasets and real-time updates.

**Data Integration:**
- Integrate data sources for real-time updates if necessary.

#### 3.2 Frontend (React)

**User Interface:**
- Create an intuitive and user-friendly interface.
- Design interactive visualizations using Recharts, React Chart.js 2, or D3.js.

**Key Features:**
- **Historical Trends:** Display historical price trends.
- **Forecasts:** Show model forecasts and confidence intervals.
- **Event Correlation:** Highlight how specific events influenced prices.
- **Filters and Date Ranges:** Allow users to filter data and select date ranges.
- **Key Indicators:** Display volatility, average price changes, and model accuracy metrics.

**Responsiveness:**
- Ensure the dashboard is responsive and accessible on various devices.

### Suggested Approach

**Data Collection:**
- Gather datasets from reliable sources like the World Bank, IMF, and IEA.

**Data Preprocessing:**
- Clean and preprocess data to ensure consistency and accuracy.

**Exploratory Data Analysis (EDA):**
- Perform EDA to identify patterns and relationships.
- Use visualizations to gain insights.

**Model Building:**
- Develop multiple models (time series, econometric, machine learning).

**Model Evaluation:**
- Evaluate models using performance metrics.
- Compare models to identify the best-performing ones.

**Insight Generation:**
- Interpret model outputs to generate actionable insights.
- Provide clear recommendations based on analysis results.



