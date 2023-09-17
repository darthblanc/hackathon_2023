import datetime

from predicitve_analysis import lobby, convert_asset


class interface:
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


s = interface(datetime.datetime.strptime("10/10/11", "%m/%d/%y"), "Elevator", 20032, 3, 4)
print(s.get_servicing_update())
