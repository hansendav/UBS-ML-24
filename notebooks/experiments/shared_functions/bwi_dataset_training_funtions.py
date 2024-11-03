# This is script holds functions that are used in the training phase for the 
# BWI dataset (UBS-ML-WS24). 

# Imports 
import os 
import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt

from sklearn.metrics import classification_report, confusion_matrix
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import SMOTENC

# Feature, Target, Group splits 
def split_input_data(df):
    """
    This function splits the input data into groups, features and targets.
    Based on the features: Tnr, Enr, bl, Ba respectively.
    """
    groups = df[['Tnr', 'Enr', 'bl']]
    features = df.drop(['Tnr', 'Enr', 'bl', 'Ba'], axis=1)
    targets = df['Ba']
    return groups, features, targets   


# Metrics display 
def compute_and_return_metrics(y_true, y_preds, file_name):
    """
    Returns and saves metrics given true labels and predictions.
    """
    # --- classification report ---
    # classification report
    # create a dataframe report for saving
    df_report = pd.DataFrame(classification_report(y_true, y_preds,
                                                   output_dict=True,
                                                   zero_division=np.nan))
    # save to file given file_name
    df_report.to_csv('./metrics/classification_report_' + file_name + '.csv')

    # print classification report -> change this such that you do not have to 
    # compute the metrics twice!
    print(classification_report(y_true, y_preds))

    # --- confusion matrix ---
    conf_m = confusion_matrix(y_true, y_preds)
    # create confusion matrix dataframes with sums for each row and column 
    # revise this part!
    df_conf_m = pd.DataFrame(conf_m)
    count_true_labels = df_conf_m.sum(axis=1).reset_index(drop=True)
    df_conf_m = pd.concat([df_conf_m, count_true_labels], axis=1)
    df_conf_m.columns = pd.Index([i for i in range(df_conf_m.columns.size)])
    count_pred_labels = df_conf_m.sum(axis=0).reset_index(drop=True)
    df_conf_m = pd.concat([df_conf_m, count_pred_labels.to_frame().T], ignore_index=True)
    df_conf_m.to_csv('./metrics/confusion_matrix_' + file_name + '.csv')

    # --- plot confusion matrix ---
    conf_m_normalized = confusion_matrix(y_true, y_preds, normalize='true')

    plt.figure(figsize=(8, 8))
    sns.heatmap(conf_m_normalized, annot=True, fmt='.2f', cmap='Blues',
                xticklabels=np.sort(y_true.unique()), yticklabels=np.sort(y_true.unique()))
    plt.xlabel('Predicted Classes')
    plt.ylabel('True Classes')
    plt.yticks(rotation=0)
    plt.title('Confusion Matrix')
    plt.tight_layout()
    plt.savefig(('./metrics/confusion_matrix_' + file_name + '.png'), bbox_inches='tight', dpi=300)
    plt.show()

# Under- and over-sampling functions 

def random_undersample(features, targets, groups, group_features=['Tnr', 'Enr', 'bl'], random_state=42):
    """Randomly Undersamples the majority class. Preserving grouping of data"""
    features = pd.concat([features, groups], axis=1)
    rus = RandomUnderSampler(random_state=random_state)
    features_resampled, targets_resampled = rus.fit_resample(features, targets)
    groups_resampled = features_resampled[group_features]
    features_resampled = features_resampled.drop(columns=group_features)
    return features_resampled, targets_resampled, groups_resampled

def smotenc_resample(features, targets, cat_index, random_state=42):
    """Performs SMOTENC with not majority strategy. This does not preserve grouping!"""
    smote_nc = SMOTENC(categorical_features=cat_index, random_state=random_state)
    features_resampled, targets_resampled = smote_nc.fit_resample(features, targets)
    return features_resampled, targets_resampled

            
def create_directory_structure():
    # Create output directory
    output_dirs = ['./metrics', './model', './cross_validation']
    
    for directory in output_dirs:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")
        else: 
            print(f"Directory already exists: {directory}")

def print_cv_results(cv_results):
    print(
    f"CV metrics:"
    f"\n---------------------------------"
    f"\nBalanced accuracy: {cv_results['test_balanced_accuracy'].mean():.2f} ± {cv_results['test_balanced_accuracy'].std():.2f}"
    f"\nPrecision-macro: {cv_results['test_precision_macro'].mean():.2f} ± {cv_results['test_precision_macro'].std():.2f}"
    f"\nF1-macro: {cv_results['test_f1_macro'].mean():.2f} ± {cv_results['test_f1_macro'].std():.2f}"
    f"\n---------------------------------"
    f"\nFitting time: {cv_results['fit_time'].mean():.2f} ± {cv_results['fit_time'].std():.2f}"
    f"\nPrediction time: {cv_results['score_time'].mean():.2f} ± {cv_results['score_time'].std():.2f}"
)
