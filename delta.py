def calc_delta(toponym):
    lowerCorner = list(map(float, toponym["boundedBy"]["Envelope"]["lowerCorner"].split()))
    upperCorner = list(map(float, toponym["boundedBy"]["Envelope"]["upperCorner"].split()))

    return [upperCorner[0] - lowerCorner[0], upperCorner[1] - lowerCorner[1]]