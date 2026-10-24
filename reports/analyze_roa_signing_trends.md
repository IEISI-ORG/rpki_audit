    [*] Fetching APNIC Labs ROA-coverage snapshots...
        - Now   (reported date 22/10/2026): 278 countries/regions
        - 3mo   (reported date 25/07/2026): 278 countries/regions
        - 6mo   (reported date 25/04/2026): 279 countries/regions
        - 12mo  (reported date 25/10/2025): 280 countries/regions
        - 24mo  (reported date 25/10/2024): 279 countries/regions

    ====================================================================================================
     GLOBAL ROA COVERAGE TREND (IPv4 Route Objects, % Valid)
    ====================================================================================================
    Period   | Reported Date  | % Valid  | Total Route Objects
    ------------------------------------------------------------
    Now      | 22/10/2026     |   67.7% |  1,323,757
    3mo      | 25/07/2026     |   66.0% |  1,274,480
    6mo      | 25/04/2026     |   59.4% |  1,254,416
    12mo     | 25/10/2025     |   53.9% |  1,252,126
    24mo     | 25/10/2024     |   48.5% |  1,190,123

    ====================================================================================================
     GLOBAL ROA COVERAGE TREND (IPv6 Route Objects, % Valid)
    ====================================================================================================
    Period   | Reported Date  | % Valid  | Total Route Objects
    ------------------------------------------------------------
    Now      | 22/10/2026     |   75.6% |    321,122
    3mo      | 25/07/2026     |   74.3% |    315,736
    6mo      | 25/04/2026     |   63.6% |    303,030
    12mo     | 25/10/2025     |   57.6% |    297,609
    24mo     | 25/10/2024     |   55.3% |    261,704

    NOTE: IPv4 and IPv6 are reported separately because they are measured
    separately by APNIC and can diverge significantly per network — do not
    average or add them into one 'global ROA coverage' number.

    ====================================================================================================
     RIR ROA COVERAGE TREND (IPv4 Route Objects, % Valid, weighted by route-object count)
    ====================================================================================================
    RIR        | ASNs (now) |     Now |     3mo |     6mo |    12mo |    24mo
    -------------------------------------------------------------------------
    afrinic    | 2,474      |   65.7% |   61.3% |   58.4% |   37.9% |   32.4%
    apnic      | 31,446     |   76.2% |   74.1% |   55.8% |   49.2% |   46.0%
    arin       | 35,553     |   52.8% |   51.4% |   49.1% |   43.6% |   34.0%
    lacnic     | 13,827     |   69.3% |   63.5% |   59.7% |   59.2% |   55.6%
    ripencc    | 38,611     |   74.5% |   74.6% |   73.7% |   68.4% |   62.2%

    ====================================================================================================
     RIR ROA COVERAGE TREND (IPv6 Route Objects, % Valid, weighted by route-object count)
    ====================================================================================================
    RIR        | ASNs (now) |     Now |     3mo |     6mo |    12mo |    24mo
    -------------------------------------------------------------------------
    afrinic    | 2,474      |   42.0% |   39.8% |   40.9% |   35.2% |   61.6%
    apnic      | 31,446     |   83.3% |   81.6% |   53.9% |   48.9% |   39.5%
    arin       | 35,553     |   74.7% |   76.6% |   75.9% |   67.7% |   61.9%
    lacnic     | 13,827     |   67.8% |   61.9% |   59.9% |   56.2% |   55.2%
    ripencc    | 38,611     |   76.8% |   77.9% |   76.7% |   66.0% |   76.2%

    [+] Full per-country trend data (IPv4 + IPv6) saved to roa_signing_trends.csv

    ====================================================================================================
     BIGGEST MOVERS — 3mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 3mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    TG   | Togo                 | afrinic  | 11     |  57.0% |  10.2% |  +46.8pp
    TJ   | Tajikistan           | ripencc  | 44     |  82.7% |  37.9% |  +44.8pp
    MX   | Mexico               | lacnic   | 662    |  78.1% |  45.0% |  +33.1pp
    KI   | Kiribati             | apnic    | 6      |  92.0% |  63.2% |  +28.8pp
    SK   | Slovakia             | ripencc  | 231    |  65.1% |  42.8% |  +22.3pp
    VG   | Virgin Islands, Brit | ripencc  | 49     |  78.4% |  58.4% |  +20.0pp
    SL   | Sierra Leone         | afrinic  | 22     |  77.6% |  58.6% |  +19.0pp
    CD   | Congo, The Democrati | afrinic  | 51     |  56.5% |  37.9% |  +18.6pp
    SO   | Somalia              | afrinic  | 22     |  82.9% |  65.5% |  +17.4pp
    KE   | Kenya                | afrinic  | 249    |  77.1% |  60.1% |  +17.0pp
    NG   | Nigeria              | afrinic  | 266    |  58.8% |  42.6% |  +16.2pp
    AU   | Australia            | apnic    | 3002   |  52.8% |  36.7% |  +16.1pp
    GQ   | Equatorial Guinea    | afrinic  | 7      |  59.5% |  45.7% |  +13.8pp
    YT   | Mayotte              | afrinic  | 1      |  75.9% |  63.2% |  +12.7pp
    MA   | Morocco              | afrinic  | 33     |  15.2% |   3.8% |  +11.4pp
    Decliners:
    MH   | Marshall Islands     | ripencc  | 11     |  41.7% |  91.7% |  -50.0pp
    BQ   | Bonaire, Sint Eustat | lacnic   | 6      |  80.4% |  97.2% |  -16.8pp
    IT   | Italy                | ripencc  | 1323   |  51.4% |  68.1% |  -16.7pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  75.0% |  83.8% |   -8.8pp
    VE   | Venezuela            | lacnic   | 261    |  89.9% |  95.2% |   -5.3pp
    CV   | Cabo Verde           | afrinic  | 8      |  35.4% |  40.6% |   -5.2pp
    SG   | Singapore            | apnic    | 727    |  76.7% |  81.1% |   -4.4pp
    SC   | Seychelles           | ripencc  | 87     |  82.4% |  85.9% |   -3.5pp
    VC   | Saint Vincent and th | arin     | 6      |  38.9% |  42.0% |   -3.1pp
    SD   | Sudan                | afrinic  | 11     |  39.1% |  41.6% |   -2.5pp
    PH   | Philippines          | apnic    | 674    |  88.5% |  90.9% |   -2.4pp
    MD   | Moldova              | ripencc  | 206    |  86.5% |  88.9% |   -2.4pp
    PE   | Peru                 | lacnic   | 226    |  35.7% |  38.1% |   -2.4pp
    QA   | Qatar                | ripencc  | 32     |  84.3% |  86.3% |   -2.0pp
    AI   | Anguilla             | arin     | 4      |   8.6% |  10.5% |   -1.9pp

    ====================================================================================================
     BIGGEST MOVERS — 6mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 6mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    DJ   | Djibouti             | afrinic  | 4      |  96.1% |   5.6% |  +90.5pp
    CN   | China                | apnic    | 6505   |  87.7% |   8.2% |  +79.5pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  75.0% |   5.9% |  +69.1pp
    CM   | Cameroon             | afrinic  | 30     |  94.5% |  36.0% |  +58.5pp
    TJ   | Tajikistan           | ripencc  | 44     |  82.7% |  37.3% |  +45.4pp
    JE   | Jersey               | ripencc  | 13     |  92.3% |  53.8% |  +38.5pp
    TT   | Trinidad and Tobago  | lacnic   | 16     |  91.8% |  54.6% |  +37.2pp
    MX   | Mexico               | lacnic   | 662    |  78.1% |  42.4% |  +35.7pp
    VG   | Virgin Islands, Brit | ripencc  | 49     |  78.4% |  45.1% |  +33.3pp
    KI   | Kiribati             | apnic    | 6      |  92.0% |  63.2% |  +28.8pp
    MT   | Malta                | ripencc  | 54     |  53.8% |  25.4% |  +28.4pp
    SO   | Somalia              | afrinic  | 22     |  82.9% |  59.9% |  +23.0pp
    SL   | Sierra Leone         | afrinic  | 22     |  77.6% |  55.2% |  +22.4pp
    GG   | Guernsey             | ripencc  | 11     |  70.6% |  49.3% |  +21.3pp
    SK   | Slovakia             | ripencc  | 231    |  65.1% |  45.0% |  +20.1pp
    Decliners:
    CV   | Cabo Verde           | afrinic  | 8      |  35.4% |  87.1% |  -51.7pp
    MH   | Marshall Islands     | ripencc  | 11     |  41.7% |  91.7% |  -50.0pp
    IT   | Italy                | ripencc  | 1323   |  51.4% |  67.2% |  -15.8pp
    SD   | Sudan                | afrinic  | 11     |  39.1% |  46.0% |   -6.9pp
    KY   | Cayman Islands       | arin     | 18     |  49.1% |  55.2% |   -6.1pp
    MP   | Northern Mariana Isl | apnic    | 2      |  94.3% | 100.0% |   -5.7pp
    MG   | Madagascar           | afrinic  | 7      |  40.2% |  45.5% |   -5.3pp
    KM   | Comoros              | afrinic  | 4      |  74.3% |  79.3% |   -5.0pp
    UZ   | Uzbekistan           | ripencc  | 130    |  72.7% |  77.5% |   -4.8pp
    TG   | Togo                 | afrinic  | 11     |  57.0% |  61.7% |   -4.7pp
    SC   | Seychelles           | ripencc  | 87     |  82.4% |  87.0% |   -4.6pp
    AE   | United Arab Emirates | ripencc  | 217    |  81.1% |  85.7% |   -4.6pp
    MD   | Moldova              | ripencc  | 206    |  86.5% |  90.8% |   -4.3pp
    MK   | North Macedonia      | ripencc  | 69     |  47.6% |  51.4% |   -3.8pp
    NE   | Niger                | afrinic  | 7      |  17.7% |  21.2% |   -3.5pp

    ====================================================================================================
     BIGGEST MOVERS — 12mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 12mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    DJ   | Djibouti             | afrinic  | 4      |  96.1% |   2.9% |  +93.2pp
    EG   | Egypt                | afrinic  | 86     |  95.5% |   7.5% |  +88.0pp
    CN   | China                | apnic    | 6505   |  87.7% |   3.9% |  +83.8pp
    PK   | Pakistan             | apnic    | 473    |  92.1% |  15.7% |  +76.4pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  75.0% |   3.1% |  +71.9pp
    BJ   | Benin                | afrinic  | 16     |  73.0% |   5.7% |  +67.3pp
    SO   | Somalia              | afrinic  | 22     |  82.9% |  19.1% |  +63.8pp
    CM   | Cameroon             | afrinic  | 30     |  94.5% |  31.7% |  +62.8pp
    HT   | Haiti                | lacnic   | 11     |  56.7% |   3.0% |  +53.7pp
    TJ   | Tajikistan           | ripencc  | 44     |  82.7% |  30.2% |  +52.5pp
    JE   | Jersey               | ripencc  | 13     |  92.3% |  42.4% |  +49.9pp
    KI   | Kiribati             | apnic    | 6      |  92.0% |  46.7% |  +45.3pp
    LS   | Lesotho              | afrinic  | 9      |  72.1% |  30.1% |  +42.0pp
    KZ   | Kazakhstan           | ripencc  | 269    |  80.2% |  39.9% |  +40.3pp
    TT   | Trinidad and Tobago  | lacnic   | 16     |  91.8% |  52.0% |  +39.8pp
    Decliners:
    CV   | Cabo Verde           | afrinic  | 8      |  35.4% |  85.5% |  -50.1pp
    MH   | Marshall Islands     | ripencc  | 11     |  41.7% |  75.0% |  -33.3pp
    IE   | Ireland              | ripencc  | 288    |  64.5% |  78.1% |  -13.6pp
    MG   | Madagascar           | afrinic  | 7      |  40.2% |  52.6% |  -12.4pp
    GT   | Guatemala            | lacnic   | 79     |  81.6% |  90.7% |   -9.1pp
    BF   | Burkina Faso         | afrinic  | 30     |  81.4% |  89.5% |   -8.1pp
    KY   | Cayman Islands       | arin     | 18     |  49.1% |  56.7% |   -7.6pp
    AO   | Angola               | afrinic  | 70     |  49.7% |  57.2% |   -7.5pp
    PY   | Paraguay             | lacnic   | 115    |  75.4% |  82.6% |   -7.2pp
    TG   | Togo                 | afrinic  | 11     |  57.0% |  64.1% |   -7.1pp
    KM   | Comoros              | afrinic  | 4      |  74.3% |  80.8% |   -6.5pp
    GL   | Greenland            | ripencc  | 1      |  77.1% |  83.3% |   -6.2pp
    MU   | Mauritius            | afrinic  | 41     |  80.0% |  85.7% |   -5.7pp
    MD   | Moldova              | ripencc  | 206    |  86.5% |  91.6% |   -5.1pp
    AE   | United Arab Emirates | ripencc  | 217    |  81.1% |  85.8% |   -4.7pp

    ====================================================================================================
     BIGGEST MOVERS — 24mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 24mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    DJ   | Djibouti             | afrinic  | 4      |  96.1% |   1.0% |  +95.1pp
    EG   | Egypt                | afrinic  | 86     |  95.5% |   7.7% |  +87.8pp
    CN   | China                | apnic    | 6505   |  87.7% |   3.0% |  +84.7pp
    CM   | Cameroon             | afrinic  | 30     |  94.5% |  13.6% |  +80.9pp
    FM   | Micronesia, Federate | apnic    | 6      |  85.0% |   4.8% |  +80.2pp
    PK   | Pakistan             | apnic    | 473    |  92.1% |  15.8% |  +76.3pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  75.0% |   0.0% |  +75.0pp
    IS   | Iceland              | ripencc  | 87     |  75.3% |   1.7% |  +73.6pp
    CI   | Côte d'Ivoire        | afrinic  | 26     |  94.5% |  21.4% |  +73.1pp
    SO   | Somalia              | afrinic  | 22     |  82.9% |  13.0% |  +69.9pp
    BJ   | Benin                | afrinic  | 16     |  73.0% |   3.4% |  +69.6pp
    JE   | Jersey               | ripencc  | 13     |  92.3% |  25.0% |  +67.3pp
    TJ   | Tajikistan           | ripencc  | 44     |  82.7% |  24.1% |  +58.6pp
    ML   | Mali                 | afrinic  | 8      |  83.3% |  25.3% |  +58.0pp
    HT   | Haiti                | lacnic   | 11     |  56.7% |   1.9% |  +54.8pp
    Decliners:
    CV   | Cabo Verde           | afrinic  | 8      |  35.4% |  83.0% |  -47.6pp
    MH   | Marshall Islands     | ripencc  | 11     |  41.7% |  82.4% |  -40.7pp
    PE   | Peru                 | lacnic   | 226    |  35.7% |  59.2% |  -23.5pp
    SD   | Sudan                | afrinic  | 11     |  39.1% |  61.0% |  -21.9pp
    KM   | Comoros              | afrinic  | 4      |  74.3% |  90.5% |  -16.2pp
    IE   | Ireland              | ripencc  | 288    |  64.5% |  75.3% |  -10.8pp
    AE   | United Arab Emirates | ripencc  | 217    |  81.1% |  88.4% |   -7.3pp
    AO   | Angola               | afrinic  | 70     |  49.7% |  56.6% |   -6.9pp
    ZM   | Zambia               | afrinic  | 21     |  49.2% |  54.9% |   -5.7pp
    ME   | Montenegro           | ripencc  | 31     |  48.8% |  54.4% |   -5.6pp
    CG   | Congo                | afrinic  | 13     |  16.3% |  21.4% |   -5.1pp
    MF   | Saint Martin (French | arin     | 6      |  40.0% |  45.0% |   -5.0pp
    BF   | Burkina Faso         | afrinic  | 30     |  81.4% |  86.2% |   -4.8pp
    TZ   | Tanzania             | afrinic  | 116    |  33.6% |  38.0% |   -4.4pp
    MD   | Moldova              | ripencc  | 206    |  86.5% |  90.8% |   -4.3pp

    ====================================================================================================
     BIGGEST MOVERS — 3mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 3mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    TJ   | Tajikistan           | ripencc  | 44     |  91.7% |  52.0% |  +39.7pp
    TH   | Thailand             | apnic    | 621    |  89.9% |  59.2% |  +30.7pp
    CL   | Chile                | lacnic   | 402    |  92.7% |  64.5% |  +28.2pp
    MX   | Mexico               | lacnic   | 662    |  82.6% |  60.3% |  +22.3pp
    SD   | Sudan                | afrinic  | 11     |  80.0% |  63.6% |  +16.4pp
    AZ   | Azerbaijan           | ripencc  | 121    |  89.0% |  72.7% |  +16.3pp
    AO   | Angola               | afrinic  | 70     |  91.2% |  77.1% |  +14.1pp
    PH   | Philippines          | apnic    | 674    |  84.0% |  72.2% |  +11.8pp
    LK   | Sri Lanka            | apnic    | 32     |  91.0% |  81.1% |   +9.9pp
    SC   | Seychelles           | ripencc  | 87     |  75.7% |  66.5% |   +9.2pp
    MM   | Myanmar              | apnic    | 172    |  99.4% |  90.7% |   +8.7pp
    MZ   | Mozambique           | afrinic  | 31     |  47.8% |  39.3% |   +8.5pp
    MY   | Malaysia             | apnic    | 406    |  54.3% |  46.1% |   +8.2pp
    LT   | Lithuania            | ripencc  | 219    |  90.8% |  83.5% |   +7.3pp
    CZ   | Czechia              | ripencc  | 717    |  83.0% |  76.0% |   +7.0pp
    Decliners:
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  33.3% |  -25.6pp
    AL   | Albania              | ripencc  | 132    |  74.2% |  95.7% |  -21.5pp
    PR   | Puerto Rico          | arin     | 124    |  30.1% |  47.0% |  -16.9pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  91.4% |  -14.1pp
    ES   | Spain                | ripencc  | 1173   |  79.8% |  92.9% |  -13.1pp
    VI   | Virgin Islands, U.S. | arin     | 12     |  48.6% |  60.7% |  -12.1pp
    AM   | Armenia              | ripencc  | 155    |  85.2% |  94.1% |   -8.9pp
    PT   | Portugal             | ripencc  | 167    |  86.6% |  93.6% |   -7.0pp
    LV   | Latvia               | ripencc  | 319    |  81.5% |  87.3% |   -5.8pp
    GE   | Georgia              | ripencc  | 175    |  85.7% |  91.2% |   -5.5pp
    KG   | Kyrgyzstan           | ripencc  | 71     |  86.4% |  91.3% |   -4.9pp
    BB   | Barbados             | arin     | 10     |  13.6% |  18.2% |   -4.6pp
    RO   | Romania              | ripencc  | 1086   |  64.9% |  69.5% |   -4.6pp
    PY   | Paraguay             | lacnic   | 115    |  54.3% |  58.8% |   -4.5pp
    LU   | Luxembourg           | ripencc  | 134    |  77.2% |  81.7% |   -4.5pp

    ====================================================================================================
     BIGGEST MOVERS — 6mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 6mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    CN   | China                | apnic    | 6505   |  97.0% |  22.0% |  +75.0pp
    TJ   | Tajikistan           | ripencc  | 44     |  91.7% |  50.0% |  +41.7pp
    RO   | Romania              | ripencc  | 1086   |  64.9% |  25.3% |  +39.6pp
    TH   | Thailand             | apnic    | 621    |  89.9% |  58.4% |  +31.5pp
    CL   | Chile                | lacnic   | 402    |  92.7% |  65.4% |  +27.3pp
    MX   | Mexico               | lacnic   | 662    |  82.6% |  57.0% |  +25.6pp
    SD   | Sudan                | afrinic  | 11     |  80.0% |  55.6% |  +24.4pp
    MA   | Morocco              | afrinic  | 33     |  45.1% |  21.6% |  +23.5pp
    PH   | Philippines          | apnic    | 674    |  84.0% |  62.9% |  +21.1pp
    BD   | Bangladesh           | apnic    | 2031   |  84.4% |  65.6% |  +18.8pp
    AZ   | Azerbaijan           | ripencc  | 121    |  89.0% |  73.4% |  +15.6pp
    UG   | Uganda               | afrinic  | 59     |  90.0% |  74.5% |  +15.5pp
    AO   | Angola               | afrinic  | 70     |  91.2% |  75.8% |  +15.4pp
    MZ   | Mozambique           | afrinic  | 31     |  47.8% |  34.6% |  +13.2pp
    ZM   | Zambia               | afrinic  | 21     | 100.0% |  90.0% |  +10.0pp
    Decliners:
    AE   | United Arab Emirates | ripencc  | 217    |  49.9% |  95.3% |  -45.4pp
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  33.3% |  -25.6pp
    AL   | Albania              | ripencc  | 132    |  74.2% |  97.3% |  -23.1pp
    VI   | Virgin Islands, U.S. | arin     | 12     |  48.6% |  65.2% |  -16.6pp
    PR   | Puerto Rico          | arin     | 124    |  30.1% |  46.1% |  -16.0pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  92.6% |  -15.3pp
    MO   | Macao                | apnic    | 15     |  64.3% |  76.8% |  -12.5pp
    PS   | Palestine, State of  | ripencc  | 69     |  86.4% |  95.2% |   -8.8pp
    SA   | Saudi Arabia         | ripencc  | 201    |  83.6% |  91.6% |   -8.0pp
    LI   | Liechtenstein        | ripencc  | 29     |  77.8% |  85.8% |   -8.0pp
    PK   | Pakistan             | apnic    | 473    |  90.3% |  97.0% |   -6.7pp
    ES   | Spain                | ripencc  | 1173   |  79.8% |  85.6% |   -5.8pp
    PT   | Portugal             | ripencc  | 167    |  86.6% |  92.3% |   -5.7pp
    UY   | Uruguay              | lacnic   | 45     |  45.2% |  50.8% |   -5.6pp
    LV   | Latvia               | ripencc  | 319    |  81.5% |  86.2% |   -4.7pp

    ====================================================================================================
     BIGGEST MOVERS — 12mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 12mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    CN   | China                | apnic    | 6505   |  97.0% |   2.1% |  +94.9pp
    CH   | Switzerland          | ripencc  | 1066   |  81.8% |  15.7% |  +66.1pp
    SO   | Somalia              | afrinic  | 22     |  85.2% |  21.4% |  +63.8pp
    TJ   | Tajikistan           | ripencc  | 44     |  91.7% |  39.1% |  +52.6pp
    SD   | Sudan                | afrinic  | 11     |  80.0% |  33.3% |  +46.7pp
    JM   | Jamaica              | arin     | 15     |  66.7% |  30.6% |  +36.1pp
    MA   | Morocco              | afrinic  | 33     |  45.1% |  17.8% |  +27.3pp
    CL   | Chile                | lacnic   | 402    |  92.7% |  65.5% |  +27.2pp
    MX   | Mexico               | lacnic   | 662    |  82.6% |  59.3% |  +23.3pp
    PH   | Philippines          | apnic    | 674    |  84.0% |  64.2% |  +19.8pp
    DE   | Germany              | ripencc  | 3274   |  81.1% |  62.0% |  +19.1pp
    AZ   | Azerbaijan           | ripencc  | 121    |  89.0% |  70.8% |  +18.2pp
    CA   | Canada               | arin     | 2537   |  74.8% |  56.7% |  +18.1pp
    AO   | Angola               | afrinic  | 70     |  91.2% |  75.0% |  +16.2pp
    NI   | Nicaragua            | lacnic   | 30     |  98.7% |  82.8% |  +15.9pp
    Decliners:
    KE   | Kenya                | afrinic  | 249    |  32.3% |  76.7% |  -44.4pp
    AE   | United Arab Emirates | ripencc  | 217    |  49.9% |  90.9% |  -41.0pp
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  42.9% |  -35.2pp
    RO   | Romania              | ripencc  | 1086   |  64.9% |  94.6% |  -29.7pp
    BT   | Bhutan               | apnic    | 43     |  73.0% | 100.0% |  -27.0pp
    AL   | Albania              | ripencc  | 132    |  74.2% |  98.3% |  -24.1pp
    ZW   | Zimbabwe             | afrinic  | 29     |  13.8% |  36.8% |  -23.0pp
    VI   | Virgin Islands, U.S. | arin     | 12     |  48.6% |  67.9% |  -19.3pp
    IE   | Ireland              | ripencc  | 288    |  72.5% |  88.5% |  -16.0pp
    ZA   | South Africa         | afrinic  | 751    |  35.6% |  50.3% |  -14.7pp
    SA   | Saudi Arabia         | ripencc  | 201    |  83.6% |  98.3% |  -14.7pp
    PR   | Puerto Rico          | arin     | 124    |  30.1% |  43.3% |  -13.2pp
    SC   | Seychelles           | ripencc  | 87     |  75.7% |  88.6% |  -12.9pp
    MO   | Macao                | apnic    | 15     |  64.3% |  76.7% |  -12.4pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  89.1% |  -11.8pp

    ====================================================================================================
     BIGGEST MOVERS — 24mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 24mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    CN   | China                | apnic    | 6505   |  97.0% |   1.6% |  +95.4pp
    IS   | Iceland              | ripencc  | 87     |  91.4% |  24.4% |  +67.0pp
    JP   | Japan                | apnic    | 984    |  82.1% |  17.8% |  +64.3pp
    SD   | Sudan                | afrinic  | 11     |  80.0% |  20.0% |  +60.0pp
    JM   | Jamaica              | arin     | 15     |  66.7% |  10.7% |  +56.0pp
    GH   | Ghana                | afrinic  | 104    |  91.0% |  36.5% |  +54.5pp
    MC   | Monaco               | ripencc  | 5      |  90.9% |  50.0% |  +40.9pp
    UZ   | Uzbekistan           | ripencc  | 130    |  84.7% |  44.4% |  +40.3pp
    AZ   | Azerbaijan           | ripencc  | 121    |  89.0% |  50.0% |  +39.0pp
    TJ   | Tajikistan           | ripencc  | 44     |  91.7% |  53.3% |  +38.4pp
    BM   | Bermuda              | arin     | 23     |  79.2% |  41.7% |  +37.5pp
    SO   | Somalia              | afrinic  | 22     |  85.2% |  50.0% |  +35.2pp
    CL   | Chile                | lacnic   | 402    |  92.7% |  58.2% |  +34.5pp
    SC   | Seychelles           | ripencc  | 87     |  75.7% |  42.0% |  +33.7pp
    TT   | Trinidad and Tobago  | lacnic   | 16     |  64.0% |  31.2% |  +32.8pp
    Decliners:
    CD   | Congo, The Democrati | afrinic  | 51     |  27.0% |  82.1% |  -55.1pp
    KE   | Kenya                | afrinic  | 249    |  32.3% |  82.8% |  -50.5pp
    ZW   | Zimbabwe             | afrinic  | 29     |  13.8% |  62.5% |  -48.7pp
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  50.0% |  -42.3pp
    AE   | United Arab Emirates | ripencc  | 217    |  49.9% |  90.3% |  -40.4pp
    VI   | Virgin Islands, U.S. | arin     | 12     |  48.6% |  85.7% |  -37.1pp
    MU   | Mauritius            | afrinic  | 41     |   2.4% |  36.8% |  -34.4pp
    MA   | Morocco              | afrinic  | 33     |  45.1% |  75.3% |  -30.2pp
    MO   | Macao                | apnic    | 15     |  64.3% |  92.9% |  -28.6pp
    BT   | Bhutan               | apnic    | 43     |  73.0% |  98.6% |  -25.6pp
    ZA   | South Africa         | afrinic  | 751    |  35.6% |  61.0% |  -25.4pp
    MZ   | Mozambique           | afrinic  | 31     |  47.8% |  71.4% |  -23.6pp
    AL   | Albania              | ripencc  | 132    |  74.2% |  97.5% |  -23.3pp
    PR   | Puerto Rico          | arin     | 124    |  30.1% |  53.1% |  -23.0pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  92.9% |  -15.6pp

    ====================================================================================================
     SPOTLIGHT: CHINA (CN)
    ====================================================================================================
    ASNs: 6505  |  RIR: apnic
    IPv4:
      Now  : 87.7% of IPv4 route objects covered by a valid ROA
      3mo  : 88.4% of IPv4 route objects covered by a valid ROA
      6mo  : 8.2% of IPv4 route objects covered by a valid ROA
      12mo : 3.9% of IPv4 route objects covered by a valid ROA
      24mo : 3.0% of IPv4 route objects covered by a valid ROA
    IPv6:
      Now  : 97.0% of IPv6 route objects covered by a valid ROA
      3mo  : 96.1% of IPv6 route objects covered by a valid ROA
      6mo  : 22.0% of IPv6 route objects covered by a valid ROA
      12mo : 2.1% of IPv6 route objects covered by a valid ROA
      24mo : 1.6% of IPv6 route objects covered by a valid ROA
