# -*- coding: utf-8 -*-
"""
Charles Thomas Wallace Truscott, Massachusetts Institute of Technology Student 6.0001  2022 Extracurricular Study

Thank you edX.org

github.com/ctwtruscottwatters

"""

import numpy
def sort_tup_list_sqr_root_primes(primes, f):
    primes_and_roots = []
    for n in primes:
        primes_and_roots.append((n, f(n)))
    return primes_and_roots

def bisection_sqr(prime):
    
    high = prime
    low = 0
    guess = (high + low) / 2.0
    while(round(abs((guess ** 2 - prime)), 5) >= 0.00001):
        #print("guess: {} high: {} low: {}".format(guess, high, low))
        if guess ** 2 > prime:
            high = guess
        elif guess ** 2 < prime:
            low = guess
        guess = (high + low) / 2.0
    
    return guess
def return_1000_primes():
    primes = []
    foundPrime = False
    for n in range(2, 1001, 1):
        for x in range(2, n, 1):
            if n % x == 0:
                foundPrime = False
                break
            else:
                foundPrime = True
        if foundPrime == True:
            primes.append(n)
        foundPrime = False
#    print(primes)
    return primes
def main():
    
    primes = return_1000_primes()
    x = sort_tup_list_sqr_root_primes(primes, bisection_sqr)
    for q in x:
        print("The square root of the prime number {} is {}".format(q[0], q[1]))
    for r in x:
        print("{} x {} is the prime number {}".format(r[1], r[1], round(r[1] * r[1], 5)))
#    diff = []
#    index = 0
#    for n in range(0, len(x), 1):
#        if n + 1 >= len(x):
#            break
#        else:
#            print("The difference between the square root of {} and {} is {}".format(x[n][0], x[n + 1][0], x[n][1] - x[n + 1][1]))
#            print("{} and {} are both consecutively occuring primes in the natural number set".format(x[n][0], x[n + 1][0]))
#            diff.append(x[n][1] - x[n + 1][1])
#    print("The mean of the differences of the consecutively occuring primes square roots are: {}; the median: {} the mode(s): {}".format(numpy.mean(diff), numpy.median(diff), numpy.unique(diff)))
#    
#    primeSum = 0
#    primeRootSum = 0
#    for s in x:
#        primeSum += s[0]
#        primeRootSum += s[1]
#    print("The sum of the primes that occur in the first 1000 natural numbers is {}".format(primeSum))
#    print("The sum of their square roots is: {}".format(primeRootSum))
#    rootSumisPrime = False
#    primeSumisPrime = False
#    for n in range(2, primeSum, 1):
#        if primeSum % n == 0:
#            break
#        else:
#            primeSumisPrime = True
#    for n in range(2, int(primeRootSum), 1):
#        if int(primeRootSum) % n == 0:
#            break
#        else:
#            rootSumisPrime = True
#            
#    if rootSumisPrime == True:
#        print("{} (The sum of the square roots of the primes that occur in the first 1000 natural numbers) is also prime".format(int(primeRootSum)))
#    if primeSumisPrime == True:
#        print("{} (The sum of the primes that occur in the first 1000 natural numbers) is also prime".format(primeSum))
#    print("Postulate: for all prime numbers in the natural number set the summation of the primes ascending to prime n is also prime")
#    print("{} {}".format(x[1][0], x[2][0]))
#    for z in range(0, len(x), 1):
#        if z + 1 >= len(x):
#            break
#        else:
#            sumofeachtwoprimes = int(x[z][0] + x[z + 1][0])
#        for pqrs in range(2, sumofeachtwoprimes):
#            if sumofeachtwoprimes % pqrs == 0:
#                continue
#        print("The sum of the two primes {} and {} (which is {}) is also prime".format(x[z][0], x[z + 1][0], x[z][0] + x[z + 1][0]))
if __name__ == "__main__": main()

"""

The square root of the prime number 3 is 1.7320518493652344
The square root of the prime number 5 is 2.2360682487487793
The square root of the prime number 7 is 2.645751476287842
The square root of the prime number 11 is 3.316624164581299
The square root of the prime number 13 is 3.6055508852005005
The square root of the prime number 17 is 4.123105049133301
The square root of the prime number 19 is 4.35889858007431
The square root of the prime number 23 is 4.795831024646759
The square root of the prime number 29 is 5.385165154933929
The square root of the prime number 31 is 5.567764461040497
The square root of the prime number 37 is 6.08276292681694
The square root of the prime number 41 is 6.403124392032623
The square root of the prime number 43 is 6.557438641786575
The square root of the prime number 47 is 6.855654686689377
The square root of the prime number 53 is 7.280109569430351
The square root of the prime number 59 is 7.681145817041397
The square root of the prime number 61 is 7.8102496191859245
The square root of the prime number 67 is 8.185352645814419
The square root of the prime number 71 is 8.426149889826775
The square root of the prime number 73 is 8.544003821909428
The square root of the prime number 79 is 8.888194307684898
The square root of the prime number 83 is 9.110433831810951
The square root of the prime number 89 is 9.433981321752071
The square root of the prime number 97 is 9.848857771605253
The square root of the prime number 101 is 10.049875549972057
The square root of the prime number 103 is 10.148891791701317
The square root of the prime number 107 is 10.344080422073603
The square root of the prime number 109 is 10.440306685864925
The square root of the prime number 113 is 10.630146011710167
The square root of the prime number 127 is 11.269427705556154
The square root of the prime number 131 is 11.445523295551538
The square root of the prime number 137 is 11.704700041562319
The square root of the prime number 139 is 11.789826013147831
The square root of the prime number 149 is 12.206555662676692
The square root of the prime number 151 is 12.288205670192838
The square root of the prime number 157 is 12.52996427565813
The square root of the prime number 163 is 12.767145270481706
The square root of the prime number 167 is 12.922847840934992
The square root of the prime number 173 is 13.152946569025517
The square root of the prime number 179 is 13.379088163375854
The square root of the prime number 181 is 13.453624175861478
The square root of the prime number 191 is 13.820275023579597
The square root of the prime number 193 is 13.892444040626287
The square root of the prime number 197 is 14.035668956115842
The square root of the prime number 199 is 14.10673601552844
The square root of the prime number 211 is 14.525839123874903
The square root of the prime number 223 is 14.933184357360005
The square root of the prime number 227 is 15.066519189625978
The square root of the prime number 229 is 15.132745963521302
The square root of the prime number 233 is 15.26433758251369
The square root of the prime number 239 is 15.459624878130853
The square root of the prime number 241 is 15.524174674414098
The square root of the prime number 251 is 15.842979525215924
The square root of the prime number 257 is 16.031219600699842
The square root of the prime number 263 is 16.217274676077068
The square root of the prime number 269 is 16.40121935494244
The square root of the prime number 271 is 16.462077704258263
The square root of the prime number 277 is 16.64331707917154
The square root of the prime number 281 is 16.763054604642093
The square root of the prime number 283 is 16.822603771463037
The square root of the prime number 293 is 17.117242730222642
The square root of the prime number 307 is 17.521415540017188
The square root of the prime number 311 is 17.635192110203207
The square root of the prime number 313 is 17.691805947571993
The square root of the prime number 317 is 17.804493785835803
The square root of the prime number 331 is 18.193405333906412
The square root of the prime number 337 is 18.35755969211459
The square root of the prime number 347 is 18.627935933880508
The square root of the prime number 349 is 18.681541660800576
The square root of the prime number 353 is 18.78829429205507
The square root of the prime number 359 is 18.947295317426324
The square root of the prime number 367 is 19.157244068570435
The square root of the prime number 373 is 19.31320783868432
The square root of the prime number 379 is 19.467922418378294
The square root of the prime number 383 is 19.570385713130236
The square root of the prime number 389 is 19.723082905169576
The square root of the prime number 397 is 19.92485889000818
The square root of the prime number 401 is 20.024984430521727
The square root of the prime number 409 is 20.223748352378607
The square root of the prime number 419 is 20.469489599578083
The square root of the prime number 421 is 20.518284537363797
The square root of the prime number 431 is 20.760539587587118
The square root of the prime number 433 is 20.808652031235397
The square root of the prime number 439 is 20.952326747588813
The square root of the prime number 443 is 21.047565136570483
The square root of the prime number 449 is 21.189620034303516
The square root of the prime number 457 is 21.377558324486017
The square root of the prime number 461 is 21.470910583157092
The square root of the prime number 463 is 21.517434821929783
The square root of the prime number 467 is 21.610182786360383
The square root of the prime number 479 is 21.886068549007177
The square root of the prime number 487 is 22.06807651137933
The square root of the prime number 491 is 22.15851972810924
The square root of the prime number 499 is 22.338307895231992
The square root of the prime number 503 is 22.427661432418972
The square root of the prime number 509 is 22.5610282975249
The square root of the prime number 521 is 22.82542446954176
The square root of the prime number 523 is 22.86919324216433
The square root of the prime number 541 is 23.259406608063728
The square root of the prime number 547 is 23.388031027279794
The square root of the prime number 557 is 23.600847456837073
The square root of the prime number 563 is 23.727621014695615
The square root of the prime number 569 is 23.853720939718187
The square root of the prime number 571 is 23.895606386475265
The square root of the prime number 577 is 24.020824291743338
The square root of the prime number 587 is 24.22808289155364
The square root of the prime number 593 is 24.351591389626265
The square root of the prime number 599 is 24.474476462695748
The square root of the prime number 601 is 24.515301308128983
The square root of the prime number 607 is 24.637370001291856
The square root of the prime number 613 is 24.75883677485399
The square root of the prime number 617 is 24.83948460407555
The square root of the prime number 619 is 24.87971063447185
The square root of the prime number 631 is 25.119713318534195
The square root of the prime number 641 is 25.317977827275172
The square root of the prime number 643 is 25.357444670051336
The square root of the prime number 647 is 25.436194715090096
The square root of the prime number 653 is 25.55386463040486
The square root of the prime number 659 is 25.670995318330824
The square root of the prime number 661 is 25.709920196328312
The square root of the prime number 673 is 25.94224345078692
The square root of the prime number 677 is 26.0192235824652
The square root of the prime number 683 is 26.13426864799112
The square root of the prime number 691 is 26.28687883168459
The square root of the prime number 701 is 26.476404600776732
The square root of the prime number 709 is 26.627053818199784
The square root of the prime number 719 is 26.814175347797573
The square root of the prime number 727 is 26.96293756365776
The square root of the prime number 733 is 27.07397279352881
The square root of the prime number 739 is 27.184554448816925
The square root of the prime number 743 is 27.258026302792132
The square root of the prime number 751 is 27.404379293555394
The square root of the prime number 757 is 27.51363306166604
The square root of the prime number 761 is 27.586228475673124
The square root of the prime number 769 is 27.730849259067327
The square root of the prime number 773 is 27.802877460606396
The square root of the prime number 787 is 28.053520328830928
The square root of the prime number 797 is 28.231188412522897
The square root of the prime number 809 is 28.442925373325124
The square root of the prime number 811 is 28.478061710484326
The square root of the prime number 821 is 28.65309753268957
The square root of the prime number 823 is 28.687976583722048
The square root of the prime number 827 is 28.757607620675117
The square root of the prime number 829 is 28.792360103689134
The square root of the prime number 839 is 28.965496733319014
The square root of the prime number 853 is 29.206163665978238
The square root of the prime number 857 is 29.274562330916524
The square root of the prime number 859 is 29.308701769215986
The square root of the prime number 863 is 29.376861634897068
The square root of the prime number 877 is 29.61418577900622
The square root of the prime number 881 is 29.68164419871755
The square root of the prime number 883 is 29.71531592134852
The square root of the prime number 887 is 29.782545207068324
The square root of the prime number 907 is 30.11644062027335
The square root of the prime number 911 is 30.182776568690315
The square root of the prime number 919 is 30.315012732055038
The square root of the prime number 929 is 30.479501298163086
The square root of the prime number 937 is 30.610455706133507
The square root of the prime number 941 is 30.6757232202217
The square root of the prime number 947 is 30.773365112952888
The square root of the prime number 953 is 30.87069805187639
The square root of the prime number 967 is 31.09662360022776
The square root of the prime number 971 is 31.160872955806553
The square root of the prime number 977 is 31.256999219185673
The square root of the prime number 983 is 31.35283079603687
The square root of the prime number 991 is 31.480152464355342
The square root of the prime number 997 is 31.57530679902993
1.7320518493652344 x 1.7320518493652344 is the prime number 3.0
2.2360682487487793 x 2.2360682487487793 is the prime number 5.0
2.645751476287842 x 2.645751476287842 is the prime number 7.0
3.316624164581299 x 3.316624164581299 is the prime number 11.0
3.6055508852005005 x 3.6055508852005005 is the prime number 13.0
4.123105049133301 x 4.123105049133301 is the prime number 17.0
4.35889858007431 x 4.35889858007431 is the prime number 19.0
4.795831024646759 x 4.795831024646759 is the prime number 23.0
5.385165154933929 x 5.385165154933929 is the prime number 29.0
5.567764461040497 x 5.567764461040497 is the prime number 31.0
6.08276292681694 x 6.08276292681694 is the prime number 37.0
6.403124392032623 x 6.403124392032623 is the prime number 41.0
6.557438641786575 x 6.557438641786575 is the prime number 43.0
6.855654686689377 x 6.855654686689377 is the prime number 47.0
7.280109569430351 x 7.280109569430351 is the prime number 53.0
7.681145817041397 x 7.681145817041397 is the prime number 59.0
7.8102496191859245 x 7.8102496191859245 is the prime number 61.0
8.185352645814419 x 8.185352645814419 is the prime number 67.0
8.426149889826775 x 8.426149889826775 is the prime number 71.0
8.544003821909428 x 8.544003821909428 is the prime number 73.0
8.888194307684898 x 8.888194307684898 is the prime number 79.0
9.110433831810951 x 9.110433831810951 is the prime number 83.0
9.433981321752071 x 9.433981321752071 is the prime number 89.0
9.848857771605253 x 9.848857771605253 is the prime number 97.0
10.049875549972057 x 10.049875549972057 is the prime number 101.0
10.148891791701317 x 10.148891791701317 is the prime number 103.0
10.344080422073603 x 10.344080422073603 is the prime number 107.0
10.440306685864925 x 10.440306685864925 is the prime number 109.0
10.630146011710167 x 10.630146011710167 is the prime number 113.0
11.269427705556154 x 11.269427705556154 is the prime number 127.0
11.445523295551538 x 11.445523295551538 is the prime number 131.0
11.704700041562319 x 11.704700041562319 is the prime number 137.0
11.789826013147831 x 11.789826013147831 is the prime number 139.0
12.206555662676692 x 12.206555662676692 is the prime number 149.0
12.288205670192838 x 12.288205670192838 is the prime number 151.0
12.52996427565813 x 12.52996427565813 is the prime number 157.0
12.767145270481706 x 12.767145270481706 is the prime number 163.0
12.922847840934992 x 12.922847840934992 is the prime number 167.0
13.152946569025517 x 13.152946569025517 is the prime number 173.0
13.379088163375854 x 13.379088163375854 is the prime number 179.0
13.453624175861478 x 13.453624175861478 is the prime number 181.0
13.820275023579597 x 13.820275023579597 is the prime number 191.0
13.892444040626287 x 13.892444040626287 is the prime number 193.0
14.035668956115842 x 14.035668956115842 is the prime number 197.0
14.10673601552844 x 14.10673601552844 is the prime number 199.0
14.525839123874903 x 14.525839123874903 is the prime number 211.0
14.933184357360005 x 14.933184357360005 is the prime number 223.0
15.066519189625978 x 15.066519189625978 is the prime number 227.0
15.132745963521302 x 15.132745963521302 is the prime number 229.0
15.26433758251369 x 15.26433758251369 is the prime number 233.0
15.459624878130853 x 15.459624878130853 is the prime number 239.0
15.524174674414098 x 15.524174674414098 is the prime number 241.0
15.842979525215924 x 15.842979525215924 is the prime number 251.0
16.031219600699842 x 16.031219600699842 is the prime number 257.0
16.217274676077068 x 16.217274676077068 is the prime number 263.0
16.40121935494244 x 16.40121935494244 is the prime number 269.0
16.462077704258263 x 16.462077704258263 is the prime number 271.0
16.64331707917154 x 16.64331707917154 is the prime number 277.0
16.763054604642093 x 16.763054604642093 is the prime number 281.0
16.822603771463037 x 16.822603771463037 is the prime number 283.0
17.117242730222642 x 17.117242730222642 is the prime number 293.0
17.521415540017188 x 17.521415540017188 is the prime number 307.0
17.635192110203207 x 17.635192110203207 is the prime number 311.0
17.691805947571993 x 17.691805947571993 is the prime number 313.0
17.804493785835803 x 17.804493785835803 is the prime number 317.0
18.193405333906412 x 18.193405333906412 is the prime number 331.0
18.35755969211459 x 18.35755969211459 is the prime number 337.0
18.627935933880508 x 18.627935933880508 is the prime number 347.0
18.681541660800576 x 18.681541660800576 is the prime number 349.0
18.78829429205507 x 18.78829429205507 is the prime number 353.0
18.947295317426324 x 18.947295317426324 is the prime number 359.0
19.157244068570435 x 19.157244068570435 is the prime number 367.0
19.31320783868432 x 19.31320783868432 is the prime number 373.0
19.467922418378294 x 19.467922418378294 is the prime number 379.0
19.570385713130236 x 19.570385713130236 is the prime number 383.0
19.723082905169576 x 19.723082905169576 is the prime number 389.0
19.92485889000818 x 19.92485889000818 is the prime number 397.0
20.024984430521727 x 20.024984430521727 is the prime number 401.0
20.223748352378607 x 20.223748352378607 is the prime number 409.0
20.469489599578083 x 20.469489599578083 is the prime number 419.0
20.518284537363797 x 20.518284537363797 is the prime number 421.0
20.760539587587118 x 20.760539587587118 is the prime number 431.0
20.808652031235397 x 20.808652031235397 is the prime number 433.0
20.952326747588813 x 20.952326747588813 is the prime number 439.0
21.047565136570483 x 21.047565136570483 is the prime number 443.0
21.189620034303516 x 21.189620034303516 is the prime number 449.0
21.377558324486017 x 21.377558324486017 is the prime number 457.0
21.470910583157092 x 21.470910583157092 is the prime number 461.0
21.517434821929783 x 21.517434821929783 is the prime number 463.0
21.610182786360383 x 21.610182786360383 is the prime number 467.0
21.886068549007177 x 21.886068549007177 is the prime number 479.0
22.06807651137933 x 22.06807651137933 is the prime number 487.0
22.15851972810924 x 22.15851972810924 is the prime number 491.0
22.338307895231992 x 22.338307895231992 is the prime number 499.0
22.427661432418972 x 22.427661432418972 is the prime number 503.0
22.5610282975249 x 22.5610282975249 is the prime number 509.0
22.82542446954176 x 22.82542446954176 is the prime number 521.0
22.86919324216433 x 22.86919324216433 is the prime number 523.0
23.259406608063728 x 23.259406608063728 is the prime number 541.0
23.388031027279794 x 23.388031027279794 is the prime number 547.0
23.600847456837073 x 23.600847456837073 is the prime number 557.0
23.727621014695615 x 23.727621014695615 is the prime number 563.0
23.853720939718187 x 23.853720939718187 is the prime number 569.0
23.895606386475265 x 23.895606386475265 is the prime number 571.0
24.020824291743338 x 24.020824291743338 is the prime number 577.0
24.22808289155364 x 24.22808289155364 is the prime number 587.0
24.351591389626265 x 24.351591389626265 is the prime number 593.0
24.474476462695748 x 24.474476462695748 is the prime number 599.0
24.515301308128983 x 24.515301308128983 is the prime number 601.0
24.637370001291856 x 24.637370001291856 is the prime number 607.0
24.75883677485399 x 24.75883677485399 is the prime number 613.0
24.83948460407555 x 24.83948460407555 is the prime number 617.0
24.87971063447185 x 24.87971063447185 is the prime number 619.0
25.119713318534195 x 25.119713318534195 is the prime number 631.0
25.317977827275172 x 25.317977827275172 is the prime number 641.0
25.357444670051336 x 25.357444670051336 is the prime number 643.0
25.436194715090096 x 25.436194715090096 is the prime number 647.0
25.55386463040486 x 25.55386463040486 is the prime number 653.0
25.670995318330824 x 25.670995318330824 is the prime number 659.0
25.709920196328312 x 25.709920196328312 is the prime number 661.0
25.94224345078692 x 25.94224345078692 is the prime number 673.0
26.0192235824652 x 26.0192235824652 is the prime number 677.0
26.13426864799112 x 26.13426864799112 is the prime number 683.0
26.28687883168459 x 26.28687883168459 is the prime number 691.0
26.476404600776732 x 26.476404600776732 is the prime number 701.0
26.627053818199784 x 26.627053818199784 is the prime number 709.0
26.814175347797573 x 26.814175347797573 is the prime number 719.0
26.96293756365776 x 26.96293756365776 is the prime number 727.0
27.07397279352881 x 27.07397279352881 is the prime number 733.0
27.184554448816925 x 27.184554448816925 is the prime number 739.0
27.258026302792132 x 27.258026302792132 is the prime number 743.0
27.404379293555394 x 27.404379293555394 is the prime number 751.0
27.51363306166604 x 27.51363306166604 is the prime number 757.0
27.586228475673124 x 27.586228475673124 is the prime number 761.0
27.730849259067327 x 27.730849259067327 is the prime number 769.0
27.802877460606396 x 27.802877460606396 is the prime number 773.0
28.053520328830928 x 28.053520328830928 is the prime number 787.0
28.231188412522897 x 28.231188412522897 is the prime number 797.0
28.442925373325124 x 28.442925373325124 is the prime number 809.0
28.478061710484326 x 28.478061710484326 is the prime number 811.0
28.65309753268957 x 28.65309753268957 is the prime number 821.0
28.687976583722048 x 28.687976583722048 is the prime number 823.0
28.757607620675117 x 28.757607620675117 is the prime number 827.0
28.792360103689134 x 28.792360103689134 is the prime number 829.0
28.965496733319014 x 28.965496733319014 is the prime number 839.0
29.206163665978238 x 29.206163665978238 is the prime number 853.0
29.274562330916524 x 29.274562330916524 is the prime number 857.0
29.308701769215986 x 29.308701769215986 is the prime number 859.0
29.376861634897068 x 29.376861634897068 is the prime number 863.0
29.61418577900622 x 29.61418577900622 is the prime number 877.0
29.68164419871755 x 29.68164419871755 is the prime number 881.0
29.71531592134852 x 29.71531592134852 is the prime number 883.0
29.782545207068324 x 29.782545207068324 is the prime number 887.0
30.11644062027335 x 30.11644062027335 is the prime number 907.0
30.182776568690315 x 30.182776568690315 is the prime number 911.0
30.315012732055038 x 30.315012732055038 is the prime number 919.0
30.479501298163086 x 30.479501298163086 is the prime number 929.0
30.610455706133507 x 30.610455706133507 is the prime number 937.0
30.6757232202217 x 30.6757232202217 is the prime number 941.0
30.773365112952888 x 30.773365112952888 is the prime number 947.0
30.87069805187639 x 30.87069805187639 is the prime number 953.0
31.09662360022776 x 31.09662360022776 is the prime number 967.0
31.160872955806553 x 31.160872955806553 is the prime number 971.0
31.256999219185673 x 31.256999219185673 is the prime number 977.0
31.35283079603687 x 31.35283079603687 is the prime number 983.0
31.480152464355342 x 31.480152464355342 is the prime number 991.0
31.57530679902993 x 31.57530679902993 is the prime number 997.0

"""

