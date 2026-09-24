# Ratings and social influence: writeup

Claude writes your answers into the slots below as you say them. You may ask it to change any of
your answers at any time, except the Part 0 predictions. Every `XXXX` in Parts 0 to 5 needs an
answer; the follow-up slots at the end are optional.

**Name:** Nadezhda Dominguez Salinas
**Date:** 2026-09-24

## Part 0. Predictions

Answered before anything runs. Claude writes them in as you said them, and they stay as written.

**1. Once people can see the counts, which artist wins most often?** Taylor Swift

**2. Does inequality rise or fall with social influence?** Rise

**3. Does the best artist ever lose a world?** Yes

**4. Can a recommender lower inequality without lowering fidelity to true taste?** No

## Part 1. Users on their own

Code: `part1_independent.py`. Figure: `figures/part1_strip.png`.

**What Gini and unpredictability each show, in your own words:** Gini demonstrates the inequality for the artists, so how popular/unpopular compared to other. Unpredictability shows how likely that artist is to be popular within a world.

**What the figure shows, one sentence:** The figure shows an artists true popularity compared to the number of downloads they have within a world.

## Part 2. The recommender

Code: `recommender.py`, `part2_recommender.py`. Figure: `figures/part2_strip.png`.

**The capabilities and limitations of `top_five`, in your words:** XXXX

**What Claude corrected in your reading, in your words, or "nothing":** XXXX

**What changed against Part 1, one sentence:** XXXX

## Part 3. Social influence

Code: `my_choice.py`, `hand_check.py`, `part3_influence.py`. Figures: `figures/part3_gini.png`,
`figures/part3_unpredictability.png`.

**Your rule in your words:** XXXX

**Hand check, before the table: which artist your rule should favor, and by a little or a lot:** XXXX

**Hand check: whether the table matched what you said:** XXXX

**The shape you expect the two curves to have, as you told Claude before the run:** XXXX

**What you changed in your rule, at the hand check or after the run, or "nothing":** XXXX

**What the two curves show against the paper's Figures 1 and 2, in one or two sentences:** XXXX

**Revisited: which of your Part 0 predictions you would now change, and why:** XXXX

## Part 4. Your recommender

Code: `my_recommender.py`, `part4_recommender.py`. Figure: `figures/part4_recommenders.png`.

**Your rule in words, before any code:** XXXX

**What you expect it to do to inequality, unpredictability and fidelity, as you told Claude before the run:** XXXX

**What it bought and what it cost, one sentence:** XXXX

## Part 5. Reflection

**Where this shows up in data you have already handled, or in an interface you use, one sentence:** XXXX

**A moment Claude was wrong or overconfident, or a judgment you kept for yourself, one sentence:** XXXX

## Follow-ups

Optional, and not graded. Nothing under this heading is ever counted as missing: leave a slot as
`XXXX` if you did not do that follow-up.

**What is shown (`followup_shown.py`): which market moved success further from quality:** XXXX

**One assumption (`followup_assumption.py`): the assumption you changed:** XXXX

**One assumption: whether the Part 3 conclusion survived:** XXXX

**Anything else you tried:** XXXX

**Anything else: what it showed:** XXXX
