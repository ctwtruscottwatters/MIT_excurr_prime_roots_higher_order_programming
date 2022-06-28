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
    diff = []
    index = 0
    for n in range(0, len(x), 1):
        if n + 1 >= len(x):
            break
        else:
            print("The difference between the square root of {} and {} is {}".format(x[n][0], x[n + 1][0], x[n + 1][1] - x[n][1]))
            print("{} and {} are both consecutively occuring primes in the natural number set".format(x[n][0], x[n + 1][0]))
            diff.append(x[n + 1][1] - x[n][1])
    print("The mean of the differences of the consecutively occuring primes square roots are: {}; the median: {} the mode(s): {}".format(numpy.mean(diff), numpy.median(diff), numpy.unique(diff)))
    
    primeSum = 0
    primeRootSum = 0
    for s in x:
        primeSum += s[0]
        primeRootSum += s[1]
    print("The sum of the primes that occur in the first 1000 natural numbers is {}".format(primeSum))
    print("The sum of their square roots is: {}".format(primeRootSum))

           
    print("Postulate: for all prime numbers in the natural number set the summation of the primes ascending to prime n is also prime")
    print("{} {}".format(x[1][0], x[2][0]))
    for z in range(0, len(x), 1):
        if z + 1 >= len(x):
            break
        else:
            sumofeachtwoprimes = int(x[z][0] + x[z + 1][0])
        for pqrs in range(2, sumofeachtwoprimes):
            if sumofeachtwoprimes % pqrs == 0:
                continue
        print("The sum of the two primes {} and {} is {}".format(x[z][0], x[z + 1][0], x[z][0] + x[z + 1][0]))
if __name__ == "__main__": main()


"""
The sum of the primes that occur in the first 1000 natural numbers is 76125 (can already see this is not a prime number, is divisible by 5)
The sum of their square roots is: 3306.354886138928


"""

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


"""
runfile('C:/Users/17/Downloads/prime_roots.py', wdir='C:/Users/17/Downloads')
The difference between the square root of 3 and 5 is 0.5040163993835449
3 and 5 are both consecutively occuring primes in the natural number set
The difference between the square root of 5 and 7 is 0.4096832275390625
5 and 7 are both consecutively occuring primes in the natural number set
The difference between the square root of 7 and 11 is 0.670872688293457
7 and 11 are both consecutively occuring primes in the natural number set
The difference between the square root of 11 and 13 is 0.28892672061920166
11 and 13 are both consecutively occuring primes in the natural number set
The difference between the square root of 13 and 17 is 0.5175541639328003
13 and 17 are both consecutively occuring primes in the natural number set
The difference between the square root of 17 and 19 is 0.23579353094100952
17 and 19 are both consecutively occuring primes in the natural number set
The difference between the square root of 19 and 23 is 0.43693244457244873
19 and 23 are both consecutively occuring primes in the natural number set
The difference between the square root of 23 and 29 is 0.5893341302871704
23 and 29 are both consecutively occuring primes in the natural number set
The difference between the square root of 29 and 31 is 0.18259930610656738
29 and 31 are both consecutively occuring primes in the natural number set
The difference between the square root of 31 and 37 is 0.5149984657764435
31 and 37 are both consecutively occuring primes in the natural number set
The difference between the square root of 37 and 41 is 0.320361465215683
37 and 41 are both consecutively occuring primes in the natural number set
The difference between the square root of 41 and 43 is 0.15431424975395203
41 and 43 are both consecutively occuring primes in the natural number set
The difference between the square root of 43 and 47 is 0.2982160449028015
43 and 47 are both consecutively occuring primes in the natural number set
The difference between the square root of 47 and 53 is 0.4244548827409744
47 and 53 are both consecutively occuring primes in the natural number set
The difference between the square root of 53 and 59 is 0.40103624761104584
53 and 59 are both consecutively occuring primes in the natural number set
The difference between the square root of 59 and 61 is 0.12910380214452744
59 and 61 are both consecutively occuring primes in the natural number set
The difference between the square root of 61 and 67 is 0.37510302662849426
61 and 67 are both consecutively occuring primes in the natural number set
The difference between the square root of 67 and 71 is 0.2407972440123558
67 and 71 are both consecutively occuring primes in the natural number set
The difference between the square root of 71 and 73 is 0.11785393208265305
71 and 73 are both consecutively occuring primes in the natural number set
The difference between the square root of 73 and 79 is 0.34419048577547073
73 and 79 are both consecutively occuring primes in the natural number set
The difference between the square root of 79 and 83 is 0.22223952412605286
79 and 83 are both consecutively occuring primes in the natural number set
The difference between the square root of 83 and 89 is 0.32354748994112015
83 and 89 are both consecutively occuring primes in the natural number set
The difference between the square root of 89 and 97 is 0.41487644985318184
89 and 97 are both consecutively occuring primes in the natural number set
The difference between the square root of 97 and 101 is 0.20101777836680412
97 and 101 are both consecutively occuring primes in the natural number set
The difference between the square root of 101 and 103 is 0.09901624172925949
101 and 103 are both consecutively occuring primes in the natural number set
The difference between the square root of 103 and 107 is 0.19518863037228584
103 and 107 are both consecutively occuring primes in the natural number set
The difference between the square root of 107 and 109 is 0.09622626379132271
107 and 109 are both consecutively occuring primes in the natural number set
The difference between the square root of 109 and 113 is 0.18983932584524155
109 and 113 are both consecutively occuring primes in the natural number set
The difference between the square root of 113 and 127 is 0.6392816938459873
113 and 127 are both consecutively occuring primes in the natural number set
The difference between the square root of 127 and 131 is 0.17609558999538422
127 and 131 are both consecutively occuring primes in the natural number set
The difference between the square root of 131 and 137 is 0.25917674601078033
131 and 137 are both consecutively occuring primes in the natural number set
The difference between the square root of 137 and 139 is 0.08512597158551216
137 and 139 are both consecutively occuring primes in the natural number set
The difference between the square root of 139 and 149 is 0.41672964952886105
139 and 149 are both consecutively occuring primes in the natural number set
The difference between the square root of 149 and 151 is 0.0816500075161457
149 and 151 are both consecutively occuring primes in the natural number set
The difference between the square root of 151 and 157 is 0.24175860546529293
151 and 157 are both consecutively occuring primes in the natural number set
The difference between the square root of 157 and 163 is 0.23718099482357502
157 and 163 are both consecutively occuring primes in the natural number set
The difference between the square root of 163 and 167 is 0.15570257045328617
163 and 167 are both consecutively occuring primes in the natural number set
The difference between the square root of 167 and 173 is 0.23009872809052467
167 and 173 are both consecutively occuring primes in the natural number set
The difference between the square root of 173 and 179 is 0.22614159435033798
173 and 179 are both consecutively occuring primes in the natural number set
The difference between the square root of 179 and 181 is 0.07453601248562336
179 and 181 are both consecutively occuring primes in the natural number set
The difference between the square root of 181 and 191 is 0.3666508477181196
181 and 191 are both consecutively occuring primes in the natural number set
The difference between the square root of 191 and 193 is 0.07216901704668999
191 and 193 are both consecutively occuring primes in the natural number set
The difference between the square root of 193 and 197 is 0.1432249154895544
193 and 197 are both consecutively occuring primes in the natural number set
The difference between the square root of 197 and 199 is 0.07106705941259861
197 and 199 are both consecutively occuring primes in the natural number set
The difference between the square root of 199 and 211 is 0.41910310834646225
199 and 211 are both consecutively occuring primes in the natural number set
The difference between the square root of 211 and 223 is 0.40734523348510265
211 and 223 are both consecutively occuring primes in the natural number set
The difference between the square root of 223 and 227 is 0.1333348322659731
223 and 227 are both consecutively occuring primes in the natural number set
The difference between the square root of 227 and 229 is 0.06622677389532328
227 and 229 are both consecutively occuring primes in the natural number set
The difference between the square root of 229 and 233 is 0.13159161899238825
229 and 233 are both consecutively occuring primes in the natural number set
The difference between the square root of 233 and 239 is 0.19528729561716318
233 and 239 are both consecutively occuring primes in the natural number set
The difference between the square root of 239 and 241 is 0.06454979628324509
239 and 241 are both consecutively occuring primes in the natural number set
The difference between the square root of 241 and 251 is 0.3188048508018255
241 and 251 are both consecutively occuring primes in the natural number set
The difference between the square root of 251 and 257 is 0.1882400754839182
251 and 257 are both consecutively occuring primes in the natural number set
The difference between the square root of 257 and 263 is 0.18605507537722588
257 and 263 are both consecutively occuring primes in the natural number set
The difference between the square root of 263 and 269 is 0.18394467886537313
263 and 269 are both consecutively occuring primes in the natural number set
The difference between the square root of 269 and 271 is 0.060858349315822124
269 and 271 are both consecutively occuring primes in the natural number set
The difference between the square root of 271 and 277 is 0.18123937491327524
271 and 277 are both consecutively occuring primes in the natural number set
The difference between the square root of 277 and 281 is 0.11973752547055483
277 and 281 are both consecutively occuring primes in the natural number set
The difference between the square root of 281 and 283 is 0.059549166820943356
281 and 283 are both consecutively occuring primes in the natural number set
The difference between the square root of 283 and 293 is 0.2946389587596059
283 and 293 are both consecutively occuring primes in the natural number set
The difference between the square root of 293 and 307 is 0.4041728097945452
293 and 307 are both consecutively occuring primes in the natural number set
The difference between the square root of 307 and 311 is 0.11377657018601894
307 and 311 are both consecutively occuring primes in the natural number set
The difference between the square root of 311 and 313 is 0.056613837368786335
311 and 313 are both consecutively occuring primes in the natural number set
The difference between the square root of 313 and 317 is 0.11268783826380968
313 and 317 are both consecutively occuring primes in the natural number set
The difference between the square root of 317 and 331 is 0.38891154807060957
317 and 331 are both consecutively occuring primes in the natural number set
The difference between the square root of 331 and 337 is 0.16415435820817947
331 and 337 are both consecutively occuring primes in the natural number set
The difference between the square root of 337 and 347 is 0.27037624176591635
337 and 347 are both consecutively occuring primes in the natural number set
The difference between the square root of 347 and 349 is 0.053605726920068264
347 and 349 are both consecutively occuring primes in the natural number set
The difference between the square root of 349 and 353 is 0.10675263125449419
349 and 353 are both consecutively occuring primes in the natural number set
The difference between the square root of 353 and 359 is 0.1590010253712535
353 and 359 are both consecutively occuring primes in the natural number set
The difference between the square root of 359 and 367 is 0.20994875114411116
359 and 367 are both consecutively occuring primes in the natural number set
The difference between the square root of 367 and 373 is 0.1559637701138854
367 and 373 are both consecutively occuring primes in the natural number set
The difference between the square root of 373 and 379 is 0.15471457969397306
373 and 379 are both consecutively occuring primes in the natural number set
The difference between the square root of 379 and 383 is 0.10246329475194216
379 and 383 are both consecutively occuring primes in the natural number set
The difference between the square root of 383 and 389 is 0.15269719203934073
383 and 389 are both consecutively occuring primes in the natural number set
The difference between the square root of 389 and 397 is 0.20177598483860493
389 and 397 are both consecutively occuring primes in the natural number set
The difference between the square root of 397 and 401 is 0.10012554051354527
397 and 401 are both consecutively occuring primes in the natural number set
The difference between the square root of 401 and 409 is 0.1987639218568802
401 and 409 are both consecutively occuring primes in the natural number set
The difference between the square root of 409 and 419 is 0.24574124719947577
409 and 419 are both consecutively occuring primes in the natural number set
The difference between the square root of 419 and 421 is 0.048794937785714865
419 and 421 are both consecutively occuring primes in the natural number set
The difference between the square root of 421 and 431 is 0.24225505022332072
421 and 431 are both consecutively occuring primes in the natural number set
The difference between the square root of 431 and 433 is 0.04811244364827871
431 and 433 are both consecutively occuring primes in the natural number set
The difference between the square root of 433 and 439 is 0.14367471635341644
433 and 439 are both consecutively occuring primes in the natural number set
The difference between the square root of 439 and 443 is 0.09523838898167014
439 and 443 are both consecutively occuring primes in the natural number set
The difference between the square root of 443 and 449 is 0.1420548977330327
443 and 449 are both consecutively occuring primes in the natural number set
The difference between the square root of 449 and 457 is 0.18793829018250108
449 and 457 are both consecutively occuring primes in the natural number set
The difference between the square root of 457 and 461 is 0.0933522586710751
457 and 461 are both consecutively occuring primes in the natural number set
The difference between the square root of 461 and 463 is 0.046524238772690296
461 and 463 are both consecutively occuring primes in the natural number set
The difference between the square root of 463 and 467 is 0.0927479644306004
463 and 467 are both consecutively occuring primes in the natural number set
The difference between the square root of 467 and 479 is 0.2758857626467943
467 and 479 are both consecutively occuring primes in the natural number set
The difference between the square root of 479 and 487 is 0.182007962372154
479 and 487 are both consecutively occuring primes in the natural number set
The difference between the square root of 487 and 491 is 0.09044321672990918
487 and 491 are both consecutively occuring primes in the natural number set
The difference between the square root of 491 and 499 is 0.17978816712275147
491 and 499 are both consecutively occuring primes in the natural number set
The difference between the square root of 499 and 503 is 0.08935353718698025
499 and 503 are both consecutively occuring primes in the natural number set
The difference between the square root of 503 and 509 is 0.133366865105927
503 and 509 are both consecutively occuring primes in the natural number set
The difference between the square root of 509 and 521 is 0.26439617201685905
509 and 521 are both consecutively occuring primes in the natural number set
The difference between the square root of 521 and 523 is 0.043768772622570395
521 and 523 are both consecutively occuring primes in the natural number set
The difference between the square root of 523 and 541 is 0.3902133658993989
523 and 541 are both consecutively occuring primes in the natural number set
The difference between the square root of 541 and 547 is 0.1286244192160666
541 and 547 are both consecutively occuring primes in the natural number set
The difference between the square root of 547 and 557 is 0.21281642955727875
547 and 557 are both consecutively occuring primes in the natural number set
The difference between the square root of 557 and 563 is 0.1267735578585416
557 and 563 are both consecutively occuring primes in the natural number set
The difference between the square root of 563 and 569 is 0.12609992502257228
563 and 569 are both consecutively occuring primes in the natural number set
The difference between the square root of 569 and 571 is 0.04188544675707817
569 and 571 are both consecutively occuring primes in the natural number set
The difference between the square root of 571 and 577 is 0.12521790526807308
571 and 577 are both consecutively occuring primes in the natural number set
The difference between the square root of 577 and 587 is 0.20725859981030226
577 and 587 are both consecutively occuring primes in the natural number set
The difference between the square root of 587 and 593 is 0.1235084980726242
587 and 593 are both consecutively occuring primes in the natural number set
The difference between the square root of 593 and 599 is 0.12288507306948304
593 and 599 are both consecutively occuring primes in the natural number set
The difference between the square root of 599 and 601 is 0.04082484543323517
599 and 601 are both consecutively occuring primes in the natural number set
The difference between the square root of 601 and 607 is 0.12206869316287339
601 and 607 are both consecutively occuring primes in the natural number set
The difference between the square root of 607 and 613 is 0.12146677356213331
607 and 613 are both consecutively occuring primes in the natural number set
The difference between the square root of 613 and 617 is 0.08064782922156155
613 and 617 are both consecutively occuring primes in the natural number set
The difference between the square root of 617 and 619 is 0.040226030396297574
617 and 619 are both consecutively occuring primes in the natural number set
The difference between the square root of 619 and 631 is 0.24000268406234682
619 and 631 are both consecutively occuring primes in the natural number set
The difference between the square root of 631 and 641 is 0.19826450874097645
631 and 641 are both consecutively occuring primes in the natural number set
The difference between the square root of 641 and 643 is 0.03946684277616441
641 and 643 are both consecutively occuring primes in the natural number set
The difference between the square root of 643 and 647 is 0.07875004503875971
643 and 647 are both consecutively occuring primes in the natural number set
The difference between the square root of 647 and 653 is 0.11766991531476378
647 and 653 are both consecutively occuring primes in the natural number set
The difference between the square root of 653 and 659 is 0.1171306879259646
653 and 659 are both consecutively occuring primes in the natural number set
The difference between the square root of 659 and 661 is 0.03892487799748778
659 and 661 are both consecutively occuring primes in the natural number set
The difference between the square root of 661 and 673 is 0.23232325445860624
661 and 673 are both consecutively occuring primes in the natural number set
The difference between the square root of 673 and 677 is 0.07698013167828321
673 and 677 are both consecutively occuring primes in the natural number set
The difference between the square root of 677 and 683 is 0.1150450655259192
677 and 683 are both consecutively occuring primes in the natural number set
The difference between the square root of 683 and 691 is 0.15261018369346857
683 and 691 are both consecutively occuring primes in the natural number set
The difference between the square root of 691 and 701 is 0.18952576909214258
691 and 701 are both consecutively occuring primes in the natural number set
The difference between the square root of 701 and 709 is 0.1506492174230516
701 and 709 are both consecutively occuring primes in the natural number set
The difference between the square root of 709 and 719 is 0.18712152959778905
709 and 719 are both consecutively occuring primes in the natural number set
The difference between the square root of 719 and 727 is 0.148762215860188
719 and 727 are both consecutively occuring primes in the natural number set
The difference between the square root of 727 and 733 is 0.11103522987104952
727 and 733 are both consecutively occuring primes in the natural number set
The difference between the square root of 733 and 739 is 0.11058165528811514
733 and 739 are both consecutively occuring primes in the natural number set
The difference between the square root of 739 and 743 is 0.07347185397520661
739 and 743 are both consecutively occuring primes in the natural number set
The difference between the square root of 743 and 751 is 0.14635299076326191
743 and 751 are both consecutively occuring primes in the natural number set
The difference between the square root of 751 and 757 is 0.1092537681106478
751 and 757 are both consecutively occuring primes in the natural number set
The difference between the square root of 757 and 761 is 0.07259541400708258
757 and 761 are both consecutively occuring primes in the natural number set
The difference between the square root of 761 and 769 is 0.1446207833942026
761 and 769 are both consecutively occuring primes in the natural number set
The difference between the square root of 769 and 773 is 0.07202820153906941
769 and 773 are both consecutively occuring primes in the natural number set
The difference between the square root of 773 and 787 is 0.2506428682245314
773 and 787 are both consecutively occuring primes in the natural number set
The difference between the square root of 787 and 797 is 0.17766808369196951
787 and 797 are both consecutively occuring primes in the natural number set
The difference between the square root of 797 and 809 is 0.21173696080222726
797 and 809 are both consecutively occuring primes in the natural number set
The difference between the square root of 809 and 811 is 0.0351363371592015
809 and 811 are both consecutively occuring primes in the natural number set
The difference between the square root of 811 and 821 is 0.1750358222052455
811 and 821 are both consecutively occuring primes in the natural number set
The difference between the square root of 821 and 823 is 0.03487905103247613
821 and 823 are both consecutively occuring primes in the natural number set
The difference between the square root of 823 and 827 is 0.06963103695306927
823 and 827 are both consecutively occuring primes in the natural number set
The difference between the square root of 827 and 829 is 0.034752483014017344
827 and 829 are both consecutively occuring primes in the natural number set
The difference between the square root of 829 and 839 is 0.1731366296298802
829 and 839 are both consecutively occuring primes in the natural number set
The difference between the square root of 839 and 853 is 0.24066693265922368
839 and 853 are both consecutively occuring primes in the natural number set
The difference between the square root of 853 and 857 is 0.06839866493828595
853 and 857 are both consecutively occuring primes in the natural number set
The difference between the square root of 857 and 859 is 0.0341394382994622
857 and 859 are both consecutively occuring primes in the natural number set
The difference between the square root of 859 and 863 is 0.06815986568108201
859 and 863 are both consecutively occuring primes in the natural number set
The difference between the square root of 863 and 877 is 0.23732414410915226
863 and 877 are both consecutively occuring primes in the natural number set
The difference between the square root of 877 and 881 is 0.06745841971132904
877 and 881 are both consecutively occuring primes in the natural number set
The difference between the square root of 881 and 883 is 0.03367172263097018
881 and 883 are both consecutively occuring primes in the natural number set
The difference between the square root of 883 and 887 is 0.06722928571980447
883 and 887 are both consecutively occuring primes in the natural number set
The difference between the square root of 887 and 907 is 0.3338954132050276
887 and 907 are both consecutively occuring primes in the natural number set
The difference between the square root of 907 and 911 is 0.06633594841696322
907 and 911 are both consecutively occuring primes in the natural number set
The difference between the square root of 911 and 919 is 0.13223616336472332
911 and 919 are both consecutively occuring primes in the natural number set
The difference between the square root of 919 and 929 is 0.16448856610804796
919 and 929 are both consecutively occuring primes in the natural number set
The difference between the square root of 929 and 937 is 0.13095440797042102
929 and 937 are both consecutively occuring primes in the natural number set
The difference between the square root of 937 and 941 is 0.06526751408819109
937 and 941 are both consecutively occuring primes in the natural number set
The difference between the square root of 941 and 947 is 0.09764189273118973
941 and 947 are both consecutively occuring primes in the natural number set
The difference between the square root of 947 and 953 is 0.09733293892350048
947 and 953 are both consecutively occuring primes in the natural number set
The difference between the square root of 953 and 967 is 0.2259255483513698
953 and 967 are both consecutively occuring primes in the natural number set
The difference between the square root of 967 and 971 is 0.06424935557879508
967 and 971 are both consecutively occuring primes in the natural number set
The difference between the square root of 971 and 977 is 0.09612626337911934
971 and 977 are both consecutively occuring primes in the natural number set
The difference between the square root of 977 and 983 is 0.09583157685119659
977 and 983 are both consecutively occuring primes in the natural number set
The difference between the square root of 983 and 991 is 0.1273216683184728
983 and 991 are both consecutively occuring primes in the natural number set
The difference between the square root of 991 and 997 is 0.09515433467458934
991 and 997 are both consecutively occuring primes in the natural number set
The mean of the differences of the consecutively occuring primes square roots are: 0.17977864427508852; the median: 0.14548688707873225 the mode(s): [0.03367172 0.03413944 0.03475248 0.03487905 0.03513634 0.03892488
 0.03946684 0.04022603 0.04082485 0.04188545 0.04376877 0.04652424
 0.04811244 0.04879494 0.05360573 0.05661384 0.05954917 0.06085835
 0.06424936 0.0645498  0.06526751 0.06622677 0.06633595 0.06722929
 0.06745842 0.06815987 0.06839866 0.06963104 0.07106706 0.0720282
 0.07216902 0.07259541 0.07347185 0.07453601 0.07698013 0.07875005
 0.08064783 0.08165001 0.08512597 0.08935354 0.09044322 0.09274796
 0.09335226 0.09515433 0.09523839 0.09583158 0.09612626 0.09622626
 0.09733294 0.09764189 0.09901624 0.10012554 0.10246329 0.10675263
 0.10925377 0.11058166 0.11103523 0.11268784 0.11377657 0.11504507
 0.11713069 0.11766992 0.11785393 0.11973753 0.12146677 0.12206869
 0.12288507 0.1235085  0.12521791 0.12609993 0.12677356 0.12732167
 0.12862442 0.1291038  0.13095441 0.13159162 0.13223616 0.13333483
 0.13336687 0.1420549  0.14322492 0.14367472 0.14462078 0.14635299
 0.14876222 0.15064922 0.15261018 0.15269719 0.15431425 0.15471458
 0.15570257 0.15596377 0.15900103 0.16415436 0.16448857 0.17313663
 0.17503582 0.17609559 0.17766808 0.17978817 0.18123937 0.18200796
 0.18259931 0.18394468 0.18605508 0.18712153 0.18793829 0.18824008
 0.18952577 0.18983933 0.19518863 0.1952873  0.19826451 0.19876392
 0.20101778 0.20177598 0.2072586  0.20994875 0.21173696 0.21281643
 0.22223952 0.22592555 0.22614159 0.23009873 0.23232325 0.23579353
 0.23718099 0.23732414 0.24000268 0.24066693 0.24079724 0.24175861
 0.24225505 0.24574125 0.25064287 0.25917675 0.26439617 0.27037624
 0.27588576 0.28892672 0.29463896 0.29821604 0.31880485 0.32036147
 0.32354749 0.33389541 0.34419049 0.36665085 0.37510303 0.38891155
 0.39021337 0.40103625 0.40417281 0.40734523 0.40968323 0.41487645
 0.41672965 0.41910311 0.42445488 0.43693244 0.5040164  0.51499847
 0.51755416 0.58933413 0.63928169 0.67087269]

"""