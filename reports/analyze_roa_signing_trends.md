    [*] Fetching APNIC Labs ROA-coverage snapshots...
        - Now   (reported date 16/09/2026): 278 countries/regions
        - 3mo   (reported date 16/06/2026): 279 countries/regions
        - 6mo   (reported date 16/03/2026): 279 countries/regions
        - 12mo  (reported date 16/09/2025): 279 countries/regions
        - 24mo  (reported date 16/09/2024): 250 countries/regions

    ====================================================================================================
     GLOBAL ROA COVERAGE TREND (IPv4 Route Objects, % Valid)
    ====================================================================================================
    Period   | Reported Date  | % Valid  | Total Route Objects
    ------------------------------------------------------------
    Now      | 16/09/2026     |   68.0% |  1,282,608
    3mo      | 16/06/2026     |   64.7% |  1,269,618
    6mo      | 16/03/2026     |   58.9% |  1,242,704
    12mo     | 16/09/2025     |   53.2% |  1,229,708
    24mo     | 16/09/2024     |   49.1% |  1,148,380

    ====================================================================================================
     GLOBAL ROA COVERAGE TREND (IPv6 Route Objects, % Valid)
    ====================================================================================================
    Period   | Reported Date  | % Valid  | Total Route Objects
    ------------------------------------------------------------
    Now      | 16/09/2026     |   75.3% |    311,032
    3mo      | 16/06/2026     |   73.5% |    309,439
    6mo      | 16/03/2026     |   62.8% |    298,829
    12mo     | 16/09/2025     |   57.4% |    296,767
    24mo     | 16/09/2024     |   55.2% |    260,093

    NOTE: IPv4 and IPv6 are reported separately because they are measured
    separately by APNIC and can diverge significantly per network — do not
    average or add them into one 'global ROA coverage' number.

    ====================================================================================================
     RIR ROA COVERAGE TREND (IPv4 Route Objects, % Valid, weighted by route-object count)
    ====================================================================================================
    RIR        | ASNs (now) |     Now |     3mo |     6mo |    12mo |    24mo
    -------------------------------------------------------------------------
    afrinic    | 2,457      |   65.4% |   61.2% |   58.0% |   38.2% |   31.4%
    apnic      | 31,245     |   76.5% |   71.5% |   55.0% |   49.1% |   51.1%
    arin       | 35,339     |   53.6% |   50.9% |   48.8% |   40.5% |   34.2%
    lacnic     | 13,754     |   68.3% |   60.7% |   59.1% |   60.1% |   55.0%
    ripencc    | 38,264     |   74.5% |   74.3% |   73.2% |   68.0% |   60.3%

    ====================================================================================================
     RIR ROA COVERAGE TREND (IPv6 Route Objects, % Valid, weighted by route-object count)
    ====================================================================================================
    RIR        | ASNs (now) |     Now |     3mo |     6mo |    12mo |    24mo
    -------------------------------------------------------------------------
    afrinic    | 2,457      |   41.2% |   38.1% |   40.5% |   35.9% |   61.7%
    apnic      | 31,245     |   83.5% |   80.9% |   51.8% |   48.1% |   39.0%
    arin       | 35,339     |   77.4% |   76.2% |   75.2% |   67.6% |   61.5%
    lacnic     | 13,754     |   63.1% |   60.9% |   60.2% |   57.8% |   56.9%
    ripencc    | 38,264     |   77.7% |   77.3% |   77.0% |   64.6% |   75.0%

    [+] Full per-country trend data (IPv4 + IPv6) saved to roa_signing_trends.csv

    ====================================================================================================
     BIGGEST MOVERS — 3mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 3mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    ST   | Sao Tome and Princip | afrinic  | 2      |  83.3% |   5.4% |  +77.9pp
    TG   | Togo                 | afrinic  | 11     |  62.8% |  10.3% |  +52.5pp
    TT   | Trinidad and Tobago  | lacnic   | 16     |  91.8% |  53.6% |  +38.2pp
    JE   | Jersey               | ripencc  | 13     |  92.2% |  56.1% |  +36.1pp
    MX   | Mexico               | lacnic   | 646    |  76.0% |  44.2% |  +31.8pp
    GG   | Guernsey             | ripencc  | 11     |  71.0% |  49.3% |  +21.7pp
    CD   | Congo, The Democrati | afrinic  | 51     |  56.1% |  36.4% |  +19.7pp
    KE   | Kenya                | afrinic  | 242    |  76.0% |  58.6% |  +17.4pp
    NG   | Nigeria              | afrinic  | 266    |  59.0% |  42.8% |  +16.2pp
    SO   | Somalia              | afrinic  | 22     |  76.2% |  60.1% |  +16.1pp
    BQ   | Bonaire, Sint Eustat | lacnic   | 6      |  97.2% |  83.8% |  +13.4pp
    AU   | Australia            | apnic    | 2986   |  49.4% |  36.3% |  +13.1pp
    RO   | Romania              | ripencc  | 1081   |  78.5% |  65.8% |  +12.7pp
    MA   | Morocco              | afrinic  | 32     |  14.9% |   3.4% |  +11.5pp
    SS   | South Sudan          | afrinic  | 20     |  57.7% |  47.4% |  +10.3pp
    Decliners:
    IT   | Italy                | ripencc  | 1316   |  51.3% |  67.8% |  -16.5pp
    LY   | Libya                | afrinic  | 27     |  58.3% |  71.6% |  -13.3pp
    MK   | North Macedonia      | ripencc  | 68     |  42.6% |  51.3% |   -8.7pp
    KY   | Cayman Islands       | arin     | 18     |  48.2% |  55.2% |   -7.0pp
    SC   | Seychelles           | ripencc  | 87     |  82.0% |  88.2% |   -6.2pp
    UZ   | Uzbekistan           | ripencc  | 129    |  72.6% |  77.8% |   -5.2pp
    KM   | Comoros              | afrinic  | 4      |  74.3% |  79.3% |   -5.0pp
    KN   | Saint Kitts and Nevi | arin     | 11     |  13.0% |  16.2% |   -3.2pp
    CF   | Central African Repu | afrinic  | 4      |  16.0% |  18.5% |   -2.5pp
    BN   | Brunei Darussalam    | apnic    | 10     |  81.1% |  83.1% |   -2.0pp
    GD   | Grenada              | arin     | 11     |  31.1% |  32.9% |   -1.8pp
    IE   | Ireland              | ripencc  | 285    |  65.1% |  66.8% |   -1.7pp
    PE   | Peru                 | lacnic   | 223    |  36.6% |  38.3% |   -1.7pp
    SB   | Solomon Islands      | apnic    | 11     |  83.7% |  85.4% |   -1.7pp
    CZ   | Czechia              | ripencc  | 714    |  80.7% |  82.4% |   -1.7pp

    ====================================================================================================
     BIGGEST MOVERS — 6mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 6mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    DJ   | Djibouti             | afrinic  | 4      |  97.3% |   5.6% |  +91.7pp
    CN   | China                | apnic    | 6482   |  89.4% |   4.3% |  +85.1pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  83.3% |   5.9% |  +77.4pp
    CM   | Cameroon             | afrinic  | 29     |  94.9% |  35.4% |  +59.5pp
    JE   | Jersey               | ripencc  | 13     |  92.2% |  53.1% |  +39.1pp
    TT   | Trinidad and Tobago  | lacnic   | 16     |  91.8% |  53.3% |  +38.5pp
    MX   | Mexico               | lacnic   | 646    |  76.0% |  42.0% |  +34.0pp
    MT   | Malta                | ripencc  | 54     |  53.6% |  25.6% |  +28.0pp
    SO   | Somalia              | afrinic  | 22     |  76.2% |  52.9% |  +23.3pp
    NA   | Namibia              | afrinic  | 18     |  86.2% |  65.4% |  +20.8pp
    MK   | North Macedonia      | ripencc  | 68     |  42.6% |  21.9% |  +20.7pp
    GG   | Guernsey             | ripencc  | 11     |  71.0% |  50.7% |  +20.3pp
    KE   | Kenya                | afrinic  | 242    |  76.0% |  55.8% |  +20.2pp
    CD   | Congo, The Democrati | afrinic  | 51     |  56.1% |  36.3% |  +19.8pp
    AF   | Afghanistan          | apnic    | 75     |  90.0% |  70.4% |  +19.6pp
    Decliners:
    CV   | Cabo Verde           | afrinic  | 8      |  36.9% |  86.4% |  -49.5pp
    LY   | Libya                | afrinic  | 27     |  58.3% |  79.8% |  -21.5pp
    IT   | Italy                | ripencc  | 1316   |  51.3% |  65.6% |  -14.3pp
    KM   | Comoros              | afrinic  | 4      |  74.3% |  80.8% |   -6.5pp
    KY   | Cayman Islands       | arin     | 18     |  48.2% |  54.6% |   -6.4pp
    MP   | Northern Mariana Isl | apnic    | 2      |  94.4% | 100.0% |   -5.6pp
    UZ   | Uzbekistan           | ripencc  | 129    |  72.6% |  77.1% |   -4.5pp
    YT   | Mayotte              | afrinic  | 1      |  73.1% |  77.4% |   -4.3pp
    GT   | Guatemala            | lacnic   | 79     |  82.2% |  86.0% |   -3.8pp
    GL   | Greenland            | ripencc  | 1      |  77.1% |  80.6% |   -3.5pp
    SD   | Sudan                | afrinic  | 11     |  42.0% |  45.3% |   -3.3pp
    MG   | Madagascar           | afrinic  | 7      |  42.4% |  45.3% |   -2.9pp
    BS   | Bahamas              | arin     | 13     |  26.2% |  28.5% |   -2.3pp
    SX   | Sint Maarten (Dutch  | lacnic   | 3      |  77.4% |  79.4% |   -2.0pp
    YE   | Yemen                | ripencc  | 6      |  75.7% |  77.7% |   -2.0pp

    ====================================================================================================
     BIGGEST MOVERS — 12mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 12mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    DJ   | Djibouti             | afrinic  | 4      |  97.3% |   2.9% |  +94.4pp
    EG   | Egypt                | afrinic  | 86     |  95.6% |   7.7% |  +87.9pp
    CN   | China                | apnic    | 6482   |  89.4% |   3.9% |  +85.5pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  83.3% |   0.0% |  +83.3pp
    PK   | Pakistan             | apnic    | 468    |  92.4% |  15.4% |  +77.0pp
    CM   | Cameroon             | afrinic  | 29     |  94.9% |  32.1% |  +62.8pp
    BJ   | Benin                | afrinic  | 16     |  65.5% |   5.8% |  +59.7pp
    SO   | Somalia              | afrinic  | 22     |  76.2% |  19.8% |  +56.4pp
    JE   | Jersey               | ripencc  | 13     |  92.2% |  38.4% |  +53.8pp
    HT   | Haiti                | lacnic   | 11     |  56.3% |   2.6% |  +53.7pp
    LS   | Lesotho              | afrinic  | 9      |  71.8% |  30.1% |  +41.7pp
    KZ   | Kazakhstan           | ripencc  | 261    |  80.0% |  38.5% |  +41.5pp
    TT   | Trinidad and Tobago  | lacnic   | 16     |  91.8% |  53.2% |  +38.6pp
    MX   | Mexico               | lacnic   | 646    |  76.0% |  41.0% |  +35.0pp
    CD   | Congo, The Democrati | afrinic  | 51     |  56.1% |  23.2% |  +32.9pp
    Decliners:
    CV   | Cabo Verde           | afrinic  | 8      |  36.9% |  84.9% |  -48.0pp
    PE   | Peru                 | lacnic   | 223    |  36.6% |  60.5% |  -23.9pp
    LY   | Libya                | afrinic  | 27     |  58.3% |  73.8% |  -15.5pp
    IE   | Ireland              | ripencc  | 285    |  65.1% |  78.5% |  -13.4pp
    MG   | Madagascar           | afrinic  | 7      |  42.4% |  52.7% |  -10.3pp
    KY   | Cayman Islands       | arin     | 18     |  48.2% |  57.3% |   -9.1pp
    GT   | Guatemala            | lacnic   | 79     |  82.2% |  90.4% |   -8.2pp
    BF   | Burkina Faso         | afrinic  | 30     |  81.0% |  89.1% |   -8.1pp
    AO   | Angola               | afrinic  | 70     |  48.4% |  56.4% |   -8.0pp
    PY   | Paraguay             | lacnic   | 115    |  75.6% |  83.0% |   -7.4pp
    GL   | Greenland            | ripencc  | 1      |  77.1% |  83.3% |   -6.2pp
    KM   | Comoros              | afrinic  | 4      |  74.3% |  80.0% |   -5.7pp
    VG   | Virgin Islands, Brit | ripencc  | 47     |  45.8% |  50.0% |   -4.2pp
    VI   | Virgin Islands, U.S. | arin     | 12     |  46.4% |  50.4% |   -4.0pp
    TZ   | Tanzania             | afrinic  | 116    |  35.2% |  39.1% |   -3.9pp

    ====================================================================================================
     BIGGEST MOVERS — 24mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 24mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    DJ   | Djibouti             | afrinic  | 4      |  97.3% |   1.0% |  +96.3pp
    EG   | Egypt                | afrinic  | 86     |  95.6% |   8.0% |  +87.6pp
    CN   | China                | apnic    | 6482   |  89.4% |   2.9% |  +86.5pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  83.3% |   0.0% |  +83.3pp
    CM   | Cameroon             | afrinic  | 29     |  94.9% |  13.6% |  +81.3pp
    FM   | Micronesia, Federate | apnic    | 6      |  85.0% |   4.8% |  +80.2pp
    SN   | Senegal              | afrinic  | 18     |  78.9% |   1.4% |  +77.5pp
    CI   | Côte d'Ivoire        | afrinic  | 24     |  94.1% |  20.1% |  +74.0pp
    IS   | Iceland              | ripencc  | 87     |  75.2% |   1.7% |  +73.5pp
    JE   | Jersey               | ripencc  | 13     |  92.2% |  25.0% |  +67.2pp
    SO   | Somalia              | afrinic  | 22     |  76.2% |  13.0% |  +63.2pp
    BJ   | Benin                | afrinic  | 16     |  65.5% |   3.3% |  +62.2pp
    ML   | Mali                 | afrinic  | 8      |  83.3% |  25.4% |  +57.9pp
    SL   | Sierra Leone         | afrinic  | 22     |  57.7% |   6.4% |  +51.3pp
    HT   | Haiti                | lacnic   | 11     |  56.3% |   5.4% |  +50.9pp
    Decliners:
    CV   | Cabo Verde           | afrinic  | 8      |  36.9% |  80.9% |  -44.0pp
    KM   | Comoros              | afrinic  | 4      |  74.3% | 100.0% |  -25.7pp
    SD   | Sudan                | afrinic  | 11     |  42.0% |  62.3% |  -20.3pp
    LY   | Libya                | afrinic  | 27     |  58.3% |  76.2% |  -17.9pp
    PE   | Peru                 | lacnic   | 223    |  36.6% |  52.2% |  -15.6pp
    AO   | Angola               | afrinic  | 70     |  48.4% |  60.0% |  -11.6pp
    IE   | Ireland              | ripencc  | 285    |  65.1% |  75.3% |  -10.2pp
    PY   | Paraguay             | lacnic   | 115    |  75.6% |  83.0% |   -7.4pp
    ME   | Montenegro           | ripencc  | 30     |  49.0% |  55.9% |   -6.9pp
    MZ   | Mozambique           | afrinic  | 31     |  15.9% |  22.2% |   -6.3pp
    SK   | Slovakia             | ripencc  | 228    |  46.0% |  52.3% |   -6.3pp
    MG   | Madagascar           | afrinic  | 7      |  42.4% |  48.2% |   -5.8pp
    BF   | Burkina Faso         | afrinic  | 30     |  81.0% |  86.1% |   -5.1pp
    CG   | Congo                | afrinic  | 13     |  17.0% |  21.7% |   -4.7pp
    ZM   | Zambia               | afrinic  | 22     |  49.1% |  53.1% |   -4.0pp

    ====================================================================================================
     BIGGEST MOVERS — 3mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 3mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    RO   | Romania              | ripencc  | 1081   |  71.0% |  38.0% |  +33.0pp
    TH   | Thailand             | apnic    | 621    |  88.3% |  59.0% |  +29.3pp
    MD   | Moldova              | ripencc  | 204    |  98.8% |  69.8% |  +29.0pp
    MA   | Morocco              | afrinic  | 32     |  43.5% |  21.6% |  +21.9pp
    UG   | Uganda               | afrinic  | 59     |  89.9% |  75.5% |  +14.4pp
    AZ   | Azerbaijan           | ripencc  | 117    |  87.7% |  73.8% |  +13.9pp
    MZ   | Mozambique           | afrinic  | 31     |  47.8% |  37.0% |  +10.8pp
    LK   | Sri Lanka            | apnic    | 32     |  91.2% |  81.4% |   +9.8pp
    IM   | Isle of Man          | ripencc  | 26     |  75.9% |  66.7% |   +9.2pp
    ZM   | Zambia               | afrinic  | 22     | 100.0% |  90.9% |   +9.1pp
    CM   | Cameroon             | afrinic  | 29     |  95.7% |  86.7% |   +9.0pp
    MY   | Malaysia             | apnic    | 405    |  53.6% |  45.5% |   +8.1pp
    TJ   | Tajikistan           | ripencc  | 41     |  55.2% |  47.8% |   +7.4pp
    AO   | Angola               | afrinic  | 70     |  83.3% |  76.5% |   +6.8pp
    PL   | Poland               | ripencc  | 2466   |  82.4% |  75.9% |   +6.5pp
    Decliners:
    AE   | United Arab Emirates | ripencc  | 213    |  49.7% |  95.1% |  -45.4pp
    AL   | Albania              | ripencc  | 131    |  71.3% |  96.9% |  -25.6pp
    PR   | Puerto Rico          | arin     | 123    |  28.9% |  47.1% |  -18.2pp
    FJ   | Fiji                 | apnic    | 20     |  86.4% | 100.0% |  -13.6pp
    MO   | Macao                | apnic    | 15     |  64.9% |  75.0% |  -10.1pp
    AM   | Armenia              | ripencc  | 154    |  85.1% |  94.4% |   -9.3pp
    PS   | Palestine, State of  | ripencc  | 69     |  86.4% |  95.0% |   -8.6pp
    SC   | Seychelles           | ripencc  | 87     |  85.2% |  91.6% |   -6.4pp
    MT   | Malta                | ripencc  | 54     |  43.1% |  49.1% |   -6.0pp
    MM   | Myanmar              | apnic    | 170    |  90.7% |  96.1% |   -5.4pp
    ES   | Spain                | ripencc  | 1158   |  81.0% |  86.1% |   -5.1pp
    PK   | Pakistan             | apnic    | 468    |  91.1% |  95.9% |   -4.8pp
    MP   | Northern Mariana Isl | apnic    | 2      |  15.0% |  19.0% |   -4.0pp
    PH   | Philippines          | apnic    | 669    |  73.3% |  77.3% |   -4.0pp
    BB   | Barbados             | arin     | 10     |  14.3% |  18.2% |   -3.9pp

    ====================================================================================================
     BIGGEST MOVERS — 6mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 6mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    CN   | China                | apnic    | 6482   |  97.5% |  13.0% |  +84.5pp
    RO   | Romania              | ripencc  | 1081   |  71.0% |  24.9% |  +46.1pp
    JM   | Jamaica              | arin     | 15     |  65.0% |  34.3% |  +30.7pp
    TH   | Thailand             | apnic    | 621    |  88.3% |  58.7% |  +29.6pp
    MA   | Morocco              | afrinic  | 32     |  43.5% |  21.1% |  +22.4pp
    ZM   | Zambia               | afrinic  | 22     | 100.0% |  80.0% |  +20.0pp
    NI   | Nicaragua            | lacnic   | 30     |  98.7% |  82.6% |  +16.1pp
    SC   | Seychelles           | ripencc  | 87     |  85.2% |  69.3% |  +15.9pp
    UG   | Uganda               | afrinic  | 59     |  89.9% |  74.7% |  +15.2pp
    SD   | Sudan                | afrinic  | 11     |  70.0% |  55.6% |  +14.4pp
    AZ   | Azerbaijan           | ripencc  | 117    |  87.7% |  73.8% |  +13.9pp
    MZ   | Mozambique           | afrinic  | 31     |  47.8% |  34.6% |  +13.2pp
    VG   | Virgin Islands, Brit | ripencc  | 47     |  75.6% |  63.0% |  +12.6pp
    BM   | Bermuda              | arin     | 22     |  78.3% |  66.7% |  +11.6pp
    PL   | Poland               | ripencc  | 2466   |  82.4% |  70.9% |  +11.5pp
    Decliners:
    KE   | Kenya                | afrinic  | 242    |  28.7% |  79.6% |  -50.9pp
    AE   | United Arab Emirates | ripencc  | 213    |  49.7% |  93.3% |  -43.6pp
    AL   | Albania              | ripencc  | 131    |  71.3% |  98.6% |  -27.3pp
    BT   | Bhutan               | apnic    | 43     |  72.5% |  97.7% |  -25.2pp
    PR   | Puerto Rico          | arin     | 123    |  28.9% |  44.4% |  -15.5pp
    FJ   | Fiji                 | apnic    | 20     |  86.4% | 100.0% |  -13.6pp
    MO   | Macao                | apnic    | 15     |  64.9% |  76.6% |  -11.7pp
    SA   | Saudi Arabia         | ripencc  | 199    |  85.5% |  97.0% |  -11.5pp
    ES   | Spain                | ripencc  | 1158   |  81.0% |  92.3% |  -11.3pp
    LI   | Liechtenstein        | ripencc  | 28     |  75.9% |  85.1% |   -9.2pp
    PS   | Palestine, State of  | ripencc  | 69     |  86.4% |  95.2% |   -8.8pp
    LY   | Libya                | afrinic  | 27     |  90.2% |  98.2% |   -8.0pp
    NG   | Nigeria              | afrinic  | 266    |  41.7% |  49.0% |   -7.3pp
    PK   | Pakistan             | apnic    | 468    |  91.1% |  96.9% |   -5.8pp
    MM   | Myanmar              | apnic    | 170    |  90.7% |  96.3% |   -5.6pp

    ====================================================================================================
     BIGGEST MOVERS — 12mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 12mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    CN   | China                | apnic    | 6482   |  97.5% |   2.1% |  +95.4pp
    CH   | Switzerland          | ripencc  | 1059   |  81.5% |  16.6% |  +64.9pp
    SO   | Somalia              | afrinic  | 22     |  85.2% |  22.2% |  +63.0pp
    JM   | Jamaica              | arin     | 15     |  65.0% |  32.4% |  +32.6pp
    SI   | Slovenia             | ripencc  | 305    |  75.4% |  48.9% |  +26.5pp
    MA   | Morocco              | afrinic  | 32     |  43.5% |  18.9% |  +24.6pp
    DE   | Germany              | ripencc  | 3256   |  82.6% |  61.4% |  +21.2pp
    SD   | Sudan                | afrinic  | 11     |  70.0% |  50.0% |  +20.0pp
    AZ   | Azerbaijan           | ripencc  | 117    |  87.7% |  70.8% |  +16.9pp
    PL   | Poland               | ripencc  | 2466   |  82.4% |  66.2% |  +16.2pp
    OM   | Oman                 | ripencc  | 26     |  50.7% |  34.8% |  +15.9pp
    CA   | Canada               | arin     | 2520   |  73.5% |  58.1% |  +15.4pp
    ZM   | Zambia               | afrinic  | 22     | 100.0% |  84.6% |  +15.4pp
    IN   | India                | apnic    | 6182   |  86.2% |  71.3% |  +14.9pp
    BM   | Bermuda              | arin     | 22     |  78.3% |  63.6% |  +14.7pp
    Decliners:
    KE   | Kenya                | afrinic  | 242    |  28.7% |  80.3% |  -51.6pp
    ZW   | Zimbabwe             | afrinic  | 28     |  13.4% |  52.0% |  -38.6pp
    MO   | Macao                | apnic    | 15     |  64.9% |  95.7% |  -30.8pp
    BT   | Bhutan               | apnic    | 43     |  72.5% | 100.0% |  -27.5pp
    AL   | Albania              | ripencc  | 131    |  71.3% |  98.3% |  -27.0pp
    RO   | Romania              | ripencc  | 1081   |  71.0% |  94.5% |  -23.5pp
    ZA   | South Africa         | afrinic  | 748    |  34.4% |  51.9% |  -17.5pp
    FJ   | Fiji                 | apnic    | 20     |  86.4% | 100.0% |  -13.6pp
    IE   | Ireland              | ripencc  | 285    |  73.3% |  86.6% |  -13.3pp
    PR   | Puerto Rico          | arin     | 123    |  28.9% |  42.0% |  -13.1pp
    SA   | Saudi Arabia         | ripencc  | 199    |  85.5% |  98.5% |  -13.0pp
    TJ   | Tajikistan           | ripencc  | 41     |  55.2% |  66.7% |  -11.5pp
    NG   | Nigeria              | afrinic  | 266    |  41.7% |  51.3% |   -9.6pp
    ES   | Spain                | ripencc  | 1158   |  81.0% |  89.9% |   -8.9pp
    KR   | South Korea          | apnic    | 1079   |  11.8% |  20.6% |   -8.8pp

    ====================================================================================================
     BIGGEST MOVERS — 24mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 24mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    CN   | China                | apnic    | 6482   |  97.5% |   1.6% |  +95.9pp
    IS   | Iceland              | ripencc  | 87     |  92.6% |  24.7% |  +67.9pp
    JP   | Japan                | apnic    | 975    |  83.2% |  17.3% |  +65.9pp
    JM   | Jamaica              | arin     | 15     |  65.0% |  14.3% |  +50.7pp
    GH   | Ghana                | afrinic  | 102    |  89.5% |  39.2% |  +50.3pp
    SC   | Seychelles           | ripencc  | 87     |  85.2% |  41.5% |  +43.7pp
    UZ   | Uzbekistan           | ripencc  | 129    |  86.2% |  45.5% |  +40.7pp
    IE   | Ireland              | ripencc  | 285    |  73.3% |  34.8% |  +38.5pp
    MC   | Monaco               | ripencc  | 4      |  91.3% |  56.2% |  +35.1pp
    AZ   | Azerbaijan           | ripencc  | 117    |  87.7% |  53.7% |  +34.0pp
    MW   | Malawi               | afrinic  | 30     |  77.8% |  44.0% |  +33.8pp
    SD   | Sudan                | afrinic  | 11     |  70.0% |  40.0% |  +30.0pp
    SI   | Slovenia             | ripencc  | 305    |  75.4% |  46.0% |  +29.4pp
    BM   | Bermuda              | arin     | 22     |  78.3% |  50.0% |  +28.3pp
    TT   | Trinidad and Tobago  | lacnic   | 16     |  63.0% |  35.4% |  +27.6pp
    Decliners:
    CD   | Congo, The Democrati | afrinic  | 51     |  25.0% |  83.9% |  -58.9pp
    KE   | Kenya                | afrinic  | 242    |  28.7% |  80.5% |  -51.8pp
    MU   | Mauritius            | afrinic  | 41     |   2.9% |  44.6% |  -41.7pp
    AE   | United Arab Emirates | ripencc  | 213    |  49.7% |  89.9% |  -40.2pp
    ZW   | Zimbabwe             | afrinic  | 28     |  13.4% |  52.6% |  -39.2pp
    MZ   | Mozambique           | afrinic  | 31     |  47.8% |  81.2% |  -33.4pp
    MA   | Morocco              | afrinic  | 32     |  43.5% |  76.3% |  -32.8pp
    MO   | Macao                | apnic    | 15     |  64.9% |  93.1% |  -28.2pp
    BT   | Bhutan               | apnic    | 43     |  72.5% | 100.0% |  -27.5pp
    AL   | Albania              | ripencc  | 131    |  71.3% |  98.3% |  -27.0pp
    VI   | Virgin Islands, U.S. | arin     | 12     |  64.0% |  90.5% |  -26.5pp
    ZA   | South Africa         | afrinic  | 748    |  34.4% |  59.8% |  -25.4pp
    TZ   | Tanzania             | afrinic  | 116    |  33.0% |  53.7% |  -20.7pp
    TJ   | Tajikistan           | ripencc  | 41     |  55.2% |  72.7% |  -17.5pp
    IT   | Italy                | ripencc  | 1316   |  71.2% |  83.8% |  -12.6pp

    ====================================================================================================
     SPOTLIGHT: CHINA (CN)
    ====================================================================================================
    ASNs: 6482  |  RIR: apnic
    IPv4:
      Now  : 89.4% of IPv4 route objects covered by a valid ROA
      3mo  : 81.2% of IPv4 route objects covered by a valid ROA
      6mo  : 4.3% of IPv4 route objects covered by a valid ROA
      12mo : 3.9% of IPv4 route objects covered by a valid ROA
      24mo : 2.9% of IPv4 route objects covered by a valid ROA
    IPv6:
      Now  : 97.5% of IPv6 route objects covered by a valid ROA
      3mo  : 93.3% of IPv6 route objects covered by a valid ROA
      6mo  : 13.0% of IPv6 route objects covered by a valid ROA
      12mo : 2.1% of IPv6 route objects covered by a valid ROA
      24mo : 1.6% of IPv6 route objects covered by a valid ROA
