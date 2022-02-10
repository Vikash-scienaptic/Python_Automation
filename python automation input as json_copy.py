import json
from collections import OrderedDict


data={
  "Stock": 143921,
  "Customer": "B2020031009354910580",
  "Name": "CORTES IRVIN R",
  "Home Phone": "(589) 912-0504",
  "Work Phone": "(589) 912-0504",
  "Cell Phone": "(589) 912-0504",
  "Balance Due": "8,939.15",
  "Past Due": 798.93,
  "Amount": 178.26,
  "Last Payment Date": "29-12-2021",
  "Next Due": "06-11-2021",
  "Irregular Next Payment Date": "07-11-2021",
  "of Days": 63,
  "Employee Name": None,
  "Branch": "ACF",
  "Payment Schedule": "B",
  "Address": "635 83 ST, Apt. 48",
  "City": "MIAMI BEACH",
  "State": "FL",
  "Zip Code": 33141,
  "VIN": "JYARJ28E3LA005462",
  "VehYear": 2020,
  "VehMake": "YAMAHA",
  "VehModel": "YZF",
  "VehBody": "M-CYCLE",
  "Insu Cancellation Date": "07-07-2020",
  "DealerCode": "IND585",
  "TypeRepo": "String",
  "PaySharePer": 0,
  "PayShareBal": 0,
  "InterestPaySharePer": 0,
  "Principal Balance": "8,939.15",
  "DsaPrincipalBalance": "8,939.15",
  "Date Sold": "07-03-2020",
  "JointName": "String",
  "JointHomeNbr": "String",
  "JointCellNbr": "String",
  "JointAddress": "String",
  "JointCity": "String",
  "JointState": "String",
  "JointZipCode": "String",
  "ResidualValue": 0,
  "MaturityDate": "06-09-2025",
  "NbrPmtsRemaining": 101
}
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

data = py_automation(data)

print(data)
