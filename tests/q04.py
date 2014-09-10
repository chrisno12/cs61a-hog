test = {
  'names': [
    'q04',
    '4',
    'q4'
  ],
  'points': 1,
  'suites': [
    [
      {
        'locked': True,
        'test': """
        >>> score0, score1, start = bid_for_start(1, 1, goal=100) # start can be 0 or 1
        >>> score0
        a126466f36e68ab87052bd7dd4830b1f
        # locked
        >>> score1
        a126466f36e68ab87052bd7dd4830b1f
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> score0, score1, start = bid_for_start(2, 7, goal=100)
        >>> score0
        6e9f9f922f7903c986f061fdb814201f
        # locked
        >>> score1
        12bcee39a50333c85820c531bad444f0
        # locked
        >>> start
        769e57a2ed15518550d8707e27bc56f9
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> score0, score1, start = bid_for_start(8, 3, goal=100)
        >>> score0
        12bcee39a50333c85820c531bad444f0
        # locked
        >>> score1
        6e9f9f922f7903c986f061fdb814201f
        # locked
        >>> start
        6e9f9f922f7903c986f061fdb814201f
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> score0, score1, start = bid_for_start(4, 3, goal=100)
        >>> score0
        2fa43f0243ea855d547f8e257a71bd93
        # locked
        >>> score1
        be43a0b9617e2c21e8b189bc6ef7fc58
        # locked
        >>> start
        6e9f9f922f7903c986f061fdb814201f
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> score0, score1, start = bid_for_start(3, 4, goal=100)
        >>> score0
        be43a0b9617e2c21e8b189bc6ef7fc58
        # locked
        >>> score1
        2fa43f0243ea855d547f8e257a71bd93
        # locked
        >>> start
        769e57a2ed15518550d8707e27bc56f9
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}