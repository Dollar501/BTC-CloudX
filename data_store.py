# data_store.py
# This file acts as the database for the bot.
# It contains all information about mining hardware and pre-defined investment plans.

from decimal import Decimal

MINING_HARDWARE = {
    'asic': [
        {
            'id': 'asic_1', 
            'name': 'Antminer S21 XP Hydro', 
            'profit': Decimal('435.0'), 
            'price': Decimal('4500'), 
            'image': 'Antminer S21 XP Hydro.jpg' # Local image file
        },
        {
            'id': 'asic_2', 
            'name': 'Antminer S21 XP 270TH', 
            'profit': Decimal('355.0'), 
            'price': Decimal('3400'), 
            'image': 'Antminer S21 XP 270TH.jpg'
        },
        {
            'id': 'asic_3', 
            'name': 'WhatsMiner M66S++', 
            'profit': Decimal('335.0'), 
            'price': Decimal('3600'), 
            'image': 'WhatsMiner M66S++.jpg'
        },
    ],
    'gpu': [
        {
            'id': 'gpu_1', 
            'name': 'NVIDIA RTX 4090', 
            'profit': Decimal('110.0'), 
            'price': Decimal('2000'), 
            'image': 'NVIDIA RTX 4090.jpg'
        },
        {
            'id': 'gpu_2', 
            'name': 'NVIDIA RTX 4080', 
            'profit': Decimal('80.0'), 
            'price': Decimal('1300'), 
            'image': 'NVIDIA RTX 4080.jpg'
        },
        {
            'id': 'gpu_3', 
            'name': 'NVIDIA RTX 4070 Ti', 
            'profit': Decimal('60.0'), 
            'price': Decimal('900'), 
            'image': 'NVIDIA RTX 4070 Ti.jpg'
        },
    ]
}

INVESTMENT_PLANS = {
    'monthly': [
        {
            'name': 'VIP1 – شهر', 'price': 100, 'devices_count': 1,
            'devices_used': 'Antminer S19 XP 140TH / WhatsMiner M50S++',
            'monthly_profit_percent': 49.2, 'monthly_profit_usd': 49.2, 'daily_profit_percent': 1.64
        },
    ],
    'quarterly': [
        {
            'name': 'VIP-PRO1 – 3 شهور', 'price': 270, 'devices_count': 10,
            'devices_used': 'Antminer S21 XP 270TH / WhatsMiner M66S+ / Antminer S19 XP',
            'total_profit_percent': 225, 'total_profit_usd': 607.5, 'total_return': 877.5, 'daily_profit_percent': 2.5
        },
    ],
    'annually': [
        {
            'name': 'VIP-PLUS+1 – سنة', 'price': 900, 'devices_count': 35,
            'devices_used': 'WhatsMiner M66S++ / Antminer S21 XP / S21 XP Hydro',
            'annual_profit_percent': 396, 'annual_profit_usd': 3564, 'total_return': 4464, 'daily_profit_percent': 1.08
        },
    ]
}
