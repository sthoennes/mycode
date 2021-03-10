#!/usr/bin/env python3
# create the list called farms
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "CHAD"]}
item = 0
#val = '0'
# loop across the list farmss
# dont repeat code, dont make inflexible, what if more farms added or removed, what if name or agg doesnt have value?
# define function for repeatable code


def farm(firefly):
# let firefly equal the farm dic being passed into this function
    print(f"Resourece is {firefly.get('name','UNAMED FARM')}:")
    for animals in firefly.get('agriculture'):
        print(animals)
    print()

for x in farms:
# i want to talke to each dict and i want to get name an aggriculture from both dicts
    farm(x)

