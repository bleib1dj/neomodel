from .. import RelationshipTo, StructuredNode, StringProperty


class Locale(StructuredNode):
    code = StringProperty(unique_index=True)
    name = StringProperty()

    def __repr__(self):
        return self.code

    def __str__(self):
        return self.code

    @classmethod
    def get(cls, code):
        return Locale.nodes.get(code=code)


class Localised(object):
    locales = RelationshipTo("Locale", "LANGUAGE")

    def __init__(self, *args, **kwargs):
        try:
            super(Localised, self).__init__(*args, **kwargs)
        except TypeError:
            super(Localised, self).__init__()

    def add_locale(self, lang):
        if not isinstance(lang, StructuredNode):
            lang = Locale.get(lang)
        self.locales.connect(lang)

    def remove_locale(self, lang):
        self.locales.disconnect(Locale.get(lang))

    def has_locale(self, lang):
        return self.locales.is_connected(Locale.get(lang))
