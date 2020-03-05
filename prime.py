from collections import Counter, defaultdict

"""
mmm... its a classic

The main idea to build a hashable histigrams of words

https://docs.python.org/3/library/collections.html#collections.Counter

Counter function is much faster then just smth like this:
[(str(i), string.count(i)) for i in string]
and also it return dictlike obj
for example:

    string = "ca23b2xcbsedsdfdf"

    %%timeit
    [(str(i), string.count(i)) for i in string]
    100000 loops, best of 3: 3.38 µs per loop

    %%timeit
    tuple(Counter(string).items())
    100000 loops, best of 3: 2.71 µs per loop
    
We have the same with defaultdict and smth like this dict(zip(keys, values))...

Tehere is a not cheep method sorted() but it balanced by hash table
"""

keywords = ["foobar", "aabb", "baba", "boofar", "test", "foboar"]
string = "abab"

def to_anagram_dict(words):
    anagrams = defaultdict(list)
    for word in words:
        hist = tuple(sorted(Counter(word).items(), \
                                 key= lambda word_tuple: word_tuple[0]))
        anagrams[hist].append(word)
    return anagrams

print(to_anagram_dict(keywords)[tuple(sorted(Counter(string).items(), \
                                 key= lambda word_tuple: word_tuple[0]))])

"""
a much more sophisticated method built on a prime numb
algorithm and again a hash table

The main idea is that you can destinguish results of mutiplication of
prime numbers

That one works a bit faster but you should never forget that 
the product of multiplication also rise so fast
"""

primeNumbers = [x for x in range(2,102) if not [t for t in range(2,x) if not x%t]]
alphabet = [i for i in "abcdefghijklmnopqrstuvwxyz"]
prime_dict = dict(zip(alphabet, primeNumbers))

def conver_to_prime(word):
    c = 1
    counter_st = Counter(word)
    for let in counter_st:
        c*=prime_dict[let]*counter_st[let]
    return c

def to_anagram_dict_prime(words):
    anagrams = defaultdict(list)
    for word in words:
        anagrams[conver_to_prime(word)].append(word)
    return anagrams

print(to_anagram_dict_prime(keywords)[conver_to_prime(string)])


"""
============
%%timeit
to_anagram_dict_prime(keywords)[conver_to_prime(string)]

100000 loops, best of 3: 16.7 µs per loop

%%timeit
to_anagram_dict(keywords)[tuple(sorted(Counter(string).items(), \
                                 key= lambda word_tuple: word_tuple[0]))]
                                 
100000 loops, best of 3: 18.5 µs per loop
============

thanks for: https://stackoverflow.com/questions/8286554/using-python-find-anagrams-for-a-list-of-words
"""
