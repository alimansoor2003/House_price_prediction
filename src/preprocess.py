

import pandas as pd

def load_data(path):
    return pd.read_csv(path, index_col=0)


def preprocess(data):

    data['Garage'] = data['Garage'].map({'Yes': 1, 'No': 0})

    data['Condition'] = data['Condition'].map({
        'Excellent': 4,
        'Good': 3,
        'Fair': 2,
        'Poor': 1
    })

    data['Family'] = ((data['Area'] > 2000) & (data['Bedrooms'] > 3)).astype(int)

    data = pd.get_dummies(data, columns=["Location"], drop_first=True)

    return data   