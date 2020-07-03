from .reqmethods import Req, Arrange

class Droplets(Req, Arrange):
	slug = 'droplets'

	def __init__(self, token):
		self.setToken(token)

	def getAllDroplet(self):
		data = self.get(f'{self.slug}')
		return self.arrangeData(data)

	def getDropletById(self, dropletId):
		data = self.get(f'{self.slug}/{dropletId}')
		if 'id' in data:
			return data
		return self.arrangeData(data)
		
	def getDropletByTag(self, tag):
		data = self.get(f'{self.slug}?tag_name={tag}')
		return data

	def getDropletActions(self, dropletId):
		data = self.get(f'{self.slug}/{dropletId}/actions')
		if 'id' in data:
			return data
		return self.arrangeData(data)

	def getDropletBackups(self, dropletId):
		data = self.get(f'{self.slug}/{dropletId}/backups')
		return self.arrangeData(data)

	def getDropletSnapchots(self, dropletId):
		data = self.get(f'{self.slug}/{dropletId}/snapshots')
		if 'id' in data:
			return data
		return self.arrangeData(data)

	def getDropletKernels(self, dropletId):
		data = self.get(f'{self.slug}/{dropletId}/kernels')
		if 'id' in data:
			return data
		return self.arrangeData(data)

	def getDropletNeighbors(self, dropletId):
		data = self.get(f'{self.slug}/{dropletId}/neighbors')
		if 'id' in data:
			return data
		return self.arrangeData(data)

	def getDropletAllNeighbors(self):
		data = self.get('/reports/droplet_neighbors_ids')
		if 'id' in data:
			return data
		return self.arrangeData(data)

	def deleteDropletById(self,dropletId):
		data = self.delete(f'{self.slug}/{dropletId}')
		return data

	def deleteDropletByTag(tag):
		data = self.delete(f'{self.slug}?tag_name={tag}')
		return data

	def createDroplet(self):
		prefrences = {
			'name':'example.com',
			'region':'nyc3',
			'size':'s-1vcpu-1gb',
			'image':'ubuntu-16-04-x64',
			'ssh_keys':[],
			'backups':False,
			'ipv6':True,
			'user_data':None,
			'private_networking':False,
			'volumes':None,
			'tags':["web"]
			}
		for key, value in prefrences.items():
			userInput = input(key + f' (Default => {value}): ')
			if userInput != '':
				prefrences[key] = userInput
		return self.storeDroplet(prefrences)

	def createMultipleDroplets(self):
		prefrences = {
			'names':['example.com', 'example1.com'],
			'region':'nyc3',
			'size':'s-1vcpu-1gb',
			'image':'ubuntu-16-04-x64',
			'ssh_keys':[],
			'backups':False,
			'ipv6':True,
			'user_data':None,
			'private_networking':False,
			'volumes':None,
			'tags':["web"]
			}
		for key, value in prefrences.items():
			userInput = input(key + f' (Default => {value}): ')
			if userInput != '':
				prefrences[key] = userInput
		return self.storeDroplet(prefrences)


	def storeDroplet(self, prefrences):
		data = self.post(self.slug, prefrences)
		return data
