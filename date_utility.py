from datetime import datetime

EPOCH_DATE = datetime(1970,1,1)
expiredate = datetime(2021,1,1)

date_format = '%Y-%m-%d'

def reverseDate(*args):
    '''Reverse Original date formart from
    yyyy-mm-dd to yyyy-dd-mm format'''
    newdata = args[0].split('-')
    newdate = '{0}-{1}-{2}'.format(newdata[0],newdata[1],newdata[2])
    return newdate

def stringToDateformat(*args):
    '''This access string with format 1/1/2000 
    and convert it to Date objecj
    Remember Default date format is Month/day/Year
    '''
    datestring = reverseDate(args[0])
    datestring = datetime.strptime(datestring, date_format)
    return datestring
    

def replaceFrontSlant(*args):
    '''Replace any String with "/" with "-" 
    and return a new format of the string'''
    return (args[0].replace('/', '-'))
    

def get_numberDays(objdate):
    '''This function return number of days
    elapsed since unix Epoch Year, given as (January 1, 1970)'''
    
    return (objdate - EPOCH_DATE).days
    
def getExpireStatus(*args):
    global expiredate
    stockAge = get_numberDays(args[0])
    actual_expired_date = get_numberDays(expiredate)

    if stockAge >= actual_expired_date:
        return False
    else:
        return True


# Test Case here
# print(stringToDateformat('11/9/2020'))
# current_row_date = stringToDateformat('6/6/2019')

# getExpireSatus(current_row_date)
