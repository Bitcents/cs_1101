def any_lowercase4(s):

     flag = False

     for c in s:

          flag = flag or c.islower()

     return flag


test = any_lowercase4('tamE')
print(test)