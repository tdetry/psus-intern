import sklearn
from sklearn.datasets import make_regression
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold

X, y = make_regression(n_samples=1000, n_features=5, n_informative=5, n_targets=2, random_state=1, noise=0.5)

testRow, testVals = X[0], y[0]
print(testRow,'\n',testVals)

#yhat = model.predict([row])
#print(yhat[0])

models = [LinearRegression(), KNeighborsRegressor(), DecisionTreeRegressor()]

for m in models:
    print(m)
    model = m
    model.fit(X, y)
    cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
    # evaluate the model and collect the scores
    n_scores = cross_val_score(model, X, y, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1)
    # force the scores to be positive
    n_scores = np.absolute(n_scores)
    # summarize performance
    print('MAE: %.3f (%.3f)' % (np.mean(n_scores), np.std(n_scores)),'\n')

    preds = []
    
    for i in range(len(y)):
        row = X[i]
        yhat = model.predict([row])
        # summarize prediction
        pred = yhat[0]
        preds.append(pred)

    plt.scatter([np.abs(p[0]) - np.abs(u[0]) for p in preds for u in y],[np.abs(p[1]) - np.abs(u[1]) for p in preds for u in y],alpha=0.36)
    
    plt.show()