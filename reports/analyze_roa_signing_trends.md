    [*] Fetching APNIC Labs ROA-coverage snapshots...
        - Now   (reported date 04/11/2026): 278 countries/regions
        - 3mo   (reported date 08/08/2026): 278 countries/regions
        - 6mo   (reported date 08/05/2026): 279 countries/regions
        - 12mo  (reported date 08/11/2025): 280 countries/regions
        - 24mo  (reported date 08/11/2024): 279 countries/regions

    ====================================================================================================
     GLOBAL ROA COVERAGE TREND (IPv4 Route Objects, % Valid)
    ====================================================================================================
    Period   | Reported Date  | % Valid  | Total Route Objects
    ------------------------------------------------------------
    Now      | 04/11/2026     |   67.7% |  1,338,399
    3mo      | 08/08/2026     |   66.9% |  1,265,091
    6mo      | 08/05/2026     |   59.8% |  1,258,400
    12mo     | 08/11/2025     |   55.7% |  1,219,439
    24mo     | 08/11/2024     |   49.4% |  1,163,760

    ====================================================================================================
     GLOBAL ROA COVERAGE TREND (IPv6 Route Objects, % Valid)
    ====================================================================================================
    Period   | Reported Date  | % Valid  | Total Route Objects
    ------------------------------------------------------------
    Now      | 04/11/2026     |   76.4% |    325,129
    3mo      | 08/08/2026     |   74.7% |    309,694
    6mo      | 08/05/2026     |   64.9% |    302,377
    12mo     | 08/11/2025     |   58.1% |    299,583
    24mo     | 08/11/2024     |   55.4% |    260,574

    NOTE: IPv4 and IPv6 are reported separately because they are measured
    separately by APNIC and can diverge significantly per network — do not
    average or add them into one 'global ROA coverage' number.

    ====================================================================================================
     RIR ROA COVERAGE TREND (IPv4 Route Objects, % Valid, weighted by route-object count)
    ====================================================================================================
    RIR        | ASNs (now) |     Now |     3mo |     6mo |    12mo |    24mo
    -------------------------------------------------------------------------
    afrinic    | 2,474      |   65.8% |   61.7% |   60.5% |   37.5% |   33.6%
    apnic      | 31,447     |   76.1% |   74.8% |   56.3% |   54.2% |   50.8%
    arin       | 35,616     |   52.8% |   52.1% |   48.7% |   44.4% |   34.1%
    lacnic     | 13,857     |   69.2% |   67.7% |   61.1% |   59.6% |   51.9%
    ripencc    | 38,516     |   74.6% |   74.1% |   73.9% |   68.9% |   62.4%

    ====================================================================================================
     RIR ROA COVERAGE TREND (IPv6 Route Objects, % Valid, weighted by route-object count)
    ====================================================================================================
    RIR        | ASNs (now) |     Now |     3mo |     6mo |    12mo |    24mo
    -------------------------------------------------------------------------
    afrinic    | 2,474      |   42.3% |   39.6% |   40.2% |   35.6% |   60.4%
    apnic      | 31,447     |   83.6% |   82.5% |   57.1% |   49.1% |   40.2%
    arin       | 35,616     |   77.4% |   76.4% |   75.8% |   68.8% |   61.9%
    lacnic     | 13,857     |   68.1% |   62.8% |   60.2% |   56.9% |   54.8%
    ripencc    | 38,516     |   77.5% |   77.7% |   77.3% |   66.1% |   76.1%

    [+] Full per-country trend data (IPv4 + IPv6) saved to roa_signing_trends.csv

    ====================================================================================================
     BIGGEST MOVERS — 3mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 3mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    TG   | Togo                 | afrinic  | 11     |  61.7% |  10.2% |  +51.5pp
    BS   | Bahamas              | arin     | 13     |  73.4% |  26.2% |  +47.2pp
    TJ   | Tajikistan           | ripencc  | 44     |  84.2% |  37.8% |  +46.4pp
    VG   | Virgin Islands, Brit | ripencc  | 50     |  83.9% |  47.9% |  +36.0pp
    SK   | Slovakia             | ripencc  | 229    |  65.6% |  43.0% |  +22.6pp
    SL   | Sierra Leone         | afrinic  | 22     |  81.0% |  58.8% |  +22.2pp
    SS   | South Sudan          | afrinic  | 20     |  72.9% |  52.9% |  +20.0pp
    SO   | Somalia              | afrinic  | 22     |  84.5% |  65.5% |  +19.0pp
    CD   | Congo, The Democrati | afrinic  | 51     |  55.3% |  37.2% |  +18.1pp
    KE   | Kenya                | afrinic  | 250    |  76.8% |  59.7% |  +17.1pp
    AU   | Australia            | apnic    | 2996   |  53.9% |  36.8% |  +17.1pp
    LR   | Liberia              | afrinic  | 15     |  59.2% |  42.9% |  +16.3pp
    NG   | Nigeria              | afrinic  | 266    |  59.3% |  43.3% |  +16.0pp
    GQ   | Equatorial Guinea    | afrinic  | 7      |  58.5% |  45.7% |  +12.8pp
    YT   | Mayotte              | afrinic  | 1      |  77.4% |  65.0% |  +12.4pp
    Decliners:
    MH   | Marshall Islands     | ripencc  | 10     |  35.4% |  91.7% |  -56.3pp
    BQ   | Bonaire, Sint Eustat | lacnic   | 6      |  80.4% |  97.2% |  -16.8pp
    BD   | Bangladesh           | apnic    | 2033   |  85.4% |  93.9% |   -8.5pp
    SB   | Solomon Islands      | apnic    | 11     |  85.7% |  93.2% |   -7.5pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  76.2% |  83.3% |   -7.1pp
    SC   | Seychelles           | ripencc  | 87     |  80.3% |  86.3% |   -6.0pp
    MD   | Moldova              | ripencc  | 206    |  83.9% |  89.8% |   -5.9pp
    MG   | Madagascar           | afrinic  | 7      |  40.5% |  45.9% |   -5.4pp
    VE   | Venezuela            | lacnic   | 261    |  90.3% |  95.4% |   -5.1pp
    CV   | Cabo Verde           | afrinic  | 8      |  35.4% |  39.7% |   -4.3pp
    SG   | Singapore            | apnic    | 726    |  76.7% |  81.0% |   -4.3pp
    SD   | Sudan                | afrinic  | 11     |  37.5% |  41.6% |   -4.1pp
    DK   | Denmark              | ripencc  | 468    |  57.6% |  61.4% |   -3.8pp
    DJ   | Djibouti             | afrinic  | 4      |  93.7% |  97.2% |   -3.5pp
    GD   | Grenada              | arin     | 11     |  31.1% |  34.1% |   -3.0pp

    ====================================================================================================
     BIGGEST MOVERS — 6mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 6mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    DJ   | Djibouti             | afrinic  | 4      |  93.7% |   5.6% |  +88.1pp
    CN   | China                | apnic    | 6490   |  87.7% |   8.7% |  +79.0pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  76.2% |   5.9% |  +70.3pp
    CM   | Cameroon             | afrinic  | 30     |  94.6% |  37.0% |  +57.6pp
    TJ   | Tajikistan           | ripencc  | 44     |  84.2% |  37.3% |  +46.9pp
    BS   | Bahamas              | arin     | 13     |  73.4% |  27.3% |  +46.1pp
    VG   | Virgin Islands, Brit | ripencc  | 50     |  83.9% |  44.9% |  +39.0pp
    JE   | Jersey               | ripencc  | 13     |  92.3% |  53.8% |  +38.5pp
    TT   | Trinidad and Tobago  | lacnic   | 16     |  91.8% |  54.6% |  +37.2pp
    KI   | Kiribati             | apnic    | 6      | 100.0% |  63.2% |  +36.8pp
    MX   | Mexico               | lacnic   | 665    |  73.5% |  42.6% |  +30.9pp
    MT   | Malta                | ripencc  | 52     |  54.4% |  25.2% |  +29.2pp
    SL   | Sierra Leone         | afrinic  | 22     |  81.0% |  55.2% |  +25.8pp
    SO   | Somalia              | afrinic  | 22     |  84.5% |  59.9% |  +24.6pp
    SS   | South Sudan          | afrinic  | 20     |  72.9% |  50.5% |  +22.4pp
    Decliners:
    MH   | Marshall Islands     | ripencc  | 10     |  35.4% |  92.2% |  -56.8pp
    CV   | Cabo Verde           | afrinic  | 8      |  35.4% |  87.1% |  -51.7pp
    IT   | Italy                | ripencc  | 1319   |  51.1% |  67.6% |  -16.5pp
    SD   | Sudan                | afrinic  | 11     |  37.5% |  46.7% |   -9.2pp
    KM   | Comoros              | afrinic  | 4      |  71.4% |  79.3% |   -7.9pp
    KY   | Cayman Islands       | arin     | 18     |  47.7% |  55.2% |   -7.5pp
    MP   | Northern Mariana Isl | apnic    | 2      |  93.0% | 100.0% |   -7.0pp
    MD   | Moldova              | ripencc  | 206    |  83.9% |  90.9% |   -7.0pp
    SC   | Seychelles           | ripencc  | 87     |  80.3% |  87.2% |   -6.9pp
    BD   | Bangladesh           | apnic    | 2033   |  85.4% |  91.0% |   -5.6pp
    MG   | Madagascar           | afrinic  | 7      |  40.5% |  45.9% |   -5.4pp
    UZ   | Uzbekistan           | ripencc  | 131    |  72.4% |  77.3% |   -4.9pp
    DK   | Denmark              | ripencc  | 468    |  57.6% |  62.1% |   -4.5pp
    MK   | North Macedonia      | ripencc  | 69     |  47.8% |  51.6% |   -3.8pp
    VE   | Venezuela            | lacnic   | 261    |  90.3% |  93.9% |   -3.6pp

    ====================================================================================================
     BIGGEST MOVERS — 12mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 12mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    DJ   | Djibouti             | afrinic  | 4      |  93.7% |   2.9% |  +90.8pp
    EG   | Egypt                | afrinic  | 86     |  95.5% |   7.5% |  +88.0pp
    CN   | China                | apnic    | 6490   |  87.7% |   3.9% |  +83.8pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  76.2% |   3.1% |  +73.1pp
    BJ   | Benin                | afrinic  | 16     |  72.9% |   5.7% |  +67.2pp
    SO   | Somalia              | afrinic  | 22     |  84.5% |  19.0% |  +65.5pp
    CM   | Cameroon             | afrinic  | 30     |  94.6% |  31.7% |  +62.9pp
    TJ   | Tajikistan           | ripencc  | 44     |  84.2% |  30.4% |  +53.8pp
    HT   | Haiti                | lacnic   | 11     |  56.9% |   3.6% |  +53.3pp
    KI   | Kiribati             | apnic    | 6      | 100.0% |  50.0% |  +50.0pp
    JE   | Jersey               | ripencc  | 13     |  92.3% |  42.4% |  +49.9pp
    BS   | Bahamas              | arin     | 13     |  73.4% |  26.4% |  +47.0pp
    LS   | Lesotho              | afrinic  | 9      |  72.9% |  30.1% |  +42.8pp
    VG   | Virgin Islands, Brit | ripencc  | 50     |  83.9% |  45.8% |  +38.1pp
    TT   | Trinidad and Tobago  | lacnic   | 16     |  91.8% |  53.8% |  +38.0pp
    Decliners:
    CV   | Cabo Verde           | afrinic  | 8      |  35.4% |  85.5% |  -50.1pp
    MH   | Marshall Islands     | ripencc  | 10     |  35.4% |  75.0% |  -39.6pp
    IE   | Ireland              | ripencc  | 287    |  65.1% |  78.0% |  -12.9pp
    MG   | Madagascar           | afrinic  | 7      |  40.5% |  52.6% |  -12.1pp
    MD   | Moldova              | ripencc  | 206    |  83.9% |  93.7% |   -9.8pp
    KM   | Comoros              | afrinic  | 4      |  71.4% |  80.8% |   -9.4pp
    GT   | Guatemala            | lacnic   | 79     |  81.5% |  90.6% |   -9.1pp
    AO   | Angola               | afrinic  | 70     |  49.7% |  58.6% |   -8.9pp
    BF   | Burkina Faso         | afrinic  | 30     |  81.6% |  89.9% |   -8.3pp
    BD   | Bangladesh           | apnic    | 2033   |  85.4% |  93.7% |   -8.3pp
    PY   | Paraguay             | lacnic   | 115    |  76.1% |  83.7% |   -7.6pp
    KY   | Cayman Islands       | arin     | 18     |  47.7% |  54.8% |   -7.1pp
    GL   | Greenland            | ripencc  | 1      |  76.5% |  83.3% |   -6.8pp
    MP   | Northern Mariana Isl | apnic    | 2      |  93.0% |  98.3% |   -5.3pp
    AE   | United Arab Emirates | ripencc  | 218    |  81.8% |  86.4% |   -4.6pp

    ====================================================================================================
     BIGGEST MOVERS — 24mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 24mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    DJ   | Djibouti             | afrinic  | 4      |  93.7% |   1.0% |  +92.7pp
    EG   | Egypt                | afrinic  | 86     |  95.5% |   7.6% |  +87.9pp
    CN   | China                | apnic    | 6490   |  87.7% |   3.0% |  +84.7pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  76.2% |   0.0% |  +76.2pp
    IS   | Iceland              | ripencc  | 87     |  76.2% |   1.7% |  +74.5pp
    CI   | Côte d'Ivoire        | afrinic  | 26     |  94.7% |  21.4% |  +73.3pp
    SO   | Somalia              | afrinic  | 22     |  84.5% |  13.0% |  +71.5pp
    BJ   | Benin                | afrinic  | 16     |  72.9% |   3.4% |  +69.5pp
    JE   | Jersey               | ripencc  | 13     |  92.3% |  25.0% |  +67.3pp
    TJ   | Tajikistan           | ripencc  | 44     |  84.2% |  23.9% |  +60.3pp
    ML   | Mali                 | afrinic  | 8      |  83.3% |  24.5% |  +58.8pp
    HT   | Haiti                | lacnic   | 11     |  56.9% |   2.3% |  +54.6pp
    LR   | Liberia              | afrinic  | 15     |  59.2% |   7.5% |  +51.7pp
    VG   | Virgin Islands, Brit | ripencc  | 50     |  83.9% |  32.4% |  +51.5pp
    BS   | Bahamas              | arin     | 13     |  73.4% |  22.7% |  +50.7pp
    Decliners:
    CV   | Cabo Verde           | afrinic  | 8      |  35.4% |  83.0% |  -47.6pp
    MH   | Marshall Islands     | ripencc  | 10     |  35.4% |  82.4% |  -47.0pp
    SD   | Sudan                | afrinic  | 11     |  37.5% |  61.3% |  -23.8pp
    KM   | Comoros              | afrinic  | 4      |  71.4% |  90.5% |  -19.1pp
    PE   | Peru                 | lacnic   | 226    |  35.5% |  49.8% |  -14.3pp
    IE   | Ireland              | ripencc  | 287    |  65.1% |  75.3% |  -10.2pp
    BD   | Bangladesh           | apnic    | 2033   |  85.4% |  94.0% |   -8.6pp
    AO   | Angola               | afrinic  | 70     |  49.7% |  57.4% |   -7.7pp
    MD   | Moldova              | ripencc  | 206    |  83.9% |  90.8% |   -6.9pp
    PY   | Paraguay             | lacnic   | 115    |  76.1% |  83.0% |   -6.9pp
    AE   | United Arab Emirates | ripencc  | 218    |  81.8% |  88.2% |   -6.4pp
    ME   | Montenegro           | ripencc  | 30     |  49.0% |  54.4% |   -5.4pp
    CG   | Congo                | afrinic  | 13     |  16.9% |  21.9% |   -5.0pp
    QA   | Qatar                | ripencc  | 32     |  84.3% |  88.7% |   -4.4pp
    BF   | Burkina Faso         | afrinic  | 30     |  81.6% |  86.0% |   -4.4pp

    ====================================================================================================
     BIGGEST MOVERS — 3mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 3mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    BS   | Bahamas              | arin     | 13     | 100.0% |   6.5% |  +93.5pp
    TJ   | Tajikistan           | ripencc  | 44     |  95.8% |  55.6% |  +40.2pp
    TH   | Thailand             | apnic    | 621    |  90.0% |  58.9% |  +31.1pp
    CL   | Chile                | lacnic   | 403    |  92.9% |  64.5% |  +28.4pp
    AZ   | Azerbaijan           | ripencc  | 121    |  89.0% |  70.8% |  +18.2pp
    SD   | Sudan                | afrinic  | 11     |  80.0% |  61.9% |  +18.1pp
    MX   | Mexico               | lacnic   | 665    |  80.2% |  63.3% |  +16.9pp
    AO   | Angola               | afrinic  | 70     |  91.2% |  77.1% |  +14.1pp
    PH   | Philippines          | apnic    | 675    |  85.5% |  72.2% |  +13.3pp
    MZ   | Mozambique           | afrinic  | 31     |  47.8% |  37.9% |   +9.9pp
    MM   | Myanmar              | apnic    | 172    |  99.4% |  90.8% |   +8.6pp
    MY   | Malaysia             | apnic    | 406    |  54.5% |  46.2% |   +8.3pp
    VI   | Virgin Islands, U.S. | arin     | 12     |  73.0% |  65.4% |   +7.6pp
    IS   | Iceland              | ripencc  | 87     |  93.8% |  86.8% |   +7.0pp
    NZ   | New Zealand          | apnic    | 698    |  73.0% |  66.4% |   +6.6pp
    Decliners:
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  33.3% |  -25.6pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  94.4% |  -17.1pp
    VG   | Virgin Islands, Brit | ripencc  | 50     |  75.2% |  88.8% |  -13.6pp
    PR   | Puerto Rico          | arin     | 124    |  30.6% |  44.2% |  -13.6pp
    AM   | Armenia              | ripencc  | 156    |  85.4% |  95.9% |  -10.5pp
    CM   | Cameroon             | afrinic  | 30     |  92.3% | 100.0% |   -7.7pp
    AL   | Albania              | ripencc  | 133    |  89.1% |  96.5% |   -7.4pp
    PK   | Pakistan             | apnic    | 473    |  90.4% |  97.7% |   -7.3pp
    IM   | Isle of Man          | ripencc  | 27     |  71.9% |  78.6% |   -6.7pp
    PT   | Portugal             | ripencc  | 166    |  88.0% |  93.9% |   -5.9pp
    RO   | Romania              | ripencc  | 1082   |  65.6% |  71.1% |   -5.5pp
    GE   | Georgia              | ripencc  | 175    |  85.9% |  91.0% |   -5.1pp
    MW   | Malawi               | afrinic  | 30     |  80.0% |  84.8% |   -4.8pp
    MC   | Monaco               | ripencc  | 5      |  87.0% |  91.7% |   -4.7pp
    BB   | Barbados             | arin     | 10     |  13.6% |  18.2% |   -4.6pp

    ====================================================================================================
     BIGGEST MOVERS — 6mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 6mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    BS   | Bahamas              | arin     | 13     | 100.0% |   6.2% |  +93.8pp
    CN   | China                | apnic    | 6490   |  96.9% |  30.0% |  +66.9pp
    TJ   | Tajikistan           | ripencc  | 44     |  95.8% |  50.0% |  +45.8pp
    TH   | Thailand             | apnic    | 621    |  90.0% |  58.4% |  +31.6pp
    CL   | Chile                | lacnic   | 403    |  92.9% |  65.4% |  +27.5pp
    MA   | Morocco              | afrinic  | 33     |  45.1% |  21.6% |  +23.5pp
    MX   | Mexico               | lacnic   | 665    |  80.2% |  57.0% |  +23.2pp
    PH   | Philippines          | apnic    | 675    |  85.5% |  63.1% |  +22.4pp
    BD   | Bangladesh           | apnic    | 2033   |  84.5% |  65.2% |  +19.3pp
    AO   | Angola               | afrinic  | 70     |  91.2% |  75.0% |  +16.2pp
    AZ   | Azerbaijan           | ripencc  | 121    |  89.0% |  73.4% |  +15.6pp
    SD   | Sudan                | afrinic  | 11     |  80.0% |  65.2% |  +14.8pp
    UG   | Uganda               | afrinic  | 59     |  90.1% |  75.3% |  +14.8pp
    MZ   | Mozambique           | afrinic  | 31     |  47.8% |  34.6% |  +13.2pp
    NL   | Netherlands          | ripencc  | 1637   |  79.6% |  68.0% |  +11.6pp
    Decliners:
    AE   | United Arab Emirates | ripencc  | 218    |  50.3% |  95.4% |  -45.1pp
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  33.3% |  -25.6pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  92.9% |  -15.6pp
    PR   | Puerto Rico          | arin     | 124    |  30.6% |  45.7% |  -15.1pp
    MO   | Macao                | apnic    | 15     |  65.8% |  75.6% |   -9.8pp
    AL   | Albania              | ripencc  | 133    |  89.1% |  97.3% |   -8.2pp
    PS   | Palestine, State of  | ripencc  | 69     |  87.0% |  95.0% |   -8.0pp
    ID   | Indonesia            | apnic    | 4089   |  58.8% |  65.7% |   -6.9pp
    UZ   | Uzbekistan           | ripencc  | 131    |  82.0% |  88.9% |   -6.9pp
    PK   | Pakistan             | apnic    | 473    |  90.4% |  97.0% |   -6.6pp
    ES   | Spain                | ripencc  | 1168   |  79.7% |  85.7% |   -6.0pp
    SA   | Saudi Arabia         | ripencc  | 201    |  82.3% |  88.2% |   -5.9pp
    LI   | Liechtenstein        | ripencc  | 28     |  79.2% |  85.1% |   -5.9pp
    AM   | Armenia              | ripencc  | 156    |  85.4% |  90.5% |   -5.1pp
    PT   | Portugal             | ripencc  | 166    |  88.0% |  92.8% |   -4.8pp

    ====================================================================================================
     BIGGEST MOVERS — 12mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 12mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    BS   | Bahamas              | arin     | 13     | 100.0% |   4.9% |  +95.1pp
    CN   | China                | apnic    | 6490   |  96.9% |   2.1% |  +94.8pp
    CH   | Switzerland          | ripencc  | 1063   |  81.2% |  16.5% |  +64.7pp
    SO   | Somalia              | afrinic  | 22     |  85.2% |  21.4% |  +63.8pp
    TJ   | Tajikistan           | ripencc  | 44     |  95.8% |  41.7% |  +54.1pp
    SD   | Sudan                | afrinic  | 11     |  80.0% |  33.3% |  +46.7pp
    JM   | Jamaica              | arin     | 15     |  66.7% |  28.1% |  +38.6pp
    MA   | Morocco              | afrinic  | 33     |  45.1% |  17.8% |  +27.3pp
    CL   | Chile                | lacnic   | 403    |  92.9% |  66.6% |  +26.3pp
    PH   | Philippines          | apnic    | 675    |  85.5% |  63.8% |  +21.7pp
    DE   | Germany              | ripencc  | 3286   |  82.9% |  62.0% |  +20.9pp
    MX   | Mexico               | lacnic   | 665    |  80.2% |  59.4% |  +20.8pp
    CA   | Canada               | arin     | 2545   |  76.9% |  57.2% |  +19.7pp
    AZ   | Azerbaijan           | ripencc  | 121    |  89.0% |  70.3% |  +18.7pp
    BM   | Bermuda              | arin     | 23     |  79.2% |  61.9% |  +17.3pp
    Decliners:
    KE   | Kenya                | afrinic  | 250    |  32.7% |  77.9% |  -45.2pp
    AE   | United Arab Emirates | ripencc  | 218    |  50.3% |  91.2% |  -40.9pp
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  42.9% |  -35.2pp
    RO   | Romania              | ripencc  | 1082   |  65.6% |  94.5% |  -28.9pp
    BT   | Bhutan               | apnic    | 43     |  73.0% | 100.0% |  -27.0pp
    ZW   | Zimbabwe             | afrinic  | 27     |  13.7% |  33.3% |  -19.6pp
    SA   | Saudi Arabia         | ripencc  | 201    |  82.3% |  98.5% |  -16.2pp
    IE   | Ireland              | ripencc  | 287    |  73.2% |  89.2% |  -16.0pp
    ZA   | South Africa         | afrinic  | 751    |  36.2% |  50.8% |  -14.6pp
    PR   | Puerto Rico          | arin     | 124    |  30.6% |  43.3% |  -12.7pp
    ES   | Spain                | ripencc  | 1168   |  79.7% |  90.7% |  -11.0pp
    MO   | Macao                | apnic    | 15     |  65.8% |  76.7% |  -10.9pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  87.2% |   -9.9pp
    AL   | Albania              | ripencc  | 133    |  89.1% |  98.4% |   -9.3pp
    KR   | South Korea          | apnic    | 1082   |  11.1% |  20.0% |   -8.9pp

    ====================================================================================================
     BIGGEST MOVERS — 24mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 24mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    BS   | Bahamas              | arin     | 13     | 100.0% |   0.7% |  +99.3pp
    CN   | China                | apnic    | 6490   |  96.9% |   1.6% |  +95.3pp
    IS   | Iceland              | ripencc  | 87     |  93.8% |  25.8% |  +68.0pp
    SD   | Sudan                | afrinic  | 11     |  80.0% |  12.5% |  +67.5pp
    JP   | Japan                | apnic    | 977    |  83.9% |  17.4% |  +66.5pp
    JM   | Jamaica              | arin     | 15     |  66.7% |  10.7% |  +56.0pp
    GH   | Ghana                | afrinic  | 103    |  91.7% |  37.7% |  +54.0pp
    TJ   | Tajikistan           | ripencc  | 44     |  95.8% |  53.3% |  +42.5pp
    SC   | Seychelles           | ripencc  | 87     |  79.2% |  40.2% |  +39.0pp
    AZ   | Azerbaijan           | ripencc  | 121    |  89.0% |  50.9% |  +38.1pp
    UZ   | Uzbekistan           | ripencc  | 131    |  82.0% |  44.4% |  +37.6pp
    BM   | Bermuda              | arin     | 23     |  79.2% |  41.7% |  +37.5pp
    MC   | Monaco               | ripencc  | 5      |  87.0% |  50.0% |  +37.0pp
    SO   | Somalia              | afrinic  | 22     |  85.2% |  50.0% |  +35.2pp
    CL   | Chile                | lacnic   | 403    |  92.9% |  58.2% |  +34.7pp
    Decliners:
    CD   | Congo, The Democrati | afrinic  | 51     |  26.6% |  83.9% |  -57.3pp
    ZW   | Zimbabwe             | afrinic  | 27     |  13.7% |  66.7% |  -53.0pp
    KE   | Kenya                | afrinic  | 250    |  32.7% |  83.7% |  -51.0pp
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  50.0% |  -42.3pp
    AE   | United Arab Emirates | ripencc  | 218    |  50.3% |  90.3% |  -40.0pp
    MU   | Mauritius            | afrinic  | 42     |   2.3% |  36.8% |  -34.5pp
    MA   | Morocco              | afrinic  | 33     |  45.1% |  74.3% |  -29.2pp
    MO   | Macao                | apnic    | 15     |  65.8% |  92.9% |  -27.1pp
    BT   | Bhutan               | apnic    | 43     |  73.0% |  98.6% |  -25.6pp
    PR   | Puerto Rico          | arin     | 124    |  30.6% |  53.6% |  -23.0pp
    ZA   | South Africa         | afrinic  | 751    |  36.2% |  58.0% |  -21.8pp
    TZ   | Tanzania             | afrinic  | 116    |  33.6% |  50.9% |  -17.3pp
    MZ   | Mozambique           | afrinic  | 31     |  47.8% |  63.6% |  -15.8pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  92.9% |  -15.6pp
    SA   | Saudi Arabia         | ripencc  | 201    |  82.3% |  96.8% |  -14.5pp

    ====================================================================================================
     SPOTLIGHT: CHINA (CN)
    ====================================================================================================
    ASNs: 6490  |  RIR: apnic
    IPv4:
      Now  : 87.7% of IPv4 route objects covered by a valid ROA
      3mo  : 89.8% of IPv4 route objects covered by a valid ROA
      6mo  : 8.7% of IPv4 route objects covered by a valid ROA
      12mo : 3.9% of IPv4 route objects covered by a valid ROA
      24mo : 3.0% of IPv4 route objects covered by a valid ROA
    IPv6:
      Now  : 96.9% of IPv6 route objects covered by a valid ROA
      3mo  : 96.9% of IPv6 route objects covered by a valid ROA
      6mo  : 30.0% of IPv6 route objects covered by a valid ROA
      12mo : 2.1% of IPv6 route objects covered by a valid ROA
      24mo : 1.6% of IPv6 route objects covered by a valid ROA
