from sqlalchemy import create_engine
import sqlite3
import pandas as pd
from IPython.display import display

# Creating the database
engine = create_engine('sqlite:///forty_yard_runs.db', echo=False)

# 2022 raw data for the first_runs_22 table
firsts_22 = {
    'ellie':[6.18],
    'keith':[4.80],
    'lawrence':[6.08],
    'sean':[7.68],
    'wade':[6.42],
    'noah':[5.90],
    'vaudree':[5.03],
    'nick':[5.23],
    'hayden':[7.47],
    'zach j':[5.15],
    'marshall':[5.57],
    'cole':[6.40],
    'elias':[4.98],
    'akeem':[21.92],
    'luke':[5.38],
    'cam':[5.90],
    'zach w':[5.38],
    'addi':[6.51],
    'bin':[4.87],
    'caleb':[4.93],
    'george':[5.33],
    'mallory':[6.80],
    'quay':[4.87],
    'clare':[5.90],
    'solo':[5.66],
    'bradley':[5.64],
    'carson':[5.22],
    'sincere':[5.69],
    'maddox':[5.15],
    'joe':[5.58],
    'anthony':[5.17],
    'paul':[5.46],
    'olivia':[6.63],
    'alyssa':[6.08]
    }

# Putting the 'firsts_22' raw data into lists
f_names_22 = []
first_run_times_22 = []
for i, j in firsts_22.items():
    f_names_22.append(i)
    if type(j) is list:
        for k in range(len(j)):
            first_run_times_22.append(j[k])
    else:
        first_run_times_22.append(j)

# first_runs_22 Pandas DataFrame
first_runs_22 = pd.DataFrame(list(zip(f_names_22, first_run_times_22)),\
    columns=['f_names_22', 'first_run_times_22'])

# Importing the first_runs_22 Pandas DataFrame into the database
# This will be our first_runs_22 table in the database
first_runs_22.to_sql('first_runs_22', engine, if_exists='replace', index=False)

# 2022 raw data for the subsequent_runs_22 table
subsequents_22 = {
    'carson':[5.43, 5.17],
    'vaudree':[4.63],
    'sean':[6.75],
    'bradley':[5.48],
    'keith':[4.70, 4.73],
    'mallory':[6.50],
    'solo':[5.80],
    'noah':[5.40],
    'maddox':[5.15, 5.06],
    'olivia':[6.15],
    'alyssa':[6.10],
    'paul':[5.42, 5.36],
    'joe':[5.44],
    'anthony':[5.03, 5.19]
    }

# Putting the 'subsequents_22' raw data into lists
s_names_22 = []
subsequent_run_times_22 = []
for i, j in subsequents_22.items():
    if type(j) is list:
        if len(j) > 1:
            for k in range(len(j)):
                s_names_22.append(i)
                subsequent_run_times_22.append(j[k])
        elif len(j) <= 1:
            for k in range(len(j)):
                s_names_22.append(i)
                subsequent_run_times_22.append(j[k])
    else:
        s_names_22.append(i)
        subsequent_run_times_22.append(j)
            

# subsequent_runs_22 Pandas DataFrame
subsequent_runs_22 = pd.DataFrame(list(zip(s_names_22,\
    subsequent_run_times_22)),\
    columns=('s_names_22', 'subsequent_run_times_22'))

# Importing the subsequent_runs_22 Pandas DataFrame into the database
# This will be our subsequent_runs_22 table in the database
subsequent_runs_22.to_sql('subsequent_runs_22', engine,\
    if_exists='replace', index=False)