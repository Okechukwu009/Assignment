# 1
def even_gen(n): yield from (x for x in range(n+1) if x % 2 == 0)

# 2
class Fibonacci: 
    def __init__(self, limit): self.a, self.b, self.limit = 0, 1, limit
    def __iter__(self): return self
    def __next__(self): 
        if self.a > self.limit: raise StopIteration
        val, self.a, self.b = self.a, self.b, self.a + self.b; return val

# 3
def logger(func): 
    def wrapper(*args, **kwargs): 
        print(f"{func.__name__} called"); return func(*args, **kwargs)
    return wrapper

# 4
vowel_count = lambda s: sum(1 for c in s.lower() if c in "aeiou")

# 5
from collections import Counter
def word_freq(filename): 
    with open(filename) as f: return Counter(f.read().split())

# 6
is_palindrome = lambda s: s == s[::-1]

# 7
def prime_gen(n):
    for num in range(2, n): 
        if all(num % i != 0 for i in range(2, int(num ** 0.5)+1)): yield num

# 8
import time
def timer(func): 
    def wrapper(*args, **kwargs): 
        start = time.time(); result = func(*args, **kwargs)
        print("Time:", time.time() - start); return result
    return wrapper

# 9
squares = {x: x*x for x in range(11)}

# 10
def reverse_lines(filename):
    with open(filename) as f: return [line[::-1] for line in f]

# 11
unique = lambda lst: list(set(lst))

# 12
def to_upper(func): 
    def wrapper(*args): return func(*args).upper()
    return wrapper

# 13
multiples_3 = [x for x in range(30) if x % 3 == 0]

# 14
get_extension = lambda f: f.split('.')[-1]

# 15
import csv
def count_rows(filename): 
    with open(filename) as f: return sum(1 for _ in csv.reader(f))

# 16
squares_gen = (x**2 for x in range(1,11))

# 17
flatten = lambda l: [item for sub in l for item in sub]

# 18
def conditional_run(condition):
    def decorator(func): 
        def wrapper(*args, **kwargs): 
            if condition(): return func(*args, **kwargs)
        return wrapper
    return decorator

# 19
char_freq = lambda s: {c: s.count(c) for c in set(s)}

# 20
def append_line(file, line): 
    with open(file, 'a') as f: f.write(line + '\n')

# 21
for idx, val in enumerate(['a', 'b']): print(idx, val)

# 22
["even" if i % 2 == 0 else "odd" for i in range(10)]

# 23
def write_read(file, data): 
    with open(file, 'w') as f: f.write(data)
    with open(file) as f: return f.read()

# 24
list(zip([1, 2], ['a', 'b']))

# 25
class Countdown:
    def __init__(self, start): self.n = start
    def __iter__(self): return self
    def __next__(self): 
        if self.n < 0: raise StopIteration
        val = self.n; self.n -= 1; return val

# 26
list(filter(lambda x: x % 2 == 0, range(10)))

# 27
list(map(lambda x: x**2, range(5)))

# 28
def count_lines(file): 
    with open(file) as f: return sum(1 for _ in f)

# 29
def repeat(n): 
    def decorator(func): 
        def wrapper(*a, **k): 
            for _ in range(n): func(*a, **k)
        return wrapper
    return decorator

# 30
def reverse_words(sentence): 
    return ' '.join(word[::-1] for word in sentence.split())

# 31
[x for x in [-1, 3, -5, 2] if x > 0]

# 32
def countdown(n): 
    while n >= 0: yield n; n -= 1

# 33
dict(zip(['a','b'], [1,2]))

# 34
def greet(name="User"): return f"Hello, {name}!"

# 35
def write_list(file, items): 
    with open(file, 'w') as f: f.writelines(f"{i}\n" for i in items)

# 36
[[i * j for j in range(1, 6)] for i in range(1, 6)]

# 37
def to_list(func): 
    def wrapper(*a, **k): return list(func(*a, **k))
    return wrapper

# 38
def word_by_word(file): 
    with open(file) as f: 
        for line in f: 
            for word in line.split(): yield word

# 39
sorted([("Alice", 90), ("Bob", 85)], key=lambda x: x[1])

# 40
lst = [1, 2, 3]; all(x > 0 for x in lst), any(x < 0 for x in lst)

# 41
def line_gen(file): 
    with open(file) as f: yield from f

# 42
def merge_dicts(*dicts): 
    result = {}; [result.update(d) for d in dicts]; return result

# 43
def check_type(val): 
    return isinstance(val, (int, float))

# 44
[x for row in [[1,2],[3,4]] for x in row]

# 45
import json
def load_json(file): 
    with open(file) as f: return json.load(f)

# 46
sorted([{"score": 5}, {"score": 2}], key=lambda x: x["score"])

# 47
from collections import Counter
def histogram(lst): 
    c = Counter(lst)
    for k, v in c.items(): print(f"{k}: {'*' * v}")

# 48
try:
    with open("file.txt") as f: data = f.read()
except FileNotFoundError: print("File not found")

# 49
def avg_scores(test1, test2): 
    return {k: (test1[k] + test2.get(k, 0))/2 for k in test1}

# 50
def menu(): 
    while True:
        choice = input("1.View 2.Exit: ")
        if choice == "1": print("Viewing...")
        elif choice == "2": break
