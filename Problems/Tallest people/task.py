def tallest_people(**kwargs):
    dsort = sorted(kwargs.items(), key=lambda x: x[1], reverse=True)
    maxheight = dsort[0][1]
    tall = {}
    for name, height in kwargs.items():
        if height == maxheight:
            tall[name] = height
    tallsorted = sorted(tall.items())
    for item in tallsorted:
        print("{} : {}".format(item[0], item[1]))

tallest_people(Jackie=176, Wilson=185)
