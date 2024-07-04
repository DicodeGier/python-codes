from abs import math   #?

triangl(a,b):                           #?
    x1 = float(a[1: a.index(",")])      #?
    y1 = float(a[a.index(","): len(a)]) #?
    x2 = float(b[1: b.index(",")])      #?
    y2 = float(b[b.index(","): len(b)]) #?
    x3 = float(c[1: c.index(",")])      #?
    y3 = float(c[c.index(","): len(c)]) #?
    area = abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))) #this line is correct
    print float("{:.2f}".format(triangle))  #?

#test code (please remove before uploading)
print(triangle_area("(5,5)", "(8,5)", "(8,8)") == 4.5)
print(triangle_area("(1,1)", "(2,2)", "(3,3)") == 0.0)
print(triangle_area("(1,1)", "(2,3)", "(3,1)") == 2.0)
