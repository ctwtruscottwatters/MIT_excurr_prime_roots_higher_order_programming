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
    for n in range(1000, 2, -1):
        for x in range(2, n, 1):
            if n % x == 0:
                break
            elif (n % x != 0) and (n in primes) == False:
                primes.append(n)
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
            print("The difference between the square root of {} and {} is {}".format(x[n][0], x[n + 1][0], x[n][1] - x[n + 1][1]))
            print("{} and {} are both consecutively occuring primes in the natural number set".format(x[n][0], x[n + 1][0]))
            diff.append(x[n][1] - x[n + 1][1])
    print("The mean of the differences of the consecutively occuring primes square roots are: {}; the median: {} the mode(s): {}".format(numpy.mean(diff), numpy.median(diff), numpy.unique(diff)))
    
    primeSum = 0
    primeRootSum = 0
    for s in x:
        primeSum += s[0]
        primeRootSum += s[1]
    print("The sum of the primes that occur in the first 1000 natural numbers is {}".format(primeSum))
    print("The sum of their square roots is: {}".format(primeRootSum))
    rootSumisPrime = False
    primeSumisPrime = False
    for n in range(2, primeSum, 1):
        if primeSum % n == 0:
            break
        else:
            primeSumisPrime = True
    for n in range(2, int(primeRootSum), 1):
        if int(primeRootSum) % n == 0:
            break
        else:
            rootSumisPrime = True
            
    if rootSumisPrime == True:
        print("{} (The sum of the square roots of the primes that occur in the first 1000 natural numbers) is also prime".format(int(primeRootSum)))
    if primeSumisPrime == True:
        print("{} (The sum of the primes that occur in the first 1000 natural numbers) is also prime".format(primeSum))
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
            else:
                print("The sum of the two primes {} and {} (which is {}) is also prime".format(x[z][0], x[z + 1][0], x[z][0] + x[z + 1][0]))
if __name__ == "__main__": main()

""" 
Square roots of the primes occuring in the first ~1000 natural (counting) numbers 

Eager to find an numerical algorithm to generate or approximate up to so many primes in the natural and real and complex number systems such as Ramanujan\'s notebooks have formulas for approximating pi, sine, cosine, tangent and inverse sine, cosine, tangent and their hyperbolic counterparts

Charles Thomas Wallace Truscott, Byron Bay NSW 2481

The square root of the prime number 997 is 31.57530679902993
The square root of the prime number 995 is 31.543620609445497

etc ...

The square root of the prime number 105 is 10.246950723230839
The square root of the prime number 103 is 10.148891791701317
The square root of the prime number 101 is 10.049875549972057
The square root of the prime number 99 is 9.949874214828014
The square root of the prime number 97 is 9.848857771605253
The square root of the prime number 95 is 9.74679410457611
The square root of the prime number 93 is 9.643650725483894
The square root of the prime number 91 is 9.539392076432705
The square root of the prime number 89 is 9.433981321752071
The square root of the prime number 87 is 9.327379144728184
The square root of the prime number 85 is 9.21954471617937
The square root of the prime number 83 is 9.110433831810951
The square root of the prime number 81 is 9.000000067055225
The square root of the prime number 79 is 8.888194307684898
The square root of the prime number 77 is 8.774964585900307
The square root of the prime number 75 is 8.660253882408142
The square root of the prime number 73 is 8.544003821909428
The square root of the prime number 71 is 8.426149889826775
The square root of the prime number 69 is 8.30662402510643

etc ...

The square root of the prime number 33 is 5.744562774896622
The square root of the prime number 31 is 5.567764461040497
The square root of the prime number 29 is 5.385165154933929
The square root of the prime number 27 is 5.196152865886688
The square root of the prime number 25 is 4.999999701976776
The square root of the prime number 23 is 4.795831024646759
The square root of the prime number 21 is 4.582576096057892
The square root of the prime number 19 is 4.35889858007431
The square root of the prime number 17 is 4.123105049133301
The square root of the prime number 15 is 3.8729828596115112
The square root of the prime number 13 is 3.6055508852005005
The square root of the prime number 11 is 3.316624164581299
The square root of the prime number 9 is 2.9999992847442627
The square root of the prime number 7 is 2.645751476287842
The square root of the prime number 5 is 2.2360682487487793
The square root of the prime number 3 is 1.7320518493652344

31.57530679902993 x 31.57530679902993 is the prime number 997.0
31.543620609445497 x 31.543620609445497 is the prime number 995.0
31.511902536149137 x 31.511902536149137 is the prime number 993.0
31.480152464355342 x 31.480152464355342 is the prime number 991.0
... etc ... 
1.7320518493652344 x 1.7320518493652344 is the prime number 3.0

etc ...

113 and 111 are both consecutively occuring primes in the natural number set
The difference between the square root of 111 and 109 is 0.0953470915555954
111 and 109 are both consecutively occuring primes in the natural number set
The difference between the square root of 109 and 107 is 0.09622626379132271
109 and 107 are both consecutively occuring primes in the natural number set
The difference between the square root of 107 and 105 is 0.0971296988427639
107 and 105 are both consecutively occuring primes in the natural number set
The difference between the square root of 105 and 103 is 0.09805893152952194
105 and 103 are both consecutively occuring primes in the natural number set
The difference between the square root of 103 and 101 is 0.09901624172925949
103 and 101 are both consecutively occuring primes in the natural number set
The difference between the square root of 101 and 99 is 0.10000133514404297
101 and 99 are both consecutively occuring primes in the natural number set
The difference between the square root of 99 and 97 is 0.10101644322276115
99 and 97 are both consecutively occuring primes in the natural number set
The difference between the square root of 97 and 95 is 0.10206366702914238
97 and 95 are both consecutively occuring primes in the natural number set
The difference between the square root of 95 and 93 is 0.10314337909221649
95 and 93 are both consecutively occuring primes in the natural number set
The difference between the square root of 93 and 91 is 0.10425864905118942
93 and 91 are both consecutively occuring primes in the natural number set
The difference between the square root of 91 and 89 is 0.10541075468063354
91 and 89 are both consecutively occuring primes in the natural number set
The difference between the square root of 89 and 87 is 0.10660217702388763
89 and 87 are both consecutively occuring primes in the natural number set
The difference between the square root of 87 and 85 is 0.10783442854881287
87 and 85 are both consecutively occuring primes in the natural number set
The difference between the square root of 85 and 83 is 0.10911088436841965
85 and 83 are both consecutively occuring primes in the natural number set
The difference between the square root of 83 and 81 is 0.11043376475572586
83 and 81 are both consecutively occuring primes in the natural number set
The difference between the square root of 81 and 79 is 0.111805759370327
81 and 79 are both consecutively occuring primes in the natural number set
The difference between the square root of 79 and 77 is 0.11322972178459167
79 and 77 are both consecutively occuring primes in the natural number set
The difference between the square root of 77 and 75 is 0.11471070349216461
77 and 75 are both consecutively occuring primes in the natural number set
The difference between the square root of 75 and 73 is 0.11625006049871445
75 and 73 are both consecutively occuring primes in the natural number set
The difference between the square root of 73 and 71 is 0.11785393208265305
73 and 71 are both consecutively occuring primes in the natural number set
The difference between the square root of 71 and 69 is 0.11952586472034454
71 and 69 are both consecutively occuring primes in the natural number set
The difference between the square root of 69 and 67 is 0.12127137929201126
69 and 67 are both consecutively occuring primes in the natural number set
The difference between the square root of 67 and 65 is 0.12309502810239792
67 and 65 are both consecutively occuring primes in the natural number set
The difference between the square root of 65 and 63 is 0.12500381469726562
65 and 63 are both consecutively occuring primes in the natural number set
The difference between the square root of 63 and 61 is 0.12700418382883072
63 and 61 are both consecutively occuring primes in the natural number set
The difference between the square root of 61 and 59 is 0.12910380214452744
61 and 59 are both consecutively occuring primes in the natural number set
The difference between the square root of 59 and 57 is 0.1313115358352661
59 and 57 are both consecutively occuring primes in the natural number set
The difference between the square root of 57 and 55 is 0.13363610208034515
57 and 55 are both consecutively occuring primes in the natural number set
The difference between the square root of 55 and 53 is 0.13608860969543457
55 and 53 are both consecutively occuring primes in the natural number set
The difference between the square root of 53 and 51 is 0.1386808156967163
53 and 51 are both consecutively occuring primes in the natural number set
The difference between the square root of 51 and 49 is 0.14142844080924988
51 and 49 are both consecutively occuring primes in the natural number set
The difference between the square root of 49 and 47 is 0.14434562623500824
49 and 47 are both consecutively occuring primes in the natural number set
The difference between the square root of 47 and 45 is 0.14745061099529266
47 and 45 are both consecutively occuring primes in the natural number set
The difference between the square root of 45 and 43 is 0.15076543390750885
45 and 43 are both consecutively occuring primes in the natural number set
The difference between the square root of 43 and 41 is 0.15431424975395203
43 and 41 are both consecutively occuring primes in the natural number set
The difference between the square root of 41 and 39 is 0.15812668204307556
41 and 39 are both consecutively occuring primes in the natural number set
The difference between the square root of 39 and 37 is 0.16223478317260742
39 and 37 are both consecutively occuring primes in the natural number set
The difference between the square root of 37 and 35 is 0.1666833460330963
37 and 35 are both consecutively occuring primes in the natural number set
The difference between the square root of 35 and 33 is 0.1715168058872223
35 and 33 are both consecutively occuring primes in the natural number set
The difference between the square root of 33 and 31 is 0.17679831385612488
33 and 31 are both consecutively occuring primes in the natural number set
The difference between the square root of 31 and 29 is 0.18259930610656738
31 and 29 are both consecutively occuring primes in the natural number set
The difference between the square root of 29 and 27 is 0.1890122890472412
29 and 27 are both consecutively occuring primes in the natural number set
The difference between the square root of 27 and 25 is 0.1961531639099121
27 and 25 are both consecutively occuring primes in the natural number set
The difference between the square root of 25 and 23 is 0.2041686773300171
25 and 23 are both consecutively occuring primes in the natural number set
The difference between the square root of 23 and 21 is 0.2132549285888672
23 and 21 are both consecutively occuring primes in the natural number set
The difference between the square root of 21 and 19 is 0.22367751598358154
21 and 19 are both consecutively occuring primes in the natural number set
The difference between the square root of 19 and 17 is 0.23579353094100952
19 and 17 are both consecutively occuring primes in the natural number set
The difference between the square root of 17 and 15 is 0.25012218952178955
17 and 15 are both consecutively occuring primes in the natural number set
The difference between the square root of 15 and 13 is 0.26743197441101074
15 and 13 are both consecutively occuring primes in the natural number set
The difference between the square root of 13 and 11 is 0.28892672061920166
13 and 11 are both consecutively occuring primes in the natural number set
The difference between the square root of 11 and 9 is 0.31662487983703613
11 and 9 are both consecutively occuring primes in the natural number set
The difference between the square root of 9 and 7 is 0.3542478084564209
9 and 7 are both consecutively occuring primes in the natural number set
The difference between the square root of 7 and 5 is 0.4096832275390625
7 and 5 are both consecutively occuring primes in the natural number set
The difference between the square root of 5 and 3 is 0.5040163993835449
5 and 3 are both consecutively occuring primes in the natural number set
The mean of the differences of the consecutively occuring primes square roots are: 0.05998977807810508; the median: 0.044676768593490124 the mode(s): [0.03165453 0.03168619 0.03171807 0.03175007 0.03178207 0.03181431
 0.03184645 0.03187883 0.03191135 0.03194377 0.03197646 0.03200917
 0.03204215 0.03207494 0.03210812 0.03214123 0.03217452 0.03220774
 0.03224137 0.03227484 0.0323086  0.03234222 0.03237625 0.03241015
 0.03244436 0.03247843 0.03251283 0.03254723 0.03258183 0.03261634
 0.03265118 0.03268603 0.0327209  0.03275612 0.03279136 0.03282664
 0.03286196 0.03289764 0.03293327 0.03296905 0.0330049  0.03304091
 0.0330771  0.03311326 0.03314971 0.03318624 0.03322265 0.03325959
 0.03329641 0.03333334 0.03337038 0.03340764 0.03344502 0.03348254
 0.03351998 0.03355787 0.0335957  0.03363358 0.03367172 0.03371003
 0.03374839 0.03378694 0.03382546 0.03386427 0.03390317 0.03394217
 0.03398147 0.03402068 0.03406011 0.03409976 0.03413944 0.03417935
 0.03421931 0.03425932 0.03429978 0.0343401  0.0343807  0.03442156
 0.03446222 0.03450326 0.03454449 0.03458573 0.03462709 0.03466876
 0.03471055 0.03475248 0.03479436 0.03483668 0.03487905 0.03492149
 0.0349642  0.0350069  0.03505007 0.03509315 0.03513634 0.03518002
 0.03522344 0.03526728 0.03531117 0.03535548 0.03539958 0.03544412
 0.03548855 0.03553345 0.03557844 0.03562353 0.03566893 0.03571427
 0.03575992 0.03580572 0.03585185 0.03589777 0.03594441 0.03599069
 0.03603751 0.03608436 0.03613159 0.03617867 0.03622617 0.0362739
 0.03632152 0.03636975 0.03641789 0.03646613 0.03651501 0.03656348
 0.03661261 0.03666188 0.03671113 0.03676072 0.03681048 0.0368606
 0.03691057 0.0369611  0.03701167 0.03706247 0.03711351 0.03716481
 0.03721603 0.03726787 0.03731966 0.03737175 0.03742415 0.03747654
 0.03752944 0.03758218 0.03763562 0.03768877 0.03774264 0.03779641
 0.0378506  0.03790488 0.0379596  0.03801428 0.03806943 0.03812456
 0.03818019 0.038236   0.03829201 0.03834823 0.03840483 0.03846152
 0.03851862 0.03857567 0.03863348 0.03869113 0.03874925 0.03880754
 0.03886618 0.03892488 0.03898411 0.03904343 0.03910315 0.03916301
 0.03922315 0.03928376 0.03934454 0.03940551 0.03946684 0.03952855
 0.03959036 0.03965259 0.0397151  0.03977791 0.03984089 0.03990436
 0.03996804 0.04003211 0.04009642 0.04016086 0.04022603 0.04029108
 0.04035675 0.04042263 0.04048875 0.0405554  0.04062218 0.04068941
 0.0407571  0.04082485 0.04089296 0.04096174 0.04103037 0.04109986
 0.04116938 0.04123926 0.04130963 0.0413804  0.04145131 0.04152266
 0.04159461 0.04166665 0.04173921 0.04181204 0.04188545 0.04195918
 0.04203314 0.04210761 0.04218237 0.04225783 0.04233336 0.04240953
 0.04248584 0.04256296 0.04264002 0.04271809 0.0427959  0.04287478
 0.04295373 0.04303305 0.043113   0.04319364 0.04327423 0.04335544
 0.04343731 0.04351937 0.04360214 0.04368518 0.04376877 0.04385294
 0.04393749 0.04402257 0.04410823 0.04419413 0.04428081 0.04436782
 0.04445544 0.0445436  0.0446321  0.04472144 0.04481098 0.04490145
 0.04499221 0.04508352 0.04517544 0.04526778 0.04536104 0.04545458
 0.0455487  0.04564364 0.0457388  0.04583512 0.04593153 0.04602875
 0.04612661 0.04622495 0.04632404 0.04642393 0.04652424 0.04662525
 0.04672701 0.04682937 0.04693239 0.04703591 0.04714063 0.04724555
 0.04735138 0.04745796 0.04756516 0.04767323 0.04778185 0.04789128
 0.04800159 0.04811244 0.04822432 0.04833688 0.04845021 0.04856438
 0.04867926 0.04879494 0.04891168 0.04902918 0.04914733 0.04926659
 0.04938647 0.04950743 0.04962919 0.04975184 0.04987545 0.05000013
 0.05012541 0.05025193 0.05037943 0.05050763 0.050637   0.05076728
 0.05089875 0.05103116 0.05116443 0.05129886 0.05143455 0.05157126
 0.05170876 0.05184752 0.05198748 0.05212876 0.0522708  0.05241442
 0.05255888 0.05270466 0.05285172 0.05299988 0.05314943 0.05330018
 0.05345245 0.05360573 0.05376033 0.05391641 0.05407381 0.05423267
 0.05439302 0.05455438 0.05471772 0.05488226 0.05504819 0.05521569
 0.0553851  0.05555568 0.0557278  0.05590166 0.05607743 0.05625446
 0.05643338 0.05661384 0.05679634 0.05698023 0.05716634 0.05735403
 0.05754355 0.05773515 0.05792851 0.05812391 0.05832132 0.05852074
 0.05872192 0.05892568 0.05913149 0.05933913 0.05954917 0.05976139
 0.05997613 0.06019318 0.06041212 0.06063407 0.06085835 0.06108483
 0.0613139  0.06154594 0.06178035 0.06201753 0.0622572  0.06250024
 0.06274567 0.06299417 0.06324575 0.06350018 0.06375772 0.06401864
 0.06428257 0.0645498  0.06482066 0.06509439 0.06537224 0.06565328
 0.06593834 0.06622677 0.06651925 0.06681559 0.06711546 0.06742042
 0.06772872 0.06804158 0.06835856 0.06868049 0.06900683 0.06933768
 0.06967355 0.07001423 0.07036011 0.07071071 0.07106706 0.07142875
 0.07179617 0.07216902 0.07254779 0.07293301 0.07332387 0.07372102
 0.07412515 0.07453601 0.07495342 0.07537827 0.0758099  0.07624966
 0.07669705 0.07715201 0.07761521 0.07808737 0.07856781 0.07905719
 0.07955599 0.08006449 0.08058283 0.08111128 0.08165001 0.08220015
 0.08276107 0.08333371 0.08391864 0.08451608 0.08512597 0.08575004
 0.08638741 0.0870393  0.08770663 0.08838896 0.08908786 0.08980332
 0.09053665 0.09128772 0.09205819 0.09284882 0.09365914 0.09449223
 0.09534709 0.09622626 0.0971297  0.09805893 0.09901624 0.10000134
 0.10101644 0.10206367 0.10314338 0.10425865 0.10541075 0.10660218
 0.10783443 0.10911088 0.11043376 0.11180576 0.11322972 0.1147107
 0.11625006 0.11785393 0.11952586 0.12127138 0.12309503 0.12500381
 0.12700418 0.1291038  0.13131154 0.1336361  0.13608861 0.13868082
 0.14142844 0.14434563 0.14745061 0.15076543 0.15431425 0.15812668
 0.16223478 0.16668335 0.17151681 0.17679831 0.18259931 0.18901229
 0.19615316 0.20416868 0.21325493 0.22367752 0.23579353 0.25012219
 0.26743197 0.28892672 0.31662488 0.35424781 0.40968323 0.5040164 ]


etc ...

Thank you Eric Grimson, Ana Bell, edX Corporate Offices


The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
Traceback (most recent call last):

  File ~\Downloads\prime_roots.py:96 in <module>
    if __name__ == "__main__": main()

  File ~\Downloads\prime_roots.py:95 in main
    print("The sum of the two primes {} and {} (which is {}) is also prime".format(x[z][0], x[z + 1][0], x[z][0] + x[z + 1][0]))

  File ~\Anaconda3\lib\site-packages\ipykernel\iostream.py:531 in write
    self.pub_thread.schedule(lambda: self._buffer.write(string))

  File ~\Anaconda3\lib\site-packages\ipykernel\iostream.py:216 in schedule
    self._event_pipe.send(b'')

  File ~\Anaconda3\lib\site-packages\zmq\sugar\socket.py:547 in send
    return super(Socket, self).send(data, flags=flags, copy=copy, track=track)

  File zmq\backend\cython\socket.pyx:718 in zmq.backend.cython.socket.Socket.send

  File zmq\backend\cython\socket.pyx:765 in zmq.backend.cython.socket.Socket.send

  File zmq\backend\cython\socket.pyx:242 in zmq.backend.cython.socket._send_copy

  File zmq\backend\cython\checkrc.pxd:13 in zmq.backend.cython.checkrc._check_rc

KeyboardInterrupt



"""

