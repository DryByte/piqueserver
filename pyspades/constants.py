HIT_VALUES = {
    2 : 100,
    1 : 40,
    3 : 25
}

HIT_CONSTANTS = dict([(v, k) for (k, v) in HIT_VALUES.iteritems()])

BUILD_BLOCK, DESTROY_BLOCK, SPADE_DESTROY, GRENADE_DESTROY = xrange(4)