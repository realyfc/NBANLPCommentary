

shot_first_comments = [
    ("Here's the first shot attempt of the game from %s.", ['primary_player'])
]

make_comments = [
    ("It's good.", []),
    ("He made a %s.", ['shot_type'])
]

miss_comments = [
    ("He misses it.", []),
    ("%s misses it.", ['primary_player'])
]

block_comments = [
    ("The shot is blocked.", []),
    ("%s swats it away!", ['secondary_player'])
]

assist_comments = [
    ("Shot is made. Nice assist from %s.", ['secondary_player']),
    ("%s hooks up with %s for the basket.", ['secondary_player', 'primary_player'])
]

fastbreak_12_comments = [
    ("%s with the quick fastbreak", ['primary_player']),
    ("After the %s by %s, %s scores a fastbreak basket.", ['fastbreak_play', 'fastbreak_creator', 'primary_player'])
]
fastbreak_11_comments = [
    ("%s with the quick fastbreak", ['primary_player']),
    ("Great play! %s with the %s and then finishes off the play with a %s.", ['primary_player', 'fastbreak_play', 'shot_type'])
]
fastbreak_123_comments = [
    ("%s with the quick fastbreak", ['primary_player']),
    ("After the %s by %s, %s passes to %s who makes a %s for %s points.", ['fastbreak_play', 'fastbreak_creator', 'secondary_player', 'primary_player', 'shot_type', 'points_worth'])
]
fastbreak_121_comments = [
    ("%s with the quick fastbreak", ['primary_player']),
    ("After the %s by %s, %s scores a fastbreak basket.", ['fastbreak_play', 'fastbreak_creator', 'primary_player'])
]
fastbreak_112_comments = [
    ("%s with the quick fastbreak", ['primary_player']),
    ("After the %s by %s, %s scores a fastbreak basket.", ['fastbreak_play', 'fastbreak_creator', 'primary_player'])
]

shot_longest_comments = [
    ("Amazing! That %s-foot shot by %s was the longest shot made all season!", ['shot_distance', 'primary_player'])
]

shot_longest_player_comments = [
    ("Wow! At %s feet, that's %s's longest shot of this season.", ['shot_distance', 'primary_player'])
]
