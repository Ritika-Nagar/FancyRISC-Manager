class LU:
	def add(params):
		"adds two integers"
		return {
			'main': params[0] + params[1],
			'flags': int(f"{int(params[0] + params[1] > 255)}000", base = 2)
		}

	def sub(params):
		"subtracts two integers"
		return {
			'main': params[0] - params[1],
		}
	
	def mul(params):
		"multiply two integers"
		return {
			'main': params[0] * params[1],
			'flags':int(f"{int(params[0] * params[1] > 255)}110", base = 2)
		}
	
	def xor(params):
		"Performs bitwise XOR operation"
		return {
			'main': params[0] ^ params[1],
		}
	def or(params):
		"Performs bitwise OR operation"
		return {
			'main': params[0] | params[1],
		}

	def and(params):
		"Performs bitwise AND operation"
		return {
			'main': params[0] & params[1],
		}

	def movr(params):
		pass

	def movi(params):
		pass

	def hlt(params):
		"stops running code"
		return {}

	switcher = {
		0b00000: add,
		0b00001: sub,
		0b00110: mul,
		0b10011: hlt,
	}

	@classmethod
	def call(cls, opc: int, params: list) -> dict:
		"""
		calls the function for the given opcode and parameters.

		all parameters are integers in raw form.

		note the purposes of the three output values:
			- main value will contain the main output, which will be stored in a registry.
			- alter value will contain either a second output value [only for div instruction].
			- branch value will contain whether or not to follow branch instruction.
			- flags value will contain the new value of the last 4 bits in the FLAGS register.

		it is to be noted that the alter, branch, and flags values can be merged into one; but they are kept separate for clearer documentation.
		"""
		toret = {
			'main'  : 0,
			'alter' : 0,
			'branch': 0,
			'flags' : 0,
		}

		gotten = cls.switcher[opc](params)

		for x in gotten:
			toret[x] = gotten[x]

		return toret
