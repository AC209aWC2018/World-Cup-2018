import pandas as pd
import numpy as np

def predict_test_data(test, model):
#     predictions = []
#     for i in range(len(test)):
#         #Rounds where there are ties
#         if i < 48:
#             prediction = model.predict(test[i].reshape(-1,1))
#             predictions.append(prediction[0])
#         else:
#             #first column is home_win = -1, second column is home_win = 0, third column is home_win = 1
#             probs = model.predict_proba(test_df)[:, [0, 2]]
#             #check if third column probability greater than first. If it is, predict home win else predict home lose.
#             if probs[0][1] > probs[0][0]:
#                 predictions.append(1)
#             else:
#                 predictions.append(-1)
                
    return [np.where(np.argsort(val) == 1)[0][0]-1 if (i >= 48) & (np.argmax(val) == 1)
                       else np.argmax(val)-1 for i, val in enumerate(model.predict_proba(test))]
            
    return predictions
        