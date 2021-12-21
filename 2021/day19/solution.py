# > 4:00:00

import json
import numpy as np
from itertools import combinations
from collections import defaultdict, Counter

def orient_points(points, axis, flip, rot, extra_flip):
    non_principal  = [j for j in list(range(3)) if not j == axis]
    points_oriented_x = [flip * extra_flip * pt2[axis] for pt2 in points]
    points_oriented_other = (1j ** rot) * np.array([pt2[non_principal[0]] + (1j * pt2[non_principal[1]]) for pt2 in points])
    points_oriented = [[x, flip * int(y.real), int(y.imag)] for (x, y) in zip(points_oriented_x, points_oriented_other)]
    return points_oriented

def check_for_1d_overlap(pts_1, pts_2):
    """A quick check to optimise rejecting pairs where no dimension
        could possibly match the x-axis of the first scanner.
    """
    for flip in [1, -1]:
        pts_2_oriented = [pt * flip for pt in pts_2]

        for pt_1 in pts_1:
            for pt_2 in pts_2_oriented:
                pts_1_shifted = [pt - pt_1 for pt in pts_1]
                pts_2_shifted = [pt - pt_2 for pt in pts_2_oriented]

                intersection = list((Counter(pts_1_shifted) & Counter(pts_2_shifted)).elements())
                if len(intersection) >= 12:
                    return True
    
    return False

def check_for_overlap(scanner_1, scanner_2):
    if any(check_for_1d_overlap([pt[0] for pt in scanner_1], [pt[i] for pt in scanner_2]) for i in range(3)):
        for axis in range(3):
            for flip in [1, -1]:
                for extra_flip in [1, -1]: # Not sure why I need this but seems to not work without it
                    for rot in range(4):
                        scanner_2_oriented = orient_points(scanner_2, axis, flip, rot, extra_flip)

                        for pos_1 in scanner_1:
                            for pos_2 in scanner_2_oriented:
                                scanner_1_shifted = [list(np.array(pos) - np.array(pos_1)) for pos in scanner_1]
                                scanner_2_shifted = [list(np.array(pos) - np.array(pos_2)) for pos in scanner_2_oriented]

                                scanner_1_pos_set = set(["_".join([str(p) for p in pos]) for pos in scanner_1_shifted])
                                scanner_2_pos_set = set(["_".join([str(p) for p in pos]) for pos in scanner_2_shifted])

                                if len(scanner_1_pos_set.intersection(scanner_2_pos_set)) >= 12:
                                    return axis, flip, rot, extra_flip, list(np.array(pos_1) - np.array(pos_2))

if __name__ == "__main__":
    f = open("./input.txt", "r")
    input = f.read().splitlines()
    
    scanners = []
    for ln in input:
        if "scanner" in ln:
            scanners.append([])
        elif "," in ln:
            scanners[-1].append(json.loads("[" + ln + "]"))

    matched_scanners = {0}
    newly_matched_scanners = {0}
    unmatched_scanners = set(range(1, len(scanners)))

    overlaps = []
    while len(unmatched_scanners) > 0:
        new_newly_matched_scanners = set()
        for scanner_1_index in newly_matched_scanners:
            for scanner_2_index in unmatched_scanners:
                scanner_1 = scanners[scanner_1_index]
                scanner_2 = scanners[scanner_2_index]

                translation = check_for_overlap(scanner_1, scanner_2)
                if translation:
                    overlaps.append({
                        "translation": translation,
                        "scanner_1_index": scanners.index(scanner_1),
                        "scanner_2_index": scanners.index(scanner_2),
                    })
                    new_newly_matched_scanners.add(scanner_2_index)

        unmatched_scanners = unmatched_scanners.difference(new_newly_matched_scanners)
        newly_matched_scanners = new_newly_matched_scanners

    scanner_translations = defaultdict(list)
    for scanner_index in range(len(scanners)):
        current_scanner_index = scanner_index
        while current_scanner_index > 0:
            next_overlap = [ r for r in overlaps if r["scanner_2_index"] == current_scanner_index ][0]
            current_scanner_index = next_overlap["scanner_1_index"]
            scanner_translations[scanner_index].append(next_overlap["translation"])

    # part 1
    all_points = set()
    for scanner_index, scanner in enumerate(scanners):
        points = scanner
        for translation in scanner_translations[scanner_index]:
            points = orient_points(points, *translation[:-1])
            points = [list(np.array(p) + np.array(translation[-1])) for p in points]

        all_points = all_points.union(set([str(p) for p in points]))
    print(len(all_points))


    # part 2
    all_centers = []
    for scanner_index, scanner in enumerate(scanners):
        points = [[0, 0, 0]]
        for translation in scanner_translations[scanner_index]:
            points = orient_points(points, *translation[:-1])
            points = [list(np.array(p) + np.array(translation[-1])) for p in points]

        all_centers.append(points[0])

    max_manhattan_dist = 0
    for pos_1, pos_2 in combinations(all_centers, r=2):
        d = sum((abs(pos_1[i] - pos_2[i]) for i in range(3)))
        if d > max_manhattan_dist:
            max_manhattan_dist = d
    print(max_manhattan_dist)
