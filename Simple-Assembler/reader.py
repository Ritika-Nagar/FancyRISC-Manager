import json

def find_variant(line):
	IN - "var X"
	OUT - "variable"
	"find what variant of command is present in this line, and returns it"

	if line == '':
		return 'blank'
	if ':' in line[1:]: # and line[line.index(':')-1] != ' ':  
		return 'label'
	if line.startswith('var'):
		return 'variable'
	return 'instruction'


insts = json.load(open('instructions.json'))
def find_cat(cmd):
	"finds what category a specific command belongs to, and its opcode"

	params = cmd.split()

	if len(params) == 0 or params[0] not in insts:  # if invalid instruction category
		return {'opcode':0b11111, 'cat':'unidentified'}

	opcode = int(insts[params[0]]['opcode'],base = 2)
	cat = 'B'
	return {'opcode':opcode, 'cat':cat}


cats = json.load(open('categories.json'))
def encode(ctg,cmd,mem):
	"encodes command according to its category"

	return 0b01000111101110
