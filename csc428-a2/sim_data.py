import pandas as pd
import numpy as np
import random as rd

DATASET = 500

CONTROL = 0.3
TREATMENT = 0.7

NO_ATT = 0.2
ATT = 0.8

START_1 = 0.05
START_2 = 0.25
START_3 = 0.4
START_4 = 0.3

data = pd.DataFrame({'received_email' : []})

# Generate the user assignment
control = [0]*int(DATASET*CONTROL)
treatment = [1]*int(DATASET*TREATMENT)
received_email = control + treatment
# Shuffle it
rd.shuffle(received_email)
data['received_email'] = received_email

# Generate if they attempted the homework or not
no_attempt = [0]*int(DATASET*NO_ATT)
attempt = [1]*int(DATASET*ATT)
attempted = no_attempt + attempt
# Shuffle it
rd.shuffle(attempted)
data['attempted'] = attempted

# Generate hours before deadline that sutdents started the homework
# People who started really early: between 65 to 80 hrs before
arr_start1 = np.random.randint(65, 80, int(DATASET*START_1)).tolist()
# People who started in the middle: between 40 to 64 hrs before
arr_start2 = np.random.randint(40, 65, int(DATASET*START_2)).tolist()
# Poeple who started late: between 20 to 39 hrs before 
arr_start3 = np.random.randint(20, 39, int(DATASET*START_3)).tolist()
# People who started really late: between 1 to 19 hrs before
arr_start4 = np.random.randint(1, 19, int(DATASET*START_4)).tolist()
start_hours = arr_start1 + arr_start2 + arr_start3 + arr_start4
rd.shuffle(start_hours)
data['start_hours'] = start_hours

data.to_csv("sim_data.csv")