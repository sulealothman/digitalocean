import digitalocean





token = 'TOKEN'
drp = digitalocean.Droplets(token)

drp.createDroplet()
print(drp.getAllDroplet())