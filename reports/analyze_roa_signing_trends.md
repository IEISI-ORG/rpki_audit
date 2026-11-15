    [*] Fetching APNIC Labs ROA-coverage snapshots...
        - Now   (reported date 14/11/2026): 278 countries/regions
        - 3mo   (reported date 15/08/2026): 278 countries/regions
        - 6mo   (reported date 15/05/2026): 279 countries/regions
        - 12mo  (reported date 15/11/2025): 279 countries/regions
        - 24mo  (reported date 15/11/2024): 278 countries/regions

    ====================================================================================================
     GLOBAL ROA COVERAGE TREND (IPv4 Route Objects, % Valid)
    ====================================================================================================
    Period   | Reported Date  | % Valid  | Total Route Objects
    ------------------------------------------------------------
    Now      | 14/11/2026     |   70.7% |  1,068,185
    3mo      | 15/08/2026     |   67.3% |  1,255,983
    6mo      | 15/05/2026     |   60.1% |  1,267,221
    12mo     | 15/11/2025     |   58.4% |  1,035,870
    24mo     | 15/11/2024     |   51.3% |    296,369

    ====================================================================================================
     GLOBAL ROA COVERAGE TREND (IPv6 Route Objects, % Valid)
    ====================================================================================================
    Period   | Reported Date  | % Valid  | Total Route Objects
    ------------------------------------------------------------
    Now      | 14/11/2026     |   76.9% |    323,308
    3mo      | 15/08/2026     |   74.8% |    309,440
    6mo      | 15/05/2026     |   67.4% |    306,805
    12mo     | 15/11/2025     |   58.7% |    299,170
    24mo     | 15/11/2024     |   55.3% |    259,999

    NOTE: IPv4 and IPv6 are reported separately because they are measured
    separately by APNIC and can diverge significantly per network — do not
    average or add them into one 'global ROA coverage' number.

    ====================================================================================================
     RIR ROA COVERAGE TREND (IPv4 Route Objects, % Valid, weighted by route-object count)
    ====================================================================================================
    RIR        | ASNs (now) |     Now |     3mo |     6mo |    12mo |    24mo
    -------------------------------------------------------------------------
    afrinic    | 2,474      |   67.5% |   63.2% |   61.9% |   38.2% |   29.1%
    apnic      | 31,481     |   80.4% |   76.1% |   57.0% |   57.6% |   53.8%
    arin       | 35,650     |   56.6% |   52.3% |   49.2% |   49.4% |   42.2%
    lacnic     | 13,870     |   69.2% |   67.5% |   60.4% |   59.9% |   41.0%
    ripencc    | 38,558     |   77.0% |   74.2% |   73.8% |   69.1% |   64.0%

    ====================================================================================================
     RIR ROA COVERAGE TREND (IPv6 Route Objects, % Valid, weighted by route-object count)
    ====================================================================================================
    RIR        | ASNs (now) |     Now |     3mo |     6mo |    12mo |    24mo
    -------------------------------------------------------------------------
    afrinic    | 2,474      |   42.6% |   39.7% |   40.1% |   35.7% |   60.3%
    apnic      | 31,481     |   84.0% |   82.4% |   63.9% |   49.8% |   40.2%
    arin       | 35,650     |   77.3% |   76.4% |   76.4% |   69.6% |   61.5%
    lacnic     | 13,870     |   67.8% |   62.7% |   60.3% |   57.3% |   54.3%
    ripencc    | 38,558     |   79.7% |   78.4% |   77.0% |   66.7% |   76.2%

    [+] Full per-country trend data (IPv4 + IPv6) saved to roa_signing_trends.csv

    ====================================================================================================
     BIGGEST MOVERS — 3mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 3mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    BS   | Bahamas              | arin     | 13     |  81.7% |  26.2% |  +55.5pp
    MG   | Madagascar           | afrinic  | 7      |  90.7% |  46.0% |  +44.7pp
    VG   | Virgin Islands, Brit | ripencc  | 51     |  92.4% |  48.2% |  +44.2pp
    TJ   | Tajikistan           | ripencc  | 44     |  84.3% |  40.1% |  +44.2pp
    MZ   | Mozambique           | afrinic  | 31     |  49.3% |  15.3% |  +34.0pp
    AS   | American Samoa       | apnic    | 2      |  47.8% |  18.7% |  +29.1pp
    SK   | Slovakia             | ripencc  | 228    |  65.2% |  43.2% |  +22.0pp
    CD   | Congo, The Democrati | afrinic  | 51     |  59.1% |  37.5% |  +21.6pp
    TG   | Togo                 | afrinic  | 11     |  31.0% |  10.2% |  +20.8pp
    GN   | Guinea               | afrinic  | 16     |  40.4% |  20.0% |  +20.4pp
    RW   | Rwanda               | afrinic  | 28     |  72.6% |  53.6% |  +19.0pp
    VI   | Virgin Islands, U.S. | arin     | 12     |  61.7% |  43.3% |  +18.4pp
    KE   | Kenya                | afrinic  | 250    |  77.3% |  59.7% |  +17.6pp
    YE   | Yemen                | ripencc  | 6      |  91.4% |  75.0% |  +16.4pp
    AU   | Australia            | apnic    | 2997   |  62.5% |  47.2% |  +15.3pp
    Decliners:
    MH   | Marshall Islands     | ripencc  | 10     |  22.5% |  91.3% |  -68.8pp
    SD   | Sudan                | afrinic  | 11     |  11.6% |  42.9% |  -31.3pp
    KM   | Comoros              | afrinic  | 4      |  54.5% |  74.3% |  -19.8pp
    WS   | Samoa                | apnic    | 10     |  72.0% |  88.1% |  -16.1pp
    VC   | Saint Vincent and th | arin     | 6      |  29.0% |  42.0% |  -13.0pp
    ME   | Montenegro           | ripencc  | 30     |  41.0% |  50.8% |   -9.8pp
    MP   | Northern Mariana Isl | apnic    | 2      |  85.0% |  94.2% |   -9.2pp
    BQ   | Bonaire, Sint Eustat | lacnic   | 6      |  88.6% |  97.2% |   -8.6pp
    FO   | Faroe Islands        | ripencc  | 6      |  42.9% |  50.0% |   -7.1pp
    ZW   | Zimbabwe             | afrinic  | 27     |  43.6% |  50.0% |   -6.4pp
    DJ   | Djibouti             | afrinic  | 4      |  90.9% |  97.2% |   -6.3pp
    BN   | Brunei Darussalam    | apnic    | 11     |  76.9% |  82.9% |   -6.0pp
    BI   | Burundi              | afrinic  | 8      |   5.1% |  11.0% |   -5.9pp
    VE   | Venezuela            | lacnic   | 264    |  89.4% |  95.0% |   -5.6pp
    PE   | Peru                 | lacnic   | 227    |  31.5% |  37.0% |   -5.5pp

    ====================================================================================================
     BIGGEST MOVERS — 6mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 6mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    DJ   | Djibouti             | afrinic  | 4      |  90.9% |   5.6% |  +85.3pp
    CN   | China                | apnic    | 6493   |  90.9% |  12.7% |  +78.2pp
    BS   | Bahamas              | arin     | 13     |  81.7% |  27.5% |  +54.2pp
    VG   | Virgin Islands, Brit | ripencc  | 51     |  92.4% |  43.1% |  +49.3pp
    TJ   | Tajikistan           | ripencc  | 44     |  84.3% |  37.4% |  +46.9pp
    MG   | Madagascar           | afrinic  | 7      |  90.7% |  46.2% |  +44.5pp
    TT   | Trinidad and Tobago  | lacnic   | 16     |  92.8% |  54.6% |  +38.2pp
    JE   | Jersey               | ripencc  | 13     |  91.1% |  54.6% |  +36.5pp
    MZ   | Mozambique           | afrinic  | 31     |  49.3% |  15.3% |  +34.0pp
    MX   | Mexico               | lacnic   | 668    |  75.2% |  42.6% |  +32.6pp
    MT   | Malta                | ripencc  | 52     |  54.3% |  25.1% |  +29.2pp
    AS   | American Samoa       | apnic    | 2      |  47.8% |  19.7% |  +28.1pp
    AU   | Australia            | apnic    | 2997   |  62.5% |  35.4% |  +27.1pp
    VI   | Virgin Islands, U.S. | arin     | 12     |  61.7% |  35.1% |  +26.6pp
    GN   | Guinea               | afrinic  | 16     |  40.4% |  16.1% |  +24.3pp
    Decliners:
    MH   | Marshall Islands     | ripencc  | 10     |  22.5% |  92.3% |  -69.8pp
    CV   | Cabo Verde           | afrinic  | 8      |  39.7% |  87.1% |  -47.4pp
    SD   | Sudan                | afrinic  | 11     |  11.6% |  46.2% |  -34.6pp
    TG   | Togo                 | afrinic  | 11     |  31.0% |  63.6% |  -32.6pp
    KM   | Comoros              | afrinic  | 4      |  54.5% |  78.6% |  -24.1pp
    IT   | Italy                | ripencc  | 1319   |  49.5% |  67.5% |  -18.0pp
    WS   | Samoa                | apnic    | 10     |  72.0% |  88.1% |  -16.1pp
    MP   | Northern Mariana Isl | apnic    | 2      |  85.0% | 100.0% |  -15.0pp
    GT   | Guatemala            | lacnic   | 79     |  79.4% |  90.1% |  -10.7pp
    PY   | Paraguay             | lacnic   | 116    |  74.4% |  83.6% |   -9.2pp
    ME   | Montenegro           | ripencc  | 30     |  41.0% |  49.8% |   -8.8pp
    BI   | Burundi              | afrinic  | 8      |   5.1% |  13.8% |   -8.7pp
    YT   | Mayotte              | afrinic  | 1      |  68.2% |  76.7% |   -8.5pp
    MK   | North Macedonia      | ripencc  | 69     |  44.4% |  51.7% |   -7.3pp
    VC   | Saint Vincent and th | arin     | 6      |  29.0% |  36.2% |   -7.2pp

    ====================================================================================================
     BIGGEST MOVERS — 12mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 12mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    DJ   | Djibouti             | afrinic  | 4      |  90.9% |   2.9% |  +88.0pp
    CN   | China                | apnic    | 6493   |  90.9% |   3.9% |  +87.0pp
    EG   | Egypt                | afrinic  | 86     |  96.2% |   9.6% |  +86.6pp
    BJ   | Benin                | afrinic  | 16     |  75.1% |   5.7% |  +69.4pp
    BS   | Bahamas              | arin     | 13     |  81.7% |  18.4% |  +63.3pp
    CM   | Cameroon             | afrinic  | 30     |  94.6% |  31.8% |  +62.8pp
    HT   | Haiti                | lacnic   | 11     |  66.3% |   4.8% |  +61.5pp
    SO   | Somalia              | afrinic  | 22     |  79.9% |  18.4% |  +61.5pp
    TJ   | Tajikistan           | ripencc  | 44     |  84.3% |  34.6% |  +49.7pp
    LS   | Lesotho              | afrinic  | 9      |  75.5% |  30.1% |  +45.4pp
    VG   | Virgin Islands, Brit | ripencc  | 51     |  92.4% |  49.1% |  +43.3pp
    JE   | Jersey               | ripencc  | 13     |  91.1% |  49.2% |  +41.9pp
    TT   | Trinidad and Tobago  | lacnic   | 16     |  92.8% |  52.6% |  +40.2pp
    MG   | Madagascar           | afrinic  | 7      |  90.7% |  52.5% |  +38.2pp
    MX   | Mexico               | lacnic   | 668    |  75.2% |  39.6% |  +35.6pp
    Decliners:
    CV   | Cabo Verde           | afrinic  | 8      |  39.7% |  90.4% |  -50.7pp
    MH   | Marshall Islands     | ripencc  | 10     |  22.5% |  66.7% |  -44.2pp
    TG   | Togo                 | afrinic  | 11     |  31.0% |  63.8% |  -32.8pp
    KM   | Comoros              | afrinic  | 4      |  54.5% |  80.0% |  -25.5pp
    SD   | Sudan                | afrinic  | 11     |  11.6% |  31.4% |  -19.8pp
    MP   | Northern Mariana Isl | apnic    | 2      |  85.0% | 100.0% |  -15.0pp
    GT   | Guatemala            | lacnic   | 79     |  79.4% |  91.4% |  -12.0pp
    AO   | Angola               | afrinic  | 70     |  51.3% |  60.8% |   -9.5pp
    GM   | Gambia               | afrinic  | 11     |  46.7% |  56.1% |   -9.4pp
    IE   | Ireland              | ripencc  | 287    |  69.9% |  79.1% |   -9.2pp
    KY   | Cayman Islands       | arin     | 18     |  49.4% |  58.5% |   -9.1pp
    PY   | Paraguay             | lacnic   | 116    |  74.4% |  83.2% |   -8.8pp
    MD   | Moldova              | ripencc  | 206    |  85.2% |  93.1% |   -7.9pp
    GL   | Greenland            | ripencc  | 1      |  75.8% |  83.3% |   -7.5pp
    UZ   | Uzbekistan           | ripencc  | 132    |  71.3% |  77.2% |   -5.9pp

    ====================================================================================================
     BIGGEST MOVERS — 24mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 24mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    GY   | Guyana               | lacnic   | 6      |  98.9% |   0.0% |  +98.9pp
    ET   | Ethiopia             | afrinic  | 8      |  97.8% |   0.0% |  +97.8pp
    EG   | Egypt                | afrinic  | 86     |  96.2% |   1.8% |  +94.4pp
    DJ   | Djibouti             | afrinic  | 4      |  90.9% |   0.0% |  +90.9pp
    TM   | Turkmenistan         | ripencc  | 9      |  89.7% |   0.0% |  +89.7pp
    BQ   | Bonaire, Sint Eustat | lacnic   | 6      |  88.6% |   0.0% |  +88.6pp
    CN   | China                | apnic    | 6493   |  90.9% |   3.8% |  +87.1pp
    SX   | Sint Maarten (Dutch  | lacnic   | 3      |  76.9% |   0.0% |  +76.9pp
    IS   | Iceland              | ripencc  | 87     |  78.9% |   2.6% |  +76.3pp
    BS   | Bahamas              | arin     | 13     |  81.7% |   5.9% |  +75.8pp
    CI   | Côte d'Ivoire        | afrinic  | 26     |  94.6% |  19.0% |  +75.6pp
    BJ   | Benin                | afrinic  | 16     |  75.1% |   1.1% |  +74.0pp
    MG   | Madagascar           | afrinic  | 7      |  90.7% |  18.5% |  +72.2pp
    DO   | Dominican Republic   | lacnic   | 218    |  81.2% |  14.9% |  +66.3pp
    VE   | Venezuela            | lacnic   | 264    |  89.4% |  25.3% |  +64.1pp
    Decliners:
    CV   | Cabo Verde           | afrinic  | 8      |  39.7% |  90.9% |  -51.2pp
    TD   | Chad                 | afrinic  | 16     |  50.7% | 100.0% |  -49.3pp
    GM   | Gambia               | afrinic  | 11     |  46.7% |  83.3% |  -36.6pp
    PF   | French Polynesia     | apnic    | 6      |  21.6% |  53.8% |  -32.2pp
    MC   | Monaco               | ripencc  | 5      |  55.3% |  83.3% |  -28.0pp
    CG   | Congo                | afrinic  | 13     |  23.2% |  50.0% |  -26.8pp
    SD   | Sudan                | afrinic  | 11     |  11.6% |  32.4% |  -20.8pp
    PG   | Papua New Guinea     | apnic    | 42     |  59.1% |  79.4% |  -20.3pp
    NI   | Nicaragua            | lacnic   | 30     |  76.9% |  92.9% |  -16.0pp
    MP   | Northern Mariana Isl | apnic    | 2      |  85.0% | 100.0% |  -15.0pp
    IE   | Ireland              | ripencc  | 287    |  69.9% |  84.6% |  -14.7pp
    JO   | Jordan               | ripencc  | 58     |  61.3% |  75.4% |  -14.1pp
    LU   | Luxembourg           | ripencc  | 131    |  55.1% |  67.2% |  -12.1pp
    AO   | Angola               | afrinic  | 70     |  51.3% |  62.7% |  -11.4pp
    PY   | Paraguay             | lacnic   | 116    |  74.4% |  85.4% |  -11.0pp

    ====================================================================================================
     BIGGEST MOVERS — 3mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 3mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    BS   | Bahamas              | arin     | 13     | 100.0% |   6.5% |  +93.5pp
    AE   | United Arab Emirates | ripencc  | 219    |  94.4% |  49.8% |  +44.6pp
    TJ   | Tajikistan           | ripencc  | 44     |  95.8% |  55.6% |  +40.2pp
    TH   | Thailand             | apnic    | 621    |  92.2% |  58.8% |  +33.4pp
    CL   | Chile                | lacnic   | 404    |  93.1% |  64.5% |  +28.6pp
    AZ   | Azerbaijan           | ripencc  | 122    |  89.0% |  70.8% |  +18.2pp
    MX   | Mexico               | lacnic   | 668    |  80.2% |  63.4% |  +16.8pp
    PH   | Philippines          | apnic    | 677    |  85.1% |  72.5% |  +12.6pp
    MZ   | Mozambique           | afrinic  | 31     |  47.8% |  35.7% |  +12.1pp
    KH   | Cambodia             | apnic    | 143    |  96.4% |  84.6% |  +11.8pp
    RO   | Romania              | ripencc  | 1083   |  82.7% |  71.2% |  +11.5pp
    VI   | Virgin Islands, U.S. | arin     | 12     |  73.7% |  64.0% |   +9.7pp
    SA   | Saudi Arabia         | ripencc  | 201    |  94.8% |  85.7% |   +9.1pp
    MY   | Malaysia             | apnic    | 406    |  55.0% |  46.2% |   +8.8pp
    PS   | Palestine, State of  | ripencc  | 69     |  95.2% |  86.4% |   +8.8pp
    Decliners:
    OM   | Oman                 | ripencc  | 26     |  56.0% |  90.3% |  -34.3pp
    MT   | Malta                | ripencc  | 52     |  44.8% |  77.1% |  -32.3pp
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  33.3% |  -25.6pp
    AL   | Albania              | ripencc  | 133    |  74.6% |  96.1% |  -21.5pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  94.4% |  -17.1pp
    VG   | Virgin Islands, Brit | ripencc  | 51     |  75.0% |  88.7% |  -13.7pp
    KZ   | Kazakhstan           | ripencc  | 273    |  38.8% |  52.2% |  -13.4pp
    MC   | Monaco               | ripencc  | 5      |  87.5% | 100.0% |  -12.5pp
    AM   | Armenia              | ripencc  | 158    |  86.2% |  95.0% |   -8.8pp
    CM   | Cameroon             | afrinic  | 30     |  92.3% | 100.0% |   -7.7pp
    PT   | Portugal             | ripencc  | 166    |  88.0% |  94.0% |   -6.0pp
    GE   | Georgia              | ripencc  | 176    |  85.2% |  90.8% |   -5.6pp
    IL   | Israel               | ripencc  | 385    |  70.0% |  75.5% |   -5.5pp
    MW   | Malawi               | afrinic  | 30     |  79.4% |  84.8% |   -5.4pp
    DK   | Denmark              | ripencc  | 468    |  70.7% |  75.7% |   -5.0pp

    ====================================================================================================
     BIGGEST MOVERS — 6mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 6mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    BS   | Bahamas              | arin     | 13     | 100.0% |   6.2% |  +93.8pp
    RO   | Romania              | ripencc  | 1083   |  82.7% |  25.0% |  +57.7pp
    CN   | China                | apnic    | 6493   |  96.9% |  50.9% |  +46.0pp
    TJ   | Tajikistan           | ripencc  | 44     |  95.8% |  50.0% |  +45.8pp
    TH   | Thailand             | apnic    | 621    |  92.2% |  58.8% |  +33.4pp
    CL   | Chile                | lacnic   | 404    |  93.1% |  65.3% |  +27.8pp
    MA   | Morocco              | afrinic  | 33     |  46.8% |  21.6% |  +25.2pp
    SD   | Sudan                | afrinic  | 11     |  80.0% |  55.6% |  +24.4pp
    MX   | Mexico               | lacnic   | 668    |  80.2% |  57.0% |  +23.2pp
    BD   | Bangladesh           | apnic    | 2034   |  86.2% |  65.3% |  +20.9pp
    PH   | Philippines          | apnic    | 677    |  85.1% |  67.8% |  +17.3pp
    AZ   | Azerbaijan           | ripencc  | 122    |  89.0% |  73.4% |  +15.6pp
    UG   | Uganda               | afrinic  | 59     |  90.0% |  75.3% |  +14.7pp
    KH   | Cambodia             | apnic    | 143    |  96.4% |  83.9% |  +12.5pp
    AO   | Angola               | afrinic  | 70     |  88.6% |  76.5% |  +12.1pp
    Decliners:
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  33.3% |  -25.6pp
    AL   | Albania              | ripencc  | 133    |  74.6% |  97.3% |  -22.7pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  92.9% |  -15.6pp
    PR   | Puerto Rico          | arin     | 124    |  30.2% |  45.7% |  -15.5pp
    FJ   | Fiji                 | apnic    | 20     |  87.0% | 100.0% |  -13.0pp
    SC   | Seychelles           | ripencc  | 87     |  82.7% |  93.9% |  -11.2pp
    MO   | Macao                | apnic    | 15     |  65.8% |  75.6% |   -9.8pp
    AM   | Armenia              | ripencc  | 158    |  86.2% |  93.4% |   -7.2pp
    UZ   | Uzbekistan           | ripencc  | 132    |  82.0% |  88.9% |   -6.9pp
    ES   | Spain                | ripencc  | 1169   |  79.6% |  85.8% |   -6.2pp
    LI   | Liechtenstein        | ripencc  | 28     |  79.6% |  84.9% |   -5.3pp
    UY   | Uruguay              | lacnic   | 45     |  44.5% |  49.6% |   -5.1pp
    PT   | Portugal             | ripencc  | 166    |  88.0% |  92.8% |   -4.8pp
    IL   | Israel               | ripencc  | 385    |  70.0% |  74.8% |   -4.8pp
    BB   | Barbados             | arin     | 10     |  13.6% |  18.2% |   -4.6pp

    ====================================================================================================
     BIGGEST MOVERS — 12mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 12mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    CN   | China                | apnic    | 6493   |  96.9% |   2.1% |  +94.8pp
    BS   | Bahamas              | arin     | 13     | 100.0% |   5.5% |  +94.5pp
    CH   | Switzerland          | ripencc  | 1062   |  81.7% |  16.5% |  +65.2pp
    SD   | Sudan                | afrinic  | 11     |  80.0% |  15.8% |  +64.2pp
    SO   | Somalia              | afrinic  | 22     |  85.2% |  21.4% |  +63.8pp
    TJ   | Tajikistan           | ripencc  | 44     |  95.8% |  41.7% |  +54.1pp
    JM   | Jamaica              | arin     | 15     |  66.7% |  34.3% |  +32.4pp
    MA   | Morocco              | afrinic  | 33     |  46.8% |  17.8% |  +29.0pp
    CL   | Chile                | lacnic   | 404    |  93.1% |  66.4% |  +26.7pp
    PH   | Philippines          | apnic    | 677    |  85.1% |  63.9% |  +21.2pp
    MX   | Mexico               | lacnic   | 668    |  80.2% |  59.4% |  +20.8pp
    SC   | Seychelles           | ripencc  | 87     |  82.7% |  63.3% |  +19.4pp
    DE   | Germany              | ripencc  | 3285   |  83.1% |  63.9% |  +19.2pp
    AZ   | Azerbaijan           | ripencc  | 122    |  89.0% |  70.8% |  +18.2pp
    NI   | Nicaragua            | lacnic   | 30     |  98.7% |  82.8% |  +15.9pp
    Decliners:
    KE   | Kenya                | afrinic  | 250    |  31.9% |  77.3% |  -45.4pp
    HK   | Hong Kong            | apnic    | 1402   |  48.2% |  83.5% |  -35.3pp
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  42.9% |  -35.2pp
    BT   | Bhutan               | apnic    | 43     |  72.7% | 100.0% |  -27.3pp
    AL   | Albania              | ripencc  | 133    |  74.6% |  97.8% |  -23.2pp
    ZA   | South Africa         | afrinic  | 751    |  36.2% |  51.0% |  -14.8pp
    FJ   | Fiji                 | apnic    | 20     |  87.0% | 100.0% |  -13.0pp
    IE   | Ireland              | ripencc  | 287    |  71.5% |  83.6% |  -12.1pp
    RO   | Romania              | ripencc  | 1083   |  82.7% |  94.5% |  -11.8pp
    ES   | Spain                | ripencc  | 1169   |  79.6% |  90.7% |  -11.1pp
    MO   | Macao                | apnic    | 15     |  65.8% |  76.7% |  -10.9pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  87.2% |   -9.9pp
    NG   | Nigeria              | afrinic  | 266    |  43.4% |  53.2% |   -9.8pp
    KR   | South Korea          | apnic    | 1085   |  11.1% |  20.1% |   -9.0pp
    BB   | Barbados             | arin     | 10     |  13.6% |  21.7% |   -8.1pp

    ====================================================================================================
     BIGGEST MOVERS — 24mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 24mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    BS   | Bahamas              | arin     | 13     | 100.0% |   0.7% |  +99.3pp
    CN   | China                | apnic    | 6493   |  96.9% |   1.6% |  +95.3pp
    IS   | Iceland              | ripencc  | 87     |  93.7% |  24.5% |  +69.2pp
    JP   | Japan                | apnic    | 978    |  84.2% |  17.5% |  +66.7pp
    SD   | Sudan                | afrinic  | 11     |  80.0% |  14.3% |  +65.7pp
    JM   | Jamaica              | arin     | 15     |  66.7% |  10.7% |  +56.0pp
    GH   | Ghana                | afrinic  | 103    |  91.7% |  37.7% |  +54.0pp
    TJ   | Tajikistan           | ripencc  | 44     |  95.8% |  46.2% |  +49.6pp
    SC   | Seychelles           | ripencc  | 87     |  82.7% |  41.3% |  +41.4pp
    UZ   | Uzbekistan           | ripencc  | 132    |  82.0% |  43.2% |  +38.8pp
    AZ   | Azerbaijan           | ripencc  | 122    |  89.0% |  50.9% |  +38.1pp
    BM   | Bermuda              | arin     | 23     |  79.2% |  41.7% |  +37.5pp
    MC   | Monaco               | ripencc  | 5      |  87.5% |  50.0% |  +37.5pp
    SO   | Somalia              | afrinic  | 22     |  85.2% |  50.0% |  +35.2pp
    CL   | Chile                | lacnic   | 404    |  93.1% |  58.4% |  +34.7pp
    Decliners:
    CD   | Congo, The Democrati | afrinic  | 51     |  26.6% |  83.9% |  -57.3pp
    KE   | Kenya                | afrinic  | 250    |  31.9% |  85.1% |  -53.2pp
    ZW   | Zimbabwe             | afrinic  | 27     |  13.8% |  66.7% |  -52.9pp
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  50.0% |  -42.3pp
    MU   | Mauritius            | afrinic  | 42     |   2.4% |  36.2% |  -33.8pp
    MA   | Morocco              | afrinic  | 33     |  46.8% |  74.3% |  -27.5pp
    MO   | Macao                | apnic    | 15     |  65.8% |  92.9% |  -27.1pp
    BT   | Bhutan               | apnic    | 43     |  72.7% |  98.6% |  -25.9pp
    AL   | Albania              | ripencc  | 133    |  74.6% |  97.6% |  -23.0pp
    PR   | Puerto Rico          | arin     | 124    |  30.2% |  52.9% |  -22.7pp
    ZA   | South Africa         | afrinic  | 751    |  36.2% |  58.3% |  -22.1pp
    TZ   | Tanzania             | afrinic  | 116    |  31.9% |  50.9% |  -19.0pp
    MZ   | Mozambique           | afrinic  | 31     |  47.8% |  63.6% |  -15.8pp
    IL   | Israel               | ripencc  | 385    |  70.0% |  85.7% |  -15.7pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  92.9% |  -15.6pp

    ====================================================================================================
     SPOTLIGHT: CHINA (CN)
    ====================================================================================================
    ASNs: 6493  |  RIR: apnic
    IPv4:
      Now  : 90.9% of IPv4 route objects covered by a valid ROA
      3mo  : 89.7% of IPv4 route objects covered by a valid ROA
      6mo  : 12.7% of IPv4 route objects covered by a valid ROA
      12mo : 3.9% of IPv4 route objects covered by a valid ROA
      24mo : 3.8% of IPv4 route objects covered by a valid ROA
    IPv6:
      Now  : 96.9% of IPv6 route objects covered by a valid ROA
      3mo  : 96.9% of IPv6 route objects covered by a valid ROA
      6mo  : 50.9% of IPv6 route objects covered by a valid ROA
      12mo : 2.1% of IPv6 route objects covered by a valid ROA
      24mo : 1.6% of IPv6 route objects covered by a valid ROA
