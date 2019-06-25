#!/usr/bin/python3

import yaml

def main():
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeuian"}, {"name": "Arthur Dent", "specied": "human"}]

    print(hitchhikers)

    zfile = open("galaxyguide.yaml", "w")

    yaml.dump(hitchhikers, zfile)
    zfile.close()

main()
