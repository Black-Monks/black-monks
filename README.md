# Jak uruchomić?
Wejść do katalogu głównego projektu i wpisać:
`docker-compose up`

Lub lokalnie:
1. `cd black_monks`
2. `poetry install`
3. `poetry run python main.py`

# Workflow pracy
1. `git pull` (synchronizacja repozytorium)
2. `git checkout -b MONK-ID` (tworzenie brancha o nazwie ID taska i przejście do niego - wykonuje się tylko raz dla brancha)
    - `git checkout MONK-ID` (przejście do już istniejącego brancha)
3. Zapisanie zmian w kodzie (gdy jesteśmy w swoim branchu)
    - `git add .` (zapisanie zmian w kodzie)
    - `git commit -m "MONK-ID komentarz"` (stworzenie commita ze zmian, w miejsce ID numer taska, w miejsce komentarza krótka uwaga po angielsku, co zmieniliście)
    - `git push -u origin MONK-ID` (pierwsze wypchnięcie swoich commitów do repozytorium zdalnego (wraz z branchem))
        - `git push` (gdy wypychamy kolejne zmiany na tym samym branchu, gdzie wykonana już była powyższa komenda)
4. Gdy skończycie taska, to wchodzicie na github i tworzycie pull request z brancha.
5. Po zamknięciu taska, lokalnie robicie `git checkout main` by wrócić do głównego brancha i `git pull`, by go zsycnhronizować

Status brancha można sprawdzać komendą `git status`.