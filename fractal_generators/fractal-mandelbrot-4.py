w,h,r,i=200,100,range,lambda c:"# "[abs(reduce(lambda z,_:z*z+c,r(h)))<=2]
print"\n".join("".join(i((x-w/2)*4./w+(y-h/2)*4j/h)for x in r(w))for y in r(h))
