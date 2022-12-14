from nltk.corpus import stopwords

UNWANTED_EN_STOPWORDS = ["no", "none"]
UNWANTED_ES_STOPWORDS = ["no", "si"]
GLOBAL_STOPWORDS = ["fizz"]


# ----------------------------------- maintenance_keywords ---------------------------------------------
MAITENANCE_KEYWORDS = ["vedlikehold", "kontroll", "vedlikehold", "tilsyn", "sikkerhetskontroll", "inspiser",
                        "inspeksjon", "fjerning", "støvfjerning", "fjerne", "service", "støvsuging", "prøves",
                       "skiftes", "ettertrekking", "ettersyn"
                       ]

# ----------------------------------- Norwegian stopwords ---------------------------------------------
NORWEGIAN_STOPWORDS = ["alle", "at", "av", "bare", "begge", "ble", "blei", "bli", "blir", "blitt",
                          "både", "båe", "da", "de", "deg", "dei", "deim", "deira", "deires", "dem", "den", "denne",
                      "der", "dere", "deres", "det", "dette", "di", "din", "disse", "ditt", "du", "dykk", "dykkar",
                      "då", "eg", "ein", "eit", "eitt", "eller", "fra", "før", "ha", "hadde", "han", "hans", "har",
                      "hennar", "henne", "hennes", "her", "hjå", "ho", "hoe", "honom", "hoss", "hossen", "hun", "hva",
                      "hvem", "hver", "hvilke", "hvilken", "hvis", "hvor", "hvordan", "hvorfor", "i", "ikke", "ikkje",
                      "ingen", "ingi", "inkje", "inn", "inni", "ja", "jeg", "kan", "kom", "korleis", "korso", "kun",
                      "kunne", "kva", "kvar", "kvarhelst", "kven", "kvi", "kvifor", "man", "mange", "me", "med",
                      "medan", "meg", "meget", "mellom", "men", "mi", "min", "mine", "mitt", "mot", "mykje", "ned",
                      "no", "noe", "noen", "noka", "noko", "nokon", "nokor", "nokre", "nå", "når", "og", "også", "om",
                      "opp", "oss", "over", "på", "samme", "seg", "selv", "si", "sia", "sidan", "siden", "sin", "sine",
                      "sitt", "sjøl", "skal", "skulle", "slik", "so", "som", "somme", "somt", "så", "sånn", "til", "um",
                      "upp", "ut", "uten", "var", "vart", "varte", "ved", "vere", "verte", "vi", "vil", "ville", "vore",
                      "vors", "vort", "være", "vært", "vår", "å"
                       ]
