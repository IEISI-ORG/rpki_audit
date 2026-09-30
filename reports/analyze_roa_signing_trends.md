    [*] Fetching APNIC Labs ROA-coverage snapshots...
        - Now   (reported date 23/09/2026): 278 countries/regions
        - 3mo   (reported date 30/06/2026): 279 countries/regions
        - 6mo   (reported date 30/03/2026): 279 countries/regions
        - 12mo  (reported date 30/09/2025): 279 countries/regions
        - 24mo  (reported date 30/09/2024): 279 countries/regions

    ====================================================================================================
     GLOBAL ROA COVERAGE TREND (IPv4 Route Objects, % Valid)
    ====================================================================================================
    Period   | Reported Date  | % Valid  | Total Route Objects
    ------------------------------------------------------------
    Now      | 23/09/2026     |   68.2% |  1,287,104
    3mo      | 30/06/2026     |   65.4% |  1,264,238
    6mo      | 30/03/2026     |   58.8% |  1,244,618
    12mo     | 30/09/2025     |   53.0% |  1,234,891
    24mo     | 30/09/2024     |   47.9% |  1,186,650

    ====================================================================================================
     GLOBAL ROA COVERAGE TREND (IPv6 Route Objects, % Valid)
    ====================================================================================================
    Period   | Reported Date  | % Valid  | Total Route Objects
    ------------------------------------------------------------
    Now      | 23/09/2026     |   75.4% |    312,210
    3mo      | 30/06/2026     |   73.7% |    313,545
    6mo      | 30/03/2026     |   62.1% |    302,471
    12mo     | 30/09/2025     |   57.2% |    297,499
    24mo     | 30/09/2024     |   54.8% |    261,129

    NOTE: IPv4 and IPv6 are reported separately because they are measured
    separately by APNIC and can diverge significantly per network — do not
    average or add them into one 'global ROA coverage' number.

    ====================================================================================================
     RIR ROA COVERAGE TREND (IPv4 Route Objects, % Valid, weighted by route-object count)
    ====================================================================================================
    RIR        | ASNs (now) |     Now |     3mo |     6mo |    12mo |    24mo
    -------------------------------------------------------------------------
    afrinic    | 2,468      |   65.4% |   61.5% |   58.3% |   38.0% |   31.5%
    apnic      | 31,337     |   76.7% |   73.8% |   54.7% |   49.0% |   45.8%
    arin       | 35,434     |   54.1% |   51.3% |   49.1% |   40.8% |   33.5%
    lacnic     | 13,791     |   68.4% |   61.0% |   57.7% |   58.4% |   54.6%
    ripencc    | 38,457     |   74.5% |   74.4% |   73.4% |   68.1% |   61.5%

    ====================================================================================================
     RIR ROA COVERAGE TREND (IPv6 Route Objects, % Valid, weighted by route-object count)
    ====================================================================================================
    RIR        | ASNs (now) |     Now |     3mo |     6mo |    12mo |    24mo
    -------------------------------------------------------------------------
    afrinic    | 2,468      |   41.3% |   38.5% |   40.4% |   35.8% |   66.2%
    apnic      | 31,337     |   83.5% |   81.7% |   50.8% |   48.0% |   39.1%
    arin       | 35,434     |   77.6% |   76.4% |   75.2% |   67.5% |   60.7%
    lacnic     | 13,791     |   63.4% |   61.4% |   59.2% |   56.2% |   55.9%
    ripencc    | 38,457     |   77.6% |   76.1% |   76.6% |   65.7% |   73.9%

    [+] Full per-country trend data (IPv4 + IPv6) saved to roa_signing_trends.csv

    ====================================================================================================
     BIGGEST MOVERS — 3mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 3mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    TG   | Togo                 | afrinic  | 11     |  62.3% |  10.2% |  +52.1pp
    TT   | Trinidad and Tobago  | lacnic   | 16     |  91.8% |  54.0% |  +37.8pp
    MX   | Mexico               | lacnic   | 654    |  76.2% |  44.3% |  +31.9pp
    JE   | Jersey               | ripencc  | 13     |  92.2% |  62.3% |  +29.9pp
    KI   | Kiribati             | apnic    | 5      |  90.5% |  63.2% |  +27.3pp
    GG   | Guernsey             | ripencc  | 11     |  71.0% |  50.0% |  +21.0pp
    CD   | Congo, The Democrati | afrinic  | 51     |  56.3% |  38.0% |  +18.3pp
    KE   | Kenya                | afrinic  | 246    |  76.1% |  59.0% |  +17.1pp
    NG   | Nigeria              | afrinic  | 266    |  58.9% |  43.1% |  +15.8pp
    BQ   | Bonaire, Sint Eustat | lacnic   | 6      |  97.2% |  83.3% |  +13.9pp
    VG   | Virgin Islands, Brit | ripencc  | 49     |  57.3% |  43.8% |  +13.5pp
    AU   | Australia            | apnic    | 2994   |  49.5% |  36.4% |  +13.1pp
    SO   | Somalia              | afrinic  | 22     |  78.5% |  65.5% |  +13.0pp
    RO   | Romania              | ripencc  | 1084   |  78.4% |  65.9% |  +12.5pp
    MA   | Morocco              | afrinic  | 32     |  15.1% |   3.2% |  +11.9pp
    Decliners:
    IT   | Italy                | ripencc  | 1321   |  51.3% |  68.2% |  -16.9pp
    MK   | North Macedonia      | ripencc  | 68     |  41.5% |  50.5% |   -9.0pp
    KY   | Cayman Islands       | arin     | 18     |  48.2% |  55.2% |   -7.0pp
    LY   | Libya                | afrinic  | 27     |  65.0% |  71.5% |   -6.5pp
    KN   | Saint Kitts and Nevi | arin     | 11     |  11.7% |  16.7% |   -5.0pp
    SC   | Seychelles           | ripencc  | 87     |  85.0% |  88.9% |   -3.9pp
    CV   | Cabo Verde           | afrinic  | 8      |  36.9% |  40.6% |   -3.7pp
    AE   | United Arab Emirates | ripencc  | 212    |  82.6% |  85.6% |   -3.0pp
    PE   | Peru                 | lacnic   | 225    |  35.6% |  38.3% |   -2.7pp
    YT   | Mayotte              | afrinic  | 1      |  75.0% |  77.4% |   -2.4pp
    CZ   | Czechia              | ripencc  | 715    |  80.8% |  82.9% |   -2.1pp
    IE   | Ireland              | ripencc  | 285    |  65.1% |  67.0% |   -1.9pp
    AS   | American Samoa       | apnic    | 2      |  17.9% |  19.7% |   -1.8pp
    AG   | Antigua and Barbuda  | arin     | 18     |  21.0% |  22.8% |   -1.8pp
    SB   | Solomon Islands      | apnic    | 11     |  83.7% |  85.4% |   -1.7pp

    ====================================================================================================
     BIGGEST MOVERS — 6mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 6mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    DJ   | Djibouti             | afrinic  | 4      |  97.3% |   5.6% |  +91.7pp
    CN   | China                | apnic    | 6503   |  89.3% |   4.4% |  +84.9pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  83.3% |   5.9% |  +77.4pp
    CM   | Cameroon             | afrinic  | 29     |  94.9% |  35.5% |  +59.4pp
    JE   | Jersey               | ripencc  | 13     |  92.2% |  53.1% |  +39.1pp
    TT   | Trinidad and Tobago  | lacnic   | 16     |  91.8% |  54.2% |  +37.6pp
    MX   | Mexico               | lacnic   | 654    |  76.2% |  42.0% |  +34.2pp
    MT   | Malta                | ripencc  | 56     |  53.7% |  25.6% |  +28.1pp
    KI   | Kiribati             | apnic    | 5      |  90.5% |  63.2% |  +27.3pp
    SO   | Somalia              | afrinic  | 22     |  78.5% |  52.9% |  +25.6pp
    MK   | North Macedonia      | ripencc  | 68     |  41.5% |  20.8% |  +20.7pp
    GG   | Guernsey             | ripencc  | 11     |  71.0% |  50.7% |  +20.3pp
    CD   | Congo, The Democrati | afrinic  | 51     |  56.3% |  36.9% |  +19.4pp
    KE   | Kenya                | afrinic  | 246    |  76.1% |  57.5% |  +18.6pp
    BW   | Botswana             | afrinic  | 33     |  72.7% |  55.3% |  +17.4pp
    Decliners:
    CV   | Cabo Verde           | afrinic  | 8      |  36.9% |  86.4% |  -49.5pp
    IT   | Italy                | ripencc  | 1321   |  51.3% |  65.8% |  -14.5pp
    LY   | Libya                | afrinic  | 27     |  65.0% |  78.5% |  -13.5pp
    KY   | Cayman Islands       | arin     | 18     |  48.2% |  55.2% |   -7.0pp
    KM   | Comoros              | afrinic  | 4      |  74.3% |  80.8% |   -6.5pp
    MP   | Northern Mariana Isl | apnic    | 2      |  94.4% | 100.0% |   -5.6pp
    SD   | Sudan                | afrinic  | 11     |  40.7% |  45.3% |   -4.6pp
    AG   | Antigua and Barbuda  | arin     | 18     |  21.0% |  25.5% |   -4.5pp
    UZ   | Uzbekistan           | ripencc  | 129    |  72.3% |  76.4% |   -4.1pp
    SX   | Sint Maarten (Dutch  | lacnic   | 3      |  77.4% |  81.2% |   -3.8pp
    MG   | Madagascar           | afrinic  | 7      |  41.8% |  45.3% |   -3.5pp
    GL   | Greenland            | ripencc  | 1      |  77.1% |  80.6% |   -3.5pp
    AE   | United Arab Emirates | ripencc  | 212    |  82.6% |  85.5% |   -2.9pp
    GT   | Guatemala            | lacnic   | 79     |  82.4% |  84.8% |   -2.4pp
    YT   | Mayotte              | afrinic  | 1      |  75.0% |  77.4% |   -2.4pp

    ====================================================================================================
     BIGGEST MOVERS — 12mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 12mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    DJ   | Djibouti             | afrinic  | 4      |  97.3% |   2.9% |  +94.4pp
    EG   | Egypt                | afrinic  | 86     |  95.5% |   7.7% |  +87.8pp
    CN   | China                | apnic    | 6503   |  89.3% |   3.9% |  +85.4pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  83.3% |   0.0% |  +83.3pp
    PK   | Pakistan             | apnic    | 473    |  92.9% |  15.4% |  +77.5pp
    CM   | Cameroon             | afrinic  | 29     |  94.9% |  31.4% |  +63.5pp
    BJ   | Benin                | afrinic  | 16     |  65.7% |   5.7% |  +60.0pp
    SO   | Somalia              | afrinic  | 22     |  78.5% |  20.1% |  +58.4pp
    JE   | Jersey               | ripencc  | 13     |  92.2% |  38.4% |  +53.8pp
    HT   | Haiti                | lacnic   | 11     |  56.3% |   3.7% |  +52.6pp
    KI   | Kiribati             | apnic    | 5      |  90.5% |  46.2% |  +44.3pp
    KZ   | Kazakhstan           | ripencc  | 261    |  80.1% |  38.9% |  +41.2pp
    LS   | Lesotho              | afrinic  | 9      |  72.1% |  31.0% |  +41.1pp
    MX   | Mexico               | lacnic   | 654    |  76.2% |  41.0% |  +35.2pp
    TT   | Trinidad and Tobago  | lacnic   | 16     |  91.8% |  58.4% |  +33.4pp
    Decliners:
    CV   | Cabo Verde           | afrinic  | 8      |  36.9% |  84.9% |  -48.0pp
    IE   | Ireland              | ripencc  | 285    |  65.1% |  78.7% |  -13.6pp
    MG   | Madagascar           | afrinic  | 7      |  41.8% |  52.7% |  -10.9pp
    AO   | Angola               | afrinic  | 70     |  49.0% |  59.4% |  -10.4pp
    KY   | Cayman Islands       | arin     | 18     |  48.2% |  57.3% |   -9.1pp
    LY   | Libya                | afrinic  | 27     |  65.0% |  73.7% |   -8.7pp
    GT   | Guatemala            | lacnic   | 79     |  82.4% |  90.5% |   -8.1pp
    BF   | Burkina Faso         | afrinic  | 30     |  81.1% |  88.9% |   -7.8pp
    PY   | Paraguay             | lacnic   | 115    |  75.6% |  82.6% |   -7.0pp
    KM   | Comoros              | afrinic  | 4      |  74.3% |  80.8% |   -6.5pp
    GL   | Greenland            | ripencc  | 1      |  77.1% |  83.3% |   -6.2pp
    KN   | Saint Kitts and Nevi | arin     | 11     |  11.7% |  17.2% |   -5.5pp
    AF   | Afghanistan          | apnic    | 75     |  90.0% |  94.6% |   -4.6pp
    SD   | Sudan                | afrinic  | 11     |  40.7% |  45.2% |   -4.5pp
    MP   | Northern Mariana Isl | apnic    | 2      |  94.4% |  98.3% |   -3.9pp

    ====================================================================================================
     BIGGEST MOVERS — 24mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 24mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    DJ   | Djibouti             | afrinic  | 4      |  97.3% |   1.0% |  +96.3pp
    EG   | Egypt                | afrinic  | 86     |  95.5% |   8.0% |  +87.5pp
    CN   | China                | apnic    | 6503   |  89.3% |   2.9% |  +86.4pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  83.3% |   0.0% |  +83.3pp
    CM   | Cameroon             | afrinic  | 29     |  94.9% |  13.6% |  +81.3pp
    FM   | Micronesia, Federate | apnic    | 6      |  85.0% |   4.8% |  +80.2pp
    PK   | Pakistan             | apnic    | 473    |  92.9% |  14.5% |  +78.4pp
    SN   | Senegal              | afrinic  | 18     |  79.0% |   1.4% |  +77.6pp
    CI   | Côte d'Ivoire        | afrinic  | 24     |  93.9% |  19.9% |  +74.0pp
    IS   | Iceland              | ripencc  | 87     |  75.2% |   1.7% |  +73.5pp
    JE   | Jersey               | ripencc  | 13     |  92.2% |  25.0% |  +67.2pp
    SO   | Somalia              | afrinic  | 22     |  78.5% |  13.1% |  +65.4pp
    BJ   | Benin                | afrinic  | 16     |  65.7% |   3.4% |  +62.3pp
    ML   | Mali                 | afrinic  | 8      |  83.3% |  25.3% |  +58.0pp
    SL   | Sierra Leone         | afrinic  | 22     |  58.2% |   5.1% |  +53.1pp
    Decliners:
    CV   | Cabo Verde           | afrinic  | 8      |  36.9% |  80.9% |  -44.0pp
    KM   | Comoros              | afrinic  | 4      |  74.3% | 100.0% |  -25.7pp
    SD   | Sudan                | afrinic  | 11     |  40.7% |  62.3% |  -21.6pp
    PE   | Peru                 | lacnic   | 225    |  35.6% |  52.0% |  -16.4pp
    LY   | Libya                | afrinic  | 27     |  65.0% |  76.4% |  -11.4pp
    IE   | Ireland              | ripencc  | 285    |  65.1% |  75.1% |  -10.0pp
    ME   | Montenegro           | ripencc  | 31     |  48.8% |  56.6% |   -7.8pp
    AO   | Angola               | afrinic  | 70     |  49.0% |  56.6% |   -7.6pp
    PY   | Paraguay             | lacnic   | 115    |  75.6% |  82.8% |   -7.2pp
    SK   | Slovakia             | ripencc  | 229    |  46.0% |  52.6% |   -6.6pp
    MZ   | Mozambique           | afrinic  | 31     |  16.0% |  22.2% |   -6.2pp
    BF   | Burkina Faso         | afrinic  | 30     |  81.1% |  86.2% |   -5.1pp
    CG   | Congo                | afrinic  | 13     |  16.9% |  21.7% |   -4.8pp
    TZ   | Tanzania             | afrinic  | 116    |  35.3% |  39.9% |   -4.6pp
    ZM   | Zambia               | afrinic  | 22     |  49.1% |  52.9% |   -3.8pp

    ====================================================================================================
     BIGGEST MOVERS — 3mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 3mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    RO   | Romania              | ripencc  | 1084   |  64.3% |  25.7% |  +38.6pp
    TH   | Thailand             | apnic    | 621    |  88.3% |  58.7% |  +29.6pp
    TJ   | Tajikistan           | ripencc  | 42     |  73.9% |  47.8% |  +26.1pp
    MA   | Morocco              | afrinic  | 32     |  43.5% |  21.6% |  +21.9pp
    AZ   | Azerbaijan           | ripencc  | 119    |  86.3% |  73.8% |  +12.5pp
    MZ   | Mozambique           | afrinic  | 31     |  47.8% |  37.0% |  +10.8pp
    LK   | Sri Lanka            | apnic    | 32     |  91.2% |  81.5% |   +9.7pp
    CM   | Cameroon             | afrinic  | 29     |  95.8% |  86.2% |   +9.6pp
    ZM   | Zambia               | afrinic  | 22     | 100.0% |  90.9% |   +9.1pp
    MY   | Malaysia             | apnic    | 406    |  53.7% |  45.6% |   +8.1pp
    IM   | Isle of Man          | ripencc  | 26     |  75.9% |  68.0% |   +7.9pp
    KH   | Cambodia             | apnic    | 143    |  84.8% |  77.0% |   +7.8pp
    IL   | Israel               | ripencc  | 385    |  75.2% |  68.6% |   +6.6pp
    SD   | Sudan                | afrinic  | 11     |  70.0% |  63.6% |   +6.4pp
    AO   | Angola               | afrinic  | 70     |  83.3% |  77.1% |   +6.2pp
    Decliners:
    AL   | Albania              | ripencc  | 132    |  71.3% |  96.6% |  -25.3pp
    PR   | Puerto Rico          | arin     | 123    |  29.2% |  46.7% |  -17.5pp
    FJ   | Fiji                 | apnic    | 20     |  86.4% | 100.0% |  -13.6pp
    MO   | Macao                | apnic    | 15     |  65.2% |  75.3% |  -10.1pp
    VE   | Venezuela            | lacnic   | 259    |  86.1% |  95.3% |   -9.2pp
    AM   | Armenia              | ripencc  | 154    |  85.1% |  94.2% |   -9.1pp
    MM   | Myanmar              | apnic    | 171    |  90.6% |  95.9% |   -5.3pp
    ES   | Spain                | ripencc  | 1169   |  81.1% |  85.9% |   -4.8pp
    BB   | Barbados             | arin     | 10     |  13.6% |  18.2% |   -4.6pp
    UY   | Uruguay              | lacnic   | 45     |  44.8% |  49.3% |   -4.5pp
    MP   | Northern Mariana Isl | apnic    | 2      |  15.0% |  19.0% |   -4.0pp
    JM   | Jamaica              | arin     | 15     |  65.0% |  68.2% |   -3.2pp
    UZ   | Uzbekistan           | ripencc  | 129    |  86.2% |  89.1% |   -2.9pp
    RW   | Rwanda               | afrinic  | 28     |  15.3% |  18.0% |   -2.7pp
    CD   | Congo, The Democrati | afrinic  | 51     |  26.3% |  28.8% |   -2.5pp

    ====================================================================================================
     BIGGEST MOVERS — 6mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 6mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    CN   | China                | apnic    | 6503   |  97.3% |  13.0% |  +84.3pp
    RO   | Romania              | ripencc  | 1084   |  64.3% |  24.7% |  +39.6pp
    JM   | Jamaica              | arin     | 15     |  65.0% |  32.4% |  +32.6pp
    TH   | Thailand             | apnic    | 621    |  88.3% |  57.0% |  +31.3pp
    TJ   | Tajikistan           | ripencc  | 42     |  73.9% |  50.0% |  +23.9pp
    MA   | Morocco              | afrinic  | 32     |  43.5% |  21.1% |  +22.4pp
    ZM   | Zambia               | afrinic  | 22     | 100.0% |  80.0% |  +20.0pp
    BD   | Bangladesh           | apnic    | 2022   |  85.7% |  67.5% |  +18.2pp
    SD   | Sudan                | afrinic  | 11     |  70.0% |  53.3% |  +16.7pp
    IR   | Iran                 | ripencc  | 855    |  94.2% |  77.8% |  +16.4pp
    NI   | Nicaragua            | lacnic   | 30     |  98.7% |  82.6% |  +16.1pp
    UG   | Uganda               | afrinic  | 59     |  89.5% |  74.7% |  +14.8pp
    MZ   | Mozambique           | afrinic  | 31     |  47.8% |  34.6% |  +13.2pp
    UY   | Uruguay              | lacnic   | 45     |  44.8% |  31.7% |  +13.1pp
    AZ   | Azerbaijan           | ripencc  | 119    |  86.3% |  74.6% |  +11.7pp
    Decliners:
    KE   | Kenya                | afrinic  | 246    |  29.4% |  80.7% |  -51.3pp
    AE   | United Arab Emirates | ripencc  | 212    |  48.4% |  95.4% |  -47.0pp
    BB   | Barbados             | arin     | 10     |  13.6% |  57.1% |  -43.5pp
    AL   | Albania              | ripencc  | 132    |  71.3% |  97.7% |  -26.4pp
    BT   | Bhutan               | apnic    | 43     |  72.5% |  97.7% |  -25.2pp
    PR   | Puerto Rico          | arin     | 123    |  29.2% |  44.8% |  -15.6pp
    FJ   | Fiji                 | apnic    | 20     |  86.4% | 100.0% |  -13.6pp
    ES   | Spain                | ripencc  | 1169   |  81.1% |  92.4% |  -11.3pp
    MO   | Macao                | apnic    | 15     |  65.2% |  76.3% |  -11.1pp
    PS   | Palestine, State of  | ripencc  | 69     |  86.4% |  95.2% |   -8.8pp
    NG   | Nigeria              | afrinic  | 266    |  41.6% |  49.5% |   -7.9pp
    LY   | Libya                | afrinic  | 27     |  90.4% |  98.2% |   -7.8pp
    VE   | Venezuela            | lacnic   | 259    |  86.1% |  93.8% |   -7.7pp
    LI   | Liechtenstein        | ripencc  | 29     |  77.8% |  85.2% |   -7.4pp
    SA   | Saudi Arabia         | ripencc  | 200    |  86.0% |  92.4% |   -6.4pp

    ====================================================================================================
     BIGGEST MOVERS — 12mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 12mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    CN   | China                | apnic    | 6503   |  97.3% |   2.1% |  +95.2pp
    CH   | Switzerland          | ripencc  | 1062   |  81.7% |  16.4% |  +65.3pp
    SO   | Somalia              | afrinic  | 22     |  85.2% |  21.4% |  +63.8pp
    SD   | Sudan                | afrinic  | 11     |  70.0% |  33.3% |  +36.7pp
    JM   | Jamaica              | arin     | 15     |  65.0% |  32.4% |  +32.6pp
    SI   | Slovenia             | ripencc  | 305    |  75.9% |  48.9% |  +27.0pp
    MA   | Morocco              | afrinic  | 32     |  43.5% |  17.8% |  +25.7pp
    DE   | Germany              | ripencc  | 3262   |  82.5% |  61.4% |  +21.1pp
    TJ   | Tajikistan           | ripencc  | 42     |  73.9% |  53.3% |  +20.6pp
    SC   | Seychelles           | ripencc  | 87     |  81.5% |  61.8% |  +19.7pp
    CA   | Canada               | arin     | 2528   |  73.7% |  57.9% |  +15.8pp
    AZ   | Azerbaijan           | ripencc  | 119    |  86.3% |  70.8% |  +15.5pp
    ZM   | Zambia               | afrinic  | 22     | 100.0% |  84.6% |  +15.4pp
    IN   | India                | apnic    | 6197   |  86.2% |  71.3% |  +14.9pp
    BM   | Bermuda              | arin     | 22     |  78.3% |  63.6% |  +14.7pp
    Decliners:
    KE   | Kenya                | afrinic  | 246    |  29.4% |  79.5% |  -50.1pp
    AE   | United Arab Emirates | ripencc  | 212    |  48.4% |  90.6% |  -42.2pp
    MO   | Macao                | apnic    | 15     |  65.2% |  95.8% |  -30.6pp
    RO   | Romania              | ripencc  | 1084   |  64.3% |  94.4% |  -30.1pp
    BT   | Bhutan               | apnic    | 43     |  72.5% | 100.0% |  -27.5pp
    AL   | Albania              | ripencc  | 132    |  71.3% |  97.5% |  -26.2pp
    ZW   | Zimbabwe             | afrinic  | 28     |  14.9% |  36.8% |  -21.9pp
    ZA   | South Africa         | afrinic  | 751    |  35.2% |  51.9% |  -16.7pp
    IE   | Ireland              | ripencc  | 285    |  73.0% |  89.0% |  -16.0pp
    FJ   | Fiji                 | apnic    | 20     |  86.4% | 100.0% |  -13.6pp
    SA   | Saudi Arabia         | ripencc  | 200    |  86.0% |  98.5% |  -12.5pp
    PR   | Puerto Rico          | arin     | 123    |  29.2% |  41.6% |  -12.4pp
    NG   | Nigeria              | afrinic  | 266    |  41.6% |  52.5% |  -10.9pp
    VE   | Venezuela            | lacnic   | 259    |  86.1% |  95.7% |   -9.6pp
    ES   | Spain                | ripencc  | 1169   |  81.1% |  89.8% |   -8.7pp

    ====================================================================================================
     BIGGEST MOVERS — 24mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 24mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    CN   | China                | apnic    | 6503   |  97.3% |   1.7% |  +95.6pp
    IS   | Iceland              | ripencc  | 87     |  92.6% |  24.8% |  +67.8pp
    JP   | Japan                | apnic    | 981    |  83.3% |  17.6% |  +65.7pp
    GH   | Ghana                | afrinic  | 104    |  89.5% |  38.5% |  +51.0pp
    JM   | Jamaica              | arin     | 15     |  65.0% |  18.2% |  +46.8pp
    SC   | Seychelles           | ripencc  | 87     |  81.5% |  40.6% |  +40.9pp
    UZ   | Uzbekistan           | ripencc  | 129    |  86.2% |  45.5% |  +40.7pp
    IE   | Ireland              | ripencc  | 285    |  73.0% |  35.1% |  +37.9pp
    MC   | Monaco               | ripencc  | 4      |  91.3% |  56.2% |  +35.1pp
    AZ   | Azerbaijan           | ripencc  | 119    |  86.3% |  52.8% |  +33.5pp
    SI   | Slovenia             | ripencc  | 305    |  75.9% |  45.3% |  +30.6pp
    SD   | Sudan                | afrinic  | 11     |  70.0% |  40.0% |  +30.0pp
    TT   | Trinidad and Tobago  | lacnic   | 16     |  63.6% |  34.8% |  +28.8pp
    BM   | Bermuda              | arin     | 22     |  78.3% |  50.0% |  +28.3pp
    IN   | India                | apnic    | 6197   |  86.2% |  59.9% |  +26.3pp
    Decliners:
    CD   | Congo, The Democrati | afrinic  | 51     |  26.3% |  83.9% |  -57.6pp
    KE   | Kenya                | afrinic  | 246    |  29.4% |  80.0% |  -50.6pp
    ZW   | Zimbabwe             | afrinic  | 28     |  14.9% |  63.2% |  -48.3pp
    MU   | Mauritius            | afrinic  | 40     |   2.6% |  40.6% |  -38.0pp
    MA   | Morocco              | afrinic  | 32     |  43.5% |  77.0% |  -33.5pp
    MZ   | Mozambique           | afrinic  | 31     |  47.8% |  81.2% |  -33.4pp
    MO   | Macao                | apnic    | 15     |  65.2% |  96.4% |  -31.2pp
    BT   | Bhutan               | apnic    | 43     |  72.5% | 100.0% |  -27.5pp
    AL   | Albania              | ripencc  | 132    |  71.3% |  98.2% |  -26.9pp
    ZA   | South Africa         | afrinic  | 751    |  35.2% |  60.2% |  -25.0pp
    PR   | Puerto Rico          | arin     | 123    |  29.2% |  53.1% |  -23.9pp
    VI   | Virgin Islands, U.S. | arin     | 12     |  67.9% |  90.5% |  -22.6pp
    TZ   | Tanzania             | afrinic  | 116    |  32.4% |  50.0% |  -17.6pp
    RO   | Romania              | ripencc  | 1084   |  64.3% |  80.6% |  -16.3pp
    UY   | Uruguay              | lacnic   | 45     |  44.8% |  57.4% |  -12.6pp

    ====================================================================================================
     SPOTLIGHT: CHINA (CN)
    ====================================================================================================
    ASNs: 6503  |  RIR: apnic
    IPv4:
      Now  : 89.3% of IPv4 route objects covered by a valid ROA
      3mo  : 88.0% of IPv4 route objects covered by a valid ROA
      6mo  : 4.4% of IPv4 route objects covered by a valid ROA
      12mo : 3.9% of IPv4 route objects covered by a valid ROA
      24mo : 2.9% of IPv4 route objects covered by a valid ROA
    IPv6:
      Now  : 97.3% of IPv6 route objects covered by a valid ROA
      3mo  : 95.7% of IPv6 route objects covered by a valid ROA
      6mo  : 13.0% of IPv6 route objects covered by a valid ROA
      12mo : 2.1% of IPv6 route objects covered by a valid ROA
      24mo : 1.7% of IPv6 route objects covered by a valid ROA
