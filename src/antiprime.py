## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
import sys
def main(x) :
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT
	i = 1
	h = 1
	y = x - 1
	sum1 = 0
	sum2 = 0
	while i <= x :
		if x % i == 0 :
			sum1 = sum1 + 1
		i = i + 1

	while 1 <= y and sum1 > sum2 :
	
		while y >= h :
			if y % h == 0 :
				sum2 = sum2 + 1
			h = h + 1
		if sum1 <= sum2 :
			return "not anti-prime"

		
		else :
			sum2 = 0
			h = 1
			y = y - 1
	

	if sum1 > sum2 :
		return "anti-prime"

	## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime"
	

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :
	#print(x)
	x = int (sys.argv[1])
	print(main(x))

	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	
