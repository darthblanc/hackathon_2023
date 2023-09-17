import datetime

from sklearn import linear_model, datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
# matplotlib inline
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from collections import Counter
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score


# import interface

def load():
    input_file = "RefinedDataset.csv"

    df = pd.read_csv(input_file, header=0)

    # print(numpy_array) convert asset type to numbers X = pd.DataFrame(np.c_[df['Asset Type'], df['Installation Date'],
    # df['Operational Time (hrs)'], df['Work Orders'], df['Repairs']], columns = ['Asset Type', 'Installation Date',
    # 'Operational Time (hrs)', 'Work Orders', 'Repairs']) y = df['Last Serviced Date']
    X = pd.DataFrame(np.c_[df['Asset Type'], df['Operation Time (hrs)'], df['Work Orders'], df['Repairs']],
                     columns=['Asset Type', 'Operation Time (hrs)', 'Work Orders', 'Repairs'])
    y = df['Duration']

    return X, y
    # X = pd.DataFrame(np.c_[df['Asset Type'], df['Installation Date'], df['Operational Time (hrs)']],
    #                  columns=[df['Asset Type'], 'Installation Date', 'Operational Time (hrs)'])
    # y = df['Last Serviced Date']


def algorithm(X, y):
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=1000000000)
    # print(f'Number of y in the training set after splitting is {Counter(y_train)}')
    # print(f'Number of y in the testing set after splitting is {Counter(y_test)}')
    # print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
    # print("len(df): {}, len(X_train): {}, len(X_valid): {}, len(y_train): {}, len(y_valid): {}".format(len(df), len(X_train), len(X_test), len(y_train), len(y_test)))

    # plt.scatter(X['Asset Type'], y)
    # plt.show()
    # plt.close()
    #
    # plt.scatter(X['Operational Time (hrs)'], y)
    # plt.show()
    # plt.close()

    # regressor = linear_model.LinearRegression()
    # regressor = linear_model.BayesianRidge()
    # model = regressor.fit(X_train, y_train)
    #
    # print('Coefficient of determination:', model.score(X, y))
    # print('Intercept:', model.intercept_)
    # print('slope:', model.coef_)
    #
    # y_test_predict = regressor.predict(X_test)
    # # print('predicted response:', y_test_predict, sep='\n')
    #
    # rmse = (np.sqrt(mean_squared_error(y_test, y_test_predict)))
    # print(rmse)

    random_forest = RandomForestRegressor(max_depth=1010, n_estimators=100000, random_state=1000)
    random_forest.fit(X_train, y_train)

    return random_forest
    # print('predicted response:', y_test_predict, sep='\n')
    # root_mean_squared_error = np.sqrt(mean_squared_error(y_train, random_forest.predict(X_train)))
    # print(root_mean_squared_error)
    # print((np.abs(y_train)).mean())

    # cross_val_scores = cross_val_score(RandomForestRegressor(max_depth=10, n_estimators=100, random_state=1),
    #                                    X, y, scoring='neg_mean_squared_error', cv=5)
    # cross_val_scores = np.sqrt(np.abs(cross_val_scores))
    # print(cross_val_scores)
    # print("mean:", np.mean(cross_val_scores))


def calculate_next_service_date(date_in, y_result):
    return date_in + datetime.timedelta(days=y_result[0])


def convert_asset(asset_type):
    a_type = 0
    if asset_type == "Elevator":
        a_type = 1
    if asset_type == "Plumbing System":
        a_type = 2
    if asset_type == "Fire Alarm":
        a_type = 3
    if asset_type == "HVAC":
        a_type = 4
    if asset_type == "Electrical Panel":
        a_type = 5

    return a_type


def lobby(date_in, asset_type, operation_time, work_orders, repairs, algo=None):
    X, y = load()
    algo = algorithm(X, y)
    new = [{"Asset Type": convert_asset(asset_type), "Operation Time (hrs)": operation_time, "Work Orders": work_orders,
            "Repairs": repairs}]
    test = pd.DataFrame.from_dict(new)
    y_result = algo.predict(test)
    return calculate_next_service_date(date_in, y_result), 1, algo
