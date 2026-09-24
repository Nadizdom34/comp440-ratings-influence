"""
Your choice rule, for Part 3.

You design the rule. Claude asks you questions about it, writes it here from your answers, and
shows you the code. Then `uv run python hand_check.py` shows each step of your rule on a
two-artist case, so you can say whether each step does what you meant.
"""

import random

from artists import TRUE_POPULARITY
from choose import normalize, step

# Picks the artist that gets the pretend download when none of the shown artists has one.
# Seeded so that a run gives the same numbers each time.
_pick = random.Random(0)

# How much more likely each spot is than the spot below it: spot 1 over 2, 2 over 3, 3 over 4,
# 4 over 5. The steps move evenly from the first list at social influence 0 to the second at 1.
STEPS_AT_0 = [0.10, 0.20, 0.30, 0.40]
STEPS_AT_1 = [0.40, 0.30, 0.20, 0.10]


def my_choice(shown, counts, social_influence):
    """Return the chance that a user picks each shown artist: a list of numbers, one per artist
    in `shown` and in the same order, summing to 1.

    shown              the artists on the list, top first (positions 0, 1, 2, ...)
    counts             the download counts shown with the artists, artist -> number; an artist
                       shown without a count is missing, so read it as counts.get(artist, 0)
    social_influence   from 0 (users ignore the counts) to 1 (users go by the counts alone)

    The rule may use `normalize`, which scales a list of weights so they sum to 1, and
    TRUE_POPULARITY, which gives each artist its hidden true popularity. `step` labels each
    stage of the rule, so that hand_check.py can show it.
    """
    taste = step("taste share: true popularity scaled to sum to 1",
                 normalize([TRUE_POPULARITY[artist] for artist in shown]))

    downloads = [counts.get(artist, 0) for artist in shown]
    if sum(downloads) == 0:
        # No shown artist has a download: one of them, picked at random, gets a pretend one.
        chosen = _pick.randrange(len(shown))
        downloads = [1 if i == chosen else 0 for i in range(len(shown))]
    downloads = step("downloads used for the counts part", downloads)
    social = step("counts share: downloads scaled to sum to 1", normalize(downloads))

    counts_part = step("counts part of the mix: half the social influence", social_influence / 2)
    mixed = step("mix: counts part times counts share, plus the rest times taste share",
                 [counts_part * s + (1 - counts_part) * t for s, t in zip(social, taste)])

    steps = step("step of each spot over the one below it, for this social influence",
                 [low + social_influence * (high - low)
                  for low, high in zip(STEPS_AT_0, STEPS_AT_1)][:len(shown) - 1])
    boost = [1.0] * len(shown)
    for i in range(len(shown) - 2, -1, -1):   # from the bottom spot up
        boost[i] = boost[i + 1] * (1 + steps[i])
    boost = step("position boost: the bottom spot is 1, each spot above is its step more", boost)

    return step("chances: mix times position boost, scaled to sum to 1",
                normalize([m * b for m, b in zip(mixed, boost)]))
