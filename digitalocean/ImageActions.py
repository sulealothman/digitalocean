from .reqmethods import Req, Arrange

class ImageActions(Req, Arrange):
	slug = 'images'

	def __init__(self, token):
		self.setToken(token)

	def transferImage(self, imageId, region):
		body = {"type":'transfer', 'region': f'{region}'}
		data = self.post(f'{self.slug}/{floatIp}/actions', body)
		return data

	def convertImageToSnapshot(self,imageId):
		body = {"type":'convert'}
		data = self.post(f'{self.slug}/{imageId}/actions', body)
		return data

	def getImageActionById(self, imageId, actionId):
		data = self.get(f'{self.slug}/{imageId}/actions/{actionId}')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)
