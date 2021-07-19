from date_utility import stringToDateformat, getExpireStatus

def extract_data_date(*args):
    data_date = args[0][0]
    current_data_date = stringToDateformat(data_date)
    status = getExpireStatus(current_data_date)
    
    return status
    

def data_bucket(label, datalist):
    '''Accept two parameter, 
    label = Column Label
    datalist = content
    '''
    final_data = []
    dataDict = dict()
    for data in datalist:
        dataDict[label[0]] = data[0]
        dataDict[label[1]] = data[1]
        dataDict[label[2]] = data[2]
        dataDict[label[3]] = data[3]
        dataDict[label[4]] = data[4]
        final_data.append(dataDict)
    return final_data    