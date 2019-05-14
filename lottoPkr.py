def lotteryPicker(numTix, picks, possible):
    import random
    import time
    import math
    possible += 1
    start_time = time.time()
    n = math.factorial(possible)
    k = math.factorial(picks)* math.factorial(possible-picks)
    combos = n/k
    comboStr= '{:,.0f}'.format(combos) 
    limit = 10000
    tix = min(numTix, limit)
    comTix = combos/tix
    odds = '{:,.0f}'.format(comTix) 
    print 'Calculating your winning numbers:'
    for i in range(tix):
        ints = sorted(random.sample(range(1, possible), picks))
        print ints

    print '\nYou have a %i in %s chance of winning the jackpot \nOr 1 in %s\nor a %f%% chance' % (tix, comboStr, odds, 100* (float(1.0)/float(comTix))) 
    output =  'This calculation took %s seconds' % round((time.time() - start_time),2)
    print output

lotteryPicker(100, 6, 49)
