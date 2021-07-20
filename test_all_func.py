from main import DATA_SOURCE
from csv_process import get_csvDdata
from other_utility import extract_data_date


def test_get_csvDdata():
    # Source file should end with ".csv"
    data_source = DATA_SOURCE
    assert (data_source.endswith('csv')) == True 
    
def test_expiration_status():
    # To check expiration status
    # Ensure that the return object is bool 
    status = extract_data_date(['2017-04-04', '100940482', 'ogun', '23'])
    assert (isinstance(status, (bool))) == True

def test_final_data_obj_isinatsnace():
    # Check that the final data is list object
    