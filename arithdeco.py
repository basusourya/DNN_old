# 
# Decompression application using static arithmetic coding
#
# Usage: python arithmetic-decompress.py InputFile OutputFile
# This decompresses files generated by the arithmetic-compress.py application.
# 
# Copyright (c) Project Nayuki
# 
# https://www.nayuki.io/page/reference-arithmetic-coding
# https://github.com/nayuki/Reference-arithmetic-coding
# 

import sys
import arithmeticcoding
python3 = sys.version_info.major >= 3

class arithdecoder(object):
	# Command line main application function.
	a = []
	def main(self, s, frequencies, num_symbols):
		# Handle command line arguments
		#if len(args) != 2:
		#	sys.exit("Usage: python arithmetic-decompress.py InputFile OutputFile")
		#inputfile  = args[0]
		#outputfile = args[1]
		
		# Perform file decompression
		#bitin = arithmeticcoding.BitInputStream(open(inputfile, "rb"))
		#with open(outputfile, "wb") as out:
		#	try:
		self.a = []
		freqs = self.read_frequencies(frequencies)
		self.a = self.decompress(s, freqs, num_symbols)
		#	finally:
		#		bitin.close()
		return self.a


	def read_frequencies(self,frequencies):

		return arithmeticcoding.SimpleFrequencyTable(frequencies)


	def decompress(self, s, freqs, num_symbols):
		dec = arithmeticcoding.ArithmeticDecoder(s)
		while 1:
			symbol = dec.read(freqs)
			if symbol == num_symbols:
				break
			self.a.append(symbol)
		return self.a

	# Reads an unsigned integer of the given bit width from the given stream.
	#def read_int(bitin, numbits):
	#	result = 0
	#	for i in range(numbits):
	#		result = (result << 1) | bitin.read_no_eof()  # Big endian
	#	return result


	# Main launcher
	#if __name__ == "__main__":
	#	main(sys.argv[1 : ]) 