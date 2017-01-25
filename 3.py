# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
# def factors(n):
#     return  set([i, n/i for i in range(2, int(n**0.5) + 1) if n % i == 0])
def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(2, int(n**0.5) + 1) if n % i == 0)))
# num_list = range(1, int(600851475143 ** 0.5) + 1)
# num_list.reverse()
# print nums_to_check[:10]

# for num in num_list:
#     for j in xrange(2, int(num ** 0.5) + 1):
#         if num % j == 0:
#             continue
#         else:
#             print num
#             break

def is_prime(ff):
    max_prime_factor = 2
    for f in ff:
        factors_list = factors(f)
        if len(factors_list) > 1:
            continue
        else:
            max_prime_factor = f
            break
        # for j in xrange(2, int(f ** 0.5)):
        #     if f % j == 0:
        #         factors_list.append(j)
        # if not factors_list:
        #     max_prime_factor = f
    return max_prime_factor


ff = factors(600851475143)
# print type(ff)
# ff.reverse()
# print max(ff)
find_max_prime = is_prime(ff)
# print find_max_prime
