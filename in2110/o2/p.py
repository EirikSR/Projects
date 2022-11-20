import spacy
from conllu import ConlluDoc


def attachment_score(true, pred):
    las = None
    uas = None

    return uas, las