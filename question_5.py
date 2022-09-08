import json
import datetime

f = open('question_5.json','r+')

data = json.load(f)

result = data

print("Payee ID")
print(data['payee']['id'])

for i in data['invoiceIds']:
    if '583' in i:
        print(i)

claimDatetime = data['claimDateTime']
fileDateTime = data['fileDateTime']
receivedDateTime = data['receivedDateTime']

result['claimDateTime'] = str(datetime.datetime.fromtimestamp(claimDatetime / 1e3))
result['fileDateTime'] = str(datetime.datetime.fromtimestamp(fileDateTime / 1e3))
result['receivedDateTime'] = str(datetime.datetime.fromtimestamp(receivedDateTime / 1e3))

with open("result.json", "w") as outfile:
    json.dump(result, outfile)

f.close()