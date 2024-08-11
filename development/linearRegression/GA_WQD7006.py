# %% [markdown]
# # WQD 7006 GROUP ASSIGNMENT: CREDIT CARD FRAUD DETECTION

# %% [markdown]
# ![grp.png](data:image/png;base64,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)

# %%
# from google.colab import drive
# drive.mount('/content/drive')

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
# df = pd.read_csv('/content/drive/MyDrive/WQD7006 ML/Group 19 Group Assignment ML/creditcard.csv')
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
#pip install missingno

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

# Plot histograms for each column except 'Time' and 'class'
features = df.columns.drop(['Time', 'class'])

# Create a histogram for each feature
for i, feature in enumerate(features):
    plt.subplot(10, 3, i + 1)
    df[feature].hist(bins=50, alpha=0.7)
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
# Creating factors dataset, X
X = df.drop('class', axis = 1)

# Creating target dataset, y
y = df['class']
X.head()

# %%
#pip install imblearn

# %%
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

# %%
# Split the dataset into training (80%) and testing sets (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the data
# to standardize the features by removing the mean and scaling to unit variance
scaler = StandardScaler()

# fit_transform: Learn the parameters and apply the transformation to new data
X_train_scaled = scaler.fit_transform(X_train) # variable train test dataset after scaled

# transform: Apply the learned transformation to new data
X_test_scaled = scaler.transform(X_test) #variable test  dataset after scaled

# %%
X_train.head()

# %%
y_train.head()

# %%
X_test.head()

# %%
y_test.head()

# %%
X_test_scaled

# %% [markdown]
# ### 3.2 Oversampling via SMOTE

# %%
# Apply SMOTE
smote = SMOTE(sampling_strategy='minority', random_state=42)

#synthetic data X_train_smote and y_train_smote
X_train_smote, y_train_smote = smote.fit_resample(X_train_scaled, y_train) 

# %%
X_train_smote

# %%
y_train_smote.head()

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
X_train_rus, y_train_rus = rus.fit_resample(X_train_scaled, y_train)

# %%
X_train_rus

# %%
y_train_rus.head()

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

# %% [markdown]
# # 4.0 Machine Learning
# 

# %% [markdown]
# ## 4.1 Logistic Regression

# %%
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve, roc_auc_score

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# %%
# Define a list to store confusion matrices
confusion_matrices = []

# Define lists to store classification reports
classification_reports = {}

# Define lists to store AUC-ROC values
auc_roc_scores = []

# Define labels for the models
model_labels = ["Normalized Data", "Normalized + SMOTE Data", "Normalized + RUS Data"]

# %%
# Define the datasets and their corresponding names
datasets = [(X_train_scaled, y_train, "Normalized Data"),
            (X_train_smote, y_train_smote, "Normalized + SMOTE Data"),
            (X_train_rus, y_train_rus, "Normalized + RUS Data")]



# %%
# Initialize lists to store AUC-ROC scores and confusion matrices
auc_roc_scores = []
confusion_matrices = []
classification_reports = {}

# %%

# Loop through each dataset, train Logistic Regression, and evaluate performance
for X_train, y_train, data_name in datasets:
    # Train Logistic Regression
    logreg = LogisticRegression(random_state=42)
    logreg.fit(X_train, y_train)

    # Predict using the trained model
    y_pred = logreg.predict(X_test_scaled)

    # Predict probabilities using the trained model
    y_pred_proba = logreg.predict_proba(X_test_scaled)[:, 1]

    # Calculate fpr, tpr, and AUC
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    auc = roc_auc_score(y_test, y_pred_proba)
    auc_roc_scores.append(auc)

    # Calculate the confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    confusion_matrices.append((data_name, cm))

    # Evaluate the performance and store the classification report
    report = classification_report(y_test, y_pred, output_dict=True)
    classification_reports[data_name] = report
    print(classification_reports[data_name])

    # Plot ROC curve
    plt.plot(fpr, tpr, label=f'{data_name} (AUC = {auc:.2f})')

# Plotting the diagonal line (random classifier)
plt.plot([0, 1], [0, 1], linestyle='--', color='black')

# Labeling the plot
plt.title('ROC Curve Comparison')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()

# Assigning the plot to a variable name
roc_curve_plot = plt.gcf()

# Show the plot
plt.show()

# Display AUC-ROC scores
for data_name, auc_roc in zip(model_labels, auc_roc_scores):
    print(f'AUC-ROC for {data_name}: {auc_roc:.3f}')



# %% [markdown]
# ## 4.1 Logistic regression evaluation
# 
# 

# %% [markdown]
# ### 4.1.1 Confusion Matrix

# %%
# Plotting confusion matrices
plt.figure(figsize=(15, 5))
for i, (data_name, cm) in enumerate(confusion_matrices, 1):
    plt.subplot(1, 3, i)
    sns.heatmap(cm, annot=True, cmap='Blues', fmt='d', cbar=False)
    plt.title(f'Confusion Matrix - {data_name}')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')

plt.tight_layout()
plt.show()

# %% [markdown]
# ### 4.1.2 Accuracy, Precision, Recall and F-1 Score

# %% [markdown]
# - **Precision (Class 0):** Measures the accuracy of the model in correctly predicting non-fraudulent (genuine) transactions among all transactions predicted as non-fraudulent.
# - **Recall (Class 0):** Calculates the proportion of actual non-fraudulent (Genuine) transactions that the model correctly identifies.
# - **F1-score (Class 0):** The harmonic mean of precision and recall for the negative class. It provides a balanced measure of a model's performance in predicting non-fraudulent transactions.
# - **Precision (Class 1):** Measures the accuracy of the model in correctly predicting fraudulent transactions among all transactions predicted as fraudulent.
# - **Recall (Class 1):** Calculates the proportion of actual fraudulent transactions that the model correctly identifies.
# - **F1-Score (Class 1):** The harmonic mean of precision and recall for the positive class. It provides a balanced measure of a model's performance in predicting fraudulent transactions.
# - **Accuracy:** the overall correctness of the model across both classes. It measures the proportion of correctly classified transactions (both fraudulent and non-fraudulent) out of all transactions.
# - **Weighted Avg F1-Score:** The weighted average F1-score considers the F1-score of each class weighted by the number of true instances for each class. It provides a comprehensive measure of the model's performance across both classes while accounting for class imbalance.
# 
# 
# | Model   | Precision (Class 0) | Recall (Class 0) | F1-Score (Class 0) | Precision (Class 1) | Recall (Class 1) | F1-Score (Class 1) | Accuracy | Weighted Avg F1-Score |
# |---------|---------------------|------------------|---------------------|---------------------|------------------|---------------------|----------|----------------------|
# | Normalized| 0.999               | 0.9999           | 0.9996              | 0.889               | 0.533            | 0.667               | 0.9992   | 0.999                |
# | Normalized + SMOTE | 0.9998              | 0.9751           | 0.9873              | 0.054               | 0.889            | 0.101               | 0.975    | 0.986                |
# | Normalized + RUS | 0.9998              | 0.9679           | 0.9836              | 0.043               | 0.9              | 0.082               | 0.9678   | 0.982                |
# 
# 

# %%
# Extract performance metrics from classification reports
accuracy_scores = [classification_reports[model]['accuracy'] for model in model_labels]
precision_scores = [classification_reports[model]['1']['precision'] for model in model_labels]
recall_scores = [classification_reports[model]['1']['recall'] for model in model_labels]
f1_scores = [classification_reports[model]['1']['f1-score'] for model in model_labels]


# %%
plt.figure(figsize=(10, 6))
bars = plt.bar(model_labels, accuracy_scores, color='skyblue')
plt.title('Accuracy Comparison')
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.ylim(0.8, 1.0)
plt.xticks(rotation=45)

# Annotate the bars with accuracy scores
for bar in bars:
    height = bar.get_height()
    plt.annotate(f'{height:.3f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),  # 3 points vertical offset
                 textcoords="offset points",
                 ha='center', va='bottom')

plt.show()

# %%
# Plotting precision, recall, and F1-score comparison as bar charts
metrics_labels = ['Precision', 'Recall', 'F1-score']
metrics_values = [precision_scores, recall_scores, f1_scores]

plt.figure(figsize=(10, 6))
x = np.arange(len(model_labels))  # the label locations
width = 0.25  # the width of the bars

for i, (metric_label, metric_values) in enumerate(zip(metrics_labels, metrics_values)):
    bars = plt.bar(x + i * width, metric_values, width=width, label=metric_label)
    for bar in bars:
        height = bar.get_height()
        plt.annotate(f'{height:.2f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3),  # 3 points vertical offset
                     textcoords="offset points",
                     ha='center', va='bottom')

plt.xlabel('Models')
plt.ylabel('Scores')
plt.title('Precision, Recall, and F1-score Comparison')
plt.xticks(ticks=x + width, labels=model_labels)
plt.legend()
plt.ylim(0, 1.1)
plt.show()

# %% [markdown]
# **Normalized Data:**
# - This model seems to perform well across both classes (fraudulent and non-fraudulent transactions), suggesting that the normalized data alone provides a good basis for fraud prediction.
# - High precision, recall, and F1-score for both classes indicate that the model can identify fraudulent transactions accurately without significantly misclassifying non-fraudulent ones.
# - An AUC-ROC of 0.967 indicates that this model has good discriminatory power. It can distinguish between fraudulent and non-fraudulent transactions quite well.
# - This value suggests that the model performs well in ranking transactions by their likelihood of being fraudulent, with a high true positive rate and a low false positive rate.
# 
# **Normalized + SMOTE Data:**
# - SMOTE was done to deal with the class imabalnce identfied in the original data, which is common in fraud detection where fraudulent transactions are often rare compared to genuine ones.
# - While SMOTE improves recall for fraudulent transactions, the lower precision and F1-score for fraud detection in this model imply that it might be flagging more genuine transactions as fraudulent (increased false positives).
# - The higher AUC-ROC of 0.977 for this model compared to previous model suggests that SMOTE has improved the model's ability to differentiate between fraudulent and non-fraudulent transactions.
# - The higher AUC-ROC generally indicates better overall performance in terms of discrimination and ranking of transactions.
# 
# **Normalized + RUS Data:**
# - RUS was also done to balance the dataset by reducing the majority class (non-fraudulent transactions), which can also help in handling class imbalance.
# - Similar to SMOTE, this model shows improved recall for fraudulent transactions but at the cost of lower precision and F1-score for fraud detection, indicating a higher rate of false positives.
# - Similar to logistic regression done to normalized + SMOTE data, the AUC-ROC of 0.973 for this model indicates good discriminatory power. RUS has also helped improve the model's ability to rank transactions by their likelihood of being fraudulent.
# - However, it's worth noting that while AUC-ROC is higher than Logistic Regression done on Normalized data, the trade-offs in precision, recall, and F1-score (as discussed earlier) should also be considered.

# %% [markdown]
# ## 5.0 Explainable AI with SHAP

# %%
#pip install shap


# %%
import shap

shap.initjs()


# %%
for X_train, y_train, data_name in datasets:
    # Initialize the SHAP explainer with the Logistic Regression model
    explainer = shap.Explainer(logreg, X_train_scaled)

    # Calculate SHAP values for the test data
    shap_values = explainer.shap_values(X_test_scaled)

    print(data_name)
    # Calculate SHAP values for the test data
    shap_values = explainer.shap_values(X_test_scaled)

    # Plot the SHAP summary plot
    shap.summary_plot(shap_values, X_test_scaled)

    # Plot the bar plot of SHAP values for each feature for the original dataset
    shap.summary_plot(shap_values, X_test_scaled, plot_type="bar")


plt.show()




# %% [markdown]
# The SHAP summary plots visualizes the impact of different features on the linear regression model to predict fraud transactions.
# 
# - **Feature importance**: The y-axist lists the top 20 features out of the 28 features in the dataset. The x-axis shows SHAP values, which measure each feature's imapact on the model's prediction.
# - **Impact Direction**: Features with dots to the right of zero on the x-axis (positive SHAP values) increase the likelihood of fraud while those to the left (negative SHAP values) decrease it.
# - **Feature Value Color Coding**: The color of the dots represents the feature value, with pink indicating high values and blue indicating low values.
# - **Significant Features**: Features with a higher concentration of dots to the right suggest a stronger positive impact on predicting fraud (class 1), while features with dots concentrated more to the left suggest they contribute less or even negatively towards predicting fraud (class 0).
# 
# 

# %% [markdown]
# **Top 5 high impact features**
# | Normalized | Normalized + SMOTE | Normalized + RUS |
# |------------------|------------------|------------------|
# | Feature 4 | Feature 4 | Feature 4 | 
# | Feature 14 | Feature 14 | Feature 14 | 
# | Feature 12 | Feature 12 | Feature 12 | 
# | Feature 1| Feature 1 | Feature 1 | 
# | Feature 10 | Feature 10 | Feature 10| 
# 
# All datasets had the same ranking of features, where the top 5 impacting features are Feature 4, Feature 14, Feature 12, Feature 1 and Feature 10.
# 
# - The highest impact feature is Feature 4 :
#     - Many pink dots are far to the right, indicating high values.
#     - This feature significantly increases the prediction for fraud (class 1).
# - Meanwhile, feature 7 being one of the low impact feature:
#     - Blue dots are concentrated to the left.
#     - Low values of this feature decrease the prediction for fraud.

