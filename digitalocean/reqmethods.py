import requests
import json

class Req():

	token = ''
	headers = {
		'Authorization' : f'Bearer {token}',
		'User-Agent' : 'DigitalOcean Api',
		'Content-Type' : 'application/json'
	}
	url = 'https://api.digitalocean.com/v2/'

	def post(self, slug, data):
		url = f'{self.url}{slug}'
		response = requests.post(url, headers=self.headers, json=data)
		data = response
		return data

	def put(self, slug, data):
		url = f'{self.url}{slug}'
		response = requests.put(url, headers=self.headers, data=data)
		data = response
		return data

	def patch(self, slug, data):
		url = f'{self.url}{slug}'
		response = requests.patch(url, headers=self.headers, data=data)
		data = response
		return data

	def get(self, slug):
		url = f'{self.url}{slug}'
		response = requests.get(url, headers=self.headers)
		data = response.json()
		return data


	def delete(self, slug, param=None):
		url = f'{self.url}{slug}'

		if param == None:
			response = requests.delete(url, headers=self.headers)
		else:
			response = requests.delete(url, headers=self.headers, data=param)
		data = response
		return data

	def setToken(self, token):
		self.headers['Authorization'] = f'Bearer {token}'


class Arrange():

	def arrangeData(self,data):
		if(isinstance(data, dict)):
			return self.dictData(data)
		elif(isinstance(data, tuple) or isinstance(data, list)):
			return self.tupleData(data)
		else:
			return data

	def dictData(self, data):
		result = ''
		for key, value in data.items():
			result += f'{key} : {value} \n' if (self.returnCheck(value)) else f'{key} : \n' + self.arrangeData(value)
		return result

	def tupleData(self, data):
		result = ''
		for element in data:
			result += self.dictData(element) if isinstance(element, dict) else f'{element} : \n'
			
		return result

	def returnCheck(self, data):
		return False if (isinstance(data, dict) or isinstance(data, list) or isinstance(data, tuple)) else True




