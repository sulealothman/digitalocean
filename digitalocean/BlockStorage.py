from .reqmethods import Req, Arrange

class BlockStorage(Req, Arrange):
	slug = 'volumes'

	def __init__(self, token):
		self.setToken(token)

	def getAllSnapshotsVolumes(self, volumeId):
		data = self.get(f'{self.slug}/{volumeId}/snapshots')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def getVolumeByName(self, volumeName):
		data = self.get(f'{self.slug}?=name{volumeName}')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def getVolumeByRegion(self, region):
		data = self.get(f'{self.slug}?region={region}')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def getVolumeByNameRegion(self, volumeName, region):
		data = self.get(f'{self.slug}?=name{volumeName}&region={region}')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def getVolumeById(self, volumeId):
		data = self.get(f'{self.slug}/{volumeId}')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def storeVolume(self, size, volName, volDesc, region, filesystemType, filesystemLabel):
		body = {"size_gigabytes":f'{size}', 'name' : f'{volName}', 'description' : f'{volDesc}', 'region' : f'{region}', 'filesystem_type' : f'{filesystemType}' , 'filesystem_label' : f'{filesystemLabel}'}
		data = self.post(f'{self.slug}', body)
		return data

	def storeSnapshotFromVolume(self, volumeId, volName, tags):
		body = {"name":f'{volName}', 'tags' : f'{tags}'}
		data = self.post(f'{self.slug}/{volumeId}/snapshots', body)
		return data

	def deleteVolume(self, volumeId):
		data = self.delete(f'{self.slug}/{volumeId}')
		return data

	def deleteVolumeByName(self, volumeName, region):
		data = self.delete(f'{self.slug}?=name{volumeName}&region={region}')
		return data

	def deleteVolumeSnapshot(self, snapshotId):
		data = self.delete(f'/snapshots/{snapshotId}')
		return data
