# -*- coding: utf-8 -*-

import urllib.request
import pandas as pd
import re, random
import numpy as np
import sklearn.linear_model, sklearn.metrics, sklearn.model_selection
import collections

ORDFILER = {
    "norsk": "https://github.com/open-dict-data/ipa-dict/blob/master/data/nb.txt?raw=true",
    "arabisk": "https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/ar.txt?raw=true",
    "finsk": "https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/fi.txt?raw=true",
    "patwa": "https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/jam.txt?raw=true",
    "farsi": "https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/fa.txt?raw=true",
    "tysk": "https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/de.txt?raw=true",
    "engelsk": "https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/en_UK.txt?raw=true",
    "rumensk": "https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/ro.txt?raw=true",
    "khmer": "https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/km.txt?raw=true",
    "fransk": "https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/fr_FR.txt?raw=true",
    "japansk": "https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/ja.txt?raw=true",
    "spansk": "https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/es_ES.txt?raw=true",
    "svensk": "https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/sv.txt?raw?true",
    "koreansk": "https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/ko.txt?raw?true",
    "swahilisk": "https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/sw.txt?raw?true",
    "vietnamesisk": "https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/vi_C.txt?raw?true",
    "mandarin": "https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/zh_hans.txt?raw?true",
    "malayisk": "https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/ma.txt?raw?true",
    "kantonesisk": "https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/yue.txt?raw?true",
    "islandsk": "https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/is.txt?raw=true",
}


class LanguageIdentifier:
    """Logistisk regresjonsmodell som tar IPA transkripsjoner av ord som input,
    og predikerer hvilke språkene disse ordene hører til."""

    def __init__(self):
        """Initialiser modellen"""
        # selve regresjonsmodellen (som brukes all CPU-er på maskinen for trening)
        self.model = sklearn.linear_model.LogisticRegression(
            solver="liblinear", multi_class="ovr"
        )
        liste = []

    def _extract_feats(self, transcriptions):
        """Gitt en rekke med IPA transkripsjoner, ekstraher en matrise av størrelse |T|x|F|,
        hvor |T| er antall transkripsjoner, og |F| er antall features brukt i modellen."""

        X = np.zeros((len(transcriptions), len(self.liste)))

        for i in range(len(transcriptions)):
            chars = list(str(transcriptions[i]))

            for j in range(len(self.liste)):
                for n in chars:
                    if self.liste[j][0] == n:
                        X[i][j] = 1
            if i % 10000 == 0:
                print(i)
        print("Extraction done")
        return X

    def train(self, transcriptions, languages):
        """Gitt en rekke med IPA transkripsjoner og en rekke med språknavn, tren
        den logistisk regresjonsmodellen. De to rekkene må ha samme lendgen"""

        X = self._extract_feats(transcriptions)
        print(X.shape)
        # print(languages[0].shape)
        self.model.fit(X, languages[0])
        print("Fitting done")

    def predict(self, transcriptions):
        """Gitt en rekke med IPA transkripsjoner, finn ut det mest sansynnlige språket
        for hver transkripsjon. Rekken som returneres må ha samme lengden som rekken i input"""
        X = self._extract_feats(transcriptions)

        predicted_langs = self.model.predict(X)
        return predicted_langs

    def _extract_unique_symbols(self, df, min_nb_occurrences=10):
        """Gitt en rekke med IPA fonetiske transkripsjoner, ektraher en liste med alle IPA
        symboler som finnes i transkripsjonene og forekommer minst min_nb_occurrences."""
        X = df["IPA"].str.cat()
        result = collections.Counter(X)

        li = []
        for i in result.items():
            if i[1] > 9:
                li.append([i[0], i[1]])
        self.liste = li

        # Code used for task 1d, creates a txt file containing every symbol used
        """
        import csv
        import io
        with io.open("fname", "w", encoding="utf-8") as f:

            # using csv.writer method from CSV package
            write = csv.writer(f)

            write.writerow(self.liste)
        """

    def evaluate(self, transcriptions, languages):
        """Gitt en rekke med IPA transkripsjoner og en rekke med språknavn, evaluer hvor godt
        modellen fungerer ved å beregne:
        1) accuracy
        2) precision, recall og F1 for hvert språk
        3) micro- og macro-averaged F1.
        """
        predicted_langs = self.predict(transcriptions)
        print(predicted_langs)
        print(languages)
        accuracy = sklearn.metrics.accuracy_score(languages, predicted_langs)
        print(accuracy)

        # Printing out f1, recall for each language
        for i in range(20):
            print("language: ", i)
            y_true = []
            y_pred = []
            for x, y in zip(languages, predicted_langs):
                if x == i:
                    y_true.append(1)
                    if x == y:
                        y_pred.append(1)
                    else:
                        y_pred.append(0)

            average_precision = sklearn.metrics.average_precision_score(y_true, y_pred)
            print("Precision: ", average_precision)

            recall = sklearn.metrics.recall_score(y_true, y_pred)
            print("recall: ", recall)

            f1 = sklearn.metrics.f1_score(y_true, y_pred)
            print("F1: ", f1)

        f1_micro = sklearn.metrics.f1_score(languages, predicted_langs, average="micro")
        print(f1_micro)
        f1_macro = sklearn.metrics.f1_score(languages, predicted_langs, average="macro")
        print(f1_macro)

        # Printing all scores (f1, recall are only from last language in for loop)
        print(accuracy, average_precision, recall, f1, f1_micro, f1_macro)
        coef = self.model.coef_

        np.savetxt("foo.csv", coef)

        # See API fra sklearn.metrics for å finne ut hvordan dette kan gjøres!
        # Returning scores
        return accuracy, average_precision, recall, f1, f1_micro, f1_macro


def extract_wordlist(max_nb_words_per_language=20000):
    """
    Laster ned fra Github ordlister med ord og deres phonetiske transkripsjoner i flere språk.
    Ordlistene er deretter satt sammen i en pandas DataFrame, og delt i en treningsett og en testsett.
    """

    full_wordlist = []
    for lang, wordfile in ORDFILER.items():

        print("Nedlasting av ordisten for", lang, end="... ")
        data = urllib.request.urlopen(wordfile)

        wordlist_for_language = []
        for linje in data:
            linje = linje.decode("utf8").rstrip("\n")
            word, transcription = linje.split("\t")

            # Noen transkripsjoner har feil tegn for "primary stress"
            transcription = transcription.replace("'", "ˈ")

            # vi tar den første transkripsjon (hvis det finnes flere)
            # og fjerner slashtegnene ved start og slutten
            match = re.match("/(.+?)/", transcription)
            if not match:
                continue
            transcription = match.group(1)
            wordlist_for_language.append(
                {"ord": word, "IPA": transcription, "språk": lang}
            )
        data.close()

        # Vi blander sammen ordene, og reduserer mengder hvis listen er for lang
        random.shuffle(wordlist_for_language)
        wordlist_for_language = wordlist_for_language[:max_nb_words_per_language]

        full_wordlist += wordlist_for_language
        print("ferdig!")

    # Nå bygger vi en DataFrame med alle ordene
    full_wordlist = pandas.DataFrame.from_records(full_wordlist)

    # Og vi blander sammen ordene i tilfeldig rekkefølge
    full_wordlist = full_wordlist.sample(frac=1)

    # Lage et treningssett og en testsett (med 10% av data)
    wordlist_train, wordlist_test = sklearn.model_selection.train_test_split(
        full_wordlist, test_size=0.1
    )
    print(
        "Treningsett: %i eksempler, testsett: %i eksempler"
        % (len(wordlist_train), len(wordlist_test))
    )
    wordlist_test.to_csv("test.csv")
    wordlist_train.to_csv("train.csv")
    return wordlist_train, wordlist_test


#######################
# Brukseksempel:
#######################
if __name__ == "__main__":

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
    # Files are downloaded using extract_wordlist() but seeing how i didnt want to do this for every run, the files were saved.
    train = pd.read_csv("train.csv")
    test = pd.read_csv("test.csv")

    # train, test = extract_wordlist()
    train_sprak = pd.factorize(train["språk"])
    test = test.replace({"språk": lang_dict})
    # print(test["språk"].tolist())
    # print(train_sprak[1])

    L = LanguageIdentifier()

    L._extract_unique_symbols(train)
    L.train(train["IPA"], train_sprak)
    L.evaluate(test["IPA"], test["språk"].tolist())