"""delegate a specialized function/method to create instances"""

class GreekGetter(object):

    """A simple localizer a la gettext"""

    def __init__(self):
        self.trans = dict(dog="σκύλος", cat="γάτα")

    def get(self, msgid):
        """We'll punt if we dont' have a translation"""
        return self.trans.get(msgid, str(msgid))

class EnglishGetter(object):

    """Simply echoes the msg ids"""

    def get(self, msgid):
        return str(msgid)

def get_localizer(language="English"):
    """The factory method"""
    languages = dict(English=EnglishGetter, Greek=GreekGetter)
    return languages[language]()

# Create our localizers
e, g = get_localizer(language="English"), get_localizer(language="Greek")

for msgid in "dog parrot cat bear".split():
    print(e.get(msgid), g.get(msgid))

