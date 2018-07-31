'''
kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
'''


def make_song(count, beverage):
    while count >= 0:
        if count > 1:
            yield ("{} bottles of {} on the wall.".format(count, beverage))

        elif count == 1:
            yield ("{} bottle of {} left!".format(count, beverage))
        else:
            yield ("No more {}!".format(beverage))
        count -= 1

    raise StopIteration


song = make_song(3, "abc")
print(next(song))
print(next(song))
print(next(song))
print(next(song))


def get_multiples(number=1, count=10):
    for i in range(1, count + 1):
        yield number * i


default_multiples = get_multiples(2, 3)
print(list(default_multiples))


def get_unlimited_multiples(num=1):
    multiplier = 0
    while True:
        multiplier += 1
        yield num * multiplier


sevens = get_unlimited_multiples(7)
print([next(sevens) for i in range(15)])
