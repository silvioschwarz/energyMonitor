from PyP100 import PyP110
import pandas as pd
from datetime import datetime

p110 = PyP110.P110("192.168.1.109", "vio.schwarz89@gmail.com", "&uR^8hQVKg%$3oLoEX") #Creating a P110 plug object

p110.handshake() #Creates the cookies required for further methods
p110.login() #Sends credentials to the plug and creates AES Key and IV for further methods

#PyP110 has all PyP100 functions and additionally allows to query energy usage infos
result = p110.getEnergyUsage() #Returns dict with all the energy usage

energy24H = pd.DataFrame.from_dict(result["result"]["past24h"])
energy7D = pd.DataFrame.from_dict(result["result"]["past7d"])
energyMonth = pd.DataFrame.from_dict(result["result"]["past30d"])

#dates24H = pd.date_range(start=datetime.today().strftime('%Y-%m-%d'), periods=24,  freq='H').tolist()

filepath = "energyMonitor-" + datetime.today().strftime('%d%m%Y')
energy24H.to_csv(filepath, header=['energy'])  


filepath = "energyMonitor-" + datetime.today().strftime("%Y-Week%W")
energy7D.to_csv(filepath, header=['energy'])

filepath = "energyMonitor-" + datetime.today().strftime("%Y-%B")
energyMonth.to_csv(filepath, header=['energy'])
