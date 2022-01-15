import requests

headers =  {
    'X-Tasktest-Token': 'f62cdf1e83bc324ba23aee3b113c6249'
}


def getChat(crmName, domain):
    r = requests.get(f'https://dev.wapp.im/v3/chat/spare?crm={crmName}&domain={domain}', headers=headers)
    if r.status_code == 200:
        items = r.json()
        if 'error_code' in items.keys():
            print(items['error_code'])
            return 
        if 'id' in items.keys() and 'token' in items.keys():
            _id = items['id']
            _token = items['token']
            return _id, _token
    
def getQRcode(id, token):
    r = requests.get(f'https://dev.wapp.im/v3/instance{id}/status?full=1&token={token}', headers=headers)
    if r.status_code == 200:
        items = r.json()
        if 'state' in  items.keys() and 'accountStatus' in items.keys():
            return items['state'], items['accountStatus'], items['qrCode']

        
def getStatus(id, token, phone):
    r = requests.get(f'https://dev.whatsapp.sipteco.ru/v3/instance{id}/isRegisteredUser?token={token}&phone={phone}', headers=headers)
    if r.status_code == 200:
        if r.text == 'false':
            print('Нет WhatsApp')
        else:
            print('Yes')
            
    
def sendMessage(id, token, phone, body):
    data = {
        'phone': phone,
        'body': body
    }
    r = requests.post(f'https://dev.whatsapp.sipteco.ru/v3/instance{id}/sendMessage?token={token}', data=data ,headers=headers)
    if r.status_code == 200:
        print('Успешно отправил')
    
    
def deleteChat(id, token, phone):
    r = requests.get(f'https://dev.whatsapp.sipteco.ru/v3/instance{id}/removeChat?token={token}&phone={phone}', headers=headers)
    if r.status_code == 200:
        print('Чат удален')

