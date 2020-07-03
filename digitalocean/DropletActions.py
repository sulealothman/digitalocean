from .reqmethods import Req, Arrange

class DropletActions(Req, Arrange):
	slug = 'droplets'

	def __init__(self, token):
		self.setToken(token)

	def enablePrivateNetworkDroplet(self, dropletId):
		body = {'type':'enable_private_networking'}
		data = self.post(f'{self.slug}/{dropletId}/actions', body)
		return data

	def enablePrivateNetworkDropletByTag(self, tagName):
		body = {'type':'enable_private_networking'}
		data = self.post(f'{self.slug}/actions?tag_name={tagName}', body)
		return data

	def enableIPv6Droplet(self, dropletId):
		body = {'type':'enable_ipv6'}
		data = self.post(f'{self.slug}/{dropletId}/actions', body)
		return data

	def enableIPv6DropletByTag(self, tagName):
		body = {'type':'enable_ipv6'}
		data = self.post(f'{self.slug}/actions?tag_name={tagName}', body)
		return data

	def passwordResetDroplet(self, dropletId):
		body = {'type':'password_reset'}
		data = self.post(f'{self.slug}/{dropletId}/actions', body)
		return data

	def enableBackupDroplet(self, dropletId):
		body = {'type':'enable_backups'}
		data = self.post(f'{self.slug}/{dropletId}/actions', body)
		return data

	def enableBackupDropletByTag(self, tagName):
		body = {'type':'enable_backups'}
		data = self.post(f'{self.slug}/actions?tag_name={tagName}', body)
		return data

	def disableBackupDroplet(self, dropletId):
		body = {'type':'disable_backups'}
		data = self.post(f'{self.slug}/{dropletId}/actions', body)
		return data

	def disableBackupDropletByTag(self, tagName):
		body = {'type':'disable_backups'}
		data = self.post(f'{self.slug}/actions?tag_name={tagName}', body)
		return data

	def shutdownDroplet(self, dropletId):
		body = {'type':'shutdown'}
		data = self.post(f'{self.slug}/{dropletId}/actions', body)
		return data

	def shutdownDropletByTag(self, tagName):
		body = {'type':'shutdown'}
		data = self.post(f'{self.slug}/actions?tag_name={tagName}', body)
		return data

	def rebootDroplet(self, dropletId):
		body = {'type':'reboot'}
		data = self.post(f'{self.slug}/{dropletId}/actions', body)
		return data

	def powercycleDroplet(self, dropletId):
		body = {'type':'power_cycle'}
		data = self.post(f'{self.slug}/{dropletId}/actions', body)
		return data

	def powercycleDropletByTag(self, tagName):
		body = {'type':'power_cycle'}
		data = self.post(f'{self.slug}/actions?tag_name={tagName}', body)
		return data

	def poweroffDroplet(self, dropletId):
		body = {'type':'power_off'}
		data = self.post(f'{self.slug}/{dropletId}/actions', body)
		return data

	def poweroffDropletByTag(self, tagName):
		body = {'type':'power_off'}
		data = self.post(f'{self.slug}/actions?tag_name={tagName}', body)
		return data

	def poweronDroplet(self, dropletId):
		body = {'type':'power_on'}
		data = self.post(f'{self.slug}/{dropletId}/actions', body)
		return data

	def poweronDropletByTag(self, tagName):
		body = {'type':'power_on'}
		data = self.post(f'{self.slug}/actions?tag_name={tagName}', body)
		return data

	def restoreDroplet(self, dropletId, image):
		body = {'type':'restore', 'image': f'{image}'}
		data = self.post(f'{self.slug}/{dropletId}/actions', body)
		return data

	def resizeDroplet(self, dropletId, size):
		body = {'type':'resize', 'size': f'{size}'}
		data = self.post(f'{self.slug}/{dropletId}/actions', body)
		return data

	def rebuildDroplet(self, dropletId, image):
		body = {'type':'rebuild', 'image': f'{image}'}
		data = self.post(f'{self.slug}/{dropletId}/actions', body)
		return data

	def renameDroplet(self, dropletId, newName):
		body = {'type':'rebuild', 'name': f'{newName}'}
		data = self.post(f'{self.slug}/{dropletId}/actions', body)
		return data

	def changeKernelDroplet(self,dropletId, kernel):
		body = {'type':'change_kernel', 'kernel': kernel}
		data = self.post(f'{self.slug}/{dropletId}/actions', body)
		return data

	def snapshotDroplet(self,dropletId, snapshot):
		body = {'type':'snapshot', 'name': f'{snapshot}'}
		data = self.post(f'{self.slug}/{dropletId}/actions', body)
		return data

	def snapshotDropletByTag(self,tagName, snapshot):
		body = {'type':'snapshot', 'name': f'{snapshot}'}
		data = self.post(f'{self.slug}/actions?tag_name={tagName}', body)
		return data

	def getDropletAction(self,dropletId, actionId):
		data = self.get(f'{self.slug}/{dropletId}/actions/{actionId}')
		if 'id' in data:
			return data
		return self.arrangeData(data)


