# SS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).

# Specifications of HEX Color Code

# ■ It must start with a '#' symbol.
# ■ It can have  or  digits.
# ■ Each digit is in the range of 0 to F. (1,2,3,4,5,6,7,9,0,A,B,C,D,E and F).
# ■ A-F letters can be lower case. (a,b,c,d,e and f are also valid digits).

# Examples

# Valid Hex Color Codes
# #FFF 
# #025 
# #F0A1FB 

# Invalid Hex Color Codes
# #fffabg
# #abcf
# #12365erff
# You are given N lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.

# CSS Code Pattern

# Selector
# {
# 	Property: Value;
# }
# Sample Input

# 11
# #BED
# {
#     color: #FfFdF8; background-color:#aef;
#     font-size: 123px;
#     background: -webkit-linear-gradient(top, #f9f9f9, #fff);
# }
# #Cab
# {
#     background-color: #ABC;
#     border: 2px dashed #fff;
# }   
# Sample Output

# #FfFdF8
# #aef
# #f9f9f9
# #fff
# #ABC
# #fff
# Explanation

# #BED and #Cab satisfy the Hex Color Code criteria, but they are used as selectors and not as color codes in the given CSS.

# Hence, the valid color codes are:

# #FfFdF8
# #aef
# #f9f9f9
# #fff
# #ABC
# #fff

# Note: There are no comments ( // or /* */) in CSS Code.

import re 

css_lines = """35
.arrow-up {
	width: 0;
	height: 0;
	border-left: 5px solid transparent;
	border-right: 5px solid transparent;

	border-bottom: 5px solid black;
}

.arrow-down {
	width: 0;
	height: 0;
	border-left: 20px solid transparent;
	border-right: 20px solid transparent;

	border-top: 20px solid #f00;
}

.arrow-right {
	width: 0;
	height: 0;
	border-top: 60px solid transparent;
	border-bottom: 60px solid transparent;

	border-left: 60px solid green;
}

#f0f {
	width: 0;
	height: 0;
	border-top: 10px solid transparent;
	border-bottom: 10px solid transparent;

	border-right:10px solid blue;
}"""

#N = int(input())

hex_code = r'#[0-9A-Fa-f]{3,6}(?=[^ {])'

colors = []
start = False

for line in css_lines.splitlines():
    #line = input()
    if bool(re.findall(r"{", line))==True:
        start = True
    if bool(re.findall(r"}", line))==True:
        start = False
    #print(line, start, re.findall(hex_code, line))
    if start==True:
        colors.extend(re.findall(hex_code, line))
        #print(start, line, re.findall(hex_code, line))

print('\n'.join(colors)) 
