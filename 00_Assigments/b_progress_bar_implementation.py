#!/usr/bin/python3
"""
Assignment: Progress bar implementation
    [          ]   3
    [*         ]  10
    [**        ]  20
    [***       ]  30
    [****      ]  40
    [*****     ]  50
    [******    ]  60
    [*******   ]  70
    [********  ]  80
    [********* ]  90
    [**********] 100
"""

for progress in range(0, 110, 10):
    steps_count = (progress // 10)
    print("[{}] {}".format('*' * steps_count, progress))
