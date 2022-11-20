from collections import defaultdict
import pandas


# Et lite skript for å vise transisjonsmatrise og emisjonsmatrise for HMM


# Tekst med padding foran og bak.
tekst = [
    [("<s>", "<s>"), ("jenta", "N"), ("ser", "V"), ("dyret", "N"), ("</s>", "</s>")],
    [("<s>", "<s>"), ("dyret", "N"), ("ser", "V"), ("jenta", "N"), ("</s>", "</s>")],
    [
        ("<s>", "<s>"),
        ("jenta", "N"),
        ("sitter", "V"),
        ("ved", "P"),
        ("vannet", "N"),
        ("</s>", "</s>"),
    ],
    [
        ("<s>", "<s>"),
        ("dyret", "N"),
        ("sitter", "V"),
        ("ved", "P"),
        ("jenta", "N"),
        ("</s>", "</s>"),
    ],
    [
        ("<s>", "<s>"),
        ("jenta", "N"),
        ("ser", "V"),
        ("dyret", "N"),
        ("ved", "P"),
        ("vannet", "N"),
        ("</s>", "</s>"),
    ],
    [
        ("<s>", "<s>"),
        ("dyret", "N"),
        ("ser", "V"),
        ("det", "D"),
        ("fristende", "A"),
        ("vannet", "N"),
        ("</s>", "</s>"),
    ],
    [
        ("<s>", "<s>"),
        ("vannet", "N"),
        ("er", "V"),
        ("fristende", "A"),
        ("</s>", "</s>"),
    ],
]

# lister med alle tagger som skal brukes til transisjonsmatrisen vår
postag_rows = ["<s>", "N", "V", "A", "D", "P"]
postag_cols = ["N", "V", "A", "D", "P", "</s>"]

transition_counts = defaultdict(int)
for s in tekst:
    for i in range(1, len(s)):
        transition_counts[(s[i - 1][1], s[i][1])] += 1

# teller
label_counts = defaultdict(int)
for s in tekst:
    for w_t in s:
        label_counts[w_t[1]] += 1


# teller (w|tag) og legger dem i ei ordbok
word_counts = defaultdict(int)
for s in tekst:
    for word, tag in s:
        word_counts[(word, tag)] += 1


# alle ordene (tokens)
vocab = [w[0] for s in tekst for w in s]

# ordforrådet vårt
V = list(set(vocab))


# Vi oppretter ordboka som skal bli transisjonsmatrisen
transition_probs = defaultdict(dict)

# For alle taggene i kolonnene, og alle i radene, tell C(ti-1,ti)/c(ti-1)
# Merk at strukturen ser slik ut: {"ti":[p,p,p,...]} hvor p=sannsynligheten

for ti in postag_cols:
    data = []
    for ti_1 in postag_rows:
        poss = transition_counts[(ti_1, ti)] / label_counts[ti_1]
        data.append(poss)
    transition_probs[ti] = data

# Gjør om til vanlig ordbok
transition_probs = dict(transition_probs)

# Oppretter ei dataramme fra Pandas
tm = pandas.DataFrame(transition_probs)
# Endrer merkelappene til radene
tm.index = postag_rows
# Skriver ut ramma
print(tm)


# Gjør det samme for emisjonsmatrisen
emission_probs = defaultdict(dict)

# Siden merkelappene vi bruker er litt annerledes, utvider vi
# lista med tagger til å inkludere både start- og sluttegnet.
extended = postag_rows[:]
extended.append("</s>")

# For hvert ord i vokabularet vårt, og for hver tag, regn ut C(w,tag)/C(tag)
# der C(w,tag) er hvor mange ganger ordet w forekommer med taggen tag.
for w in V:
    data = []
    for ti in extended:
        poss = word_counts[(w, ti)] / label_counts[ti]
        data.append(poss)
        emission_probs[w] = data
print(transition_probs)
# Gjør om til vanlig ordbok
emission_probs = dict(emission_probs)

# Lager dataramme
em = pandas.DataFrame(emission_probs)

# Endrer merkelappene
em.index = extended

# Skriver ut
print(emission_probs)

# Husk at vi kan sjekke at matrisene våre blir riktige ved
# å summere radene hver for seg. Hver rad skal summeres til
# 1.
