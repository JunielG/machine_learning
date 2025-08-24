# GridSearch
param_grid = {
    'max_depth': [3, 5, 7, 10, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'criterion': ['gini', 'entropy']
}

dt = DecisionTreeClassifier(random_state=42)
grid_search = GridSearchCV(dt, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)


# RandomizedSearchCV
param_dist = {
    'max_depth': randint(3, 20),
    'min_samples_split': randint(2, 20),
    'min_samples_leaf': randint(1, 10),
    'criterion': ['gini', 'entropy']
}

random_search = RandomizedSearchCV(dt, param_dist, n_iter=100, cv=5)


dt2 = DecisionTreeClassifier(random_state=42)
grid_search = GridSearchCV(dt2, random_search, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)