# %%


# %% [markdown]
# # WQD 7006 GROUP ASSIGNMENT: CREDIT CARD FRAUD DETECTION

# %% [markdown]
# ![grp.png](data:image/png;base64,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)

# %%
#from google.colab import drive
#drive.mount('/content/drive')

# %%
#pip install numpy pandas matplotlib seaborn


# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
#df = pd.read_csv('/content/drive/MyDrive/creditcard.csv')
df = pd.read_csv('creditcard.csv')

# %%
df.head()

# %%
df.tail()

# %% [markdown]
# # 1. Data Understanding

# %%
df.shape

# %%
df.info()

# %%
df.nunique()

# %%
# Check for missing values
df.isnull().sum()

# %%
##pip install missingno

# %%
import missingno as mn
mn.matrix(df)

# %%
df.duplicated().any()

# %%
df.describe()

# %% [markdown]
# **Observations**
# - Dataset has total of `284,807 rows` and `31 columns`.
# - Dataset contains no null values.
# - Dataset contains duplicated values.
# - The mean of principle components `V1 - V28` are close to 0, which is expected as a result of PCA which involves centering the data by subtracting the mean.
# - The average transaction amount based on the feature `Amount` is approximately 88.35.

# %% [markdown]
# # 2. Data Preprocessing

# %% [markdown]
# ### 2.1 Dropping Duplicated Values

# %%
df.drop_duplicates(keep = 'first', inplace = True)
df.duplicated().any()

# %%
df.shape

# %%
df.head()

# %% [markdown]
# ### 2.2 Check Skewness of Features

# %%
df.skew().sort_values()

# %% [markdown]
# - Highly `-vely` skewed features: V8, V23, V2, V17, V1, V5, V12, V3, V20, V14
# - Highly `+vely` skewed features: V6, V7, V21, V28, Amount, class

# %%
plt.figure(figsize=(18, 30))

# Assuming 'df' is your DataFrame and you want to exclude 'Time' and 'class' from the histograms
features = df.columns.drop(['Time', 'class'])

# Create a histogram for each feature
for i, feature in enumerate(features):
    plt.subplot(10, 3, i + 1)
    sns.histplot(df[feature], bins=50, kde=True, color='blue', alpha=0.7)
    plt.title(feature)

plt.tight_layout()
plt.show()

# %% [markdown]
# # 3. Data Sampling
# 

# %% [markdown]
# ### Handling Imbalanced Class

# %%
df['class'].value_counts()

# %%
a = df['class'].value_counts().rename('count')
b = (df['class'].value_counts(normalize=True)*100).rename('distribution')

df_class = pd.concat([a,b], axis=1)
df_class.index = ["Genuine", "Fraud"]
df_class['distribution'].plot(kind='bar', figsize=[5,5])
df_class

# %% [markdown]
# - The `class` feature demonstrates `'0 - Genuine'` with a relatively higher count than `'1 - Fraud'` presenting an imbalanced distribution.
# 
# Due to the imbalanced distribution in `class`, it needs to be addressed prior to ML training and testing. In order to overcome this problem, 2 methods of sampling will be employed:
# 
# 
# 1.   Oversampling via SMOTE
# 2.   Undersampling
# 
# 

# %% [markdown]
# SMOTE stands for Synthetic Minority Oversampling Technique.This is a statistical technique for increasing the number of cases in your dataset in a balanced way. The module works by generating new instances from existing minority cases.

# %% [markdown]
# ### 3.1 Splitting the Dataset (X = Features, y = Target)

# %%
X = df.drop(['Time', 'class'], axis=1)
y = df['class']
X.head()

# %%
#pip install scikit-learn

# %%
#pip install imbalanced-learn

# %%
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

# %%
# Scale the data
scaler = StandardScaler()
X['scaled_amount'] = scaler.fit_transform(X[['Amount']])
X.drop('Amount', axis=1, inplace=True)

# Split the dataset into training (80%) and testing sets (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# %%
X.head()

# %% [markdown]
# ### 3.2 Oversampling via SMOTE

# %%
# Apply SMOTE
smote = SMOTE(sampling_strategy='minority', random_state=42)
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)

# %%
sns.countplot(x=y_train_smote, palette='viridis')
plt.title('Class Distribution After SMOTE Resampling')
plt.xlabel('Class')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()

# %%
print(pd.Series(y_train_smote).value_counts())

# %% [markdown]
# ### 3.3 Undersampling Majority Class
# 
# 

# %%
from imblearn.under_sampling import RandomUnderSampler

# Initialize RandomUnderSampler
rus = RandomUnderSampler(random_state=42)

# Resample the dataset
X_train_rus, y_train_rus = rus.fit_resample(X_train, y_train)

# %%
plt.figure(figsize=(8, 4))
sns.countplot(x=y_train_rus, palette='viridis')
plt.title('Class Distribution After Random Under-Sampling')
plt.xlabel('Class')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()

# %%
print(pd.Series(y_train_rus).value_counts())

# %%
import psutil
#Measure the execution time 
import time

# %%
import psutil
 
# Before a process
cpu_before = psutil.cpu_percent()
memory_before = psutil.virtual_memory().used

# %% [markdown]
# 4.0 MACHINE LEARNING - XGBOOST

# %% [markdown]
# 4.1 USING ORIGINAL DATASET

# %%
#pip install xgboost

# %%

# Importing necessary libraries
import xgboost as xgb
from sklearn.metrics import classification_report

# Define XGBoost parameters
params = {
    'objective': 'binary:logistic',  # Binary classification
    'eval_metric': 'logloss',         # Evaluation metric: log loss
    'eta': 0.1,                       # Learning rate
    'max_depth': 6,                   # Maximum tree depth
    'min_child_weight': 1,            # Minimum sum of instance weight needed in a child
    'subsample': 0.8,                 # Subsample ratio of the training instances
    'colsample_bytree': 0.8,          # Subsample ratio of columns when constructing each tree
    'gamma': 0,                       # Minimum loss reduction required to make a further partition on a leaf node
    'seed': 42                        # Random seed
}

# Record resource usage before training
cpu_before = psutil.cpu_percent()
memory_before = psutil.virtual_memory().used
start_time = time.time()

# Convert data into DMatrix format for XGBoost for original data
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test)

# Train the model with original data
num_rounds = 100
model = xgb.train(params, dtrain, num_rounds)

# Predictions for original data
y_pred = model.predict(dtest)

# Convert predicted probabilities to binary predictions
y_pred_binary = [1 if p >= 0.5 else 0 for p in y_pred]

# Evaluate the model for original data
print("Evaluation for original data:")
print(classification_report(y_test, y_pred_binary))

# Record resource usage after training
end_time = time.time()
cpu_after = psutil.cpu_percent()
memory_after = psutil.virtual_memory().used

# Calculate execution time and resource usage changes
execution_time_xgb = end_time - start_time
cpu_usage_change = cpu_after - cpu_before
memory_usage_change = memory_after - memory_before

print(f"Execution Time for original dataset: {execution_time_xgb:.4f} seconds")
print(f"CPU usage change: {cpu_usage_change}%")
print(f"Memory usage change: {memory_usage_change} bytes")


# %% [markdown]
# - Precision measures the accuracy of positive predictions. For class 0 (genuine transactions), the precision is 1.00, indicating that all transactions predicted as genuine are indeed genuine. For class 1 (fraudulent transactions), the precision is 0.94, suggesting that 94% of the transactions predicted as fraudulent are correct.
# -Recall, also known as sensitivity, measures the proportion of actual positives that are correctly identified by the model. For class 0, the recall is 1.00, indicating that all genuine transactions are correctly identified as genuine. However, for class 1, the recall is 0.69, meaning that only 69% of the fraudulent transactions are correctly identified by the model.
# - The F1-score is the harmonic mean of precision and recall and provides a balance between the two metrics. For class 0, the F1-score is 1.00, indicating excellent performance. For class 1, the F1-score is 0.79, which is lower due to the lower recall.
# -Accuracy measures the overall correctness of the model's predictions. In this case, the accuracy is high at 1.00, but it may not be the most informative metric due to the class imbalance (vast majority of transactions are genuine).
# 
# Overall, the model performs very well in identifying genuine transactions (class 0) with high precision and recall. However, it struggles to correctly identify fraudulent transactions (class 1) with lower recall, indicating room for improvement, particularly in detecting fraud.

# %% [markdown]
# 4.2 USING SMOTE DATASET

# %%
import xgboost as xgb
from sklearn.metrics import classification_report

# Define XGBoost parameters
params = {
    'objective': 'binary:logistic',
    'eval_metric': 'logloss',
    'eta': 0.1,
    'max_depth': 6,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
    'seed': 42
}

# Record resource usage before training
cpu_before = psutil.cpu_percent()
memory_before = psutil.virtual_memory().used
start_time = time.time()


# Convert data into DMatrix format for XGBoost for SMOTE data
dtrain_smote = xgb.DMatrix(X_train_smote, label=y_train_smote)
dtest_smote = xgb.DMatrix(X_test)  # Note: Using the scaled test data

# Train the model with SMOTE data
num_rounds = 100
model_smote = xgb.train(params, dtrain_smote, num_rounds)

# Predictions for SMOTE data
y_pred_smote = model_smote.predict(dtest_smote)

# Convert predicted probabilities to binary predictions
y_pred_smote_binary = [1 if p >= 0.5 else 0 for p in y_pred_smote]

# Evaluate the model for SMOTE data
print("Evaluation for SMOTE data:")
print(classification_report(y_test, y_pred_smote_binary))

# Record resource usage after training
end_time = time.time()
cpu_after = psutil.cpu_percent()
memory_after = psutil.virtual_memory().used

# Calculate execution time and resource usage changes
execution_time_xgb = end_time - start_time
cpu_usage_change = cpu_after - cpu_before
memory_usage_change = memory_after - memory_before

print(f"Execution Time SMOTE Dataset: {execution_time_xgb:.4f} seconds")
print(f"CPU usage change: {cpu_usage_change}%")
print(f"Memory usage change: {memory_usage_change} bytes")

# %% [markdown]
# - The precision for class 0 (genuine transactions) is 1.00, indicating that all transactions predicted as genuine are indeed genuine. For class 1 (fraudulent transactions), the precision is 0.38, suggesting that only 38% of the transactions predicted as fraudulent are correct.
# - The recall for class 0 is 1.00, indicating that all genuine transactions are correctly identified as genuine. However, for class 1, the recall is 0.80, meaning that 80% of the fraudulent transactions are correctly identified by the model.
# - The F1-score for class 0 is 1.00, indicating excellent performance. For class 1, the F1-score is 0.51, which is lower due to the lower precision.
# - The overall accuracy is high at 1.00, but, similar to the original dataset, it may not provide a complete picture due to the class imbalance.
# 
# Overall, the model trained on the SMOTE-resampled dataset performs well in identifying both genuine and fraudulent transactions. However, there is a trade-off between precision and recall, with lower precision for fraudulent transactions but higher recall compared to the original dataset. This indicates that while more fraudulent transactions are correctly identified, there is a higher rate of false positives.

# %% [markdown]
# 4.3 USING RUS DATASET

# %%
import xgboost as xgb
from sklearn.metrics import classification_report

# Define XGBoost parameters
params = {
    'objective': 'binary:logistic',
    'eval_metric': 'logloss',
    'eta': 0.1,
    'max_depth': 6,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
    'seed': 42
}

# Record resource usage before training
cpu_before = psutil.cpu_percent()
memory_before = psutil.virtual_memory().used
start_time = time.time()

# Convert data into DMatrix format for XGBoost for RUS data
dtrain_rus = xgb.DMatrix(X_train_rus, label=y_train_rus)
dtest_rus = xgb.DMatrix(X_test)  # Note: Using the scaled test data

# Train the model with RUS data
num_rounds = 100
model_rus = xgb.train(params, dtrain_rus, num_rounds)

# Predictions for RUS data
y_pred_rus = model_rus.predict(dtest_rus)

# Convert predicted probabilities to binary predictions
y_pred_rus_binary = [1 if p >= 0.5 else 0 for p in y_pred_rus]

# Evaluate the model for RUS data
print("Evaluation for RUS data:")
print(classification_report(y_test, y_pred_rus_binary))

# Record resource usage after training
end_time = time.time()
cpu_after = psutil.cpu_percent()
memory_after = psutil.virtual_memory().used

# Calculate execution time and resource usage changes
execution_time_xgb = end_time - start_time
cpu_usage_change = cpu_after - cpu_before
memory_usage_change = memory_after - memory_before

print(f"Execution Time RUS Dataset: {execution_time_xgb:.4f} seconds")
print(f"CPU usage change: {cpu_usage_change}%")
print(f"Memory usage change: {memory_usage_change} bytes")

# %% [markdown]
# - The precision for class 0 (genuine transactions) is 1.00, indicating that all transactions predicted as genuine are indeed genuine. For class 1 (fraudulent transactions), the precision is 0.05, suggesting that only 5% of the transactions predicted as fraudulent are correct.
# - The recall for class 0 is 0.97, indicating that 97% of the genuine transactions are correctly identified as genuine. For class 1, the recall is 0.89, meaning that 89% of the fraudulent transactions are correctly identified by the model.
# - The F1-score for class 0 is 0.99, indicating high performance in identifying genuine transactions. However, for class 1, the F1-score is only 0.10, which is significantly lower due to the low precision.
# - The overall accuracy is 0.97, indicating that 97% of the predictions are correct. However, similar to the other datasets, accuracy may not be the most informative metric due to the class imbalance.
# 
# Overall, the model trained on the RUS dataset performs well in identifying genuine transactions but struggles with identifying fraudulent transactions, as indicated by the low precision and F1-score for class 1. While the recall for class 1 is relatively high, it comes at the expense of a high rate of false positives, resulting in lower precision.

# %% [markdown]
# EXECUTION TIME FOR XGBOOST MODELLING

# %%
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution Time: {execution_time} seconds")

# %% [markdown]
# EVALUATION MATRIX COMPARISON TABLE

# %% [markdown]
# | Model   | Precision (Class 0) | Recall (Class 0) | F1-Score (Class 0) | Precision (Class 1) | Recall (Class 1) | F1-Score (Class 1) | Accuracy | Weighted Avg F1-Score |
# |---------|---------------------|------------------|---------------------|---------------------|------------------|---------------------|----------|----------------------|
# | Original| 1.00               | 1.00           | 1.00              | 0.98               | 0.69            | 0.81               | 1.00   | 1.00                |
# | SMOTE | 1.00              | 1.00           | 1.00              | 0.36               | 0.80            | 0.49               | 1.00    | 1.00                |
# | RUS | 1.00              | 0.97           | 0.99              | 0.05               | 0.89              | 0.09               | 0.97   | 0.98                |

# %% [markdown]
# ACCURACY COMPARISON PLOT

# %%
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

# Define evaluation metrics for each dataset
accuracy = [accuracy_score(y_test, y_pred_binary), 
            accuracy_score(y_test, y_pred_smote_binary), 
            accuracy_score(y_test, y_pred_rus_binary)]

# Define labels for each dataset
labels = ['Original', 'SMOTE', 'RUS']

# Make the plot
bars = plt.bar(labels, accuracy, color=['blue', 'orange', 'green'])

# Annotate the bars with accuracy scores
for bar in bars:
    height = bar.get_height()
    plt.annotate(f'{height:.3f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),  # 3 points vertical offset
                 textcoords="offset points",
                 ha='center', va='bottom')
    
# Add labels and title
plt.xlabel('Dataset')
plt.ylabel('Accuracy')
plt.title('Accuracy Comparison Across Datasets')

# Show the plot
plt.show()


# %% [markdown]
# PRECISION, RECALL AND F1-SCORE COMPARISON PLOT

# %%
import matplotlib.pyplot as plt
import numpy as np

# Define evaluation metrics for each dataset
precision = [precision_score(y_test, y_pred_binary), 
             precision_score(y_test, y_pred_smote_binary), 
             precision_score(y_test, y_pred_rus_binary)]

recall = [recall_score(y_test, y_pred_binary), 
          recall_score(y_test, y_pred_smote_binary), 
          recall_score(y_test, y_pred_rus_binary)]

f1 = [f1_score(y_test, y_pred_binary), 
      f1_score(y_test, y_pred_smote_binary), 
      f1_score(y_test, y_pred_rus_binary)]

# Define labels for each dataset
labels = ['Original', 'SMOTE', 'RUS']

# Set width of bar
bar_width = 0.25

# Set position of bars on X axis
r1 = np.arange(len(precision))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

# Make the plot
plt.bar(r1, precision, color='b', width=bar_width, edgecolor='grey', label='Precision')
plt.bar(r2, recall, color='g', width=bar_width, edgecolor='grey', label='Recall')
plt.bar(r3, f1, color='r', width=bar_width, edgecolor='grey', label='F1 Score')

# Add numerical scores on top of each bar
for i in range(len(precision)):
    plt.text(r1[i], precision[i], '{:.2f}'.format(precision[i]), ha='center', va='bottom')
    plt.text(r2[i], recall[i], '{:.2f}'.format(recall[i]), ha='center', va='bottom')
    plt.text(r3[i], f1[i], '{:.2f}'.format(f1[i]), ha='center', va='bottom')

# Add xticks on the middle of the group bars
plt.xlabel('Dataset')
plt.ylabel('Scores')
plt.xticks([r + bar_width for r in range(len(precision))], labels)


# Create legend & Show graphic
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.title('XGBoost Model Precision, Recall and F1-Score Comparison in Predicting Class 1')
plt.show()


# %% [markdown]
# CONFUSION MATRIX USING ALL DATASET

# %% [markdown]
# ![1_jMs1RmSwnYgR9CsBw-z1dw.png](data:image/png;base64,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)

# %%
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Define function to plot confusion matrix
def plot_confusion_matrix(ax, cm, title):
    sns.heatmap(cm, annot=True, cmap='Blues', fmt='g', ax=ax)
    ax.set_xlabel('Predicted Label')
    ax.set_ylabel('True Label')
    ax.set_title(title)

# Original Data
cm_original = confusion_matrix(y_test, y_pred_binary)

# SMOTE Data
cm_smote = confusion_matrix(y_test, y_pred_smote_binary)

# RUS Data
cm_rus = confusion_matrix(y_test, y_pred_rus_binary)

# Plotting
fig, axes = plt.subplots(1, 3, figsize=(20, 5))  # One row, three columns

plot_confusion_matrix(axes[0], cm_original, title='Original Data')
plot_confusion_matrix(axes[1], cm_smote, title='SMOTE Data')
plot_confusion_matrix(axes[2], cm_rus, title='RUS Data')

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()

# %% [markdown]
# AUC-ROC  USING ALL DATASET

# %%
from sklearn.metrics import roc_curve, auc, classification_report
import matplotlib.pyplot as plt

# Function to train the model and get predictions
def train_and_predict(X_train, y_train, X_test, params, num_rounds=100):
    dtrain = xgb.DMatrix(X_train, label=y_train)
    dtest = xgb.DMatrix(X_test)
    model = xgb.train(params, dtrain, num_rounds)
    y_pred = model.predict(dtest)
    return y_pred

# Training parameters
params = {
    'objective': 'binary:logistic',
    'eval_metric': 'logloss',
    'eta': 0.1,
    'max_depth': 6,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
    'seed': 42
}

# Train and predict for each dataset
y_pred_original = train_and_predict(X_train, y_train, X_test, params)
y_pred_smote = train_and_predict(X_train_smote, y_train_smote, X_test, params)
y_pred_rus = train_and_predict(X_train_rus, y_train_rus, X_test, params)

# Compute ROC curve and ROC area for each dataset
fpr_original, tpr_original, _ = roc_curve(y_test, y_pred_original)
roc_auc_original = auc(fpr_original, tpr_original)

fpr_smote, tpr_smote, _ = roc_curve(y_test, y_pred_smote)
roc_auc_smote = auc(fpr_smote, tpr_smote)

fpr_rus, tpr_rus, _ = roc_curve(y_test, y_pred_rus)
roc_auc_rus = auc(fpr_rus, tpr_rus)

# Plot all ROC curves on the same plot
plt.figure()
plt.plot(fpr_original, tpr_original, color='blue', lw=2, label='Original (AUC = %0.4f)' % roc_auc_original)
plt.plot(fpr_smote, tpr_smote, color='green', lw=2, label='SMOTE (AUC = %0.4f)' % roc_auc_smote)
plt.plot(fpr_rus, tpr_rus, color='red', lw=2, label='RUS (AUC = %0.4f)' % roc_auc_rus)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.show()

# %%
#!pip install shap


# %% [markdown]
# 4.4 SHAP USING ORIGINAL DATASET

# %%
# Record resource usage before training
cpu_before = psutil.cpu_percent()
memory_before = psutil.virtual_memory().used
start_time = time.time()

import shap
# Initialize the SHAP explainer with the XGBoost model and the training data for the original dataset
explainer_original = shap.Explainer(model, X_train)

# Calculate SHAP values for the test data for the original dataset
shap_values_original = explainer_original.shap_values(X_test)

# Visualize the SHAP values for the original dataset
shap.summary_plot(shap_values_original, X_test)

# Record resource usage after training
end_time = time.time()
cpu_after = psutil.cpu_percent()
memory_after = psutil.virtual_memory().used

# Calculate execution time and resource usage changes
execution_time_xgb = end_time - start_time
cpu_usage_change = cpu_after - cpu_before
memory_usage_change = memory_after - memory_before

print(f"Execution Time SHAP for Original Dataset: {execution_time_xgb:.4f} seconds")
print(f"CPU usage change: {cpu_usage_change}%")
print(f"Memory usage change: {memory_usage_change} bytes")

# %%
import shap
import matplotlib.pyplot as plt

# Calculate SHAP values for the test data for the original dataset
shap_values_original = explainer_original.shap_values(X_test)

# Plot the bar plot of SHAP values for each feature for the original dataset
shap.summary_plot(shap_values_original, X_test, plot_type="bar")
plt.show()


# %% [markdown]
# - High Impact Features:
# 
# V4, V14, V8, and V19 stand out as the most influential features, exhibiting large positive and negative SHAP values.
# These features likely play a significant role in driving the model's predictions, with their presence or absence having a substantial effect on the output.
# 
# - Moderate Impact Features:
# 
# Features like V18 show moderate positive and negative SHAP values, suggesting they contribute to the model's decision-making process to some extent, but not as prominently as the high impact features.
# 
# - Low Impact Features:
# 
# A large number of features, including scaled_amount, V12, V17, V26, V11, V23, V3, V10, V22, V20, V24, V13, V16, V7, and V28, have relatively small SHAP values.
# These features likely have minimal influence on the model's output and may not be as valuable in predicting the target variable.

# %% [markdown]
# 4.5 SHAP USING SMOTE DATASET

# %%
# Record resource usage before training
cpu_before = psutil.cpu_percent()
memory_before = psutil.virtual_memory().used
start_time = time.time()

# Initialize the SHAP explainer with the XGBoost model and the training data for the SMOTE-resampled dataset
explainer_smote = shap.Explainer(model_smote, X_train_smote)

# Calculate SHAP values for the test data for the SMOTE-resampled dataset
shap_values_smote = explainer_smote.shap_values(X_test)

# Visualize the SHAP values for the SMOTE-resampled dataset
shap.summary_plot(shap_values_smote, X_test)

# Record resource usage after training
end_time = time.time()
cpu_after = psutil.cpu_percent()
memory_after = psutil.virtual_memory().used

# Calculate execution time and resource usage changes
execution_time_xgb = end_time - start_time
cpu_usage_change = cpu_after - cpu_before
memory_usage_change = memory_after - memory_before

print(f"Execution Time SHAP for SMOTE Dataset: {execution_time_xgb:.4f} seconds")
print(f"CPU usage change: {cpu_usage_change}%")
print(f"Memory usage change: {memory_usage_change} bytes")

# %%
# Calculate SHAP values for the test data for the SMOTE-resampled dataset
shap_values_smote = explainer_smote.shap_values(X_test)

# Plot the bar plot of SHAP values for each feature for the SMOTE-resampled dataset
shap.summary_plot(shap_values_smote, X_test, plot_type="bar")
plt.show()


# %% [markdown]
# - High Impact Features:
# 
# V14 stands out as the most influential feature, exhibiting the largest positive and negative SHAP values as well as the longest bar.
# Other features like V4, V12, V10, V11, and V8 also show relatively high positive and negative SHAP values and longer bars.
# These features likely play a significant role in driving the model's predictions and have a substantial impact on the output.
# 
# - Moderate Impact Features:
# 
# Features such as V18, V1, V7, and V3 display moderate positive and negative SHAP values and bar lengths.
# These features contribute to the model's decision-making process to some extent but not as prominently as the high impact features.
# 
# - Low Impact Features:
# 
# A number of features, including V28, V27, V16, V24, V25, V19, and V2, exhibit relatively small SHAP values and shorter bars.
# These features likely have minimal influence on the model's output and may not be as valuable in predicting the target variable for the SMOTE-resampled dataset.

# %% [markdown]
# 4.6 SHAP USING RUS DATASET

# %%
# Record resource usage before training
cpu_before = psutil.cpu_percent()
memory_before = psutil.virtual_memory().used
start_time = time.time()

# Initialize the SHAP explainer with the XGBoost model and the training data for the RUS-resampled dataset
explainer_rus = shap.Explainer(model_rus, X_train_rus)

# Calculate SHAP values for the test data for the RUS-resampled dataset
shap_values_rus = explainer_rus.shap_values(X_test)

# Visualize the SHAP values for the RUS-resampled dataset
shap.summary_plot(shap_values_rus, X_test)

# Record resource usage after training
end_time = time.time()
cpu_after = psutil.cpu_percent()
memory_after = psutil.virtual_memory().used

# Calculate execution time and resource usage changes
execution_time_xgb = end_time - start_time
cpu_usage_change = cpu_after - cpu_before
memory_usage_change = memory_after - memory_before

print(f"Execution Time SHAP for RUS Dataset: {execution_time_xgb:.4f} seconds")
print(f"CPU usage change: {cpu_usage_change}%")
print(f"Memory usage change: {memory_usage_change} bytes")

# %%
# Calculate SHAP values for the test data for the RUS-resampled dataset
shap_values_rus = explainer_rus.shap_values(X_test)

# Plot the bar plot of SHAP values for each feature for the RUS-resampled dataset
shap.summary_plot(shap_values_rus, X_test, plot_type="bar")
plt.show()


# %% [markdown]
# - High Impact Features:
# 
# V14 stands out as the most influential feature, exhibiting the largest positive and negative SHAP values as well as the longest bar.
# Other features like V4, V12, V10, V11, and V19 also show relatively high positive and negative SHAP values and longer bars.
# These features likely play a significant role in driving the model's predictions and have a substantial impact on the output.
# 
# - Moderate Impact Features:
# 
# Features such as V8, V7, V17, and V16 display moderate positive and negative SHAP values and bar lengths.
# These features contribute to the model's decision-making process to some extent but not as prominently as the high impact features.
# 
# - Low Impact Features:
# 
# A number of features, including V23, V15, V24, V21, V9, V18, and V6, exhibit relatively small SHAP values and shorter bars.
# These features likely have minimal influence on the model's output and may not be as valuable in predicting the target variable for the RUS dataset.

# %%
# After process
cpu_after = psutil.cpu_percent()
memory_after = psutil.virtual_memory().used
 
print(f"CPU usage change: {cpu_after - cpu_before}%")
print(f"Memory usage change: {memory_after - memory_before} bytes")

# %% [markdown]
# 4.7 AUPRC USING ORIGINAL DATASET

# %%
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, auc

# Function to plot the Precision-Recall Curve and calculate AUPRC
def plot_auprc(y_test, y_pred_proba, title):
    precision, recall, _ = precision_recall_curve(y_test, y_pred_proba)
    auprc = auc(recall, precision)
    plt.plot(recall, precision, marker='.')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title(f'{title} (AUPRC = {auprc:.4f})')
    plt.show()

# For the original dataset
y_pred_proba_original = model.predict(dtest)
plot_auprc(y_test, y_pred_proba_original, "Original Dataset")

# %% [markdown]
# - High Precision: The curve starts at a high precision of 1.0, indicating that the model has a high accuracy in identifying fraud cases with minimal false positives at the beginning.
# - Recall Decrease: As recall increases, precision starts to drop, indicating that as the model tries to identify more fraud cases (increasing recall), it also starts to make more mistakes, reducing precision.
# - AUPRC of 0.8214: This value indicates a good balance between precision and recall, showing that the model performs well in distinguishing between fraud and genuine transactions.

# %% [markdown]
# 4.8 AUPRC USING SMOTE DATASET

# %%
# For the SMOTE dataset
y_pred_proba_smote = model_smote.predict(dtest_smote)
plot_auprc(y_test, y_pred_proba_smote, "SMOTE Dataset")

# %% [markdown]
# - The curve shows a similar pattern to the original dataset, but with slightly lower overall performance.
# - SMOTE helps to address the class imbalance, which is crucial in datasets with few positive samples (fraud cases). However, the introduction of synthetic data might lead to a few more false positives, impacting precision slightly.

# %% [markdown]
# 4.9 AUPRC USING RUS DATASET

# %%
# For the RUS dataset
y_pred_proba_rus = model_rus.predict(dtest_rus)
plot_auprc(y_test, y_pred_proba_rus, "RUS Dataset")

# %% [markdown]
# - The precision-recall curve for the RUS dataset shows more fluctuation, indicating less stability in performance.
# - RUS can be effective in situations where you want to reduce the number of majority class examples to balance the dataset. However, this can lead to a loss of information and a decrease in the model's ability to correctly identify fraud cases, as reflected by the lower AUPRC.

# %% [markdown]
# Summary:
# - Original Dataset: Shows the best balance with an AUPRC of 0.8214, indicating good model performance without any resampling techniques.
# - SMOTE Dataset: Slightly lower performance (AUPRC of 0.8036) but helps in addressing class imbalance, improving recall at the cost of some precision.
# - RUS Dataset: The lowest performance (AUPRC of 0.7348) with more fluctuation, suggesting a loss of valuable information due to undersampling of the majority class.

# %% [markdown]
# 5.0 AUPRC FOR ALL THREE DATASET

# %%
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, auc

# Function to plot the Precision-Recall Curve and calculate AUPRC
def plot_auprc(y_test, y_pred_proba, title):
    precision, recall, _ = precision_recall_curve(y_test, y_pred_proba)
    auprc = auc(recall, precision)
    plt.plot(recall, precision, marker='.', label=f'{title} (AUPRC = {auprc:.4f})')

# For the original dataset
y_pred_proba_original = model.predict(dtest)
plot_auprc(y_test, y_pred_proba_original, "Original Dataset")

# For the SMOTE dataset
y_pred_proba_smote = model_smote.predict(dtest_smote)
plot_auprc(y_test, y_pred_proba_smote, "SMOTE Dataset")

# For the RUS dataset
y_pred_proba_rus = model_rus.predict(dtest_rus)
plot_auprc(y_test, y_pred_proba_rus, "RUS Dataset")

plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend()
plt.show()


# %% [markdown]
# Save Model

# %%
import pickle

with open('model.pkl', 'wb') as file:
    pickle.dump(model_rus, file)

# %%
import pickle

with open('scaler.pkl', 'wb') as file:
    pickle.dump(scaler, file)


# %%
import xgboost as xgb

feature_importance = model_rus.get_score(importance_type='weight')
print(feature_importance)



