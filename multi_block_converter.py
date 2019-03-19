import nbtlib
import json
import os
from os import walk
from os.path import isfile, join

def check_path(path):
	dir = path.replace("\\", "/").split("/")
	if "." in dir[-1]:
		dir = "/".join(dir[:len(dir) - 1])
	else:
		dir = "/".join(dir)
	if not os.path.exists(dir):
		os.makedirs(dir)
	return path

def nested(data):
	result = 0
	if type(data) is nbtlib.tag.List:
		result = []
		for i in data:
			temp = nested(data)
			result.append(temp)
	elif type(data) is nbtlib.tag.Compound:
		result = {}
		for i in data:
			temp = nested(data[i])
			result[i] = temp
	else:
		result = data
	return result


def convert(nbt_file):
	result = {}
	for i in nbt_file.keys():
		result[i] = nested(nbt_file[i])
	return result

def nested_nbt(data):
	result = ""
	if type(data) is nbtlib.tag.Compound:
		temp = []
		for key in data:
			temp.append(key + ":" + nested_nbt(data[key]))
		result = "{" + ", ".join(temp) + "}"
	elif type(data) is nbtlib.tag.List:
		temp = []
		for i in data:
			temp.append(nested_nbt(i))
		result = "[" + ", ".join(temp) + "]"
	else:
		result = str(data)
	return result

def nbt(data):
	result = ""
	if "nbt" in data:
		result = nested_nbt(data["nbt"])
	return result

def block_state(data):
	result = ""
	if "Properties" in data:
		result = "["
		for state in data["Properties"]:
			result = result + state + "=" + data["Properties"][state] + ","
		result = result[:-1] + "]"
	else:
		result = ""
	return result

def generate(path):
	commands = {
		"start": "scoreboard players set @s bb.success 1",
		"block": "execute as @s[scores={bb.success=1}] store success score @s bb.success if block ~<x> ~<y> ~<z> <block>",
		"end": "execute as @s[scores={bb.success=1}] run tag @s add <tag>"
	}
	
	file_list = [join(directory, file) for (directory, _, files) in walk(path) if (len(files) > 0) 
							for file in files if (file.endswith(".nbt") and isfile(join(directory, file)))]
	for file in file_list:
		out = open(check_path(file.replace(path, "./output").replace(".nbt", ".mcfunction")), "w")
		f = nbtlib.load(file)
		data = convert(f)
		palette = [ x["Name"] + block_state(x) for x in data[""]["palette"] ]
		blocks = data[""]["blocks"]
		out.write(commands['start'] + "\n")

		for block in blocks:
			nbt_state = nbt(block)
			line = commands['block'] + "\n"
			line = line.replace("<x>", str(block["pos"][0])).replace("<y>", str(block["pos"][1])).replace("<z>", str(block["pos"][2])).replace("<block>", str(palette[block["state"]]) + nbt_state)
			out.write(line)

		out.write(commands['end'].replace("<tag>", file.replace(path, "").replace(".nbt", "").replace("\\", ".").replace("/", ".")[1:]) + "\n")
		out.close()
		
		print("Generated: " + file)

generate("./input")