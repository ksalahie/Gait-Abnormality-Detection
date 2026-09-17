import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel

def top_features(X, y):
    '''
    Random Forest used to select the most predictive
    gait variables based on importance from the data.
    '''
    rf_selector = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_selector.fit(X, y)
    
    importances = pd.Series(rf_selector.feature_importances_, index=X.columns)
    importances = importances.sort_values(ascending=False)
    
    selector = SelectFromModel(rf_selector, prefit=True)
    X_selected = selector.transform(X)
    
    return X_selected, importances
