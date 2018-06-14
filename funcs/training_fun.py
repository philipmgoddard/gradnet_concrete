from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd


def train_test(features_train, outcome_train, 
               features_test, outcome_test,
               n_trees = 100,
               n_features = 3,
               max_depth = 6):
    model  = RandomForestRegressor(n_estimators = n_trees,
                                   max_depth = max_depth,
                                   max_features = n_features,
                                   random_state = 1234)
    
    model.fit(features_train, outcome_train)
    pred_train = model.predict(features_train)
    pred_test = model.predict(features_test)
    
    rmse_train = mean_squared_error(outcome_train, pred_train) ** 0.5
    rmse_test = mean_squared_error(outcome_test, pred_test) ** 0.5

    print("rmse train: {}".format(rmse_train))
    print("rmse test: {}".format(rmse_test))
    
    return 