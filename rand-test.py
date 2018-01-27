#Imports
from randgen import randn, calculate_ratio
import sys

if __name__ == '__main__':
    
    #Read parameters from terminal and calculate randoms
    u_limit = int(sys.argv[1])
    l_limit = int(sys.argv[2])
    n = int(sys.argv[3])
    if(len(sys.argv) == 4):
        res = randn(u_limit, l_limit, n)
    else:
        seed = int(sys.argv[4])
        res = randn(u_limit, l_limit, n, seed)

    #Print generated randoms
    print(res)

    #Calculate ratio of small and large numbers
    s_frac, l_frac = calculate_ratio(res, u_limit, l_limit, n)

    #Print the ratio
    print("\nFraction of small numbers is {} and fraction of large numbers is {}"
    .format(s_frac, l_frac))
