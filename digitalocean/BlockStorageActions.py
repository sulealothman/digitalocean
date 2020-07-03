from .reqmethods import Req, Arrange

class BlockStorageActions(Req, Arrange):
	slug = 'volumes'

	def __init__(self, token):
		self.setToken(token)

	def getAllVolumeActions(self, volumeId):
		data = self.get(f'{self.slug}/{volumeId}/actions')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def getVolumeActionById(self, volumeId, actionId):
		data = self.get(f'{self.slug}/{volumeId}/actions/{actionId}')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def attachVolumeDroplet(self, volumeId, dropletId, region, tags):
		body = {"type": 'attach', 'droplet_id' : f'{dropletId}', 'region' : f'{region}', 'tags' : f'{tags}'}
		data = self.post(f'{self.slug}/{volumeId}/actions', body)
		return data

	def datachVolumeDroplet(self, volumeId, dropletId, region):
		body = {"type": 'detach', 'droplet_id' : f'{dropletId}', 'region' : f'{region}'}
		data = self.post(f'{self.slug}/{volumeId}/actions', body)
		return data

	def attachVolumeDropletByName(self, volName, dropletId, region, tags):
		body = {"type": 'attach', 'volume_name': f'{volName}', 'region' : f'{region}', 'droplet_id' : f'{dropletId}', 'tags' : f'{tags}'}
		data = self.post(f'{self.slug}/actions', body)
		return data

	def datachVolumeDropletByName(self, dropletId, volName, region):
		body = {"type": 'detach', 'droplet_id' : f'{dropletId}', 'volume_name': f'{volName}', 'region' : f'{region}'}
		data = self.post(f'{self.slug}/actions', body)
		return data

	def resizeVolume(self, volumeId, newSize, region):
		body = {"type": 'resize', 'size_gigabytes' : f'{newSize}', 'region' : f'{region}'}
		data = self.post(f'{self.slug}/{volumeId}/actions', body)
		return data
