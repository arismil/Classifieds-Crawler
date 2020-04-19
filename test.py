import re

#Check if the string starts with "The" and ends with "Spain":

txt = "iphone xs max silver 64"
x = re.findall(r"iphone\s([6-8]s?|xs?)\s(max|plus)?", txt)

if x:
    print(x[0][0])
