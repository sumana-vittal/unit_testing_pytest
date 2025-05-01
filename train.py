def get_route_score(num_trains):
    # return the points for a train route of the given length
    if num_trains <= 2:
        score = num_trains
    elif num_trains == 3:
        score = 4
    elif num_trains == 4:
        score = 7
    else:
        score = num_trains * 2

    return score



