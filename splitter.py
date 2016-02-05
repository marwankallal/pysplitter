

words = set(["ab", "bc", "bb"])
string = "abbc"
strlen = len(string)

found = dict()

for start in range(0, strlen):
    for end in range(strlen, start, -1):
        test_str = string[start:end]
        if test_str in words:
            found[(start, end - 1)] = test_str

for key in found.keys():
    #TODO: assemble into sentences

