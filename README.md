# Digitalocean api



## Requirement :

- Install requests lib, "pip3 install requests" -> for linux & macos | "pip install requests" for windows

- Install json lib, "pip3 install json" -> for linux & macos | "pip install json" for windows



## Examples :

- Create new droplet

```
import digitalocean

token = 'TOKEN'
drp = digitalocean.Droplets(token)
drp.createDroplet()
```

- Get all droplet

```
import digitalocean

token = 'TOKEN'
drp = digitalocean.Droplets(token)
droplets = drp.getAllDroplet()
print(droplets)
```


## Supports

- Account

- Actions

- Balance

- Billing

- Block Storage

- Block Storage Actions

- CDN Endpoints

- Certificates

- Domain Records

- Domains

- Droplet Actions

- Droplets

- Firewalls

- Floating IP Actions

- Floating IPs

- Image Actions

- Images

- Invoices

- Load Balancers

- Project Resources

- Projects

- Regions

- Sizes

- Snapshots

- SSH Keys

- Tags

- VPCs
