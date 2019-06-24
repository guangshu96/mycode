#!/usr/bin/python3

proto = ['ssh', 'http', 'https']
protoa = ['ssh', 'http', 'https']
print(proto)
#print(proto[1])
#proto.extend('dns')
proto.append('dns')
protoa.append('dns')
print(proto)
#proto.extend(["dns"])
proto2 = [22,80,443,53]
proto.extend(proto2)
protoa.append(proto2)
print(proto)
print(protoa)
