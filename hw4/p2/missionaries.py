from __future__ import annotations


def cross_river(cannibals:int, missionaries:int) -> list|None:
    """
    Traditional missionaries and cannibals problem.  3 missionaries
    and 3 cannibals come to a river with a boat that will seat up to
    two people.  All 3 missionaries and 3 cannibals must reach the
    far side, but at no time can there be more cannibals than missionaries
    on either side of the river or the cannibals will eat the missionaries.
    By what sequence of crossings can all missionaries and cannibals
    reach the far side with none being eaten?
    
    :param missionaries: number of missionaries 
    :param cannibals: number of canibals.
    :return: list of crossings where each pair represents a crossing of
       (m, c) where m and c are integers denoting the number of
       missionaries and cannibals in the boat respectively. m + c <= 2.
       The ith pair corresponds to the ith crossing. All crosses for
       which i is even corresponds to crossing starting from the near
       side.  Odd i corresponds to a crossing starting from the far side.
       The end of the sequence of crossings all missionaries and cannibals
       have been moved from the near to the far side of the river.
    """
    already_considered = set()

    def near(near_c, near_m, far_c, far_m) -> list|None:
        # taking boat from near side to far side.
        assert near_m + far_m == missionaries
        assert near_c + far_c == cannibals
        if near_c > near_m > 0 or far_c > far_m > 0:
            return None
        if (near_c, near_m, far_c, far_m) in already_considered:
            return None
        elif near_c == 0 and near_m == 0:
            return []

        already_considered.add((near_c, near_m, far_c, far_m))

        # three possibilities on the mix of people in the boat
        # crossing from the near side: send m and c, m and m, or c and c.
        
        # going from near to far side. "xings" == "crossings"
        if near_m > 0 and near_c > 0:
            xings = far(near_c - 1, near_m - 1, far_c + 1, far_m + 1)
            if xings is not None:
                xings.append((1, 1))
                return xings

        if near_m > 1:
            xings = far(near_c, near_m - 2, far_c, far_m + 2)
            if xings is not None:
                xings.append((0, 2))
                return xings

        if near_c > 1:
            xings = far(near_c - 2, near_m, far_c + 2, far_m)
            if xings is not None:
                xings.append((2, 0))
                return xings

        
    def far(near_c, near_m, far_c, far_m) -> list|None:
        # taking boat from far side to near side.
        assert near_m + far_m == missionaries
        assert near_c + far_c == cannibals
        if near_c > near_m > 0 or far_c > far_m > 0:
            return None
        elif near_c == 0 and near_m == 0:
            return []

        # back
        if far_m > 0:
            xings = near(near_c, near_m + 1, far_c, far_m - 1)
            if xings is not None:
                xings.append((0, 1))
                return xings

        if far_c > 0:
            xings = near(near_c + 1, near_m, far_c - 1, far_m)
            if xings is not None:
                xings.append((1, 0))
                return xings

        if far_m > 0 and far_c > 0:
            xings = near(near_c + 1, near_m + 1, far_c - 1, far_m - 1)
            if xings is not None:
                xings.append((1, 1))
                return xings

        if far_m > 1:
            xings = near(near_c, near_m + 2, far_c, far_m - 2)
            if xings is not None:
                xings.append((0, 2))
                return xings

        if far_c > 1:
            xings = near(near_c + 2, near_m, far_c - 2, far_m)
            if xings is not None:
                xings.append((2, 0))
                return xings

        return None

    # The next two cases don't occur in the 3-missionaries and 3 cannibals problem.
    # They may however occur if I don't constrain the number of missionaries
    # and cannibals to 3.
    if cannibals == 0 and missionaries == 1:
        return [(0, 1)]
    elif cannibals == 1 and missionaries == 0:
        return [(1, 0)]

    x = near(cannibals, missionaries, 0, 0)
    return list(reversed(x))


if __name__ == "__main__":
    crossings = cross_river(3, 3)
    for i, (m, c) in enumerate(crossings):
        if i % 2 == 0:
            print(f"Near to far with {c} cannibals and {m} missionaries")
        else:
            print(f"Far to near with {c} cannibals and {m} missionaries")