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
    epsilon = 0.0001
    while((guess ** 2 - prime) >= epsilon):
       # print("guess: {} high: {} low: {}".format(guess, high, low))
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
    #print(x)
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
if __name__ == "__main__": main()

""" 
Square roots of the primes occuring in the first ~1000 natural (counting) numbers 

Eager to find an numerical algorithm to generate or approximate up to so many primes in the natural and real and complex number systems such as Ramanujan\'s notebooks have formulas for approximating pi, sine, cosine, tangent and inverse sine, cosine, tangent and their hyperbolic counterparts

Charles Thomas Wallace Truscott, Byron Bay NSW 2481

[(999, 31.21875), (997, 31.15625), (995, 31.09375), (993, 31.03125), (991, 30.96875), (989, 30.90625), (987, 30.84375), (985, 30.78125), (983, 30.71875), (981, 30.65625), (979, 30.59375), (977, 30.53125), (975, 30.46875), (973, 30.40625), (971, 30.34375), (969, 30.28125), (967, 30.21875), (965, 30.15625), (963, 30.09375), (961, 30.03125), (959, 29.96875), (957, 29.90625), (955, 29.84375), (953, 29.78125), (951, 29.71875), (949, 29.65625), (947, 29.59375), (945, 29.53125), (943, 29.46875), (941, 29.40625), (939, 29.34375), (937, 29.28125), (935, 29.21875), (933, 29.15625), (931, 29.09375), (929, 29.03125), (927, 28.96875), (925, 28.90625), (923, 28.84375), (921, 28.78125), (919, 28.71875), (917, 28.65625), (915, 28.59375), (913, 28.53125), (911, 28.46875), (909, 28.40625), (907, 28.34375), (905, 28.28125), (903, 28.21875), (901, 28.15625), (899, 28.09375), (897, 28.03125), (895, 27.96875), (893, 27.90625), (891, 27.84375), (889, 27.78125), (887, 27.71875), (885, 27.65625), (883, 27.59375), (881, 27.53125), (879, 27.46875), (877, 27.40625), (875, 27.34375), (873, 27.28125), (871, 27.21875), (869, 27.15625), (867, 27.09375), (865, 27.03125), (863, 26.96875), (861, 26.90625), (859, 26.84375), (857, 26.78125), (855, 26.71875), (853, 26.65625), (851, 26.59375), (849, 26.53125), (847, 26.46875), (845, 26.40625), (843, 26.34375), (841, 26.28125), (839, 26.21875), (837, 26.15625), (835, 26.09375), (833, 26.03125), (831, 25.96875), (829, 25.90625), (827, 25.84375), (825, 25.78125), (823, 25.71875), (821, 25.65625), (819, 25.59375), (817, 25.53125), (815, 25.46875), (813, 25.40625), (811, 25.34375), (809, 25.28125), (807, 25.21875), (805, 25.15625), (803, 25.09375), (801, 25.03125), (799, 24.96875), (797, 24.90625), (795, 24.84375), (793, 24.78125), (791, 24.71875), (789, 24.65625), (787, 24.59375), (785, 24.53125), (783, 24.46875), (781, 24.40625), (779, 24.34375), (777, 24.28125), (775, 24.21875), (773, 24.15625), (771, 24.09375), (769, 24.03125), (767, 23.96875), (765, 23.90625), (763, 23.84375), (761, 23.78125), (759, 23.71875), (757, 23.65625), (755, 23.59375), (753, 23.53125), (751, 23.46875), (749, 23.40625), (747, 23.34375), (745, 23.28125), (743, 23.21875), (741, 23.15625), (739, 23.09375), (737, 23.03125), (735, 22.96875), (733, 22.90625), (731, 22.84375), (729, 22.78125), (727, 22.71875), (725, 22.65625), (723, 22.59375), (721, 22.53125), (719, 22.46875), (717, 22.40625), (715, 22.34375), (713, 22.28125), (711, 22.21875), (709, 22.15625), (707, 22.09375), (705, 22.03125), (703, 21.96875), (701, 21.90625), (699, 21.84375), (697, 21.78125), (695, 21.71875), (693, 21.65625), (691, 21.59375), (689, 21.53125), (687, 21.46875), (685, 21.40625), (683, 21.34375), (681, 21.28125), (679, 21.21875), (677, 21.15625), (675, 21.09375), (673, 21.03125), (671, 20.96875), (669, 20.90625), (667, 20.84375), (665, 20.78125), (663, 20.71875), (661, 20.65625), (659, 20.59375), (657, 20.53125), (655, 20.46875), (653, 20.40625), (651, 20.34375), (649, 20.28125), (647, 20.21875), (645, 20.15625), (643, 20.09375), (641, 20.03125), (639, 19.96875), (637, 19.90625), (635, 19.84375), (633, 19.78125), (631, 19.71875), (629, 19.65625), (627, 19.59375), (625, 19.53125), (623, 19.46875), (621, 19.40625), (619, 19.34375), (617, 19.28125), (615, 19.21875), (613, 19.15625), (611, 19.09375), (609, 19.03125), (607, 18.96875), (605, 18.90625), (603, 18.84375), (601, 18.78125), (599, 18.71875), (597, 18.65625), (595, 18.59375), (593, 18.53125), (591, 18.46875), (589, 18.40625), (587, 18.34375), (585, 18.28125), (583, 18.21875), (581, 18.15625), (579, 18.09375), (577, 18.03125), (575, 17.96875), (573, 17.90625), (571, 17.84375), (569, 17.78125), (567, 17.71875), (565, 17.65625), (563, 17.59375), (561, 17.53125), (559, 17.46875), (557, 17.40625), (555, 17.34375), (553, 17.28125), (551, 17.21875), (549, 17.15625), (547, 17.09375), (545, 17.03125), (543, 16.96875), (541, 16.90625), (539, 16.84375), (537, 16.78125), (535, 16.71875), (533, 16.65625), (531, 16.59375), (529, 16.53125), (527, 16.46875), (525, 16.40625), (523, 16.34375), (521, 16.28125), (519, 16.21875), (517, 16.15625), (515, 16.09375), (513, 16.03125), (511, 15.96875), (509, 15.90625), (507, 15.84375), (505, 15.78125), (503, 15.71875), (501, 15.65625), (499, 15.59375), (497, 15.53125), (495, 15.46875), (493, 15.40625), (491, 15.34375), (489, 15.28125), (487, 15.21875), (485, 15.15625), (483, 15.09375), (481, 15.03125), (479, 14.96875), (477, 14.90625), (475, 14.84375), (473, 14.78125), (471, 14.71875), (469, 14.65625), (467, 14.59375), (465, 14.53125), (463, 14.46875), (461, 14.40625), (459, 14.34375), (457, 14.28125), (455, 14.21875), (453, 14.15625), (451, 14.09375), (449, 14.03125), (447, 13.96875), (445, 13.90625), (443, 13.84375), (441, 13.78125), (439, 13.71875), (437, 13.65625), (435, 13.59375), (433, 13.53125), (431, 13.46875), (429, 13.40625), (427, 13.34375), (425, 13.28125), (423, 13.21875), (421, 13.15625), (419, 13.09375), (417, 13.03125), (415, 12.96875), (413, 12.90625), (411, 12.84375), (409, 12.78125), (407, 12.71875), (405, 12.65625), (403, 12.59375), (401, 12.53125), (399, 12.46875), (397, 12.40625), (395, 12.34375), (393, 12.28125), (391, 12.21875), (389, 12.15625), (387, 12.09375), (385, 12.03125), (383, 11.96875), (381, 11.90625), (379, 11.84375), (377, 11.78125), (375, 11.71875), (373, 11.65625), (371, 11.59375), (369, 11.53125), (367, 11.46875), (365, 11.40625), (363, 11.34375), (361, 11.28125), (359, 11.21875), (357, 11.15625), (355, 11.09375), (353, 11.03125), (351, 10.96875), (349, 10.90625), (347, 10.84375), (345, 10.78125), (343, 10.71875), (341, 10.65625), (339, 10.59375), (337, 10.53125), (335, 10.46875), (333, 10.40625), (331, 10.34375), (329, 10.28125), (327, 10.21875), (325, 10.15625), (323, 10.09375), (321, 10.03125), (319, 9.96875), (317, 9.90625), (315, 9.84375), (313, 9.78125), (311, 9.71875), (309, 9.65625), (307, 9.59375), (305, 9.53125), (303, 9.46875), (301, 9.40625), (299, 9.34375), (297, 9.28125), (295, 9.21875), (293, 9.15625), (291, 9.09375), (289, 9.03125), (287, 8.96875), (285, 8.90625), (283, 8.84375), (281, 8.78125), (279, 8.71875), (277, 8.65625), (275, 8.59375), (273, 8.53125), (271, 8.46875), (269, 8.40625), (267, 8.34375), (265, 8.28125), (263, 8.21875), (261, 8.15625), (259, 8.09375), (257, 8.03125), (255, 15.9375), (253, 15.8125), (251, 15.6875), (249, 15.5625), (247, 15.4375), (245, 15.3125), (243, 15.1875), (241, 15.0625), (239, 14.9375), (237, 14.8125), (235, 14.6875), (233, 14.5625), (231, 14.4375), (229, 14.3125), (227, 14.1875), (225, 14.0625), (223, 13.9375), (221, 13.8125), (219, 13.6875), (217, 13.5625), (215, 13.4375), (213, 13.3125), (211, 13.1875), (209, 13.0625), (207, 12.9375), (205, 12.8125), (203, 12.6875), (201, 12.5625), (199, 12.4375), (197, 12.3125), (195, 12.1875), (193, 12.0625), (191, 11.9375), (189, 11.8125), (187, 11.6875), (185, 11.5625), (183, 11.4375), (181, 11.3125), (179, 11.1875), (177, 11.0625), (175, 10.9375), (173, 10.8125), (171, 10.6875), (169, 10.5625), (167, 10.4375), (165, 10.3125), (163, 10.1875), (161, 10.0625), (159, 9.9375), (157, 9.8125), (155, 9.6875), (153, 9.5625), (151, 9.4375), (149, 9.3125), (147, 9.1875), (145, 9.0625), (143, 8.9375), (141, 8.8125), (139, 8.6875), (137, 8.5625), (135, 8.4375), (133, 8.3125), (131, 8.1875), (129, 8.0625), (127, 7.9375), (125, 7.8125), (123, 7.6875), (121, 7.5625), (119, 7.4375), (117, 7.3125), (115, 7.1875), (113, 7.0625), (111, 6.9375), (109, 6.8125), (107, 6.6875), (105, 6.5625), (103, 6.4375), (101, 6.3125), (99, 6.1875), (97, 6.0625), (95, 5.9375), (93, 5.8125), (91, 5.6875), (89, 5.5625), (87, 5.4375), (85, 5.3125), (83, 5.1875), (81, 5.0625), (79, 4.9375), (77, 4.8125), (75, 4.6875), (73, 4.5625), (71, 4.4375), (69, 4.3125), (67, 4.1875), (65, 4.0625), (63, 7.875), (61, 7.625), (59, 7.375), (57, 7.125), (55, 6.875), (53, 6.625), (51, 6.375), (49, 6.125), (47, 5.875), (45, 5.625), (43, 5.375), (41, 5.125), (39, 4.875), (37, 4.625), (35, 4.375), (33, 4.125), (31, 3.875), (29, 3.625), (27, 3.375), (25, 3.125), (23, 2.875), (21, 2.625), (19, 2.375), (17, 2.125), (15, 3.75), (13, 3.25), (11, 2.75), (9, 2.25), (7, 1.75), (5, 1.25), (3, 1.5)]

Thank you Eric Grimson, Ana Bell, edX Corporate Offices

"""

"""
501 and 499 are both consecutively occuring primes in the natural number set
The difference between the square root of 499 and 497 is 0.0625
499 and 497 are both consecutively occuring primes in the natural number set
The difference between the square root of 497 and 495 is 0.0625
497 and 495 are both consecutively occuring primes in the natural number set
The difference between the square root of 495 and 493 is 0.0625
495 and 493 are both consecutively occuring primes in the natural number set
The difference between the square root of 493 and 491 is 0.0625
493 and 491 are both consecutively occuring primes in the natural number set
The difference between the square root of 491 and 489 is 0.0625
491 and 489 are both consecutively occuring primes in the natural number set
The difference between the square root of 489 and 487 is 0.0625
489 and 487 are both consecutively occuring primes in the natural number set
The difference between the square root of 487 and 485 is 0.0625
487 and 485 are both consecutively occuring primes in the natural number set
The difference between the square root of 485 and 483 is 0.0625
485 and 483 are both consecutively occuring primes in the natural number set
The difference between the square root of 483 and 481 is 0.0625
483 and 481 are both consecutively occuring primes in the natural number set
The difference between the square root of 481 and 479 is 0.0625
481 and 479 are both consecutively occuring primes in the natural number set
The difference between the square root of 479 and 477 is 0.0625
479 and 477 are both consecutively occuring primes in the natural number set
The difference between the square root of 477 and 475 is 0.0625
477 and 475 are both consecutively occuring primes in the natural number set
The difference between the square root of 475 and 473 is 0.0625
475 and 473 are both consecutively occuring primes in the natural number set
The difference between the square root of 473 and 471 is 0.0625
473 and 471 are both consecutively occuring primes in the natural number set
The difference between the square root of 471 and 469 is 0.0625
471 and 469 are both consecutively occuring primes in the natural number set
The difference between the square root of 469 and 467 is 0.0625
469 and 467 are both consecutively occuring primes in the natural number set
The difference between the square root of 467 and 465 is 0.0625
467 and 465 are both consecutively occuring primes in the natural number set
The difference between the square root of 465 and 463 is 0.0625
465 and 463 are both consecutively occuring primes in the natural number set
The difference between the square root of 463 and 461 is 0.0625
463 and 461 are both consecutively occuring primes in the natural number set
The difference between the square root of 461 and 459 is 0.0625
461 and 459 are both consecutively occuring primes in the natural number set
The difference between the square root of 459 and 457 is 0.0625
459 and 457 are both consecutively occuring primes in the natural number set
The difference between the square root of 457 and 455 is 0.0625
457 and 455 are both consecutively occuring primes in the natural number set
The difference between the square root of 455 and 453 is 0.0625
455 and 453 are both consecutively occuring primes in the natural number set
The difference between the square root of 453 and 451 is 0.0625
453 and 451 are both consecutively occuring primes in the natural number set
The difference between the square root of 451 and 449 is 0.0625
451 and 449 are both consecutively occuring primes in the natural number set
The difference between the square root of 449 and 447 is 0.0625
449 and 447 are both consecutively occuring primes in the natural number set
The difference between the square root of 447 and 445 is 0.0625
447 and 445 are both consecutively occuring primes in the natural number set
The difference between the square root of 445 and 443 is 0.0625
445 and 443 are both consecutively occuring primes in the natural number set
The difference between the square root of 443 and 441 is 0.0625
443 and 441 are both consecutively occuring primes in the natural number set
The difference between the square root of 441 and 439 is 0.0625
441 and 439 are both consecutively occuring primes in the natural number set
The difference between the square root of 439 and 437 is 0.0625
439 and 437 are both consecutively occuring primes in the natural number set
The difference between the square root of 437 and 435 is 0.0625
437 and 435 are both consecutively occuring primes in the natural number set
The difference between the square root of 435 and 433 is 0.0625
435 and 433 are both consecutively occuring primes in the natural number set
The difference between the square root of 433 and 431 is 0.0625
433 and 431 are both consecutively occuring primes in the natural number set
The difference between the square root of 431 and 429 is 0.0625
431 and 429 are both consecutively occuring primes in the natural number set
The difference between the square root of 429 and 427 is 0.0625
429 and 427 are both consecutively occuring primes in the natural number set
The difference between the square root of 427 and 425 is 0.0625
427 and 425 are both consecutively occuring primes in the natural number set
The difference between the square root of 425 and 423 is 0.0625
425 and 423 are both consecutively occuring primes in the natural number set
The difference between the square root of 423 and 421 is 0.0625
423 and 421 are both consecutively occuring primes in the natural number set
The difference between the square root of 421 and 419 is 0.0625
421 and 419 are both consecutively occuring primes in the natural number set
The difference between the square root of 419 and 417 is 0.0625
419 and 417 are both consecutively occuring primes in the natural number set
The difference between the square root of 417 and 415 is 0.0625
417 and 415 are both consecutively occuring primes in the natural number set
The difference between the square root of 415 and 413 is 0.0625
415 and 413 are both consecutively occuring primes in the natural number set
The difference between the square root of 413 and 411 is 0.0625
413 and 411 are both consecutively occuring primes in the natural number set
The difference between the square root of 411 and 409 is 0.0625
411 and 409 are both consecutively occuring primes in the natural number set
The difference between the square root of 409 and 407 is 0.0625
409 and 407 are both consecutively occuring primes in the natural number set
The difference between the square root of 407 and 405 is 0.0625
407 and 405 are both consecutively occuring primes in the natural number set
The difference between the square root of 405 and 403 is 0.0625
405 and 403 are both consecutively occuring primes in the natural number set
The difference between the square root of 403 and 401 is 0.0625
403 and 401 are both consecutively occuring primes in the natural number set
The difference between the square root of 401 and 399 is 0.0625
401 and 399 are both consecutively occuring primes in the natural number set
The difference between the square root of 399 and 397 is 0.0625
399 and 397 are both consecutively occuring primes in the natural number set
The difference between the square root of 397 and 395 is 0.0625
397 and 395 are both consecutively occuring primes in the natural number set
The difference between the square root of 395 and 393 is 0.0625
395 and 393 are both consecutively occuring primes in the natural number set
The difference between the square root of 393 and 391 is 0.0625
393 and 391 are both consecutively occuring primes in the natural number set
The difference between the square root of 391 and 389 is 0.0625
391 and 389 are both consecutively occuring primes in the natural number set
The difference between the square root of 389 and 387 is 0.0625
389 and 387 are both consecutively occuring primes in the natural number set
The difference between the square root of 387 and 385 is 0.0625
387 and 385 are both consecutively occuring primes in the natural number set
The difference between the square root of 385 and 383 is 0.0625
385 and 383 are both consecutively occuring primes in the natural number set
The difference between the square root of 383 and 381 is 0.0625
383 and 381 are both consecutively occuring primes in the natural number set
The difference between the square root of 381 and 379 is 0.0625
381 and 379 are both consecutively occuring primes in the natural number set
The difference between the square root of 379 and 377 is 0.0625
379 and 377 are both consecutively occuring primes in the natural number set
The difference between the square root of 377 and 375 is 0.0625
377 and 375 are both consecutively occuring primes in the natural number set
The difference between the square root of 375 and 373 is 0.0625
375 and 373 are both consecutively occuring primes in the natural number set
The difference between the square root of 373 and 371 is 0.0625
373 and 371 are both consecutively occuring primes in the natural number set
The difference between the square root of 371 and 369 is 0.0625
371 and 369 are both consecutively occuring primes in the natural number set
The difference between the square root of 369 and 367 is 0.0625
369 and 367 are both consecutively occuring primes in the natural number set
The difference between the square root of 367 and 365 is 0.0625
367 and 365 are both consecutively occuring primes in the natural number set
The difference between the square root of 365 and 363 is 0.0625
365 and 363 are both consecutively occuring primes in the natural number set
The difference between the square root of 363 and 361 is 0.0625
363 and 361 are both consecutively occuring primes in the natural number set
The difference between the square root of 361 and 359 is 0.0625
361 and 359 are both consecutively occuring primes in the natural number set
The difference between the square root of 359 and 357 is 0.0625
359 and 357 are both consecutively occuring primes in the natural number set
The difference between the square root of 357 and 355 is 0.0625
357 and 355 are both consecutively occuring primes in the natural number set
The difference between the square root of 355 and 353 is 0.0625
355 and 353 are both consecutively occuring primes in the natural number set
The difference between the square root of 353 and 351 is 0.0625
353 and 351 are both consecutively occuring primes in the natural number set
The difference between the square root of 351 and 349 is 0.0625
351 and 349 are both consecutively occuring primes in the natural number set
The difference between the square root of 349 and 347 is 0.0625
349 and 347 are both consecutively occuring primes in the natural number set
The difference between the square root of 347 and 345 is 0.0625
347 and 345 are both consecutively occuring primes in the natural number set
The difference between the square root of 345 and 343 is 0.0625
345 and 343 are both consecutively occuring primes in the natural number set
The difference between the square root of 343 and 341 is 0.0625
343 and 341 are both consecutively occuring primes in the natural number set
The difference between the square root of 341 and 339 is 0.0625
341 and 339 are both consecutively occuring primes in the natural number set
The difference between the square root of 339 and 337 is 0.0625
339 and 337 are both consecutively occuring primes in the natural number set
The difference between the square root of 337 and 335 is 0.0625
337 and 335 are both consecutively occuring primes in the natural number set
The difference between the square root of 335 and 333 is 0.0625
335 and 333 are both consecutively occuring primes in the natural number set
The difference between the square root of 333 and 331 is 0.0625
333 and 331 are both consecutively occuring primes in the natural number set
The difference between the square root of 331 and 329 is 0.0625
331 and 329 are both consecutively occuring primes in the natural number set
The difference between the square root of 329 and 327 is 0.0625
329 and 327 are both consecutively occuring primes in the natural number set
The difference between the square root of 327 and 325 is 0.0625
327 and 325 are both consecutively occuring primes in the natural number set
The difference between the square root of 325 and 323 is 0.0625
325 and 323 are both consecutively occuring primes in the natural number set
The difference between the square root of 323 and 321 is 0.0625
323 and 321 are both consecutively occuring primes in the natural number set
The difference between the square root of 321 and 319 is 0.0625
321 and 319 are both consecutively occuring primes in the natural number set
The difference between the square root of 319 and 317 is 0.0625
319 and 317 are both consecutively occuring primes in the natural number set
The difference between the square root of 317 and 315 is 0.0625
317 and 315 are both consecutively occuring primes in the natural number set
The difference between the square root of 315 and 313 is 0.0625
315 and 313 are both consecutively occuring primes in the natural number set
The difference between the square root of 313 and 311 is 0.0625
313 and 311 are both consecutively occuring primes in the natural number set
The difference between the square root of 311 and 309 is 0.0625
311 and 309 are both consecutively occuring primes in the natural number set
The difference between the square root of 309 and 307 is 0.0625
309 and 307 are both consecutively occuring primes in the natural number set
The difference between the square root of 307 and 305 is 0.0625
307 and 305 are both consecutively occuring primes in the natural number set
The difference between the square root of 305 and 303 is 0.0625
305 and 303 are both consecutively occuring primes in the natural number set
The difference between the square root of 303 and 301 is 0.0625
303 and 301 are both consecutively occuring primes in the natural number set
The difference between the square root of 301 and 299 is 0.0625
301 and 299 are both consecutively occuring primes in the natural number set
The difference between the square root of 299 and 297 is 0.0625
299 and 297 are both consecutively occuring primes in the natural number set
The difference between the square root of 297 and 295 is 0.0625
297 and 295 are both consecutively occuring primes in the natural number set
The difference between the square root of 295 and 293 is 0.0625
295 and 293 are both consecutively occuring primes in the natural number set
The difference between the square root of 293 and 291 is 0.0625
293 and 291 are both consecutively occuring primes in the natural number set
The difference between the square root of 291 and 289 is 0.0625
291 and 289 are both consecutively occuring primes in the natural number set
The difference between the square root of 289 and 287 is 0.0625
289 and 287 are both consecutively occuring primes in the natural number set
The difference between the square root of 287 and 285 is 0.0625
287 and 285 are both consecutively occuring primes in the natural number set
The difference between the square root of 285 and 283 is 0.0625
285 and 283 are both consecutively occuring primes in the natural number set
The difference between the square root of 283 and 281 is 0.0625
283 and 281 are both consecutively occuring primes in the natural number set
The difference between the square root of 281 and 279 is 0.0625
281 and 279 are both consecutively occuring primes in the natural number set
The difference between the square root of 279 and 277 is 0.0625
279 and 277 are both consecutively occuring primes in the natural number set
The difference between the square root of 277 and 275 is 0.0625
277 and 275 are both consecutively occuring primes in the natural number set
The difference between the square root of 275 and 273 is 0.0625
275 and 273 are both consecutively occuring primes in the natural number set
The difference between the square root of 273 and 271 is 0.0625
273 and 271 are both consecutively occuring primes in the natural number set
The difference between the square root of 271 and 269 is 0.0625
271 and 269 are both consecutively occuring primes in the natural number set
The difference between the square root of 269 and 267 is 0.0625
269 and 267 are both consecutively occuring primes in the natural number set
The difference between the square root of 267 and 265 is 0.0625
267 and 265 are both consecutively occuring primes in the natural number set
The difference between the square root of 265 and 263 is 0.0625
265 and 263 are both consecutively occuring primes in the natural number set
The difference between the square root of 263 and 261 is 0.0625
263 and 261 are both consecutively occuring primes in the natural number set
The difference between the square root of 261 and 259 is 0.0625
261 and 259 are both consecutively occuring primes in the natural number set
The difference between the square root of 259 and 257 is 0.0625
259 and 257 are both consecutively occuring primes in the natural number set
The difference between the square root of 257 and 255 is -7.90625
257 and 255 are both consecutively occuring primes in the natural number set
The difference between the square root of 255 and 253 is 0.125
255 and 253 are both consecutively occuring primes in the natural number set
The difference between the square root of 253 and 251 is 0.125
253 and 251 are both consecutively occuring primes in the natural number set
The difference between the square root of 251 and 249 is 0.125
251 and 249 are both consecutively occuring primes in the natural number set
The difference between the square root of 249 and 247 is 0.125
249 and 247 are both consecutively occuring primes in the natural number set
The difference between the square root of 247 and 245 is 0.125
247 and 245 are both consecutively occuring primes in the natural number set
The difference between the square root of 245 and 243 is 0.125
245 and 243 are both consecutively occuring primes in the natural number set
The difference between the square root of 243 and 241 is 0.125
243 and 241 are both consecutively occuring primes in the natural number set
The difference between the square root of 241 and 239 is 0.125
241 and 239 are both consecutively occuring primes in the natural number set
The difference between the square root of 239 and 237 is 0.125
239 and 237 are both consecutively occuring primes in the natural number set
The difference between the square root of 237 and 235 is 0.125
237 and 235 are both consecutively occuring primes in the natural number set
The difference between the square root of 235 and 233 is 0.125
235 and 233 are both consecutively occuring primes in the natural number set
The difference between the square root of 233 and 231 is 0.125
233 and 231 are both consecutively occuring primes in the natural number set
The difference between the square root of 231 and 229 is 0.125
231 and 229 are both consecutively occuring primes in the natural number set
The difference between the square root of 229 and 227 is 0.125
229 and 227 are both consecutively occuring primes in the natural number set
The difference between the square root of 227 and 225 is 0.125
227 and 225 are both consecutively occuring primes in the natural number set
The difference between the square root of 225 and 223 is 0.125
225 and 223 are both consecutively occuring primes in the natural number set
The difference between the square root of 223 and 221 is 0.125
223 and 221 are both consecutively occuring primes in the natural number set
The difference between the square root of 221 and 219 is 0.125
221 and 219 are both consecutively occuring primes in the natural number set
The difference between the square root of 219 and 217 is 0.125
219 and 217 are both consecutively occuring primes in the natural number set
The difference between the square root of 217 and 215 is 0.125
217 and 215 are both consecutively occuring primes in the natural number set
The difference between the square root of 215 and 213 is 0.125
215 and 213 are both consecutively occuring primes in the natural number set
The difference between the square root of 213 and 211 is 0.125
213 and 211 are both consecutively occuring primes in the natural number set
The difference between the square root of 211 and 209 is 0.125
211 and 209 are both consecutively occuring primes in the natural number set
The difference between the square root of 209 and 207 is 0.125
209 and 207 are both consecutively occuring primes in the natural number set
The difference between the square root of 207 and 205 is 0.125
207 and 205 are both consecutively occuring primes in the natural number set
The difference between the square root of 205 and 203 is 0.125
205 and 203 are both consecutively occuring primes in the natural number set
The difference between the square root of 203 and 201 is 0.125
203 and 201 are both consecutively occuring primes in the natural number set
The difference between the square root of 201 and 199 is 0.125
201 and 199 are both consecutively occuring primes in the natural number set
The difference between the square root of 199 and 197 is 0.125
199 and 197 are both consecutively occuring primes in the natural number set
The difference between the square root of 197 and 195 is 0.125
197 and 195 are both consecutively occuring primes in the natural number set
The difference between the square root of 195 and 193 is 0.125
195 and 193 are both consecutively occuring primes in the natural number set
The difference between the square root of 193 and 191 is 0.125
193 and 191 are both consecutively occuring primes in the natural number set
The difference between the square root of 191 and 189 is 0.125
191 and 189 are both consecutively occuring primes in the natural number set
The difference between the square root of 189 and 187 is 0.125
189 and 187 are both consecutively occuring primes in the natural number set
The difference between the square root of 187 and 185 is 0.125
187 and 185 are both consecutively occuring primes in the natural number set
The difference between the square root of 185 and 183 is 0.125
185 and 183 are both consecutively occuring primes in the natural number set
The difference between the square root of 183 and 181 is 0.125
183 and 181 are both consecutively occuring primes in the natural number set
The difference between the square root of 181 and 179 is 0.125
181 and 179 are both consecutively occuring primes in the natural number set
The difference between the square root of 179 and 177 is 0.125
179 and 177 are both consecutively occuring primes in the natural number set
The difference between the square root of 177 and 175 is 0.125
177 and 175 are both consecutively occuring primes in the natural number set
The difference between the square root of 175 and 173 is 0.125
175 and 173 are both consecutively occuring primes in the natural number set
The difference between the square root of 173 and 171 is 0.125
173 and 171 are both consecutively occuring primes in the natural number set
The difference between the square root of 171 and 169 is 0.125
171 and 169 are both consecutively occuring primes in the natural number set
The difference between the square root of 169 and 167 is 0.125
169 and 167 are both consecutively occuring primes in the natural number set
The difference between the square root of 167 and 165 is 0.125
167 and 165 are both consecutively occuring primes in the natural number set
The difference between the square root of 165 and 163 is 0.125
165 and 163 are both consecutively occuring primes in the natural number set
The difference between the square root of 163 and 161 is 0.125
163 and 161 are both consecutively occuring primes in the natural number set
The difference between the square root of 161 and 159 is 0.125
161 and 159 are both consecutively occuring primes in the natural number set
The difference between the square root of 159 and 157 is 0.125
159 and 157 are both consecutively occuring primes in the natural number set
The difference between the square root of 157 and 155 is 0.125
157 and 155 are both consecutively occuring primes in the natural number set
The difference between the square root of 155 and 153 is 0.125
155 and 153 are both consecutively occuring primes in the natural number set
The difference between the square root of 153 and 151 is 0.125
153 and 151 are both consecutively occuring primes in the natural number set
The difference between the square root of 151 and 149 is 0.125
151 and 149 are both consecutively occuring primes in the natural number set
The difference between the square root of 149 and 147 is 0.125
149 and 147 are both consecutively occuring primes in the natural number set
The difference between the square root of 147 and 145 is 0.125
147 and 145 are both consecutively occuring primes in the natural number set
The difference between the square root of 145 and 143 is 0.125
145 and 143 are both consecutively occuring primes in the natural number set
The difference between the square root of 143 and 141 is 0.125
143 and 141 are both consecutively occuring primes in the natural number set
The difference between the square root of 141 and 139 is 0.125
141 and 139 are both consecutively occuring primes in the natural number set
The difference between the square root of 139 and 137 is 0.125
139 and 137 are both consecutively occuring primes in the natural number set
The difference between the square root of 137 and 135 is 0.125
137 and 135 are both consecutively occuring primes in the natural number set
The difference between the square root of 135 and 133 is 0.125
135 and 133 are both consecutively occuring primes in the natural number set
The difference between the square root of 133 and 131 is 0.125
133 and 131 are both consecutively occuring primes in the natural number set
The difference between the square root of 131 and 129 is 0.125
131 and 129 are both consecutively occuring primes in the natural number set
The difference between the square root of 129 and 127 is 0.125
129 and 127 are both consecutively occuring primes in the natural number set
The difference between the square root of 127 and 125 is 0.125
127 and 125 are both consecutively occuring primes in the natural number set
The difference between the square root of 125 and 123 is 0.125
125 and 123 are both consecutively occuring primes in the natural number set
The difference between the square root of 123 and 121 is 0.125
123 and 121 are both consecutively occuring primes in the natural number set
The difference between the square root of 121 and 119 is 0.125
121 and 119 are both consecutively occuring primes in the natural number set
The difference between the square root of 119 and 117 is 0.125
119 and 117 are both consecutively occuring primes in the natural number set
The difference between the square root of 117 and 115 is 0.125
117 and 115 are both consecutively occuring primes in the natural number set
The difference between the square root of 115 and 113 is 0.125
115 and 113 are both consecutively occuring primes in the natural number set
The difference between the square root of 113 and 111 is 0.125
113 and 111 are both consecutively occuring primes in the natural number set
The difference between the square root of 111 and 109 is 0.125
111 and 109 are both consecutively occuring primes in the natural number set
The difference between the square root of 109 and 107 is 0.125
109 and 107 are both consecutively occuring primes in the natural number set
The difference between the square root of 107 and 105 is 0.125
107 and 105 are both consecutively occuring primes in the natural number set
The difference between the square root of 105 and 103 is 0.125
105 and 103 are both consecutively occuring primes in the natural number set
The difference between the square root of 103 and 101 is 0.125
103 and 101 are both consecutively occuring primes in the natural number set
The difference between the square root of 101 and 99 is 0.125
101 and 99 are both consecutively occuring primes in the natural number set
The difference between the square root of 99 and 97 is 0.125
99 and 97 are both consecutively occuring primes in the natural number set
The difference between the square root of 97 and 95 is 0.125
97 and 95 are both consecutively occuring primes in the natural number set
The difference between the square root of 95 and 93 is 0.125
95 and 93 are both consecutively occuring primes in the natural number set
The difference between the square root of 93 and 91 is 0.125
93 and 91 are both consecutively occuring primes in the natural number set
The difference between the square root of 91 and 89 is 0.125
91 and 89 are both consecutively occuring primes in the natural number set
The difference between the square root of 89 and 87 is 0.125
89 and 87 are both consecutively occuring primes in the natural number set
The difference between the square root of 87 and 85 is 0.125
87 and 85 are both consecutively occuring primes in the natural number set
The difference between the square root of 85 and 83 is 0.125
85 and 83 are both consecutively occuring primes in the natural number set
The difference between the square root of 83 and 81 is 0.125
83 and 81 are both consecutively occuring primes in the natural number set
The difference between the square root of 81 and 79 is 0.125
81 and 79 are both consecutively occuring primes in the natural number set
The difference between the square root of 79 and 77 is 0.125
79 and 77 are both consecutively occuring primes in the natural number set
The difference between the square root of 77 and 75 is 0.125
77 and 75 are both consecutively occuring primes in the natural number set
The difference between the square root of 75 and 73 is 0.125
75 and 73 are both consecutively occuring primes in the natural number set
The difference between the square root of 73 and 71 is 0.125
73 and 71 are both consecutively occuring primes in the natural number set
The difference between the square root of 71 and 69 is 0.125
71 and 69 are both consecutively occuring primes in the natural number set
The difference between the square root of 69 and 67 is 0.125
69 and 67 are both consecutively occuring primes in the natural number set
The difference between the square root of 67 and 65 is 0.125
67 and 65 are both consecutively occuring primes in the natural number set
The difference between the square root of 65 and 63 is -3.8125
65 and 63 are both consecutively occuring primes in the natural number set
The difference between the square root of 63 and 61 is 0.25
63 and 61 are both consecutively occuring primes in the natural number set
The difference between the square root of 61 and 59 is 0.25
61 and 59 are both consecutively occuring primes in the natural number set
The difference between the square root of 59 and 57 is 0.25
59 and 57 are both consecutively occuring primes in the natural number set
The difference between the square root of 57 and 55 is 0.25
57 and 55 are both consecutively occuring primes in the natural number set
The difference between the square root of 55 and 53 is 0.25
55 and 53 are both consecutively occuring primes in the natural number set
The difference between the square root of 53 and 51 is 0.25
53 and 51 are both consecutively occuring primes in the natural number set
The difference between the square root of 51 and 49 is 0.25
51 and 49 are both consecutively occuring primes in the natural number set
The difference between the square root of 49 and 47 is 0.25
49 and 47 are both consecutively occuring primes in the natural number set
The difference between the square root of 47 and 45 is 0.25
47 and 45 are both consecutively occuring primes in the natural number set
The difference between the square root of 45 and 43 is 0.25
45 and 43 are both consecutively occuring primes in the natural number set
The difference between the square root of 43 and 41 is 0.25
43 and 41 are both consecutively occuring primes in the natural number set
The difference between the square root of 41 and 39 is 0.25
41 and 39 are both consecutively occuring primes in the natural number set
The difference between the square root of 39 and 37 is 0.25
39 and 37 are both consecutively occuring primes in the natural number set
The difference between the square root of 37 and 35 is 0.25
37 and 35 are both consecutively occuring primes in the natural number set
The difference between the square root of 35 and 33 is 0.25
35 and 33 are both consecutively occuring primes in the natural number set
The difference between the square root of 33 and 31 is 0.25
33 and 31 are both consecutively occuring primes in the natural number set
The difference between the square root of 31 and 29 is 0.25
31 and 29 are both consecutively occuring primes in the natural number set
The difference between the square root of 29 and 27 is 0.25
29 and 27 are both consecutively occuring primes in the natural number set
The difference between the square root of 27 and 25 is 0.25
27 and 25 are both consecutively occuring primes in the natural number set
The difference between the square root of 25 and 23 is 0.25
25 and 23 are both consecutively occuring primes in the natural number set
The difference between the square root of 23 and 21 is 0.25
23 and 21 are both consecutively occuring primes in the natural number set
The difference between the square root of 21 and 19 is 0.25
21 and 19 are both consecutively occuring primes in the natural number set
The difference between the square root of 19 and 17 is 0.25
19 and 17 are both consecutively occuring primes in the natural number set
The difference between the square root of 17 and 15 is -1.625
17 and 15 are both consecutively occuring primes in the natural number set
The difference between the square root of 15 and 13 is 0.5
15 and 13 are both consecutively occuring primes in the natural number set
The difference between the square root of 13 and 11 is 0.5
13 and 11 are both consecutively occuring primes in the natural number set
The difference between the square root of 11 and 9 is 0.5
11 and 9 are both consecutively occuring primes in the natural number set
The difference between the square root of 9 and 7 is 0.5
9 and 7 are both consecutively occuring primes in the natural number set
The difference between the square root of 7 and 5 is 0.5
7 and 5 are both consecutively occuring primes in the natural number set
The difference between the square root of 5 and 3 is -0.25
5 and 3 are both consecutively occuring primes in the natural number set
The mean of the differences of the consecutively occuring primes square roots are: 0.05967620481927711; the median: 0.0625 the mode(s): [-7.90625 -3.8125  -1.625   -0.25     0.0625   0.125    0.25     0.5    ]
"""