# -*- coding: UTF-8 -*-


def reflect_get_class(class_full_name):
    # Get the class by name.
    # Input: full class name
    # Output: the class itself
    parts = class_full_name.split('.')
    # print(parts);
    module = ".".join(parts[:-1])
    # print(module);
    m = __import__(module)
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m