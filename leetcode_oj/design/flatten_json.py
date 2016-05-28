def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[str(name[:-1])] = str(x)
            print "x: ", x, " name: ", name , " out: ", out

    flatten(y)
    return out

s = {'x':1, 'y':1, 'z':{'a':1,'b':2}}
print flatten_json(s)
