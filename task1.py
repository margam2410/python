import re
m = re.search("name is <b>(\d+)</b>",
      "xxx name is <b>mahesh</b>  fdjsk")
if m:
    print m.groups()[0]



