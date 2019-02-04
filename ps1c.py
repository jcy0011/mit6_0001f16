def ts36(ans):
    a = 0
    for i in range(1,37):
        a = a * (1+0.04/12) + ans/12 * (1.07)**((i-1)//6)
    return a

def bsr36(annual_salary):
    i = 5000
    lb = 0
    ub = 10000
    itr = 0
    while 0 < i <= 10000:
        itr += 1
        if i == 10000:
            if ts36(annual_salary) >=250000:
                return (10000, itr)
            else:
                return None
        if ts36(annual_salary * i /10000) > 250000:
            if ts36(annual_salary * (i-1) /10000) > 250000:
                if (i + lb)% 2 == 0:
                    ub = i
                    i = (i+lb) / 2
                else:
                    ub = i
                    i = ((i+lb) / 2)-0.5
            else:
                return ((i - 1), itr)
        elif ts36(annual_salary * i /10000) > 250000:
            return (i, itr)
        else:
            if ts36(annual_salary * (i+1) /10000) < 250000:
                if (i + ub)%2 == 0:
                    lb = i
                    i = (ub+i)/2
                else:
                    lb = i
                    i = ((i+ub)/2)+0.5
            else:
                return((i+1),itr)
sal = int(input('Enter the starting salary: '))
if bsr36(sal) == None:
    print('It is not possible to pay down payment in three years.')
else:
    print('Best savings rate: %.4f' % (bsr36(sal)[0]/10000))
    print('Steps in bisection search: %d' % (bsr36(sal)[1]))
