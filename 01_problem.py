f = open("poem.txt")
content = f.read()
if("twnikle" in content):
    print("The word twinkle is present in the content ")
else:
    print("The word twnikle present in the content")
f.close()