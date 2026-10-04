from load import Load
import json
load = Load()
load.addnewblock()
with open('blocks.json', 'r') as File:
    result = json.load(File)
    for items in result:
        print(items["block name"], items["durabilitytaken"], items["resource"])

