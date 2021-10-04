from patterns import search_in_patterns as srch_patt


def matcher_add(db, nlp, matcher, language):
    matcher.add("move", [srch_patt(db, nlp, ["move"], language)])
    matcher.add("info_artist", [srch_patt(db, nlp, ["info_artist"], language)])
    matcher.add("info_artwork", [srch_patt(db, nlp, ["info_artwork"], language)])
    matcher.add("show", [srch_patt(db, nlp, ["show"], language)])

    return matcher
