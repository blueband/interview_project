from main import DATA_SOURCE
from csv_process import get_csvDdata
from other_utility import extract_data_date, data_bucket

# The file contain "use case" scenario test (Test was done with Pytest)

def test_get_csvDdata():
    # Source file should end with ".csv"
    data_source = DATA_SOURCE
    assert (data_source.endswith('csv')) == True 
    
def test_expiration_status():
    # To check expiration status
    # Ensure that the return object is bool 
    status = extract_data_date(['2017-04-04', '100940482', 'ogun', '23'])
    assert (isinstance(status, (bool))) == True

def test_check_finaldata_type():
    # Check that the final data consists of Python dictionary object
    label = ['date', 'sku', 'warehouse_location', 'quantity', 'obsolete']
    datalist = [['2021-01-02', '100940478', 'lagos', '23', False], ['2020-11-09', '100940479', 'lagos', '84', True]]
    data = data_bucket(label, datalist)
    
    assert (isinstance(data[0],(dict))) == True
    