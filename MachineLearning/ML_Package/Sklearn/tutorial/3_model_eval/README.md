# 3. Model selection and evaluation

## Core Functions Review:

### 3.1 Cross Validation
* `cross_val_score(clf, X, y, cv=cv)`
* `preprocessing.StandardScaler().fit(X_train)`
* `kf = KFold(n_splits=n_splits)`
    * `kf.split(X)`
* `RepeatedKFold()`
* `StratifiedKFold()`
* `StratifiedShuffleSplit()`
* `GroupKFold()`
* `StratifiedGroupKFold()`

### 3.2 Tuning hyper-parameter
* `clf = GridSearchCV(estimator, param_grid)`
    * `clf.fit(X_train, y_train)`
* `random_search = RandomizedSearchCV(clf, param_dist, n_iter)`
    * `random_search.fit(X, y)`
* `gsh = HalvingGridSearchCV(clf, param_grid, factor=2)`
    * `gsh.fit(X, y)`