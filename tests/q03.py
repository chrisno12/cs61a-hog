test = {
  'names': [
    'q03',
    '3',
    'q3'
  ],
  'points': 1,
  'suites': [
    [
      {
        'locked': True,
        'test': """
        >>> select_dice(4, 24) == six_sided
        66be736141b909f3883fb7e31e602087
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> select_dice(16, 64) == six_sided
        69e4b371710dec69cbc0c8d00d96933a
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> select_dice(0, 0) == six_sided
        66be736141b909f3883fb7e31e602087
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> select_dice(50, 80) == six_sided
        69e4b371710dec69cbc0c8d00d96933a
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}