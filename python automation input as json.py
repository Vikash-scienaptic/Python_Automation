import json
from collections import OrderedDict


def py_automation(data):
    data = OrderedDict(data)

    key_remove = ["Customer","Work Phone","Balance Due","Amount","Last Payment Date","Next Due","Irregular Next Payment Date",
              "VIN","Employee Name","Payment Schedule","Address","VehYear","VehMake","VehModel","VehBody","Insu Cancellation Date",
              "DealerCode","TypeRepo","PaySharePer","PayShareBal","InterestPaySharePer","Principal Balance","DsaPrincipalBalance",
              "Date Sold","JointName","JointHomeNbr","JointCellNbr","JointAddress","JointCity","JointState","JointZipCode",
              "ResidualValue","MaturityDate","NbrPmtsRemaining"]
    data = dict([(key, val) for key, val in data.items() if key not in key_remove])
    data['Stock number'] = data.pop('Stock')
    data['name']=data.pop('Name')
    data['Home Phone']=data.pop('Home Phone')
    data['Cell Phone']=data.pop('Cell Phone')
    data['Past Due amount']=data.pop('Past Due')
    data['days late']=data.pop('of Days')
    data['portfolio'] = data.pop('Branch')
    data['City'] = data.pop('City')
    data['State'] = data.pop('State')
    data['Zip Code'] = data.pop('Zip Code')

    if data['Cell Phone'] in ['',None]:
        data['Cell Phone'] = data['Home Phone']

    if data['Cell Phone'] in ['',None]:
        data.pop('Cell Phone')

    del data['Home Phone']

    data['name'] = data['name'].split(' ')
    data['name'] = data['name'][1] + " " + data['name'][0] 
    data = json.dumps(data)
    return data

