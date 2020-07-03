

# token - headers - url - slug - param
# post - get - put - patch - delete method


import api





token = '51894b90ad504dd51f14abb23c9165f2c4bfa1efc04d7c2994a0cbfbd49b0c65'
act = api.DropletActions(token)
drp = api.Droplets(token)
dom = api.Domains(token)
tg = api.Tags(token)
print(drp.getDropletSnapchots('185682498'))
#print(drp.getDropletById('185682498'))
#print(act.getDropletAction('198271163','969063345'))
#print(tg.getAllTags())
#print(bi.getBilling())














