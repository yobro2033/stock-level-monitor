import requests
import difflib
import time
from datetime import datetime
from dhooks import Webhook, Embed

url = "https://www.adidas.co.uk/api/products/GW1934/availability?sitePath=vi"
headers = {'User-Agent': 'Mozilla/5.0'}

hook = Webhook('https://discord.com/api/webhooks/806458887590248448/z4tRaaU73tCVmAVFNtwGzLwpZWlEltsQuM-1W4lGFa2u2vYaNyTVp2cPl_DI9OuXyc6O')

embed = Embed(
  description='SLIDE RESTOCKED',
  color=0x5CDBF0,
  timestamp='now'
  )

embed.add_field(name='Click this link', value='https://www.adidas.co.uk/en/yeezy-slide/GW1934.html')

print ("Start Monitoring "+url+ " @ "+ str(datetime.now()))

while True:
    response = requests.get(url, headers=headers)
    json_data = response.json()
    StockLevel = json_data['availability_status']
    StockLevel = str(StockLevel)
    if StockLevel == "NOT_AVAILABLE":
        print("No Change " + str(datetime.now()))
    else:
        print("Detected change @ " + str(datetime.now()))
        hook.send(embed=embed)
        time.sleep(0.5)