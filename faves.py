#!/usr/bin/env python3


def faves(movie="default", food="default", boardgame="default"):
    print(movie,"is my fave movie!")
    print(food,"is my fave food!")
    print(boardgame,"is my fave board game!")


#faves("Shrek","Dumplings","Risk")

args= ["Gladiator","Dumplings","Clue"]

# * allows you to send lists
faves(*args)

sue= {"movie":"Gladiator","food":"coffee","boardgame":"Clue"}

# ** allows you to send dicts with movie, food, and boardgame keys in the definition
# keys in dict must be specified as args in the defintion def()
faves(**sue)
