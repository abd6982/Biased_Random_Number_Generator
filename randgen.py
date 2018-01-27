from time import gmtime, strftime

#Function to generate randoms
def randn(u_limit, l_limit, n, seed=-1):
    mid_limit = (u_limit + l_limit) // 2            #Compute mid_limit
    if seed == -1:                                  #Use current time as seed if not provided
        seed = int(strftime("%Y%m%d%H%M%S", gmtime()))
    result = list()
    for i in range(n):                              #Loop to generate desired number of elements
        seed = (1103515245 * seed + 12345) & (2 ** 31 - 1)
        num = (seed >> 16) % 20 + 1
        if(num % 4 == 0):                           #Generate small numbers
            result.append((seed >> 16) % (mid_limit + 1 - l_limit) + l_limit)
        else:                                       #Generate large numbers
            result.append((seed >> 16) % (u_limit + 1 - mid_limit) + mid_limit)
    return result

#Function to calculate ratios
def calculate_ratio(res, u_limit, l_limit, n):
    small = [x for x in res if x < (u_limit + l_limit) // 2]
    large = [x for x in res if x >= (u_limit + l_limit) // 2]
    return (len(small) / n, len(large) / n)

if __name__ == '__main__':
    pass   
