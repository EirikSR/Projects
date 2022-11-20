import logistisk_regresjon
from logistisk_regresjon import LanguageIdentifier
import pandas as pd
import collections
import numpy as np

"""
def _extract_unique_symbols(transcriptions, min_nb_occurrences=10):
    """  # Gitt en rekke med IPA fonetiske transkripsjoner, ektraher en liste med alle IPA
# symboler som finnes i transkripsjonene og forekommer minst min_nb_occurrences.
"""
    liste = []
    ant = []
    for i in transcriptions:
        L = list(str(i))

        for j in L:
            if len(liste) == 0:
                liste.append(j)
                ant.append(1)
            for k in range(len(liste)):
                if j == liste[k]:

                    ant[k] += 1
                elif k == len(liste) - 1:
                    liste.append(j)
                    ant.append(1)
    return liste, ant
"""

lang_dict = {
    "arabisk": 0,
    "engelsk": 1,
    "tysk": 2,
    "spansk": 3,
    "swahilisk": 4,
    "kantonesisk": 5,
    "patwa": 6,
    "islandsk": 7,
    "fransk": 8,
    "finsk": 9,
    "mandarin": 10,
    "vietnamesisk": 11,
    "svensk": 12,
    "norsk": 13,
    "rumensk": 14,
    "farsi": 15,
    "malayisk": 16,
    "koreansk": 17,
    "japansk": 18,
    "khmer": 19,
}

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

# , test = logistisk_regresjon.extract_wordlist()
train_sprak = pd.factorize(train["språk"])
test = test.replace({"språk": lang_dict})
# print(test["språk"].tolist())
L = LanguageIdentifier()
print(train_sprak[1])
L._extract_unique_symbols(train)
L.train(train["IPA"], train_sprak)
# L.predict("word")
L.evaluate(test["IPA"], test["språk"].tolist())
"""
X = train["IPA"].str.cat()
result = collections.Counter(X)

liste = []
for i in result.items():
    if i[1] > 9:
        liste.append([i[0], i[1]])

transcript = "konsumiðoɾas"
print(len(transcript))
X = np.zeros((len(transcript), len(liste)))
a = list(transcript)
print(a)
for i in range(len(a)):
    for j in range(len(liste)):
        if a[i] == liste[j][0]:
            X[i][j] = 1
print(X)
"""
