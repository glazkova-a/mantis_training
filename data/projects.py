from model.project import Project
import random
import string

testdata = [
    Project(name="name1", description="header1"),
    Project(name="name2", description="header2")
]


#def random_string(prefix, maxlen):
    #symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    #return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


#testdata = [Group(name="", header="", footer="")] + [
    #Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
   # for i in range(5)
#]