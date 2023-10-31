#!/usr/bin/python3
def magic_string(time=[0]):
    time[0] = time[0] + 1
    return "BestSchool" + (", BestSchool" * (time[0] - 1))
