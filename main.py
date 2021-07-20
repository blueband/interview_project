from csv_process import get_csvDdata
from other_utility import extract_data_date, data_bucket
import json
DATA_SOURCE = 'python_hands_on_dataset.csv'

# Load and read csv data from local Source
raw_data = get_csvDdata(DATA_SOURCE)

# Getting Column label and adding new column lanel to accomodate new column
hearder_label = raw_data[0]
hearder_label.append('obsolete')

global_container = []
for data in raw_data[1:]:
    print(data)
    status = extract_data_date(data)
    global_container.append([data[0], data[1], data[2], data[3], status])

final_data = (data_bucket(hearder_label, global_container))

# Writing data to json file
with open('databucket.json', 'w') as file:
    json.dump(final_data, file)
    print('Data save into json file successfully, Please, Check your working directory')
