
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def great_magicians(magicians, make_great):
    while magicians:
        name = magicians.pop()
        print(name)
        make_great.append(name)



magicians = ['natsu', 'gray', 'makarov']
make_great = []
great_magicians(magicians, make_great)
print(magicians)
print(make_great)
