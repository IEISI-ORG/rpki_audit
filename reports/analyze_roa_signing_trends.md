    [*] Fetching APNIC Labs ROA-coverage snapshots...
        - Now   (reported date 30/09/2026): 278 countries/regions
        - 3mo   (reported date 04/07/2026): 279 countries/regions
        - 6mo   (reported date 04/04/2026): 279 countries/regions
        - 12mo  (reported date 04/10/2025): 279 countries/regions
        - 24mo  (reported date 04/10/2024): 278 countries/regions

    ====================================================================================================
     GLOBAL ROA COVERAGE TREND (IPv4 Route Objects, % Valid)
    ====================================================================================================
    Period   | Reported Date  | % Valid  | Total Route Objects
    ------------------------------------------------------------
    Now      | 30/09/2026     |   68.5% |  1,289,991
    3mo      | 04/07/2026     |   65.5% |  1,263,907
    6mo      | 04/04/2026     |   58.9% |  1,245,628
    12mo     | 04/10/2025     |   53.4% |  1,229,004
    24mo     | 04/10/2024     |   48.3% |    306,395

    ====================================================================================================
     GLOBAL ROA COVERAGE TREND (IPv6 Route Objects, % Valid)
    ====================================================================================================
    Period   | Reported Date  | % Valid  | Total Route Objects
    ------------------------------------------------------------
    Now      | 30/09/2026     |   75.7% |    317,763
    3mo      | 04/07/2026     |   74.0% |    311,764
    6mo      | 04/04/2026     |   62.4% |    301,878
    12mo     | 04/10/2025     |   57.4% |    297,450
    24mo     | 04/10/2024     |   55.4% |    260,253

    NOTE: IPv4 and IPv6 are reported separately because they are measured
    separately by APNIC and can diverge significantly per network — do not
    average or add them into one 'global ROA coverage' number.

    ====================================================================================================
     RIR ROA COVERAGE TREND (IPv4 Route Objects, % Valid, weighted by route-object count)
    ====================================================================================================
    RIR        | ASNs (now) |     Now |     3mo |     6mo |    12mo |    24mo
    -------------------------------------------------------------------------
    afrinic    | 2,469      |   65.3% |   60.8% |   59.1% |   37.8% |   27.6%
    apnic      | 31,360     |   76.9% |   74.0% |   54.6% |   49.1% |   47.0%
    arin       | 35,452     |   54.4% |   51.3% |   49.2% |   40.7% |   40.2%
    lacnic     | 13,804     |   68.9% |   61.2% |   57.7% |   59.2% |   39.2%
    ripencc    | 38,481     |   74.8% |   74.5% |   73.8% |   69.7% |   62.7%

    ====================================================================================================
     RIR ROA COVERAGE TREND (IPv6 Route Objects, % Valid, weighted by route-object count)
    ====================================================================================================
    RIR        | ASNs (now) |     Now |     3mo |     6mo |    12mo |    24mo
    -------------------------------------------------------------------------
    afrinic    | 2,469      |   41.7% |   39.1% |   40.3% |   35.2% |   66.6%
    apnic      | 31,360     |   83.4% |   82.6% |   51.1% |   48.0% |   39.3%
    arin       | 35,452     |   77.4% |   76.4% |   75.2% |   66.9% |   62.0%
    lacnic     | 13,804     |   65.3% |   61.2% |   59.5% |   57.6% |   56.2%
    ripencc    | 38,481     |   77.7% |   76.1% |   77.4% |   65.7% |   75.5%

    [+] Full per-country trend data (IPv4 + IPv6) saved to roa_signing_trends.csv

    ====================================================================================================
     BIGGEST MOVERS — 3mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 3mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    TG   | Togo                 | afrinic  | 11     |  62.3% |  10.2% |  +52.1pp
    TJ   | Tajikistan           | ripencc  | 43     |  82.3% |  36.5% |  +45.8pp
    TT   | Trinidad and Tobago  | lacnic   | 16     |  91.8% |  56.4% |  +35.4pp
    MX   | Mexico               | lacnic   | 654    |  78.0% |  44.3% |  +33.7pp
    JE   | Jersey               | ripencc  | 13     |  92.2% |  62.6% |  +29.6pp
    KI   | Kiribati             | apnic    | 5      |  90.5% |  63.2% |  +27.3pp
    CD   | Congo, The Democrati | afrinic  | 51     |  56.3% |  38.2% |  +18.1pp
    GG   | Guernsey             | ripencc  | 11     |  71.0% |  52.9% |  +18.1pp
    KE   | Kenya                | afrinic  | 247    |  76.1% |  59.1% |  +17.0pp
    BJ   | Benin                | afrinic  | 16     |  72.6% |  56.1% |  +16.5pp
    NG   | Nigeria              | afrinic  | 266    |  58.9% |  42.6% |  +16.3pp
    AU   | Australia            | apnic    | 2993   |  50.6% |  36.4% |  +14.2pp
    VG   | Virgin Islands, Brit | ripencc  | 49     |  56.9% |  44.1% |  +12.8pp
    YT   | Mayotte              | afrinic  | 1      |  75.9% |  63.2% |  +12.7pp
    RO   | Romania              | ripencc  | 1084   |  78.5% |  65.9% |  +12.6pp
    Decliners:
    IT   | Italy                | ripencc  | 1322   |  51.4% |  68.2% |  -16.8pp
    KY   | Cayman Islands       | arin     | 18     |  49.1% |  55.2% |   -6.1pp
    LY   | Libya                | afrinic  | 27     |  65.5% |  71.6% |   -6.1pp
    VE   | Venezuela            | lacnic   | 260    |  90.1% |  94.5% |   -4.4pp
    KN   | Saint Kitts and Nevi | arin     | 11     |  12.6% |  16.7% |   -4.1pp
    CV   | Cabo Verde           | afrinic  | 8      |  36.9% |  40.6% |   -3.7pp
    MK   | North Macedonia      | ripencc  | 68     |  47.1% |  50.4% |   -3.3pp
    SC   | Seychelles           | ripencc  | 87     |  84.8% |  87.9% |   -3.1pp
    CF   | Central African Repu | afrinic  | 4      |  19.2% |  22.2% |   -3.0pp
    BQ   | Bonaire, Sint Eustat | lacnic   | 6      |  80.4% |  83.3% |   -2.9pp
    PE   | Peru                 | lacnic   | 225    |  35.7% |  38.2% |   -2.5pp
    SD   | Sudan                | afrinic  | 11     |  39.8% |  42.1% |   -2.3pp
    GP   | Guadeloupe           | arin     | 10     |  91.2% |  93.4% |   -2.2pp
    ME   | Montenegro           | ripencc  | 31     |  49.0% |  51.0% |   -2.0pp
    AG   | Antigua and Barbuda  | arin     | 18     |  21.0% |  22.8% |   -1.8pp

    ====================================================================================================
     BIGGEST MOVERS — 6mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 6mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    DJ   | Djibouti             | afrinic  | 4      |  97.4% |   5.6% |  +91.8pp
    CN   | China                | apnic    | 6502   |  89.4% |   4.4% |  +85.0pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  83.3% |   5.9% |  +77.4pp
    TJ   | Tajikistan           | ripencc  | 43     |  82.3% |  42.3% |  +40.0pp
    JE   | Jersey               | ripencc  | 13     |  92.2% |  53.6% |  +38.6pp
    TT   | Trinidad and Tobago  | lacnic   | 16     |  91.8% |  54.1% |  +37.7pp
    MX   | Mexico               | lacnic   | 654    |  78.0% |  42.0% |  +36.0pp
    MT   | Malta                | ripencc  | 56     |  53.8% |  26.2% |  +27.6pp
    KI   | Kiribati             | apnic    | 5      |  90.5% |  63.2% |  +27.3pp
    SO   | Somalia              | afrinic  | 22     |  78.3% |  52.9% |  +25.4pp
    GG   | Guernsey             | ripencc  | 11     |  71.0% |  50.7% |  +20.3pp
    CD   | Congo, The Democrati | afrinic  | 51     |  56.3% |  37.1% |  +19.2pp
    KE   | Kenya                | afrinic  | 247    |  76.1% |  57.7% |  +18.4pp
    NG   | Nigeria              | afrinic  | 266    |  58.9% |  40.9% |  +18.0pp
    BW   | Botswana             | afrinic  | 33     |  72.9% |  55.3% |  +17.6pp
    Decliners:
    CV   | Cabo Verde           | afrinic  | 8      |  36.9% |  86.4% |  -49.5pp
    ME   | Montenegro           | ripencc  | 31     |  49.0% |  82.5% |  -33.5pp
    IT   | Italy                | ripencc  | 1322   |  51.4% |  65.9% |  -14.5pp
    LY   | Libya                | afrinic  | 27     |  65.5% |  73.1% |   -7.6pp
    UZ   | Uzbekistan           | ripencc  | 129    |  72.3% |  79.2% |   -6.9pp
    KM   | Comoros              | afrinic  | 4      |  74.3% |  80.8% |   -6.5pp
    KY   | Cayman Islands       | arin     | 18     |  49.1% |  55.2% |   -6.1pp
    MP   | Northern Mariana Isl | apnic    | 2      |  94.5% | 100.0% |   -5.5pp
    SD   | Sudan                | afrinic  | 11     |  39.8% |  45.2% |   -5.4pp
    AE   | United Arab Emirates | ripencc  | 212    |  82.9% |  87.1% |   -4.2pp
    SX   | Sint Maarten (Dutch  | lacnic   | 3      |  77.4% |  81.2% |   -3.8pp
    MG   | Madagascar           | afrinic  | 7      |  41.7% |  45.5% |   -3.8pp
    BQ   | Bonaire, Sint Eustat | lacnic   | 6      |  80.4% |  83.3% |   -2.9pp
    MK   | North Macedonia      | ripencc  | 68     |  47.1% |  50.0% |   -2.9pp
    NE   | Niger                | afrinic  | 7      |  18.0% |  20.8% |   -2.8pp

    ====================================================================================================
     BIGGEST MOVERS — 12mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 12mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    DJ   | Djibouti             | afrinic  | 4      |  97.4% |   2.9% |  +94.5pp
    EG   | Egypt                | afrinic  | 86     |  95.5% |   7.6% |  +87.9pp
    CN   | China                | apnic    | 6502   |  89.4% |   3.9% |  +85.5pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  83.3% |   3.1% |  +80.2pp
    PK   | Pakistan             | apnic    | 473    |  92.5% |  15.4% |  +77.1pp
    BJ   | Benin                | afrinic  | 16     |  72.6% |   5.7% |  +66.9pp
    CM   | Cameroon             | afrinic  | 29     |  94.8% |  31.5% |  +63.3pp
    SO   | Somalia              | afrinic  | 22     |  78.3% |  19.7% |  +58.6pp
    TJ   | Tajikistan           | ripencc  | 43     |  82.3% |  27.1% |  +55.2pp
    JE   | Jersey               | ripencc  | 13     |  92.2% |  39.4% |  +52.8pp
    HT   | Haiti                | lacnic   | 11     |  56.1% |   3.7% |  +52.4pp
    KI   | Kiribati             | apnic    | 5      |  90.5% |  46.2% |  +44.3pp
    KZ   | Kazakhstan           | ripencc  | 261    |  80.0% |  38.6% |  +41.4pp
    LS   | Lesotho              | afrinic  | 9      |  72.1% |  31.0% |  +41.1pp
    MX   | Mexico               | lacnic   | 654    |  78.0% |  41.1% |  +36.9pp
    Decliners:
    CV   | Cabo Verde           | afrinic  | 8      |  36.9% |  84.9% |  -48.0pp
    IE   | Ireland              | ripencc  | 285    |  66.1% |  78.7% |  -12.6pp
    MG   | Madagascar           | afrinic  | 7      |  41.7% |  52.7% |  -11.0pp
    AO   | Angola               | afrinic  | 71     |  49.1% |  59.3% |  -10.2pp
    GT   | Guatemala            | lacnic   | 79     |  82.3% |  90.6% |   -8.3pp
    KY   | Cayman Islands       | arin     | 18     |  49.1% |  57.3% |   -8.2pp
    BF   | Burkina Faso         | afrinic  | 30     |  81.1% |  89.3% |   -8.2pp
    LY   | Libya                | afrinic  | 27     |  65.5% |  73.7% |   -8.2pp
    PY   | Paraguay             | lacnic   | 115    |  75.5% |  82.8% |   -7.3pp
    KM   | Comoros              | afrinic  | 4      |  74.3% |  80.8% |   -6.5pp
    GL   | Greenland            | ripencc  | 1      |  77.1% |  83.3% |   -6.2pp
    KN   | Saint Kitts and Nevi | arin     | 11     |  12.6% |  17.7% |   -5.1pp
    SD   | Sudan                | afrinic  | 11     |  39.8% |  44.3% |   -4.5pp
    MP   | Northern Mariana Isl | apnic    | 2      |  94.5% |  98.3% |   -3.8pp
    UZ   | Uzbekistan           | ripencc  | 129    |  72.3% |  75.9% |   -3.6pp

    ====================================================================================================
     BIGGEST MOVERS — 24mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 24mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    ET   | Ethiopia             | afrinic  | 8      |  99.5% |   0.0% |  +99.5pp
    GY   | Guyana               | lacnic   | 6      |  98.9% |   0.0% |  +98.9pp
    DJ   | Djibouti             | afrinic  | 4      |  97.4% |   0.0% |  +97.4pp
    MH   | Marshall Islands     | ripencc  | 11     |  94.4% |   0.0% |  +94.4pp
    EG   | Egypt                | afrinic  | 86     |  95.5% |   1.8% |  +93.7pp
    SB   | Solomon Islands      | apnic    | 11     |  91.1% |   0.0% |  +91.1pp
    KI   | Kiribati             | apnic    | 5      |  90.5% |   0.0% |  +90.5pp
    CN   | China                | apnic    | 6502   |  89.4% |   3.6% |  +85.8pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  83.3% |   0.0% |  +83.3pp
    BQ   | Bonaire, Sint Eustat | lacnic   | 6      |  80.4% |   0.0% |  +80.4pp
    PK   | Pakistan             | apnic    | 473    |  92.5% |  12.2% |  +80.3pp
    CI   | Côte d'Ivoire        | afrinic  | 24     |  94.1% |  14.4% |  +79.7pp
    SN   | Senegal              | afrinic  | 18     |  79.0% |   0.8% |  +78.2pp
    SX   | Sint Maarten (Dutch  | lacnic   | 3      |  77.4% |   0.0% |  +77.4pp
    CM   | Cameroon             | afrinic  | 29     |  94.8% |  20.2% |  +74.6pp
    Decliners:
    TC   | Turks and Caicos Isl | arin     | 2      |  33.3% |  92.3% |  -59.0pp
    MZ   | Mozambique           | afrinic  | 31     |  16.0% |  69.3% |  -53.3pp
    CV   | Cabo Verde           | afrinic  | 8      |  36.9% |  83.3% |  -46.4pp
    TD   | Chad                 | afrinic  | 16     |  55.1% | 100.0% |  -44.9pp
    HT   | Haiti                | lacnic   | 11     |  56.1% | 100.0% |  -43.9pp
    PF   | French Polynesia     | apnic    | 6      |  17.3% |  53.8% |  -36.5pp
    CG   | Congo                | afrinic  | 13     |  17.0% |  50.0% |  -33.0pp
    GM   | Gambia               | afrinic  | 11     |  52.4% |  83.3% |  -30.9pp
    MC   | Monaco               | ripencc  | 4      |  56.2% |  83.3% |  -27.1pp
    PG   | Papua New Guinea     | apnic    | 39     |  62.3% |  81.8% |  -19.5pp
    IE   | Ireland              | ripencc  | 285    |  66.1% |  84.3% |  -18.2pp
    SK   | Slovakia             | ripencc  | 229    |  44.1% |  60.2% |  -16.1pp
    NI   | Nicaragua            | lacnic   | 30     |  77.1% |  92.9% |  -15.8pp
    YE   | Yemen                | ripencc  | 6      |  75.1% |  87.9% |  -12.8pp
    LU   | Luxembourg           | ripencc  | 133    |  55.1% |  67.4% |  -12.3pp

    ====================================================================================================
     BIGGEST MOVERS — 3mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 3mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    TJ   | Tajikistan           | ripencc  | 43     |  92.3% |  50.0% |  +42.3pp
    RO   | Romania              | ripencc  | 1084   |  65.4% |  25.7% |  +39.7pp
    TH   | Thailand             | apnic    | 621    |  88.3% |  58.7% |  +29.6pp
    MA   | Morocco              | afrinic  | 32     |  44.1% |  21.6% |  +22.5pp
    MX   | Mexico               | lacnic   | 654    |  82.7% |  60.3% |  +22.4pp
    VI   | Virgin Islands, U.S. | arin     | 12     |  75.7% |  53.8% |  +21.9pp
    LK   | Sri Lanka            | apnic    | 32     | 100.0% |  81.1% |  +18.9pp
    SC   | Seychelles           | ripencc  | 87     |  83.0% |  69.0% |  +14.0pp
    SD   | Sudan                | afrinic  | 11     |  76.9% |  63.6% |  +13.3pp
    AZ   | Azerbaijan           | ripencc  | 120    |  85.5% |  73.8% |  +11.7pp
    MZ   | Mozambique           | afrinic  | 31     |  47.8% |  37.0% |  +10.8pp
    ZM   | Zambia               | afrinic  | 21     | 100.0% |  90.9% |   +9.1pp
    MY   | Malaysia             | apnic    | 406    |  53.8% |  45.6% |   +8.2pp
    KH   | Cambodia             | apnic    | 142    |  84.8% |  76.8% |   +8.0pp
    IM   | Isle of Man          | ripencc  | 26     |  75.9% |  68.0% |   +7.9pp
    Decliners:
    AL   | Albania              | ripencc  | 132    |  71.2% |  96.3% |  -25.1pp
    PR   | Puerto Rico          | arin     | 123    |  29.0% |  46.7% |  -17.7pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  91.4% |  -14.1pp
    FJ   | Fiji                 | apnic    | 20     |  86.4% | 100.0% |  -13.6pp
    MO   | Macao                | apnic    | 15     |  65.2% |  75.3% |  -10.1pp
    VE   | Venezuela            | lacnic   | 260    |  86.9% |  95.4% |   -8.5pp
    ID   | Indonesia            | apnic    | 4038   |  57.5% |  65.2% |   -7.7pp
    MM   | Myanmar              | apnic    | 171    |  90.3% |  96.1% |   -5.8pp
    UY   | Uruguay              | lacnic   | 45     |  43.5% |  49.3% |   -5.8pp
    BB   | Barbados             | arin     | 10     |  13.6% |  18.2% |   -4.6pp
    ES   | Spain                | ripencc  | 1169   |  81.3% |  85.9% |   -4.6pp
    TL   | Timor-Leste          | apnic    | 21     |  86.4% |  90.9% |   -4.5pp
    MP   | Northern Mariana Isl | apnic    | 2      |  15.0% |  19.0% |   -4.0pp
    CA   | Canada               | arin     | 2531   |  69.2% |  72.7% |   -3.5pp
    JM   | Jamaica              | arin     | 15     |  65.0% |  68.2% |   -3.2pp

    ====================================================================================================
     BIGGEST MOVERS — 6mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 6mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    CN   | China                | apnic    | 6502   |  96.9% |  13.0% |  +83.9pp
    TJ   | Tajikistan           | ripencc  | 43     |  92.3% |  50.0% |  +42.3pp
    RO   | Romania              | ripencc  | 1084   |  65.4% |  25.1% |  +40.3pp
    TH   | Thailand             | apnic    | 621    |  88.3% |  57.1% |  +31.2pp
    JM   | Jamaica              | arin     | 15     |  65.0% |  37.8% |  +27.2pp
    MX   | Mexico               | lacnic   | 654    |  82.7% |  57.2% |  +25.5pp
    SD   | Sudan                | afrinic  | 11     |  76.9% |  52.9% |  +24.0pp
    MA   | Morocco              | afrinic  | 32     |  44.1% |  21.1% |  +23.0pp
    ZM   | Zambia               | afrinic  | 21     | 100.0% |  80.0% |  +20.0pp
    PH   | Philippines          | apnic    | 670    |  82.2% |  63.4% |  +18.8pp
    LK   | Sri Lanka            | apnic    | 32     | 100.0% |  81.7% |  +18.3pp
    BD   | Bangladesh           | apnic    | 2024   |  85.7% |  67.7% |  +18.0pp
    NI   | Nicaragua            | lacnic   | 30     |  98.7% |  82.6% |  +16.1pp
    UG   | Uganda               | afrinic  | 59     |  89.8% |  75.0% |  +14.8pp
    LY   | Libya                | afrinic  | 27     |  90.5% |  76.8% |  +13.7pp
    Decliners:
    KE   | Kenya                | afrinic  | 247    |  31.7% |  81.1% |  -49.4pp
    AE   | United Arab Emirates | ripencc  | 212    |  48.5% |  95.4% |  -46.9pp
    OM   | Oman                 | ripencc  | 26     |  51.1% |  91.0% |  -39.9pp
    MT   | Malta                | ripencc  | 56     |  44.8% |  71.9% |  -27.1pp
    AL   | Albania              | ripencc  | 132    |  71.2% |  97.7% |  -26.5pp
    BT   | Bhutan               | apnic    | 43     |  71.9% |  93.3% |  -21.4pp
    PR   | Puerto Rico          | arin     | 123    |  29.0% |  45.8% |  -16.8pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  91.3% |  -14.0pp
    FJ   | Fiji                 | apnic    | 20     |  86.4% | 100.0% |  -13.6pp
    ES   | Spain                | ripencc  | 1169   |  81.3% |  92.4% |  -11.1pp
    MO   | Macao                | apnic    | 15     |  65.2% |  76.3% |  -11.1pp
    MM   | Myanmar              | apnic    | 171    |  90.3% |  99.4% |   -9.1pp
    PS   | Palestine, State of  | ripencc  | 69     |  86.4% |  95.2% |   -8.8pp
    MC   | Monaco               | ripencc  | 4      |  91.3% | 100.0% |   -8.7pp
    LI   | Liechtenstein        | ripencc  | 29     |  77.8% |  85.8% |   -8.0pp

    ====================================================================================================
     BIGGEST MOVERS — 12mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 12mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    CN   | China                | apnic    | 6502   |  96.9% |   2.1% |  +94.8pp
    CH   | Switzerland          | ripencc  | 1062   |  82.2% |  16.5% |  +65.7pp
    SO   | Somalia              | afrinic  | 22     |  82.1% |  21.4% |  +60.7pp
    SD   | Sudan                | afrinic  | 11     |  76.9% |  33.3% |  +43.6pp
    TJ   | Tajikistan           | ripencc  | 43     |  92.3% |  53.3% |  +39.0pp
    JM   | Jamaica              | arin     | 15     |  65.0% |  28.6% |  +36.4pp
    SI   | Slovenia             | ripencc  | 305    |  76.9% |  48.7% |  +28.2pp
    SC   | Seychelles           | ripencc  | 87     |  83.0% |  55.5% |  +27.5pp
    MA   | Morocco              | afrinic  | 32     |  44.1% |  18.4% |  +25.7pp
    MX   | Mexico               | lacnic   | 654    |  82.7% |  59.1% |  +23.6pp
    DE   | Germany              | ripencc  | 3264   |  82.2% |  61.4% |  +20.8pp
    PH   | Philippines          | apnic    | 670    |  82.2% |  64.0% |  +18.2pp
    BM   | Bermuda              | arin     | 22     |  78.3% |  61.9% |  +16.4pp
    ZM   | Zambia               | afrinic  | 21     | 100.0% |  84.6% |  +15.4pp
    AZ   | Azerbaijan           | ripencc  | 120    |  85.5% |  70.3% |  +15.2pp
    Decliners:
    KE   | Kenya                | afrinic  | 247    |  31.7% |  77.0% |  -45.3pp
    AE   | United Arab Emirates | ripencc  | 212    |  48.5% |  90.6% |  -42.1pp
    MO   | Macao                | apnic    | 15     |  65.2% |  95.8% |  -30.6pp
    RO   | Romania              | ripencc  | 1084   |  65.4% |  94.3% |  -28.9pp
    BT   | Bhutan               | apnic    | 43     |  71.9% | 100.0% |  -28.1pp
    AL   | Albania              | ripencc  | 132    |  71.2% |  97.5% |  -26.3pp
    ZW   | Zimbabwe             | afrinic  | 28     |  14.7% |  33.3% |  -18.6pp
    IE   | Ireland              | ripencc  | 285    |  73.1% |  90.6% |  -17.5pp
    ZA   | South Africa         | afrinic  | 751    |  35.4% |  50.1% |  -14.7pp
    FJ   | Fiji                 | apnic    | 20     |  86.4% | 100.0% |  -13.6pp
    PR   | Puerto Rico          | arin     | 123    |  29.0% |  42.0% |  -13.0pp
    SA   | Saudi Arabia         | ripencc  | 200    |  86.4% |  98.5% |  -12.1pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  89.1% |  -11.8pp
    NG   | Nigeria              | afrinic  | 266    |  43.2% |  52.5% |   -9.3pp
    UY   | Uruguay              | lacnic   | 45     |  43.5% |  52.5% |   -9.0pp

    ====================================================================================================
     BIGGEST MOVERS — 24mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 24mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    CN   | China                | apnic    | 6502   |  96.9% |   1.7% |  +95.2pp
    IS   | Iceland              | ripencc  | 87     |  93.8% |  24.8% |  +69.0pp
    JP   | Japan                | apnic    | 981    |  83.4% |  17.7% |  +65.7pp
    GH   | Ghana                | afrinic  | 103    |  89.5% |  38.5% |  +51.0pp
    JM   | Jamaica              | arin     | 15     |  65.0% |  18.2% |  +46.8pp
    SC   | Seychelles           | ripencc  | 87     |  83.0% |  40.4% |  +42.6pp
    UZ   | Uzbekistan           | ripencc  | 129    |  86.4% |  45.5% |  +40.9pp
    IE   | Ireland              | ripencc  | 285    |  73.1% |  35.1% |  +38.0pp
    SD   | Sudan                | afrinic  | 11     |  76.9% |  40.0% |  +36.9pp
    MC   | Monaco               | ripencc  | 4      |  91.3% |  56.2% |  +35.1pp
    AZ   | Azerbaijan           | ripencc  | 120    |  85.5% |  52.8% |  +32.7pp
    SI   | Slovenia             | ripencc  | 305    |  76.9% |  46.0% |  +30.9pp
    TT   | Trinidad and Tobago  | lacnic   | 16     |  63.6% |  32.8% |  +30.8pp
    BM   | Bermuda              | arin     | 22     |  78.3% |  50.0% |  +28.3pp
    IN   | India                | apnic    | 6207   |  86.3% |  59.8% |  +26.5pp
    Decliners:
    CD   | Congo, The Democrati | afrinic  | 51     |  26.3% |  83.9% |  -57.6pp
    KE   | Kenya                | afrinic  | 247    |  31.7% |  81.7% |  -50.0pp
    ZW   | Zimbabwe             | afrinic  | 28     |  14.7% |  63.2% |  -48.5pp
    AE   | United Arab Emirates | ripencc  | 212    |  48.5% |  89.8% |  -41.3pp
    MU   | Mauritius            | afrinic  | 41     |   2.6% |  40.6% |  -38.0pp
    MZ   | Mozambique           | afrinic  | 31     |  47.8% |  81.2% |  -33.4pp
    MA   | Morocco              | afrinic  | 32     |  44.1% |  76.1% |  -32.0pp
    MO   | Macao                | apnic    | 15     |  65.2% |  96.4% |  -31.2pp
    BT   | Bhutan               | apnic    | 43     |  71.9% | 100.0% |  -28.1pp
    AL   | Albania              | ripencc  | 132    |  71.2% |  98.3% |  -27.1pp
    PR   | Puerto Rico          | arin     | 123    |  29.0% |  54.6% |  -25.6pp
    ZA   | South Africa         | afrinic  | 751    |  35.4% |  60.2% |  -24.8pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  95.2% |  -17.9pp
    VI   | Virgin Islands, U.S. | arin     | 12     |  75.7% |  90.5% |  -14.8pp
    RO   | Romania              | ripencc  | 1084   |  65.4% |  80.1% |  -14.7pp

    ====================================================================================================
     SPOTLIGHT: CHINA (CN)
    ====================================================================================================
    ASNs: 6502  |  RIR: apnic
    IPv4:
      Now  : 89.4% of IPv4 route objects covered by a valid ROA
      3mo  : 88.9% of IPv4 route objects covered by a valid ROA
      6mo  : 4.4% of IPv4 route objects covered by a valid ROA
      12mo : 3.9% of IPv4 route objects covered by a valid ROA
      24mo : 3.6% of IPv4 route objects covered by a valid ROA
    IPv6:
      Now  : 96.9% of IPv6 route objects covered by a valid ROA
      3mo  : 95.8% of IPv6 route objects covered by a valid ROA
      6mo  : 13.0% of IPv6 route objects covered by a valid ROA
      12mo : 2.1% of IPv6 route objects covered by a valid ROA
      24mo : 1.7% of IPv6 route objects covered by a valid ROA
