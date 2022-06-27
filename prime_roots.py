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


Hopefully researching mathematics after passing 6.0002 to earn an XSeries certificate fingers crossed I am awarded a certificate in 6.0001

The sum of the two primes 999 and 997 (which is 1996) is also prime
The sum of the two primes 997 and 995 (which is 1992) is also prime
The sum of the two primes 995 and 993 (which is 1988) is also prime
The sum of the two primes 993 and 991 (which is 1984) is also prime
The sum of the two primes 991 and 989 (which is 1980) is also prime
The sum of the two primes 989 and 987 (which is 1976) is also prime
The sum of the two primes 987 and 985 (which is 1972) is also prime
The sum of the two primes 985 and 983 (which is 1968) is also prime
The sum of the two primes 983 and 981 (which is 1964) is also prime
The sum of the two primes 981 and 979 (which is 1960) is also prime
The sum of the two primes 979 and 977 (which is 1956) is also prime
The sum of the two primes 977 and 975 (which is 1952) is also prime
The sum of the two primes 975 and 973 (which is 1948) is also prime
The sum of the two primes 973 and 971 (which is 1944) is also prime
The sum of the two primes 971 and 969 (which is 1940) is also prime
The sum of the two primes 969 and 967 (which is 1936) is also prime
The sum of the two primes 967 and 965 (which is 1932) is also prime
The sum of the two primes 965 and 963 (which is 1928) is also prime
The sum of the two primes 963 and 961 (which is 1924) is also prime
The sum of the two primes 961 and 959 (which is 1920) is also prime
The sum of the two primes 959 and 957 (which is 1916) is also prime
The sum of the two primes 957 and 955 (which is 1912) is also prime
The sum of the two primes 955 and 953 (which is 1908) is also prime
The sum of the two primes 953 and 951 (which is 1904) is also prime
The sum of the two primes 951 and 949 (which is 1900) is also prime
The sum of the two primes 949 and 947 (which is 1896) is also prime
The sum of the two primes 947 and 945 (which is 1892) is also prime
The sum of the two primes 945 and 943 (which is 1888) is also prime
The sum of the two primes 943 and 941 (which is 1884) is also prime
The sum of the two primes 941 and 939 (which is 1880) is also prime
The sum of the two primes 939 and 937 (which is 1876) is also prime
The sum of the two primes 937 and 935 (which is 1872) is also prime
The sum of the two primes 935 and 933 (which is 1868) is also prime
The sum of the two primes 933 and 931 (which is 1864) is also prime
The sum of the two primes 931 and 929 (which is 1860) is also prime
The sum of the two primes 929 and 927 (which is 1856) is also prime
The sum of the two primes 927 and 925 (which is 1852) is also prime
The sum of the two primes 925 and 923 (which is 1848) is also prime
The sum of the two primes 923 and 921 (which is 1844) is also prime
The sum of the two primes 921 and 919 (which is 1840) is also prime
The sum of the two primes 919 and 917 (which is 1836) is also prime
The sum of the two primes 917 and 915 (which is 1832) is also prime
The sum of the two primes 915 and 913 (which is 1828) is also prime
The sum of the two primes 913 and 911 (which is 1824) is also prime
The sum of the two primes 911 and 909 (which is 1820) is also prime
The sum of the two primes 909 and 907 (which is 1816) is also prime
The sum of the two primes 907 and 905 (which is 1812) is also prime
The sum of the two primes 905 and 903 (which is 1808) is also prime
The sum of the two primes 903 and 901 (which is 1804) is also prime
The sum of the two primes 901 and 899 (which is 1800) is also prime
The sum of the two primes 899 and 897 (which is 1796) is also prime
The sum of the two primes 897 and 895 (which is 1792) is also prime
The sum of the two primes 895 and 893 (which is 1788) is also prime
The sum of the two primes 893 and 891 (which is 1784) is also prime
The sum of the two primes 891 and 889 (which is 1780) is also prime
The sum of the two primes 889 and 887 (which is 1776) is also prime
The sum of the two primes 887 and 885 (which is 1772) is also prime
The sum of the two primes 885 and 883 (which is 1768) is also prime
The sum of the two primes 883 and 881 (which is 1764) is also prime
The sum of the two primes 881 and 879 (which is 1760) is also prime
The sum of the two primes 879 and 877 (which is 1756) is also prime
The sum of the two primes 877 and 875 (which is 1752) is also prime
The sum of the two primes 875 and 873 (which is 1748) is also prime
The sum of the two primes 873 and 871 (which is 1744) is also prime
The sum of the two primes 871 and 869 (which is 1740) is also prime
The sum of the two primes 869 and 867 (which is 1736) is also prime
The sum of the two primes 867 and 865 (which is 1732) is also prime
The sum of the two primes 865 and 863 (which is 1728) is also prime
The sum of the two primes 863 and 861 (which is 1724) is also prime
The sum of the two primes 861 and 859 (which is 1720) is also prime
The sum of the two primes 859 and 857 (which is 1716) is also prime
The sum of the two primes 857 and 855 (which is 1712) is also prime
The sum of the two primes 855 and 853 (which is 1708) is also prime
The sum of the two primes 853 and 851 (which is 1704) is also prime
The sum of the two primes 851 and 849 (which is 1700) is also prime
The sum of the two primes 849 and 847 (which is 1696) is also prime
The sum of the two primes 847 and 845 (which is 1692) is also prime
The sum of the two primes 845 and 843 (which is 1688) is also prime
The sum of the two primes 843 and 841 (which is 1684) is also prime
The sum of the two primes 841 and 839 (which is 1680) is also prime
The sum of the two primes 839 and 837 (which is 1676) is also prime
The sum of the two primes 837 and 835 (which is 1672) is also prime
The sum of the two primes 835 and 833 (which is 1668) is also prime
The sum of the two primes 833 and 831 (which is 1664) is also prime
The sum of the two primes 831 and 829 (which is 1660) is also prime
The sum of the two primes 829 and 827 (which is 1656) is also prime
The sum of the two primes 827 and 825 (which is 1652) is also prime
The sum of the two primes 825 and 823 (which is 1648) is also prime
The sum of the two primes 823 and 821 (which is 1644) is also prime
The sum of the two primes 821 and 819 (which is 1640) is also prime
The sum of the two primes 819 and 817 (which is 1636) is also prime
The sum of the two primes 817 and 815 (which is 1632) is also prime
The sum of the two primes 815 and 813 (which is 1628) is also prime
The sum of the two primes 813 and 811 (which is 1624) is also prime
The sum of the two primes 811 and 809 (which is 1620) is also prime
The sum of the two primes 809 and 807 (which is 1616) is also prime
The sum of the two primes 807 and 805 (which is 1612) is also prime
The sum of the two primes 805 and 803 (which is 1608) is also prime
The sum of the two primes 803 and 801 (which is 1604) is also prime
The sum of the two primes 801 and 799 (which is 1600) is also prime
The sum of the two primes 799 and 797 (which is 1596) is also prime
The sum of the two primes 797 and 795 (which is 1592) is also prime
The sum of the two primes 795 and 793 (which is 1588) is also prime
The sum of the two primes 793 and 791 (which is 1584) is also prime
The sum of the two primes 791 and 789 (which is 1580) is also prime
The sum of the two primes 789 and 787 (which is 1576) is also prime
The sum of the two primes 787 and 785 (which is 1572) is also prime
The sum of the two primes 785 and 783 (which is 1568) is also prime
The sum of the two primes 783 and 781 (which is 1564) is also prime
The sum of the two primes 781 and 779 (which is 1560) is also prime
The sum of the two primes 779 and 777 (which is 1556) is also prime
The sum of the two primes 777 and 775 (which is 1552) is also prime
The sum of the two primes 775 and 773 (which is 1548) is also prime
The sum of the two primes 773 and 771 (which is 1544) is also prime
The sum of the two primes 771 and 769 (which is 1540) is also prime
The sum of the two primes 769 and 767 (which is 1536) is also prime
The sum of the two primes 767 and 765 (which is 1532) is also prime
The sum of the two primes 765 and 763 (which is 1528) is also prime
The sum of the two primes 763 and 761 (which is 1524) is also prime
The sum of the two primes 761 and 759 (which is 1520) is also prime
The sum of the two primes 759 and 757 (which is 1516) is also prime
The sum of the two primes 757 and 755 (which is 1512) is also prime
The sum of the two primes 755 and 753 (which is 1508) is also prime
The sum of the two primes 753 and 751 (which is 1504) is also prime
The sum of the two primes 751 and 749 (which is 1500) is also prime
The sum of the two primes 749 and 747 (which is 1496) is also prime
The sum of the two primes 747 and 745 (which is 1492) is also prime
The sum of the two primes 745 and 743 (which is 1488) is also prime
The sum of the two primes 743 and 741 (which is 1484) is also prime
The sum of the two primes 741 and 739 (which is 1480) is also prime
The sum of the two primes 739 and 737 (which is 1476) is also prime
The sum of the two primes 737 and 735 (which is 1472) is also prime
The sum of the two primes 735 and 733 (which is 1468) is also prime
The sum of the two primes 733 and 731 (which is 1464) is also prime
The sum of the two primes 731 and 729 (which is 1460) is also prime
The sum of the two primes 729 and 727 (which is 1456) is also prime
The sum of the two primes 727 and 725 (which is 1452) is also prime
The sum of the two primes 725 and 723 (which is 1448) is also prime
The sum of the two primes 723 and 721 (which is 1444) is also prime
The sum of the two primes 721 and 719 (which is 1440) is also prime
The sum of the two primes 719 and 717 (which is 1436) is also prime
The sum of the two primes 717 and 715 (which is 1432) is also prime
The sum of the two primes 715 and 713 (which is 1428) is also prime
The sum of the two primes 713 and 711 (which is 1424) is also prime
The sum of the two primes 711 and 709 (which is 1420) is also prime
The sum of the two primes 709 and 707 (which is 1416) is also prime
The sum of the two primes 707 and 705 (which is 1412) is also prime
The sum of the two primes 705 and 703 (which is 1408) is also prime
The sum of the two primes 703 and 701 (which is 1404) is also prime
The sum of the two primes 701 and 699 (which is 1400) is also prime
The sum of the two primes 699 and 697 (which is 1396) is also prime
The sum of the two primes 697 and 695 (which is 1392) is also prime
The sum of the two primes 695 and 693 (which is 1388) is also prime
The sum of the two primes 693 and 691 (which is 1384) is also prime
The sum of the two primes 691 and 689 (which is 1380) is also prime
The sum of the two primes 689 and 687 (which is 1376) is also prime
The sum of the two primes 687 and 685 (which is 1372) is also prime
The sum of the two primes 685 and 683 (which is 1368) is also prime
The sum of the two primes 683 and 681 (which is 1364) is also prime
The sum of the two primes 681 and 679 (which is 1360) is also prime
The sum of the two primes 679 and 677 (which is 1356) is also prime
The sum of the two primes 677 and 675 (which is 1352) is also prime
The sum of the two primes 675 and 673 (which is 1348) is also prime
The sum of the two primes 673 and 671 (which is 1344) is also prime
The sum of the two primes 671 and 669 (which is 1340) is also prime
The sum of the two primes 669 and 667 (which is 1336) is also prime
The sum of the two primes 667 and 665 (which is 1332) is also prime
The sum of the two primes 665 and 663 (which is 1328) is also prime
The sum of the two primes 663 and 661 (which is 1324) is also prime
The sum of the two primes 661 and 659 (which is 1320) is also prime
The sum of the two primes 659 and 657 (which is 1316) is also prime
The sum of the two primes 657 and 655 (which is 1312) is also prime
The sum of the two primes 655 and 653 (which is 1308) is also prime
The sum of the two primes 653 and 651 (which is 1304) is also prime
The sum of the two primes 651 and 649 (which is 1300) is also prime
The sum of the two primes 649 and 647 (which is 1296) is also prime
The sum of the two primes 647 and 645 (which is 1292) is also prime
The sum of the two primes 645 and 643 (which is 1288) is also prime
The sum of the two primes 643 and 641 (which is 1284) is also prime
The sum of the two primes 641 and 639 (which is 1280) is also prime
The sum of the two primes 639 and 637 (which is 1276) is also prime
The sum of the two primes 637 and 635 (which is 1272) is also prime
The sum of the two primes 635 and 633 (which is 1268) is also prime
The sum of the two primes 633 and 631 (which is 1264) is also prime
The sum of the two primes 631 and 629 (which is 1260) is also prime
The sum of the two primes 629 and 627 (which is 1256) is also prime
The sum of the two primes 627 and 625 (which is 1252) is also prime
The sum of the two primes 625 and 623 (which is 1248) is also prime
The sum of the two primes 623 and 621 (which is 1244) is also prime
The sum of the two primes 621 and 619 (which is 1240) is also prime
The sum of the two primes 619 and 617 (which is 1236) is also prime
The sum of the two primes 617 and 615 (which is 1232) is also prime
The sum of the two primes 615 and 613 (which is 1228) is also prime
The sum of the two primes 613 and 611 (which is 1224) is also prime
The sum of the two primes 611 and 609 (which is 1220) is also prime
The sum of the two primes 609 and 607 (which is 1216) is also prime
The sum of the two primes 607 and 605 (which is 1212) is also prime
The sum of the two primes 605 and 603 (which is 1208) is also prime
The sum of the two primes 603 and 601 (which is 1204) is also prime
The sum of the two primes 601 and 599 (which is 1200) is also prime
The sum of the two primes 599 and 597 (which is 1196) is also prime
The sum of the two primes 597 and 595 (which is 1192) is also prime
The sum of the two primes 595 and 593 (which is 1188) is also prime
The sum of the two primes 593 and 591 (which is 1184) is also prime
The sum of the two primes 591 and 589 (which is 1180) is also prime
The sum of the two primes 589 and 587 (which is 1176) is also prime
The sum of the two primes 587 and 585 (which is 1172) is also prime
The sum of the two primes 585 and 583 (which is 1168) is also prime
The sum of the two primes 583 and 581 (which is 1164) is also prime
The sum of the two primes 581 and 579 (which is 1160) is also prime
The sum of the two primes 579 and 577 (which is 1156) is also prime
The sum of the two primes 577 and 575 (which is 1152) is also prime
The sum of the two primes 575 and 573 (which is 1148) is also prime
The sum of the two primes 573 and 571 (which is 1144) is also prime
The sum of the two primes 571 and 569 (which is 1140) is also prime
The sum of the two primes 569 and 567 (which is 1136) is also prime
The sum of the two primes 567 and 565 (which is 1132) is also prime
The sum of the two primes 565 and 563 (which is 1128) is also prime
The sum of the two primes 563 and 561 (which is 1124) is also prime
The sum of the two primes 561 and 559 (which is 1120) is also prime
The sum of the two primes 559 and 557 (which is 1116) is also prime
The sum of the two primes 557 and 555 (which is 1112) is also prime
The sum of the two primes 555 and 553 (which is 1108) is also prime
The sum of the two primes 553 and 551 (which is 1104) is also prime
The sum of the two primes 551 and 549 (which is 1100) is also prime
The sum of the two primes 549 and 547 (which is 1096) is also prime
The sum of the two primes 547 and 545 (which is 1092) is also prime
The sum of the two primes 545 and 543 (which is 1088) is also prime
The sum of the two primes 543 and 541 (which is 1084) is also prime
The sum of the two primes 541 and 539 (which is 1080) is also prime
The sum of the two primes 539 and 537 (which is 1076) is also prime
The sum of the two primes 537 and 535 (which is 1072) is also prime
The sum of the two primes 535 and 533 (which is 1068) is also prime
The sum of the two primes 533 and 531 (which is 1064) is also prime
The sum of the two primes 531 and 529 (which is 1060) is also prime
The sum of the two primes 529 and 527 (which is 1056) is also prime
The sum of the two primes 527 and 525 (which is 1052) is also prime
The sum of the two primes 525 and 523 (which is 1048) is also prime
The sum of the two primes 523 and 521 (which is 1044) is also prime
The sum of the two primes 521 and 519 (which is 1040) is also prime
The sum of the two primes 519 and 517 (which is 1036) is also prime
The sum of the two primes 517 and 515 (which is 1032) is also prime
The sum of the two primes 515 and 513 (which is 1028) is also prime
The sum of the two primes 513 and 511 (which is 1024) is also prime
The sum of the two primes 511 and 509 (which is 1020) is also prime
The sum of the two primes 509 and 507 (which is 1016) is also prime
The sum of the two primes 507 and 505 (which is 1012) is also prime
The sum of the two primes 505 and 503 (which is 1008) is also prime
The sum of the two primes 503 and 501 (which is 1004) is also prime
The sum of the two primes 501 and 499 (which is 1000) is also prime
The sum of the two primes 499 and 497 (which is 996) is also prime
The sum of the two primes 497 and 495 (which is 992) is also prime
The sum of the two primes 495 and 493 (which is 988) is also prime
The sum of the two primes 493 and 491 (which is 984) is also prime
The sum of the two primes 491 and 489 (which is 980) is also prime
The sum of the two primes 489 and 487 (which is 976) is also prime
The sum of the two primes 487 and 485 (which is 972) is also prime
The sum of the two primes 485 and 483 (which is 968) is also prime
The sum of the two primes 483 and 481 (which is 964) is also prime
The sum of the two primes 481 and 479 (which is 960) is also prime
The sum of the two primes 479 and 477 (which is 956) is also prime
The sum of the two primes 477 and 475 (which is 952) is also prime
The sum of the two primes 475 and 473 (which is 948) is also prime
The sum of the two primes 473 and 471 (which is 944) is also prime
The sum of the two primes 471 and 469 (which is 940) is also prime
The sum of the two primes 469 and 467 (which is 936) is also prime
The sum of the two primes 467 and 465 (which is 932) is also prime
The sum of the two primes 465 and 463 (which is 928) is also prime
The sum of the two primes 463 and 461 (which is 924) is also prime
The sum of the two primes 461 and 459 (which is 920) is also prime
The sum of the two primes 459 and 457 (which is 916) is also prime
The sum of the two primes 457 and 455 (which is 912) is also prime
The sum of the two primes 455 and 453 (which is 908) is also prime
The sum of the two primes 453 and 451 (which is 904) is also prime
The sum of the two primes 451 and 449 (which is 900) is also prime
The sum of the two primes 449 and 447 (which is 896) is also prime
The sum of the two primes 447 and 445 (which is 892) is also prime
The sum of the two primes 445 and 443 (which is 888) is also prime
The sum of the two primes 443 and 441 (which is 884) is also prime
The sum of the two primes 441 and 439 (which is 880) is also prime
The sum of the two primes 439 and 437 (which is 876) is also prime
The sum of the two primes 437 and 435 (which is 872) is also prime
The sum of the two primes 435 and 433 (which is 868) is also prime
The sum of the two primes 433 and 431 (which is 864) is also prime
The sum of the two primes 431 and 429 (which is 860) is also prime
The sum of the two primes 429 and 427 (which is 856) is also prime
The sum of the two primes 427 and 425 (which is 852) is also prime
The sum of the two primes 425 and 423 (which is 848) is also prime
The sum of the two primes 423 and 421 (which is 844) is also prime
The sum of the two primes 421 and 419 (which is 840) is also prime
The sum of the two primes 419 and 417 (which is 836) is also prime
The sum of the two primes 417 and 415 (which is 832) is also prime
The sum of the two primes 415 and 413 (which is 828) is also prime
The sum of the two primes 413 and 411 (which is 824) is also prime
The sum of the two primes 411 and 409 (which is 820) is also prime
The sum of the two primes 409 and 407 (which is 816) is also prime
The sum of the two primes 407 and 405 (which is 812) is also prime
The sum of the two primes 405 and 403 (which is 808) is also prime
The sum of the two primes 403 and 401 (which is 804) is also prime
The sum of the two primes 401 and 399 (which is 800) is also prime
The sum of the two primes 399 and 397 (which is 796) is also prime
The sum of the two primes 397 and 395 (which is 792) is also prime
The sum of the two primes 395 and 393 (which is 788) is also prime
The sum of the two primes 393 and 391 (which is 784) is also prime
The sum of the two primes 391 and 389 (which is 780) is also prime
The sum of the two primes 389 and 387 (which is 776) is also prime
The sum of the two primes 387 and 385 (which is 772) is also prime
The sum of the two primes 385 and 383 (which is 768) is also prime
The sum of the two primes 383 and 381 (which is 764) is also prime
The sum of the two primes 381 and 379 (which is 760) is also prime
The sum of the two primes 379 and 377 (which is 756) is also prime
The sum of the two primes 377 and 375 (which is 752) is also prime
The sum of the two primes 375 and 373 (which is 748) is also prime
The sum of the two primes 373 and 371 (which is 744) is also prime
The sum of the two primes 371 and 369 (which is 740) is also prime
The sum of the two primes 369 and 367 (which is 736) is also prime
The sum of the two primes 367 and 365 (which is 732) is also prime
The sum of the two primes 365 and 363 (which is 728) is also prime
The sum of the two primes 363 and 361 (which is 724) is also prime
The sum of the two primes 361 and 359 (which is 720) is also prime
The sum of the two primes 359 and 357 (which is 716) is also prime
The sum of the two primes 357 and 355 (which is 712) is also prime
The sum of the two primes 355 and 353 (which is 708) is also prime
The sum of the two primes 353 and 351 (which is 704) is also prime
The sum of the two primes 351 and 349 (which is 700) is also prime
The sum of the two primes 349 and 347 (which is 696) is also prime
The sum of the two primes 347 and 345 (which is 692) is also prime
The sum of the two primes 345 and 343 (which is 688) is also prime
The sum of the two primes 343 and 341 (which is 684) is also prime
The sum of the two primes 341 and 339 (which is 680) is also prime
The sum of the two primes 339 and 337 (which is 676) is also prime
The sum of the two primes 337 and 335 (which is 672) is also prime
The sum of the two primes 335 and 333 (which is 668) is also prime
The sum of the two primes 333 and 331 (which is 664) is also prime
The sum of the two primes 331 and 329 (which is 660) is also prime
The sum of the two primes 329 and 327 (which is 656) is also prime
The sum of the two primes 327 and 325 (which is 652) is also prime
The sum of the two primes 325 and 323 (which is 648) is also prime
The sum of the two primes 323 and 321 (which is 644) is also prime
The sum of the two primes 321 and 319 (which is 640) is also prime
The sum of the two primes 319 and 317 (which is 636) is also prime
The sum of the two primes 317 and 315 (which is 632) is also prime
The sum of the two primes 315 and 313 (which is 628) is also prime
The sum of the two primes 313 and 311 (which is 624) is also prime
The sum of the two primes 311 and 309 (which is 620) is also prime
The sum of the two primes 309 and 307 (which is 616) is also prime
The sum of the two primes 307 and 305 (which is 612) is also prime
The sum of the two primes 305 and 303 (which is 608) is also prime
The sum of the two primes 303 and 301 (which is 604) is also prime
The sum of the two primes 301 and 299 (which is 600) is also prime
The sum of the two primes 299 and 297 (which is 596) is also prime
The sum of the two primes 297 and 295 (which is 592) is also prime
The sum of the two primes 295 and 293 (which is 588) is also prime
The sum of the two primes 293 and 291 (which is 584) is also prime
The sum of the two primes 291 and 289 (which is 580) is also prime
The sum of the two primes 289 and 287 (which is 576) is also prime
The sum of the two primes 287 and 285 (which is 572) is also prime
The sum of the two primes 285 and 283 (which is 568) is also prime
The sum of the two primes 283 and 281 (which is 564) is also prime
The sum of the two primes 281 and 279 (which is 560) is also prime
The sum of the two primes 279 and 277 (which is 556) is also prime
The sum of the two primes 277 and 275 (which is 552) is also prime
The sum of the two primes 275 and 273 (which is 548) is also prime
The sum of the two primes 273 and 271 (which is 544) is also prime
The sum of the two primes 271 and 269 (which is 540) is also prime
The sum of the two primes 269 and 267 (which is 536) is also prime
The sum of the two primes 267 and 265 (which is 532) is also prime
The sum of the two primes 265 and 263 (which is 528) is also prime
The sum of the two primes 263 and 261 (which is 524) is also prime
The sum of the two primes 261 and 259 (which is 520) is also prime
The sum of the two primes 259 and 257 (which is 516) is also prime
The sum of the two primes 257 and 255 (which is 512) is also prime
The sum of the two primes 255 and 253 (which is 508) is also prime
The sum of the two primes 253 and 251 (which is 504) is also prime
The sum of the two primes 251 and 249 (which is 500) is also prime
The sum of the two primes 249 and 247 (which is 496) is also prime
The sum of the two primes 247 and 245 (which is 492) is also prime
The sum of the two primes 245 and 243 (which is 488) is also prime
The sum of the two primes 243 and 241 (which is 484) is also prime
The sum of the two primes 241 and 239 (which is 480) is also prime
The sum of the two primes 239 and 237 (which is 476) is also prime
The sum of the two primes 237 and 235 (which is 472) is also prime
The sum of the two primes 235 and 233 (which is 468) is also prime
The sum of the two primes 233 and 231 (which is 464) is also prime
The sum of the two primes 231 and 229 (which is 460) is also prime
The sum of the two primes 229 and 227 (which is 456) is also prime
The sum of the two primes 227 and 225 (which is 452) is also prime
The sum of the two primes 225 and 223 (which is 448) is also prime
The sum of the two primes 223 and 221 (which is 444) is also prime
The sum of the two primes 221 and 219 (which is 440) is also prime
The sum of the two primes 219 and 217 (which is 436) is also prime
The sum of the two primes 217 and 215 (which is 432) is also prime
The sum of the two primes 215 and 213 (which is 428) is also prime
The sum of the two primes 213 and 211 (which is 424) is also prime
The sum of the two primes 211 and 209 (which is 420) is also prime
The sum of the two primes 209 and 207 (which is 416) is also prime
The sum of the two primes 207 and 205 (which is 412) is also prime
The sum of the two primes 205 and 203 (which is 408) is also prime
The sum of the two primes 203 and 201 (which is 404) is also prime
The sum of the two primes 201 and 199 (which is 400) is also prime
The sum of the two primes 199 and 197 (which is 396) is also prime
The sum of the two primes 197 and 195 (which is 392) is also prime
The sum of the two primes 195 and 193 (which is 388) is also prime
The sum of the two primes 193 and 191 (which is 384) is also prime
The sum of the two primes 191 and 189 (which is 380) is also prime
The sum of the two primes 189 and 187 (which is 376) is also prime
The sum of the two primes 187 and 185 (which is 372) is also prime
The sum of the two primes 185 and 183 (which is 368) is also prime
The sum of the two primes 183 and 181 (which is 364) is also prime
The sum of the two primes 181 and 179 (which is 360) is also prime
The sum of the two primes 179 and 177 (which is 356) is also prime
The sum of the two primes 177 and 175 (which is 352) is also prime
The sum of the two primes 175 and 173 (which is 348) is also prime
The sum of the two primes 173 and 171 (which is 344) is also prime
The sum of the two primes 171 and 169 (which is 340) is also prime
The sum of the two primes 169 and 167 (which is 336) is also prime
The sum of the two primes 167 and 165 (which is 332) is also prime
The sum of the two primes 165 and 163 (which is 328) is also prime
The sum of the two primes 163 and 161 (which is 324) is also prime
The sum of the two primes 161 and 159 (which is 320) is also prime
The sum of the two primes 159 and 157 (which is 316) is also prime
The sum of the two primes 157 and 155 (which is 312) is also prime
The sum of the two primes 155 and 153 (which is 308) is also prime
The sum of the two primes 153 and 151 (which is 304) is also prime
The sum of the two primes 151 and 149 (which is 300) is also prime
The sum of the two primes 149 and 147 (which is 296) is also prime
The sum of the two primes 147 and 145 (which is 292) is also prime
The sum of the two primes 145 and 143 (which is 288) is also prime
The sum of the two primes 143 and 141 (which is 284) is also prime
The sum of the two primes 141 and 139 (which is 280) is also prime
The sum of the two primes 139 and 137 (which is 276) is also prime
The sum of the two primes 137 and 135 (which is 272) is also prime
The sum of the two primes 135 and 133 (which is 268) is also prime
The sum of the two primes 133 and 131 (which is 264) is also prime
The sum of the two primes 131 and 129 (which is 260) is also prime
The sum of the two primes 129 and 127 (which is 256) is also prime
The sum of the two primes 127 and 125 (which is 252) is also prime
The sum of the two primes 125 and 123 (which is 248) is also prime
The sum of the two primes 123 and 121 (which is 244) is also prime
The sum of the two primes 121 and 119 (which is 240) is also prime
The sum of the two primes 119 and 117 (which is 236) is also prime
The sum of the two primes 117 and 115 (which is 232) is also prime
The sum of the two primes 115 and 113 (which is 228) is also prime
The sum of the two primes 113 and 111 (which is 224) is also prime
The sum of the two primes 111 and 109 (which is 220) is also prime
The sum of the two primes 109 and 107 (which is 216) is also prime
The sum of the two primes 107 and 105 (which is 212) is also prime
The sum of the two primes 105 and 103 (which is 208) is also prime
The sum of the two primes 103 and 101 (which is 204) is also prime
The sum of the two primes 101 and 99 (which is 200) is also prime
The sum of the two primes 99 and 97 (which is 196) is also prime
The sum of the two primes 97 and 95 (which is 192) is also prime
The sum of the two primes 95 and 93 (which is 188) is also prime
The sum of the two primes 93 and 91 (which is 184) is also prime
The sum of the two primes 91 and 89 (which is 180) is also prime
The sum of the two primes 89 and 87 (which is 176) is also prime
The sum of the two primes 87 and 85 (which is 172) is also prime
The sum of the two primes 85 and 83 (which is 168) is also prime
The sum of the two primes 83 and 81 (which is 164) is also prime
The sum of the two primes 81 and 79 (which is 160) is also prime
The sum of the two primes 79 and 77 (which is 156) is also prime
The sum of the two primes 77 and 75 (which is 152) is also prime
The sum of the two primes 75 and 73 (which is 148) is also prime
The sum of the two primes 73 and 71 (which is 144) is also prime
The sum of the two primes 71 and 69 (which is 140) is also prime
The sum of the two primes 69 and 67 (which is 136) is also prime
The sum of the two primes 67 and 65 (which is 132) is also prime
The sum of the two primes 65 and 63 (which is 128) is also prime
The sum of the two primes 63 and 61 (which is 124) is also prime
The sum of the two primes 61 and 59 (which is 120) is also prime
The sum of the two primes 59 and 57 (which is 116) is also prime
The sum of the two primes 57 and 55 (which is 112) is also prime
The sum of the two primes 55 and 53 (which is 108) is also prime
The sum of the two primes 53 and 51 (which is 104) is also prime
The sum of the two primes 51 and 49 (which is 100) is also prime
The sum of the two primes 49 and 47 (which is 96) is also prime
The sum of the two primes 47 and 45 (which is 92) is also prime
The sum of the two primes 45 and 43 (which is 88) is also prime
The sum of the two primes 43 and 41 (which is 84) is also prime
The sum of the two primes 41 and 39 (which is 80) is also prime
The sum of the two primes 39 and 37 (which is 76) is also prime
The sum of the two primes 37 and 35 (which is 72) is also prime
The sum of the two primes 35 and 33 (which is 68) is also prime
The sum of the two primes 33 and 31 (which is 64) is also prime
The sum of the two primes 31 and 29 (which is 60) is also prime
The sum of the two primes 29 and 27 (which is 56) is also prime
The sum of the two primes 27 and 25 (which is 52) is also prime
The sum of the two primes 25 and 23 (which is 48) is also prime
The sum of the two primes 23 and 21 (which is 44) is also prime
The sum of the two primes 21 and 19 (which is 40) is also prime
The sum of the two primes 19 and 17 (which is 36) is also prime
The sum of the two primes 17 and 15 (which is 32) is also prime
The sum of the two primes 15 and 13 (which is 28) is also prime
The sum of the two primes 13 and 11 (which is 24) is also prime
The sum of the two primes 11 and 9 (which is 20) is also prime
The sum of the two primes 9 and 7 (which is 16) is also prime
The sum of the two primes 7 and 5 (which is 12) is also prime
The sum of the two primes 5 and 3 (which is 8) is also prime

"""

