import re
import os
res = list()
def fincComment(directory):

    result = dict()
    for dir in directory:
        if type(dir) is None:
            break
        hand = open(dir)
        for line in hand:
            line = line.rstrip()
            if re.search('#', line):
                result[line] = dir
                # print(result)
                # print(line)
    return result


def search(dirname):
    flist = os.listdir(dirname)
    for f in flist:
        if f is None:
            break
        next = os.path.join(dirname, f)
        if os.path.isdir(next):
            search(next)
        else:
            doFileWork(next)

def doFileWork(filename):
    ext = os.path.splitext(filename)[-1]
    if ext == '.py': res.append(filename)
    return res

search("/Users/yevgnenll/dev/python/django")
for idx, a in enumerate(res):
    if a is None:
        del res[idx]
# print(res)
print(fincComment(res)["        # realiased when used in a subquery"])


# print(fincComment(search("/Users/yevgnenll/dev/python/django")))

