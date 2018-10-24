import pandas as pd
import os


def read_results(path):
    data = pd.read_csv(os.path.join(path,"data.csv"),usecols=["MAP","Model","P10"])
    data_o = pd.read_csv(os.path.join(path,"data_o.csv"),usecols=["MAP","Model with Ouliers","P10"])
    data_sorted_P10 = pd.read_csv(os.path.join(path,"data_sorted_P10.csv"),usecols=["MAP","Model","P10"])
    data_o_sorted_P10 = pd.read_csv(os.path.join(path,"data_o_sorted_P10.csv"),usecols=["MAP","Model with Ouliers","P10"])
    data_sorted_Map = pd.read_csv(os.path.join(path,"data_sorted_Map.csv"),usecols=["MAP","Model","P10"])
    data_o_sorted_Map = pd.read_csv(os.path.join(path,"data_o_sorted_Map.csv"),usecols=["MAP","Model with Ouliers","P10"])
    
    return data,data_o,data_sorted_P10,data_o_sorted_P10,data_sorted_Map,data_o_sorted_Map