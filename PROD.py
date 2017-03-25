#Import and use requests module
import requests
#Define the string to send in the loop url
mac = ['4c4e.35f1.6849', '0022.90fe.1a4b', '3037.a6fc.f0c3', '0000.0c07.ac01', '001b.0c38.f8ed', 'b43a.28a1.2602', 'ec1f.7280.b7c0', 'fcf8.ae6f.b1d9', '0000.0c07.ac01', '4c4e.35f1.6846', '0000.0c07.ac01', '10f3.119e.8bce', '4c4e.35f1.6856', '0000.0c07.ac01', '10f3.119e.8bcf', '0000.0c07.ac01', '0008.5d2f.2607', '0008.5d35.4025', '4055.39fc.1b94', 'a0d3.c11f.72f6', 'c434.6b72.97b5', '0022.90fe.1a4c', '3037.a6fc.f0c1', '0022.90fe.1a4a', '4c4e.35f1.684a', '10f3.119e.8bca', '4c4e.35f1.684c', '001b.0c38.f8eb', '0022.909d.e35d', '3037.a6fc.f0c5', '0022.909d.e35d', '3037.a6fc.f0c7', '0022.909d.e35d', '3037.a6fc.f0c9', '0022.909d.e35d', '3037.a6fc.f0cb', '0022.909d.e35d', '3037.a6fc.f0cd', '0022.909d.e35d', '3037.a6fc.f0cf', '0022.909d.e35d', '3037.a6fc.f0d1', '0022.909d.e35d', '3037.a6fc.f0d3', '0022.909d.e35d', '3037.a6fc.f0d5', '0022.909d.e35d', '3037.a6fc.f0d7', '0022.909d.e35d', '3037.a6fc.f0d9', '0022.909d.e35d', '3037.a6fc.f0db', '0000.0c07.acc8', '001b.0c38.f8ec', '3037.a6fc.f0dd', '4c4e.35f1.6801', '0022.90fe.1a4d', '0022.909d.e35f', '0000.0c07.ac01', '10f3.119e.8bcc', '4c4e.35f1.684e', '0000.0c07.ac01', '10f3.119e.8bcd', '0021.d8b0.42cb', '001b.0c38.f8ed', '0024.b25c.97e7', '0024.b25c.97e9', '204e.7f86.d157', 'c03f.0e73.7343', 'c03f.0e7c.c415', 'c03f.0e7c.c41c', 'e046.9a57.b9b5', 'e091.f5c8.9805', 'e091.f5c8.9ad8', 'e091.f5c8.9ae6', '0000.0c07.ac01', '0000.0c07.ac01', '001b.0c38.f8ed', '0000.0c07.ac01', '10f3.119e.8bd0']
#Begin the loop including the print out of mac address and result of lookup of mac address
for i in mac:
	url = 'http://api.macvendors.com/' + i
	headers = {'cache-control': 'no-cache'}
	response = requests.get(url,headers=headers)
	print(i),(response.text)
