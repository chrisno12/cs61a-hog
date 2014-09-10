test = {
  'names': [
    'q02',
    '2',
    'q2'
  ],
  'points': 1,
  'suites': [
    [
      {
        'locked': True,
        'test': """
        >>> take_turn(2, 0,  make_test_dice(4, 6, 1))
        12bcee39a50333c85820c531bad444f0
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> take_turn(3, 20, make_test_dice(4, 6, 1))
        769e57a2ed15518550d8707e27bc56f9
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> take_turn(0, 35)
        2fa43f0243ea855d547f8e257a71bd93
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> take_turn(0, 71)
        96c4b13904868f0a2565d778a1a0244f
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> take_turn(0, 7)
        26a5e511aecc1517235e1be3b1eb57e8
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}