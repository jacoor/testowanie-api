Kilka przykładów testowania zewnętrznego API.

Instalacja:

PIPENV_VENV_IN_PROJECT=1   pipenv install

___
### Mój katalog to imgw_api

* plik z "aplikacją" jest w get_imgw_data.py
* testy znajdują się w katalogu tests
* w katalogu sample data umieściłem fikcyjne dane
* w conftest.py zrobiłem fixtury "zapodające" fałszywe dnae
* w pytest.ini zrobiłem marker, który wydziela moje testy

