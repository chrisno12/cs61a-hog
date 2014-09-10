test = {
  'names': [
    'q07',
    '7',
    'q7'
  ],
  'points': 2,
  'suites': [
    [
      {
        'locked': True,
        'test': """
        >>> dice = make_test_dice(3)   # dice always returns 3
        >>> max_scoring_num_rolls(dice)
        12bcee39a50333c85820c531bad444f0
        # locked
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'answer': '14730c3a2dabd5598f8fc409e1d15dbc',
        'choices': [
          'The lowest num_rolls',
          'The highest num_rolls',
          'A random num_rolls'
        ],
        'locked': True,
        'question': """
        If multiple num_rolls are tied for the highest scoring
        average, which should you return?
        """,
        'type': 'concept'
      },
      {
        'locked': True,
        'test': """
        >>> dice = make_test_dice(2)     # dice always rolls 2
        >>> max_scoring_num_rolls(dice)
        12bcee39a50333c85820c531bad444f0
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> dice = make_test_dice(1, 2)  # dice alternates 1 and 2
        >>> max_scoring_num_rolls(dice)
        769e57a2ed15518550d8707e27bc56f9
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}