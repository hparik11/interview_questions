import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler


def split_data_into_train_validation(features, labels, random_state=42, split_size=0.2):
    if features.shape[0] != labels.shape[0]:
        raise ValueError("features and labels don't match")
    
    return train_test_split(features, labels, test_size=split_size, random_state=random_state, stratify=labels)


def get_features_labels_from_data(input_dataframe, label_col="churn", columns_to_remove=[]):
    
    features = drop_columns_from_dataframe(input_dataframe, [label_col] + columns_to_remove)
    labels= input_dataframe[label_col]
    
    return features, labels


def scale_dataframe(input_dataframe, scale_type="standard"):
    if scale_type == 'min-max':
        scaler = MinMaxScaler()
    elif scale_type == "robust":
        scaler = RobustScaler()
    else:
        scaler = StandardScaler()
    
    
    return scaler.fit_transform(input_dataframe)


def drop_columns_from_dataframe(input_dataframe, columns_to_remove):
    return input_dataframe.drop(columns_to_remove, axis=1)