from neomodel import StructuredNode, StringProperty
from neomodel.contrib import Localised, Locale


class Student(Localised, StructuredNode):
    name = StringProperty(unique_index=True)


def setup():
    for l in ['fr', 'ar', 'pl', 'es']:
        Locale(code=l).save()


def test_localised():
    bob = Student(name="Bob").save()
    bob.add_locale(Locale.get("fr"))
    bob.add_locale("ar")
    bob.add_locale(Locale.get("ar"))
    bob.add_locale(Locale.get("pl"))

    assert bob.has_locale("fr")
    assert not bob.has_locale("es")

    bob.remove_locale("fr")
    assert not bob.has_locale("fr")

    assert len(bob.locales) == 2
    assert Locale.get("pl") in bob.locales.all()
    assert Locale.get("ar") in bob.locales.all()