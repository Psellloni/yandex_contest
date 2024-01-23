import pandas as pd
import xgboost as xgb
from sklearn.metrics import roc_auc_score

df_train = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')

for val in df_train.drop(['target'], axis=1).columns:
  ser = df_train[val]
  ser2 = df_test[val]
  df_train[val] = df_train[val].apply(lambda x: (x - min(min(ser), min(ser2)))/ (max(max(ser), max(ser2)) - min(min(ser), min(ser2))))


for val in df_test.columns:
  ser = df_train[val]
  ser2 = df_test[val]
  df_test[val] = df_test[val].apply(lambda x: (x - min(min(ser), min(ser2)))/ (max(max(ser), max(ser2)) - min(min(ser), min(ser2))))

params = {
    'eta': 0.1,
    'max_depth': 3,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
    "device": "cuda",
    
    'gamma': 0,
    'lambda': 0,
    'alpha': 0,
    'min_child_weight': 0,
    
    'eval_metric': 'auc',
    'objective': 'binary:logistic' ,
    'booster': 'gbtree',
    'njobs': -1,
    'tree_method': 'approx',
}

res = xgb.cv(params, xgb.DMatrix(df_train.drop(['target'], axis=1), df_train['target']),
                  early_stopping_rounds=10, maximize=True, 
                  num_boost_round=10000, nfold=5, stratified=True)

russian_most_wanted = res['test-auc-mean'].argmax()
print('ROC_AUC: ', res.loc[russian_most_wanted]['test-auc-mean'], '+-', 
      res.loc[russian_most_wanted]['test-auc-std'], 'trees: ', russian_most_wanted)

model = xgb.train(params, xgb.DMatrix(df_train.drop(['target'], axis=1).values, df_train['target'], 
                    feature_names=list(df_train.drop(['target'], axis=1).columns)), 
                    num_boost_round=russian_most_wanted, maximize=True)

y_pred = model.predict(xgb.DMatrix(df_test.values, feature_names=list(df_test.columns)))

submission = pd.DataFrame(index=df_test.index, data=y_pred, columns=['target'])

submission.to_csv('answer.csv')