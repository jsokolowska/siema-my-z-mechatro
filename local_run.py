import pandas as pd

from sklearn.model_selection import RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data_path = "final_train.csv"
df = pd.read_csv(data_path, index_col=0)

params = {
    'C': [0.6, 0.7, 0.8, 0.9, 1.0],
    'penalty': ['l1', 'l2', 'elasticnet'],
    'tol': [1e-4, 1e-3],
    'solver': ['liblinear', 'saga', 'lbfgs'],
    'max_iter': [100, 200],
    'multi_class': ['ovr']
}

dropped_features = ['angle(X,gravityMean)', 'angle(tBodyAccJerkMean),gravityMean)',
                    'angle(tBodyAccMean,gravity)',
                    'angle(tBodyGyroJerkMean,gravityMean)',
                    'angle(tBodyGyroMean,gravityMean)',
                    'energy-mean()',
                    'fBodyAcc-energy()-X',
                    'fBodyAcc-entropy()-X',
                    'fBodyAcc-entropy()-Y',
                    'fBodyAcc-entropy()-Z',
                    'fBodyAcc-iqr()-X',
                    'fBodyAcc-iqr()-Y',
                    'fBodyAcc-iqr()-Z',
                    'fBodyAcc-kurtosis()-X',
                    'fBodyAcc-kurtosis()-Y',
                    'fBodyAcc-kurtosis()-Z',
                    'fBodyAcc-mad()-X',
                    'fBodyAcc-mad()-Z',
                    'fBodyAcc-main()-X',
                    'fBodyAcc-main()-Z',
                    'fBodyAcc-max()-X',
                    'fBodyAcc-maxInds-X',
                    'fBodyAcc-maxInds-Y',
                    'fBodyAcc-maxInds-Z',
                    'fBodyAcc-meanFreq()-X',
                    'fBodyAcc-min()-X',
                    'fBodyAcc-skewness()-X',
                    'fBodyAcc-skewness()-Y',
                    'fBodyAcc-skewness()-Z',
                    'fBodyAcc-sma()',
                    'fBodyAcc-std()-X',
                    'fBodyAcc-std()-Y',
                    'fBodyAcc-std()-Z',
                    'fBodyAccJerk-energy()-Y',
                    'fBodyAccJerk-entropy()-X',
                    'fBodyAccJerk-mad()-Z',
                    'fBodyAccJerk-max()-Z',
                    'fBodyAccJerk-maxInds-Y',
                    'fBodyAccJerk-maxInds-Z',
                    'fBodyAccJerk-min()-X',
                    'fBodyAccJerk-min()-Y',
                    'fBodyAccJerk-sma()',
                    'fBodyAccJerk-std()-X',
                    'fBodyAccJerk-std()-Z',
                    'fBodyAccMag-energy()',
                    'fBodyAccMag-entropy()',
                    'fBodyAccMag-iqr()',
                    'fBodyAccMag-kurtosis()',
                    'fBodyAccMag-mad()',
                    'fBodyAccMag-maxInds',
                    'fBodyAccMag-meanFreq()',
                    'fBodyAccMag-min()',
                    'fBodyAccMag-skewness()',
                    'fBodyAccMag-sma()',
                    'fBodyAccMag-std()',
                    'fBodyBodyAccJerkMag-kurtosis()',
                    'fBodyBodyAccJerkMag-maxInds',
                    'fBodyBodyAccJerkMag-meanFreq()',
                    'fBodyBodyAccJerkMag-skewness()',
                    'fBodyBodyGyroJerkMag-kurtosis()',
                    'fBodyBodyGyroJerkMag-maxInds',
                    'fBodyBodyGyroJerkMag-meanFreq()',
                    'fBodyBodyGyroJerkMag-skewness()',
                    'fBodyBodyGyroMag-kurtosis()',
                    'fBodyBodyGyroMag-maxInds',
                    'fBodyBodyGyroMag-meanFreq()',
                    'fBodyBodyGyroMag-skewness()',
                    'fBodyGyro-energy()-X',
                    'fBodyGyro-energy()-Y',
                    'fBodyGyro-energy()-Z',
                    'fBodyGyro-entropy()-X',
                    'fBodyGyro-entropy()-Y',
                    'fBodyGyro-iqr()-X',
                    'fBodyGyro-iqr()-Z',
                    'fBodyGyro-kurtosis()-X',
                    'fBodyGyro-kurtosis()-Y',
                    'fBodyGyro-kurtosis()-Z',
                    'fBodyGyro-mad()-X',
                    'fBodyGyro-mad()-Y',
                    'fBodyGyro-max()-X',
                    'fBodyGyro-max()-Y',
                    'fBodyGyro-max()-Z',
                    'fBodyGyro-maxInds-X',
                    'fBodyGyro-maxInds-Z',
                    'fBodyGyro-meanFreq()-Y',
                    'fBodyGyro-meanFreq()-Z',
                    'fBodyGyro-min()-X',
                    'fBodyGyro-skewness()-X',
                    'fBodyGyro-skewness()-Y',
                    'fBodyGyro-skewness()-Z',
                    'fBodyGyro-sma()',
                    'fBodyGyro-std()-X',
                    'fBodyGyro-std()-Y',
                    'fBodyGyro-std()-Z',
                    'shadow-gravity-angle()',
                    'subject',
                    'tBodyAcc-arCoeff()-X,2',
                    'tBodyAcc-arCoeff()-X,3',
                    'tBodyAcc-arCoeff()-X,4',
                    'tBodyAcc-arCoeff()-Y,2',
                    'tBodyAcc-arCoeff()-Y,3',
                    'tBodyAcc-arCoeff()-Y,4',
                    'tBodyAcc-arCoeff()-Z,3',
                    'tBodyAcc-arCoeff()-Z,4',
                    'tBodyAcc-correlation()-X,Y',
                    'tBodyAcc-correlation()-X,Z',
                    'tBodyAcc-correlation()-Y,Z',
                    'tBodyAcc-mean()-X',
                    'tBodyAcc-mean()-Y',
                    'tBodyAcc-mean()-Z',
                    'tBodyAccJerk-arCoeff()-X,2',
                    'tBodyAccJerk-arCoeff()-X,3',
                    'tBodyAccJerk-arCoeff()-X,4',
                    'tBodyAccJerk-arCoeff()-Y,2',
                    'tBodyAccJerk-arCoeff()-Y,3',
                    'tBodyAccJerk-arCoeff()-Y,4',
                    'tBodyAccJerk-arCoeff()-Z,2',
                    'tBodyAccJerk-arCoeff()-Z,3',
                    'tBodyAccJerk-arCoeff()-Z,4',
                    'tBodyAccJerk-correlation()-X,Y',
                    'tBodyAccJerk-correlation()-X,Z',
                    'tBodyAccJerk-correlation()-Y,Z',
                    'tBodyAccJerk-mean()-X',
                    'tBodyAccJerk-mean()-Y',
                    'tBodyAccJerk-mean()-Z',
                    'tBodyAccJerkMag-arCoeff()3',
                    'tBodyAccJerkMag-arCoeff()4',
                    'tBodyAccMag-arCoeff()3',
                    'tBodyAccMag-arCoeff()4',
                    'tBodyGyro-arCoeff()-X,2',
                    'tBodyGyro-arCoeff()-X,3',
                    'tBodyGyro-arCoeff()-Y,1',
                    'tBodyGyro-arCoeff()-Y,3',
                    'tBodyGyro-arCoeff()-Y,4',
                    'tBodyGyro-arCoeff()-Z,3',
                    'tBodyGyro-arCoeff()-Z,4',
                    'tBodyGyro-correlation()-X,Y',
                    'tBodyGyro-correlation()-X,Z',
                    'tBodyGyro-correlation()-Y,Z',
                    'tBodyGyro-low()-X',
                    'tBodyGyro-low()-Y',
                    'tBodyGyro-low()-Z',
                    'tBodyGyro-mean()-X',
                    'tBodyGyro-mean()-Y',
                    'tBodyGyro-mean()-Z',
                    'tBodyGyroJerk-arCoeff()-X,2',
                    'tBodyGyroJerk-arCoeff()-X,3',
                    'tBodyGyroJerk-arCoeff()-X,4',
                    'tBodyGyroJerk-arCoeff()-Y,2',
                    'tBodyGyroJerk-arCoeff()-Y,3',
                    'tBodyGyroJerk-arCoeff()-Y,4',
                    'tBodyGyroJerk-arCoeff()-Z,2',
                    'tBodyGyroJerk-arCoeff()-Z,3',
                    'tBodyGyroJerk-arCoeff()-Z,4',
                    'tBodyGyroJerk-correlation()-X,Y',
                    'tBodyGyroJerk-correlation()-X,Z',
                    'tBodyGyroJerk-correlation()-Y,Z',
                    'tBodyGyroJerk-mean()-X',
                    'tBodyGyroJerk-mean()-Y',
                    'tBodyGyroJerk-mean()-Z',
                    'tBodyGyroJerkMag-arCoeff()1',
                    'tBodyGyroJerkMag-arCoeff()2',
                    'tBodyGyroJerkMag-arCoeff()3',
                    'tBodyGyroJerkMag-arCoeff()4',
                    'tBodyGyroMag-arCoeff()1',
                    'tBodyGyroMag-arCoeff()2',
                    'tBodyGyroMag-arCoeff()3',
                    'tBodyGyroMag-arCoeff()4',
                    'tBodyGyroMag-entropy()',
                    'tGravityAcc-arCoeff()-X,1',
                    'tGravityAcc-arCoeff()-X,2',
                    'tGravityAcc-arCoeff()-X,3',
                    'tGravityAcc-arCoeff()-X,4',
                    'tGravityAcc-arCoeff()-Y,1',
                    'tGravityAcc-arCoeff()-Y,2',
                    'tGravityAcc-arCoeff()-Y,3',
                    'tGravityAcc-arCoeff()-Y,4',
                    'tGravityAcc-arCoeff()-Z,1',
                    'tGravityAcc-arCoeff()-Z,2',
                    'tGravityAcc-arCoeff()-Z,3',
                    'tGravityAcc-arCoeff()-Z,4',
                    'tGravityAcc-correlation()-X,Y',
                    'tGravityAcc-correlation()-X,Z',
                    'tGravityAcc-correlation()-Y,Z',
                    'tGravityAcc-energy()-X',
                    'tGravityAcc-energy()-Z',
                    'tGravityAcc-entropy()-X',
                    'tGravityAcc-entropy()-Y',
                    'tGravityAcc-entropy()-Z',
                    'tGravityAcc-iqr()-X',
                    'tGravityAcc-mad()-X',
                    'tGravityAcc-max()-X',
                    'tGravityAcc-mean()-X',
                    'tGravityAcc-min()-X',
                    'tGravityAcc-sma()',
                    'tGravityAcc-std()-X',
                    'tGravityAccMag-arCoeff()3',
                    'tGravityAccMag-arCoeff()4',
                    'tGravityAccMag-mad()',
                    'tGravityAccMag-sma()',
                    'void()']

clf = LogisticRegression(random_state=69)

X = df.drop("Activity", axis=1)
y = df["Activity"]
X = X.drop(dropped_features, axis=1)

X = X.fillna(X.mean())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=69)

scaler = StandardScaler()
X_train = pd.DataFrame(scaler.fit_transform(X_train.values), columns=X_train.columns, index=X_train.index)
X_test = pd.DataFrame(scaler.transform(X_test.values), columns=X_test.columns, index=X_test.index)

search = RandomizedSearchCV(estimator=clf, param_distributions=params, n_iter=100, cv=3, verbose=2, random_state=69,
                            n_jobs=-1)

search.fit(X_train, y_train)
print(search.best_estimator_.score(X_test, y_test))
print(search.best_params_)
