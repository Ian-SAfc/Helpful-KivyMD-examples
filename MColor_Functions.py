
#Takes a KivyMD color statement and converts it into hex format e.g. #FF00FF
#This is Rgba to Hex essentially.  We ignore the [a]lpha.
#For example you can pass self.theme_cls.primary_color and it will convert it to hex
#I've written this code out "longhand".  You can acheive the same result in half the lines,
#I just wanted to make the formula clearer. 

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
