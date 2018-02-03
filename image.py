f=open("image.ppm", "w")
lines=[]
lines.append("P3\n")
lines.append("500 500\n")
lines.append("255\n")

for i in range(250):
    for j in range(500):
        if j==499:
            lines.append("51 "+str(i)+" 204\n")
        else:
            lines.append("51 "+str(i)+" 204 ")

for i in range(250):
    for j in range(500):
        if j==499:
            lines.append("204 "+str(i)+" 51\n")
        else:
            lines.append("204 "+str(i)+" 51 ")

            
f.writelines(lines)
f.close()
