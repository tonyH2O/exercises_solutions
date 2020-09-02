


# 1 - Class Book


class Book():
    
    def __init__(self,name,author,pages):
        self.name = name
        self.author = author
        self.pages = pages

book = Book('my book', 'me', '200')
print(book.name)
print(book.author)
print(book.pages)

# 2 - Scope

x = 'global'

def outer():
    x = 'local'
    y = 'nonlocal'

    def inner():
        x = 'nonlocal'
        print('inner: ',x)

    def change_global():
        x = 'global: changed!'
        print(x)

    print('outer: ',x)
    inner()
    print('outer: ',y)
    change_global()

print(x)
outer()

####
# 3 - Music


class Music():

    def __init__(self,title,artist,lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def get_info(self):
        return 'This is the song: {} from the Group: {}'.format(self.title,self.artist)

    def play(self):
        return 'Get these lyrics bitches:\n {}'.format(self.lyrics)



song = Music('Let it Burn','Red','I watched the city burn ')
print(song.get_info())
print(song.play())


###################
################
# 4 - Cup

class Cup():

    def __init__(self,size,q):
        self.size = size
        self.q = q

    def fill(self,m):
        self.q += m
        self.q = min(self.q,self.size)
    
    def status(self):
        return self.size - self.q
    

cup = Cup(100,50)
cup.fill(50)
cup.fill(10)
print(cup.status())


# 4 - Flower

class Flower():

    is_happy = False
    

    def __init__(self, name, w):
        self.name = name
        self.w = w

    def water(self,qq):
    
        self.is_happy = self.w <= qq

    def status(self):
        if self.is_happy == True:
            return '{} is happy'.format(self.name)
        else:
            return '{} is not happy'.format(self.name)


f = Flower('Lilly', 100)
f.water(50)
print(f.status())
f.water(100)
print(f.status())





































