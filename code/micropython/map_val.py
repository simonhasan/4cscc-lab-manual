def map_val(val, in_01, in_02, map_to_01, map_to_02):
    '''Map a value from one range to another
    :param val: The value to map
    :param in_01: The start of the input range
    :param in_02: The end of the input range
    :param map_to_01: The start of the output range
    :param map_to_02: The end of the output range
    return: The mapped value
    '''
    return (val - in_01) * (map_to_02 - map_to_01) // (in_02 - in_01) + map_to_01