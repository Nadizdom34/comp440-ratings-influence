"""
Your recommender, for Part 4.

Describe your rule to Claude in words first. Claude writes it here, and part4_recommender.py
compares it with top_five and random_five from recommender.py, which are written the same way.
"""

from sim import ARTISTS, NUM_SHOWN


def my_recommender(counts, rng):
    """Return two things: five different artist names in display order (position 0 is the top of
    the list), and the download counts to show with them, artist -> number.

    counts  downloads so far in this world, artist -> int; an artist with no downloads yet is
            missing, so read it as counts.get(artist, 0)
    rng     a numpy random generator; use it for anything random, so that runs repeat exactly

    The counts you return are the counts the user sees, and they are what the choice rule reads.
    Return `counts` to show the real counts, `{}` to show no counts at all, or a dict of your own
    to show changed numbers.

    A recommender may use the counts and the list of artists (sim.ARTISTS). It must never use
    TRUE_POPULARITY: a real recommender cannot see how much users truly like each artist.
    """
    shown = sorted(counts, key=lambda artist: counts[artist], reverse=True)[:NUM_SHOWN]
    for artist in sorted(ARTISTS):   # fewer than five with a download: fill alphabetically
        if len(shown) == NUM_SHOWN:
            break
        if artist not in shown:
            shown.append(artist)
    return shown, counts
