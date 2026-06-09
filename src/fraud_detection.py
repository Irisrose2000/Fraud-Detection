
import pandas as pd
#read the file
t = pd.read_csv("C:/Users/Aleena Johnson/Downloads/transactions.csv")
#structure and size of data
print("size of the data\n")
print(t.shape)
#column names
print("\n column names \n")
print(t.columns)
#sample data
print("\n first 5 columns\n")
print(t.head())
#data type
print("\n information of data\n")
t.info()
#count the values 
a=t['is_fraud'].value_counts()
print(a)
#convert the values into percentage 
b=t['is_fraud'].value_counts(normalize=True)*100
print(b)

#find the fraud pattern
c=t['fraud_pattern'].value_counts(dropna=False)
print(c)

#group the data to investigate them
y=t.groupby ('is_fraud')['amount'].describe()
print(y)

#count the foriegn transactions
f=t['is_foreign_txn'].value_counts(normalize=True)*100
print(f)

#to compare 2 categoricL values
p=pd.crosstab(t['is_foreign_txn'],t['is_fraud'],normalize='index')*100
print(p)

#calulate the device know
device = t['device_known'].value_counts(normalize=True)*100
print(device)

#compare the catgorical values
f=pd.crosstab(t['device_known'],t['is_fraud'],normalize='index')*100
print(f)

#card present data
print(t['card_present'].value_counts(normalize=True)*100)

print(pd.crosstab(t['card_present'],t['is_fraud'],normalize="index")*100)

#understanding ip risk score
print("ip risk scores \n")
print(t['ip_risk_score'].describe())

print(t.groupby('is_fraud')['ip_risk_score'].describe())

#understanding the velocity 1 hour data
print("velocity data\n")
print(t['velocity_1h'].describe())
print(t.groupby('is_fraud')['velocity_1h'].describe())

#understanding the time of last transcations
print("last transcations\n")
print(t['time_since_last_s'].describe())
print(t.groupby('is_fraud')['time_since_last_s'].describe())

#find the missing values
print(t.isnull().sum())

# if you dont want any column but dont want to delete from the original file
transaction_model=t.drop(columns=['transaction_id','account_id','timestamp'])
print("modified dataframe is ready")

print(transaction_model.shape)

#finalizing the x variable
x=transaction_model.drop(columns=['is_fraud','fraud_pattern'])
#finalizing the y variable the target variable
y=transaction_model['is_fraud']

#import the model
from sklearn.model_selection import train_test_split

#splitling of the data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42,stratify=y)

#check the shapes
print("x_train:",x_train.shape)
print("y_train:",y_train.shape)
print("x_test:",x_test.shape)
print("y_test:",y_test.shape)

print(y_train.value_counts(normalize=True)*100)
print(y_test.value_counts(normalize=True)*100)

#understnad the data type of the features selected for training
print(x_train.dtypes)

#check the unique values in the columns
print(x_train['merchant_country'].nunique())
print(x_train['mcc_code'].nunique())
print(x_train['merchant_category'].nunique())
print(x_train['day_of_week'].nunique())
print(x_train['device_type'].nunique())

#encoding of the columns
categorical_cols=['merchant_country','mcc_code','merchant_category','day_of_week','device_type']
x_trian_encoded = pd.get_dummies(x_train,columns=categorical_cols,drop_first=True)
x_test_encoded=pd.get_dummies(x_test,columns=categorical_cols,drop_first=True)
print(x_trian_encoded.shape)
print(x_test_encoded.shape)

# random forest
from sklearn.ensemble import RandomForestClassifier
rf_model=RandomForestClassifier(n_estimators=100,random_state=42)
rf_model.fit(x_trian_encoded ,y_train)
y_pred_rf=rf_model.predict(x_test_encoded)

#import the metrices
from sklearn.metrics import confusion_matrix,classification_report
print(confusion_matrix(y_test,y_pred_rf))
print(classification_report(y_test,y_pred_rf))

#feauture importance
feature_importance=pd.DataFrame({'Feature':x_trian_encoded.columns,
                                 'importance':rf_model.feature_importances_})
feature_importance=feature_importance.sort_values(by='importance',ascending=False)
print(feature_importance.head(10))

# roc-auc curve
from sklearn.metrics import roc_auc_score
y_prob=rf_model.predict_proba(x_test_encoded)[:,1]
auc=roc_auc_score(y_test,y_prob)
print("roc auc score",auc)

#training the model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=1000)
model.fit(x_trian_encoded,y_train)
y_pred=model.predict(x_test_encoded)


#calculate the accuracy score
from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y_test,y_pred)
print(accuracy)

#calulate the classification report and confusion matrix
from sklearn.metrics import confusion_matrix,classification_report
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

#balancing the dataset which is imbalance

balanced_model=LogisticRegression(class_weight='balanced',max_iter=1000)
balanced_model.fit(x_trian_encoded,y_train)
y_pred_balanced=balanced_model.predict(x_test_encoded)
print(confusion_matrix(y_test,y_pred_balanced))
print(classification_report(y_test,y_pred_balanced))


