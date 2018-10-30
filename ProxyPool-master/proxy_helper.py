import json
import random
import requests

def get_proxy_ip2():
	ips = [{"port":"28156","ip":"60.175.198.25"},{"port":"47447","ip":"115.230.68.173"},{"port":"31828","ip":"110.18.139.118"},{"port":"35805","ip":"119.116.76.118"},{"port":"41218","ip":"115.209.78.137"},{"port":"31339","ip":"119.116.74.63"},{"port":"44584","ip":"183.142.157.134"},{"port":"22602","ip":"113.110.195.154"},{"port":"34716","ip":"121.231.183.39"},{"port":"22556","ip":"114.217.159.188"},{"port":"43905","ip":"123.134.129.104"},{"port":"40901","ip":"113.74.34.122"},{"port":"47868","ip":"112.113.164.78"},{"port":"48791","ip":"49.81.17.208"},{"port":"47278","ip":"49.81.83.95"},{"port":"30422","ip":"183.142.112.124"},{"port":"26930","ip":"119.138.195.21"},{"port":"47403","ip":"60.214.162.206"},{"port":"20761","ip":"125.86.166.228"},{"port":"47861","ip":"115.58.75.228"}]
	ip_dict = random.choice(ips)

	return ip_dict

def get_proxy_ip():
	url = 'http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=72a2b845b4114d05aa77d110e9b97e03&count=20&expiryDate=0&format=1&newLine=2'

	headers =  {
		"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)" 
	}
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		# print(response.text)
		json_data = json.loads(response.text)
		ip_list = json_data['msg']
		ip_dict = random.choice(ip_list)

		return ip_dict
	return None

if __name__ == '__main__':
	ip = get_proxy_ip2()
	print(ip)