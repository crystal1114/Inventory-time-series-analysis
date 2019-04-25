# Inventory-time-series-analysis
Objective: To manage inventory of electric equipment by using time series rolling horizon inventory model to make order plan to realize the objective which is minimize the expected cost of holding inventory plus expected cost of lost sales.

Data cleaning and training(R)to predict the demand.

Build Deterministic Model(AMPL) to make order plan based on predict demand and start inventory.

Build Stochastics Model (Python-pyomo) same as Deterministic but add error terms which were generated in the training process.
