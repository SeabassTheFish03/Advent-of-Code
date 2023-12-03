import json

f = open("7", "r")
raw_commands = f.read()
f.close()

commands = raw_commands.split("$ ")
file_system = {"/": dict()}
path = []

# File format: {"file name": file_size}
def add_file(initial, file, pth):
	if len(pth) == 0:
		initial.update(file)
	else:
		initial.update({pth[0]:add_file(initial[pth[0].strip()], file, pth[1:])})
	return initial

def add_directory(initial, dir_name, pth):
	if len(pth) == 0:
		initial[dir_name] = dict()
		return initial
	if pth[0] in initial:
		print("Duplicate!")
	initial.update({pth[0]: add_directory(initial[pth[0].strip()], dir_name, pth[1:])})
	return initial

def ls(output):
	global file_system
	for file_dir in output:
		file_dir = file_dir.strip()
		if len(file_dir) == 0:
			continue
		if file_dir.__contains__("dir"):
			file_system = add_directory(file_system, file_dir.split(" ")[1].strip(), path)
		else:
			file_system = add_file(file_system, {file_dir.split(" ")[1].strip(): int(file_dir.split(" ")[0])}, path)
def cd(new_dir):
	global path
	if new_dir == "..\n":
		path.pop()
	else:
		path.append(new_dir.strip())

for command in commands:
	try:
		if command.__contains__("ls"):
			ls(command.split("\n")[1:])
		elif command.__contains__("cd"):
			cd(command.split(" ")[1])
	except:
		print(command)
		print("File System: " + json.dumps(file_system, indent=4))
		print("Path: " + str(path))
		raise TypeError

print(file_system)