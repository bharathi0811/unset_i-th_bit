n =int(input())
i =int(input())
def check_bit(n,i):
    if n&(1<<i)!=0:
        return True
    else:
        return False
def unset(n,i):
    if check_bit(n,i):
        return n^(1<<i)
    return n
print(unset(n,i))