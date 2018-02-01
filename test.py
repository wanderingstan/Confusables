#!/usr/bin/env python
# -*- coding: utf-8 -*-
from confusables import Confusables
import re

c = Confusables('confusables.txt')

string = "Hello"
cpattern = c.confusables_regex(string)
print("Regexp pattern: {}".format(cpattern))
r = re.compile(cpattern)

fake_string = "𝓗℮𝐥1೦"

if r.match(fake_string):
    print("Matched!")
else:
    print("No match")
