import sys

from Euler_1_10 import *
from Euler_11_19 import *
from Euler_20_29 import *
from Euler_30_39 import *
from Euler_40_49 import *
from Euler_50_59 import *
from Euler_60_ import *

def main():
	prob_number = sys.argv[1]
	func = "prob"+prob_number+"()"
	result = eval(func)
	print result

if __name__=="__main__":
	main()