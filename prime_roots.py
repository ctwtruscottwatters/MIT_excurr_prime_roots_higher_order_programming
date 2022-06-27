# -*- coding: utf-8 -*-
"""
Charles Thomas Wallace Truscott, Massachusetts Institute of Technology Student 6.0001  2022 Extracurricular Study

Thank you edX.org

github.com/ctwtruscottwatters

"""


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
        print("guess: {} high: {} low: {}".format(guess, high, low))
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
    print(x)
if __name__ == "__main__": main()

""" 
Square roots of the first ~1000 prime numbers 

Charles Thomas Wallace Truscott, Byron Bay NSW 2481

[(999, 31.21875), (997, 31.15625), (995, 31.09375), (993, 31.03125), (991, 30.96875), (989, 30.90625), (987, 30.84375), (985, 30.78125), (983, 30.71875), (981, 30.65625), (979, 30.59375), (977, 30.53125), (975, 30.46875), (973, 30.40625), (971, 30.34375), (969, 30.28125), (967, 30.21875), (965, 30.15625), (963, 30.09375), (961, 30.03125), (959, 29.96875), (957, 29.90625), (955, 29.84375), (953, 29.78125), (951, 29.71875), (949, 29.65625), (947, 29.59375), (945, 29.53125), (943, 29.46875), (941, 29.40625), (939, 29.34375), (937, 29.28125), (935, 29.21875), (933, 29.15625), (931, 29.09375), (929, 29.03125), (927, 28.96875), (925, 28.90625), (923, 28.84375), (921, 28.78125), (919, 28.71875), (917, 28.65625), (915, 28.59375), (913, 28.53125), (911, 28.46875), (909, 28.40625), (907, 28.34375), (905, 28.28125), (903, 28.21875), (901, 28.15625), (899, 28.09375), (897, 28.03125), (895, 27.96875), (893, 27.90625), (891, 27.84375), (889, 27.78125), (887, 27.71875), (885, 27.65625), (883, 27.59375), (881, 27.53125), (879, 27.46875), (877, 27.40625), (875, 27.34375), (873, 27.28125), (871, 27.21875), (869, 27.15625), (867, 27.09375), (865, 27.03125), (863, 26.96875), (861, 26.90625), (859, 26.84375), (857, 26.78125), (855, 26.71875), (853, 26.65625), (851, 26.59375), (849, 26.53125), (847, 26.46875), (845, 26.40625), (843, 26.34375), (841, 26.28125), (839, 26.21875), (837, 26.15625), (835, 26.09375), (833, 26.03125), (831, 25.96875), (829, 25.90625), (827, 25.84375), (825, 25.78125), (823, 25.71875), (821, 25.65625), (819, 25.59375), (817, 25.53125), (815, 25.46875), (813, 25.40625), (811, 25.34375), (809, 25.28125), (807, 25.21875), (805, 25.15625), (803, 25.09375), (801, 25.03125), (799, 24.96875), (797, 24.90625), (795, 24.84375), (793, 24.78125), (791, 24.71875), (789, 24.65625), (787, 24.59375), (785, 24.53125), (783, 24.46875), (781, 24.40625), (779, 24.34375), (777, 24.28125), (775, 24.21875), (773, 24.15625), (771, 24.09375), (769, 24.03125), (767, 23.96875), (765, 23.90625), (763, 23.84375), (761, 23.78125), (759, 23.71875), (757, 23.65625), (755, 23.59375), (753, 23.53125), (751, 23.46875), (749, 23.40625), (747, 23.34375), (745, 23.28125), (743, 23.21875), (741, 23.15625), (739, 23.09375), (737, 23.03125), (735, 22.96875), (733, 22.90625), (731, 22.84375), (729, 22.78125), (727, 22.71875), (725, 22.65625), (723, 22.59375), (721, 22.53125), (719, 22.46875), (717, 22.40625), (715, 22.34375), (713, 22.28125), (711, 22.21875), (709, 22.15625), (707, 22.09375), (705, 22.03125), (703, 21.96875), (701, 21.90625), (699, 21.84375), (697, 21.78125), (695, 21.71875), (693, 21.65625), (691, 21.59375), (689, 21.53125), (687, 21.46875), (685, 21.40625), (683, 21.34375), (681, 21.28125), (679, 21.21875), (677, 21.15625), (675, 21.09375), (673, 21.03125), (671, 20.96875), (669, 20.90625), (667, 20.84375), (665, 20.78125), (663, 20.71875), (661, 20.65625), (659, 20.59375), (657, 20.53125), (655, 20.46875), (653, 20.40625), (651, 20.34375), (649, 20.28125), (647, 20.21875), (645, 20.15625), (643, 20.09375), (641, 20.03125), (639, 19.96875), (637, 19.90625), (635, 19.84375), (633, 19.78125), (631, 19.71875), (629, 19.65625), (627, 19.59375), (625, 19.53125), (623, 19.46875), (621, 19.40625), (619, 19.34375), (617, 19.28125), (615, 19.21875), (613, 19.15625), (611, 19.09375), (609, 19.03125), (607, 18.96875), (605, 18.90625), (603, 18.84375), (601, 18.78125), (599, 18.71875), (597, 18.65625), (595, 18.59375), (593, 18.53125), (591, 18.46875), (589, 18.40625), (587, 18.34375), (585, 18.28125), (583, 18.21875), (581, 18.15625), (579, 18.09375), (577, 18.03125), (575, 17.96875), (573, 17.90625), (571, 17.84375), (569, 17.78125), (567, 17.71875), (565, 17.65625), (563, 17.59375), (561, 17.53125), (559, 17.46875), (557, 17.40625), (555, 17.34375), (553, 17.28125), (551, 17.21875), (549, 17.15625), (547, 17.09375), (545, 17.03125), (543, 16.96875), (541, 16.90625), (539, 16.84375), (537, 16.78125), (535, 16.71875), (533, 16.65625), (531, 16.59375), (529, 16.53125), (527, 16.46875), (525, 16.40625), (523, 16.34375), (521, 16.28125), (519, 16.21875), (517, 16.15625), (515, 16.09375), (513, 16.03125), (511, 15.96875), (509, 15.90625), (507, 15.84375), (505, 15.78125), (503, 15.71875), (501, 15.65625), (499, 15.59375), (497, 15.53125), (495, 15.46875), (493, 15.40625), (491, 15.34375), (489, 15.28125), (487, 15.21875), (485, 15.15625), (483, 15.09375), (481, 15.03125), (479, 14.96875), (477, 14.90625), (475, 14.84375), (473, 14.78125), (471, 14.71875), (469, 14.65625), (467, 14.59375), (465, 14.53125), (463, 14.46875), (461, 14.40625), (459, 14.34375), (457, 14.28125), (455, 14.21875), (453, 14.15625), (451, 14.09375), (449, 14.03125), (447, 13.96875), (445, 13.90625), (443, 13.84375), (441, 13.78125), (439, 13.71875), (437, 13.65625), (435, 13.59375), (433, 13.53125), (431, 13.46875), (429, 13.40625), (427, 13.34375), (425, 13.28125), (423, 13.21875), (421, 13.15625), (419, 13.09375), (417, 13.03125), (415, 12.96875), (413, 12.90625), (411, 12.84375), (409, 12.78125), (407, 12.71875), (405, 12.65625), (403, 12.59375), (401, 12.53125), (399, 12.46875), (397, 12.40625), (395, 12.34375), (393, 12.28125), (391, 12.21875), (389, 12.15625), (387, 12.09375), (385, 12.03125), (383, 11.96875), (381, 11.90625), (379, 11.84375), (377, 11.78125), (375, 11.71875), (373, 11.65625), (371, 11.59375), (369, 11.53125), (367, 11.46875), (365, 11.40625), (363, 11.34375), (361, 11.28125), (359, 11.21875), (357, 11.15625), (355, 11.09375), (353, 11.03125), (351, 10.96875), (349, 10.90625), (347, 10.84375), (345, 10.78125), (343, 10.71875), (341, 10.65625), (339, 10.59375), (337, 10.53125), (335, 10.46875), (333, 10.40625), (331, 10.34375), (329, 10.28125), (327, 10.21875), (325, 10.15625), (323, 10.09375), (321, 10.03125), (319, 9.96875), (317, 9.90625), (315, 9.84375), (313, 9.78125), (311, 9.71875), (309, 9.65625), (307, 9.59375), (305, 9.53125), (303, 9.46875), (301, 9.40625), (299, 9.34375), (297, 9.28125), (295, 9.21875), (293, 9.15625), (291, 9.09375), (289, 9.03125), (287, 8.96875), (285, 8.90625), (283, 8.84375), (281, 8.78125), (279, 8.71875), (277, 8.65625), (275, 8.59375), (273, 8.53125), (271, 8.46875), (269, 8.40625), (267, 8.34375), (265, 8.28125), (263, 8.21875), (261, 8.15625), (259, 8.09375), (257, 8.03125), (255, 15.9375), (253, 15.8125), (251, 15.6875), (249, 15.5625), (247, 15.4375), (245, 15.3125), (243, 15.1875), (241, 15.0625), (239, 14.9375), (237, 14.8125), (235, 14.6875), (233, 14.5625), (231, 14.4375), (229, 14.3125), (227, 14.1875), (225, 14.0625), (223, 13.9375), (221, 13.8125), (219, 13.6875), (217, 13.5625), (215, 13.4375), (213, 13.3125), (211, 13.1875), (209, 13.0625), (207, 12.9375), (205, 12.8125), (203, 12.6875), (201, 12.5625), (199, 12.4375), (197, 12.3125), (195, 12.1875), (193, 12.0625), (191, 11.9375), (189, 11.8125), (187, 11.6875), (185, 11.5625), (183, 11.4375), (181, 11.3125), (179, 11.1875), (177, 11.0625), (175, 10.9375), (173, 10.8125), (171, 10.6875), (169, 10.5625), (167, 10.4375), (165, 10.3125), (163, 10.1875), (161, 10.0625), (159, 9.9375), (157, 9.8125), (155, 9.6875), (153, 9.5625), (151, 9.4375), (149, 9.3125), (147, 9.1875), (145, 9.0625), (143, 8.9375), (141, 8.8125), (139, 8.6875), (137, 8.5625), (135, 8.4375), (133, 8.3125), (131, 8.1875), (129, 8.0625), (127, 7.9375), (125, 7.8125), (123, 7.6875), (121, 7.5625), (119, 7.4375), (117, 7.3125), (115, 7.1875), (113, 7.0625), (111, 6.9375), (109, 6.8125), (107, 6.6875), (105, 6.5625), (103, 6.4375), (101, 6.3125), (99, 6.1875), (97, 6.0625), (95, 5.9375), (93, 5.8125), (91, 5.6875), (89, 5.5625), (87, 5.4375), (85, 5.3125), (83, 5.1875), (81, 5.0625), (79, 4.9375), (77, 4.8125), (75, 4.6875), (73, 4.5625), (71, 4.4375), (69, 4.3125), (67, 4.1875), (65, 4.0625), (63, 7.875), (61, 7.625), (59, 7.375), (57, 7.125), (55, 6.875), (53, 6.625), (51, 6.375), (49, 6.125), (47, 5.875), (45, 5.625), (43, 5.375), (41, 5.125), (39, 4.875), (37, 4.625), (35, 4.375), (33, 4.125), (31, 3.875), (29, 3.625), (27, 3.375), (25, 3.125), (23, 2.875), (21, 2.625), (19, 2.375), (17, 2.125), (15, 3.75), (13, 3.25), (11, 2.75), (9, 2.25), (7, 1.75), (5, 1.25), (3, 1.5)]

Thank you Eric Grimson, Ana Bell, edX Corporate Offices

"""