import base64

pp = open("url.txt","r")
dd = pp.read()

#print(dd)

ur = dd

gg = base64.b64encode(ur)
#print(gg)
pp.close()

ap = open("url.txt","w")
ff = ap.write(gg)
ap.close()
print("DONE")