import datetime
from os import environ
import logging
import requests
from predicitve_analysis import lobby, convert_asset

import datetime
from sklearn import linear_model, datasets
from sklearn.model_selection import train_test_split
# import matplotlib.pyplot as plt
# matplotlib inline
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
# from collections import Counter
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score


# import interface


class Interface:
    def __init__(self, date_in, asset_type, operation_time, work_orders, repairs, flag=0):
        self.date_in = date_in
        self.asset_type = asset_type
        self.operation_time = operation_time
        self.work_orders = work_orders
        self.repairs = repairs
        self.flag = flag
        self.algo = None

    def get_servicing_update(self):
        return self.request()

    def request(self):
        if self.flag == 1:
            return self.algo.predict({"Asset Type": convert_asset(self.asset_type),
                                      "Operation Time (hrs)": self.operation_time, "Work Orders": self.work_orders,
                                      "Repairs": self.repairs})
        else:
            date_out, flag, algo = lobby(self.date_in, self.asset_type, self.operation_time, self.work_orders,
                                         self.repairs)
            self.algo = algo
            self.flag = flag

        return date_out


def check_asset_in():
    asset_in = input("Input the asset here: ").lower()
    if asset_in not in {"elevator", "fire alarm", "plumbing system", "hvac", "electric panel"}:
        return check_asset_in()
    return asset_in


if __name__ == '__main__':
    in_ = input("Enter the date in MM/DD/YY format: ")
    asset_in = check_asset_in()
    operation_time_in = int(input("Enter the operation time: "))
    work_orders = int(input("Enter the number of work orders: "))
    repairs = int(input("Enter the number of repairs: "))

    s = Interface(datetime.datetime.strptime(in_, "%m/%d/%y"), asset_in, operation_time_in, work_orders, repairs)
    print(s.get_servicing_update())
