from .reqmethods import Req, Arrange

class LoadBalancers(Req, Arrange):
	slug = 'load_balancers'

	def __init__(self, token):
		self.setToken(token)

	def getAllLoadBalancers(self):
		data = self.get(f'{self.slug}')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def getLoadBalancerById(self, lbId):
		data = self.get(f'{self.slug}/{lbId}')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def storeLoadBalancer(self, body):
		data = self.post(f'{self.slug}', body)
		return data

	def updateLoadBalancer(self, lbId, body):
		data = self.put(f'{self.slug}/{lbId}', body)
		return data

	def storeForwardingRulesLoadBalancer(self, lbId, body):
		data = self.post(f'{self.slug}/{lbId}/forwarding_rules', body)
		return data

	def deleteForwardingRulesLoadBalancer(self, lbId, body):
		data = self.delete(f'{self.slug}/{lbId}/forwarding_rules', body)
		return data

	def deleteLoadBalancer(self, lbId):
		data = self.delete(f'{self.slug}/{lbId}')
		return data

	def storeDropletsLoadBalancer(self, lbId, dropletsId):
		body = {'droplet_ids' : f'{dropletsId}'}
		data = self.post(f'{self.slug}/{firewallId}/droplets', body)
		return data

	def deleteDropletsLoadBalancer(self, lbId, dropletsId):
		body = {'droplet_ids' : f'{dropletsId}'}
		data = self.delete(f'{self.slug}/{lbId}/droplets', body)
		return data
