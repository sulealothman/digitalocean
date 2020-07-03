from .reqmethods import Req, Arrange

class Firewalls(Req, Arrange):
	slug = 'firewalls'

	def __init__(self, token):
		self.setToken(token)

	def getAllFirewalls(self):
		data = self.get(f'{self.slug}')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def getFirewallById(self, firewallId):
		data = self.get(f'{self.slug}/{firewallId}')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def storeFirewall(self, body):
		data = self.post(f'{self.slug}', body)
		return data

	def updateFirewall(self, firewallId, body):
		data = self.put(f'{self.slug}/{firewallId}', body)
		return data

	def storeRulesFirewall(self, firewallId, body):
		data = self.post(f'{self.slug}/{firewallId}/rules', body)
		return data

	def deleteRulesFirewall(self, firewallId, body):
		data = self.delete(f'{self.slug}/{firewallId}/rules', body)
		return data

	def deleteFirewall(self, firewallId):
		data = self.delete(f'{self.slug}/{firewallId}')
		return data

	def storeTagsFirewall(self, firewallId, tags):
		body = {'tags' : f'{tags}'}
		data = self.post(f'{self.slug}/{firewallId}/tags', body)
		return data

	def deleteTagsFirewall(self, firewallId, tags):
		body = {'tags' : f'{tags}'}
		data = self.delete(f'{self.slug}/{firewallId}/tags', body)
		return data

	def storeeDropletsFirewall(self, firewallId, dropletsId):
		body = {'droplet_ids' : f'{dropletsId}'}
		data = self.post(f'{self.slug}/{firewallId}/droplets', body)
		return data

	def deleteDropletsFirewall(self, firewallId, dropletsId):
		body = {'droplet_ids' : f'{dropletsId}'}
		data = self.delete(f'{self.slug}/{firewallId}/droplets', body)
		return data
