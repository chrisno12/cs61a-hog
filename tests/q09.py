test = {
  'names': [
    'q09',
    '9',
    'q9'
  ],
  'points': 2,
  'suites': [
    [
      {
        'locked': True,
        'test': """
        >>> swap_strategy(23, 60) # 23 + (1 + abs(6 - 0)) = 30
        6e9f9f922f7903c986f061fdb814201f
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> swap_strategy(27, 17) # 27 + (1 + abs(1 - 7)) = 34
        9cab5c18250a8cf7f8ef476e052af033
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> swap_strategy(50, 80) # 1 + abs(8 - 0) = 9
        6e9f9f922f7903c986f061fdb814201f
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> swap_strategy(12, 12) # Baseline
        9cab5c18250a8cf7f8ef476e052af033
        # locked
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'locked': True,
        'test': """
        >>> swap_strategy(15, 34, 5, 4) # beneficial swap
        6e9f9f922f7903c986f061fdb814201f
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> swap_strategy(8, 9, 5, 4) # harmful swap
        be43a0b9617e2c21e8b189bc6ef7fc58
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}