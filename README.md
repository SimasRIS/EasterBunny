# EasterBunny# Pokalbių programa vaikams su Velykų Triušiuku

## Turinys

1. Kas tai per programa
2. Kaip programa veikia
3. Kaip įsidiegti programą
4. Kaip naudotis programa

---

## Kas tai per programa

Tai paprasta programa vaikams, kur jie gali pasikalbėti su Velykų Triušiuku. Programa naudoja OpenAI technologiją, kad Triušiukas galėtų linksmai ir draugiškai atsakyti į vaikų klausimus.

Kai vaikas atidaro programą, Triušiukas pasisveikina ir laukia klausimų. Vaikas gali klausti bet ko, o Triušiukas visada atsakys maloniu ir žaismingu būdu.

---

## Kaip programa veikia

- Programa veikia interneto naršyklėje ir naudoja Flask sistemą
- Visi pokalbiai saugomi saugiai, kad niekas kitas negalėtų jų matyti
- Puslapis papuoštas linksmais Velykų piešiniais ir animuotais burbuliukais 🐰🥚
- Programa saugiai bendrauja su OpenAI sistema per specialų raktą

---

## Kaip įsidiegti programą

```
# 1 — Atsisiųskite programą
$ git clone https://github.com/SimasRIS/EasterBunny.git
$ cd EasterBunny

# 2 — Pasiruoškite programos aplinką
$ python -m venv venv
# Windows kompiuteriams:
$ venv\Scripts\activate
# Apple/Linux kompiuteriams:
$ source venv/bin/activate

# 3 — Įdiekite reikalingas dalis
$ pip install -r requirements.txt

# 4 — Nustatykite slaptažodžius
$ copy .env.example .env  # arba sukurkite .env patys
# Įrašykite į .env failą:
OPENAI_API_KEY="sk-..."
FLASK_SECRET_KEY="slapta_velyku_morka"

# 5 — Paleiskite programą
$ python app.py

# 6 — Atidarykite naršyklėje
http://127.0.0.1:5000/
```

---

## Kaip naudotis programa

1. Atidarykite puslapį naršyklėje - Triušiukas jus pasveikins
2. Parašykite klausimą (pavyzdžiui, *"Kiek kiaušinių galiu nuspalvinti rytoj?"*)
3. Programa išsiųs jūsų klausimą Triušiukui
4. Triušiukas atsakys į jūsų klausimą
5. Galite toliau kalbėtis su Triušiuku kiek norite

Jei norite pradėti naują pokalbį, paspauskite mygtuką "Naujas pokalbis".