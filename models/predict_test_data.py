import pandas as pd
import numpy as np

def predict_test_data(test_df, columns, model):
    outcomes = test_df['home_win']
    predictions = []
    for i in range(len(test_df)):
        #Rounds where there are ties
        if len(test_df.iloc[i]['Group']) == 1:
            prediction = model.predict(test_df.iloc[i][columns].values.reshape(1, len(columns)))
            predictions.append(prediction[0])
        else:
            #first column is home_win = -1, second column is home_win = 0, third column is home_win = 1
            probs = model.predict_proba(test_df.iloc[i][columns].values.reshape(1, len(columns)))[:, [0, 2]]
            #check if third column probability greater than first. If it is, predict home win else predict home lose.
            if probs[0][1] > probs[0][0]:
                predictions.append(1)
            else:
                predictions.append(-1)
            
    return predictions
        