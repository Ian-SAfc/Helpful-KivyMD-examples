
#Takes a KivyMD color statement and converts it into #999999
#This is Rgba to Hex essentially.  We ignore the [a]lpha.

def MTupleToHexColor(MRgba_value):
	Mfirst_hex = int(MRgba_value[0] * 256)
	Msecond_hex = int(MRgba_value[1] * 256)
	Mthird_hex = int(MRgba_value[2] * 256)
	if Mfirst_hex > 255: Mfirst_hex = 255
	if Msecond_hex > 255: Msecond_hex = 255
	if Mthird_hex > 255: Mthird_hex = 255
	Mfirst_hex_str = "%02x" % Mfirst_hex
	Msecond_hex_str = "%02x" % Msecond_hex
	Mthird_hex_str = "%02x" % Mthird_hex
	return ("#" + Mfirst_hex_str + Msecond_hex_str + Mthird_hex_str)