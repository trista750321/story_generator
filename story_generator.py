import random
when = ["Couple years ago", "Yesterday", "A long time ago"]
who = ["a boy", "a cat", "a rabbit"]
name = ["Roger", "Billy", "Dylan"]
residence = ["a kingdom", "Taiwan", "Europe"]
went = ["Disney Land", "school", "bathroom"]
happened = ["ate a burger", "wrote a book", "met an old friend"]
print(random.choice(when) + ", " + random.choice(who) + " whose name is " + \
      random.choice(name) + " that lived in " + random.choice(residence) + " went to the " +\
      random.choice(went) + " and " + random.choice(happened) + ".")