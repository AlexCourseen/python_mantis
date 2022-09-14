from model.project import Project
import random
import os.path
import jsonpickle
import string #хранит константы символов
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of projects", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 1
f = "data/projects.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Project(projectName="", description="")] + \
           [Project(projectName=random_string('projectName', 5), description=random_string('description', 5))
            for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)# ..-точки для перехода на один урровень верх,
 # чтобы получилось "..data/<file_name>.json"

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
