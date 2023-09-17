import pandas as pd
from datetime import date
from datetime import datetime

input_file = "/Dataset_-_CBRE_Challenge_-_HackSMU_2023.csv"

df = pd.read_csv(input_file, header=0)
new_stuff = []
# elevator_stuff = []
# plumbing_system_stuff = []
# fire_alarm_stuff = []
# hvac_stuff = []
# electrical_panel_stuff = []

for i in range(500):
    a_type = 0
    if df.loc[i, "Asset Type"] == "Elevator":
        a_type = 1
    if df.loc[i, "Asset Type"] == "Plumbing System":
        a_type = 2
    if df.loc[i, "Asset Type"] == "Fire Alarm":
        a_type = 3
    if df.loc[i, "Asset Type"] == "HVAC":
        a_type = 4
    if df.loc[i, "Asset Type"] == "Electrical Panel":
        a_type = 5

    install_date = df.loc[i, "Installation Date"].split("/")[::-1]

    service_date = df.loc[i, "Last Serviced Date"].split("/")[::-1]

    a_ops = df.loc[i, "Operational Time (hrs)"]
    a_work = df.loc[i, "Work Orders"]
    a_repairs = df.loc[i, "Repairs"]
    # print(r_[1], r[1])
    a_dur = date(int(service_date[0]), int(service_date[2]), int(service_date[1])) - date(int(install_date[0]),
                                                                                          int(install_date[2]),
                                                                                          int(install_date[1]))

    d1 = int(str(a_dur).split(" day")[0])
    if d1 < 0:
        continue

    # match a_type:
    new_stuff.append(
        {"Asset Type": a_type, "Operation Time (hrs)": a_ops, "Work Orders": a_work, "Duration": d1,
         "Repairs": a_repairs})

    # case 1:
    #     elevator_stuff.append(
    #         {"Asset Type": a_type, "Operation Time (hrs)": a_ops, "Work Orders": a_work, "Duration": d1,
    #          "Repairs": a_repairs})
    #
    # case 2:
    #     plumbing_system_stuff.append(
    #         {"Asset Type": a_type, "Operation Time (hrs)": a_ops, "Work Orders": a_work, "Duration": d1,
    #          "Repairs": a_repairs})
    #
    # case 3:
    #     fire_alarm_stuff.append(
    #         {"Asset Type": a_type, "Operation Time (hrs)": a_ops, "Work Orders": a_work, "Duration": d1,
    #          "Repairs": a_repairs})
    #
    # case 4:
    #     hvac_stuff.append(
    #         {"Asset Type": a_type, "Operation Time (hrs)": a_ops, "Work Orders": a_work, "Duration": d1,
    #          "Repairs": a_repairs})
    #
    # case 5:
    #     electrical_panel_stuff.append(
    #         {"Asset Type": a_type, "Operation Time (hrs)": a_ops, "Work Orders": a_work, "Duration": d1,
    #          "Repairs": a_repairs})

# df["Time to Servicing"] = delta

# print(df["Installation Date"])
r = pd.DataFrame.from_dict(new_stuff)
# writing into the file
r.to_csv("C:/Users/Andi/PycharmProjects/hackathon_2023/RefinedDataset.csv", index=False)

# elevator_ = pd.DataFrame.from_dict(elevator_stuff)
# plumbing_system_ = pd.DataFrame.from_dict(plumbing_system_stuff)
# fire_alarm_ = pd.DataFrame.from_dict(fire_alarm_stuff)
# hvac_ = pd.DataFrame.from_dict(hvac_stuff)
# electrical_panel_ = pd.DataFrame.from_dict(electrical_panel_stuff)

# elevator_.to_csv("C:/Users/Andi/PycharmProjects/hackathon_2023/ElevatorDataset.csv", index=False)
# plumbing_system_.to_csv("C:/Users/Andi/PycharmProjects/hackathon_2023/PlumbingSystemDataset.csv", index=False)
# fire_alarm_.to_csv("C:/Users/Andi/PycharmProjects/hackathon_2023/FireAlarmDataset.csv", index=False)
# hvac_.to_csv("C:/Users/Andi/PycharmProjects/hackathon_2023/HVACDataset.csv", index=False)
# electrical_panel_.to_csv("C:/Users/Andi/PycharmProjects/hackathon_2023/ElectricalPanelDataset.csv", index=False)
