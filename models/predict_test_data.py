import pandas as pd
import numpy as np

def predict_test_data(test, model, softmax = True, wc_playoff_model = None):
    #48 and beyond is playoffs
    if softmax:    
        return [np.where(np.argsort(val) == 1)[0][0]-1 if (i >= 48) & (np.argmax(val) == 1)
                           else np.argmax(val)-1 for i, val in enumerate(model.predict_proba(test))] 
    else:      
        return list(model.predict(test[:48])) + list(wc_playoff_model.predict(test[48:]))
            
        