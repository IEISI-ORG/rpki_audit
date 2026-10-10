    [*] Fetching APNIC Labs ROA-coverage snapshots...
        - Now   (reported date 07/10/2026): 278 countries/regions
        - 3mo   (reported date 11/07/2026): 278 countries/regions
        - 6mo   (reported date 11/04/2026): 279 countries/regions
        - 12mo  (reported date 11/10/2025): 279 countries/regions
        - 24mo  (reported date 11/10/2024): 279 countries/regions

    ====================================================================================================
     GLOBAL ROA COVERAGE TREND (IPv4 Route Objects, % Valid)
    ====================================================================================================
    Period   | Reported Date  | % Valid  | Total Route Objects
    ------------------------------------------------------------
    Now      | 07/10/2026     |   68.7% |  1,278,948
    3mo      | 11/07/2026     |   65.8% |  1,265,733
    6mo      | 11/04/2026     |   58.9% |  1,251,814
    12mo     | 11/10/2025     |   53.6% |  1,254,526
    24mo     | 11/10/2024     |   48.0% |  1,188,598

    ====================================================================================================
     GLOBAL ROA COVERAGE TREND (IPv6 Route Objects, % Valid)
    ====================================================================================================
    Period   | Reported Date  | % Valid  | Total Route Objects
    ------------------------------------------------------------
    Now      | 07/10/2026     |   75.6% |    319,804
    3mo      | 11/07/2026     |   74.0% |    313,201
    6mo      | 11/04/2026     |   62.5% |    303,246
    12mo     | 11/10/2025     |   57.9% |    296,577
    24mo     | 11/10/2024     |   55.6% |    260,203

    NOTE: IPv4 and IPv6 are reported separately because they are measured
    separately by APNIC and can diverge significantly per network — do not
    average or add them into one 'global ROA coverage' number.

    ====================================================================================================
     RIR ROA COVERAGE TREND (IPv4 Route Objects, % Valid, weighted by route-object count)
    ====================================================================================================
    RIR        | ASNs (now) |     Now |     3mo |     6mo |    12mo |    24mo
    -------------------------------------------------------------------------
    afrinic    | 2,170      |   65.3% |   60.9% |   58.1% |   37.9% |   32.2%
    apnic      | 16,818     |   76.9% |   74.1% |   54.9% |   49.0% |   45.7%
    arin       | 20,447     |   54.7% |   51.3% |   48.9% |   42.9% |   33.9%
    lacnic     | 12,621     |   69.1% |   63.0% |   58.4% |   59.2% |   54.6%
    ripencc    | 30,831     |   74.9% |   74.5% |   73.6% |   68.3% |   61.7%

    ====================================================================================================
     RIR ROA COVERAGE TREND (IPv6 Route Objects, % Valid, weighted by route-object count)
    ====================================================================================================
    RIR        | ASNs (now) |     Now |     3mo |     6mo |    12mo |    24mo
    -------------------------------------------------------------------------
    afrinic    | 2,170      |   41.7% |   38.8% |   40.6% |   35.1% |   66.9%
    apnic      | 16,818     |   83.5% |   81.5% |   51.3% |   49.3% |   39.4%
    arin       | 20,447     |   76.3% |   76.5% |   75.5% |   67.0% |   62.5%
    lacnic     | 12,621     |   65.7% |   61.2% |   60.0% |   57.5% |   55.9%
    ripencc    | 30,831     |   77.4% |   77.5% |   76.6% |   66.1% |   76.0%

    [+] Full per-country trend data (IPv4 + IPv6) saved to roa_signing_trends.csv

    ====================================================================================================
     BIGGEST MOVERS — 3mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 3mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    TG   | Togo                 | afrinic  | 9      |  62.3% |  10.2% |  +52.1pp
    TJ   | Tajikistan           | ripencc  | 39     |  85.1% |  36.8% |  +48.3pp
    MX   | Mexico               | lacnic   | 539    |  78.1% |  44.8% |  +33.3pp
    KI   | Kiribati             | apnic    | 3      |  90.9% |  63.2% |  +27.7pp
    CD   | Congo, The Democrati | afrinic  | 39     |  56.1% |  38.2% |  +17.9pp
    KE   | Kenya                | afrinic  | 229    |  77.0% |  59.4% |  +17.6pp
    SO   | Somalia              | afrinic  | 19     |  82.8% |  65.5% |  +17.3pp
    NG   | Nigeria              | afrinic  | 232    |  58.8% |  42.6% |  +16.2pp
    AU   | Australia            | apnic    | 1688   |  51.1% |  36.5% |  +14.6pp
    BJ   | Benin                | afrinic  | 16     |  69.3% |  55.8% |  +13.5pp
    YT   | Mayotte              | afrinic  | 1      |  75.9% |  63.2% |  +12.7pp
    MA   | Morocco              | afrinic  | 29     |  15.3% |   3.2% |  +12.1pp
    SL   | Sierra Leone         | afrinic  | 17     |  69.8% |  58.6% |  +11.2pp
    GQ   | Equatorial Guinea    | afrinic  | 7      |  60.0% |  51.3% |   +8.7pp
    VG   | Virgin Islands, Brit | ripencc  | 36     |  51.6% |  43.5% |   +8.1pp
    Decliners:
    IT   | Italy                | ripencc  | 1126   |  50.6% |  68.5% |  -17.9pp
    MG   | Madagascar           | afrinic  | 5      |  28.1% |  42.0% |  -13.9pp
    LY   | Libya                | afrinic  | 25     |  63.7% |  71.7% |   -8.0pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  76.9% |  83.8% |   -6.9pp
    CV   | Cabo Verde           | afrinic  | 7      |  35.4% |  40.6% |   -5.2pp
    KY   | Cayman Islands       | arin     | 10     |  49.5% |  54.6% |   -5.1pp
    MK   | North Macedonia      | ripencc  | 60     |  46.9% |  50.4% |   -3.5pp
    CF   | Central African Repu | afrinic  | 4      |  16.0% |  19.2% |   -3.2pp
    LR   | Liberia              | afrinic  | 14     |  41.1% |  44.3% |   -3.2pp
    BQ   | Bonaire, Sint Eustat | lacnic   | 5      |  80.4% |  83.3% |   -2.9pp
    PE   | Peru                 | lacnic   | 190    |  35.5% |  38.3% |   -2.8pp
    GU   | Guam                 | apnic    | 7      |  78.6% |  81.2% |   -2.6pp
    VE   | Venezuela            | lacnic   | 213    |  91.7% |  94.3% |   -2.6pp
    KN   | Saint Kitts and Nevi | arin     | 9      |  12.5% |  15.1% |   -2.6pp
    GP   | Guadeloupe           | arin     | 5      |  91.0% |  93.4% |   -2.4pp

    ====================================================================================================
     BIGGEST MOVERS — 6mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 6mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    DJ   | Djibouti             | afrinic  | 3      |  96.1% |   5.6% |  +90.5pp
    CN   | China                | apnic    | 1341   |  89.4% |   5.0% |  +84.4pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  76.9% |   5.9% |  +71.0pp
    CM   | Cameroon             | afrinic  | 21     |  94.9% |  35.3% |  +59.6pp
    TJ   | Tajikistan           | ripencc  | 39     |  85.1% |  37.1% |  +48.0pp
    JE   | Jersey               | ripencc  | 9      |  92.1% |  53.8% |  +38.3pp
    TT   | Trinidad and Tobago  | lacnic   | 14     |  91.6% |  54.6% |  +37.0pp
    MX   | Mexico               | lacnic   | 539    |  78.1% |  42.0% |  +36.1pp
    SO   | Somalia              | afrinic  | 19     |  82.8% |  52.9% |  +29.9pp
    MT   | Malta                | ripencc  | 44     |  53.8% |  25.2% |  +28.6pp
    KI   | Kiribati             | apnic    | 3      |  90.9% |  63.2% |  +27.7pp
    GG   | Guernsey             | ripencc  | 7      |  71.0% |  49.3% |  +21.7pp
    KE   | Kenya                | afrinic  | 229    |  77.0% |  57.6% |  +19.4pp
    CD   | Congo, The Democrati | afrinic  | 39     |  56.1% |  37.0% |  +19.1pp
    BW   | Botswana             | afrinic  | 29     |  74.4% |  55.4% |  +19.0pp
    Decliners:
    CV   | Cabo Verde           | afrinic  | 7      |  35.4% |  86.7% |  -51.3pp
    MG   | Madagascar           | afrinic  | 5      |  28.1% |  45.5% |  -17.4pp
    IT   | Italy                | ripencc  | 1126   |  50.6% |  65.9% |  -15.3pp
    LY   | Libya                | afrinic  | 25     |  63.7% |  71.5% |   -7.8pp
    SD   | Sudan                | afrinic  | 9      |  39.4% |  45.9% |   -6.5pp
    KY   | Cayman Islands       | arin     | 10     |  49.5% |  55.2% |   -5.7pp
    UZ   | Uzbekistan           | ripencc  | 108    |  72.6% |  77.3% |   -4.7pp
    MK   | North Macedonia      | ripencc  | 60     |  46.9% |  51.3% |   -4.4pp
    NE   | Niger                | afrinic  | 7      |  15.5% |  19.5% |   -4.0pp
    MP   | Northern Mariana Isl | apnic    | 1      |  94.7% |  98.1% |   -3.4pp
    GL   | Greenland            | ripencc  | 1      |  77.1% |  79.4% |   -2.3pp
    PE   | Peru                 | lacnic   | 190    |  35.5% |  37.7% |   -2.2pp
    AS   | American Samoa       | apnic    | 2      |  18.2% |  20.3% |   -2.1pp
    GP   | Guadeloupe           | arin     | 5      |  91.0% |  92.6% |   -1.6pp
    FM   | Micronesia, Federate | apnic    | 5      |  85.0% |  86.4% |   -1.4pp

    ====================================================================================================
     BIGGEST MOVERS — 12mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 12mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    CK   | Cook Islands         | apnic    | 2      | 100.0% |   5.0% |  +95.0pp
    DJ   | Djibouti             | afrinic  | 3      |  96.1% |   2.9% |  +93.2pp
    EG   | Egypt                | afrinic  | 74     |  95.5% |   7.6% |  +87.9pp
    CN   | China                | apnic    | 1341   |  89.4% |   3.8% |  +85.6pp
    PK   | Pakistan             | apnic    | 307    |  93.0% |  15.4% |  +77.6pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  76.9% |   3.1% |  +73.8pp
    BJ   | Benin                | afrinic  | 16     |  69.3% |   5.7% |  +63.6pp
    CM   | Cameroon             | afrinic  | 21     |  94.9% |  31.7% |  +63.2pp
    SO   | Somalia              | afrinic  | 19     |  82.8% |  19.7% |  +63.1pp
    TJ   | Tajikistan           | ripencc  | 39     |  85.1% |  27.4% |  +57.7pp
    HT   | Haiti                | lacnic   | 4      |  55.9% |   3.7% |  +52.2pp
    JE   | Jersey               | ripencc  | 9      |  92.1% |  42.4% |  +49.7pp
    KI   | Kiribati             | apnic    | 3      |  90.9% |  42.9% |  +48.0pp
    LS   | Lesotho              | afrinic  | 7      |  72.6% |  30.1% |  +42.5pp
    KZ   | Kazakhstan           | ripencc  | 218    |  80.1% |  38.8% |  +41.3pp
    Decliners:
    CV   | Cabo Verde           | afrinic  | 7      |  35.4% |  84.9% |  -49.5pp
    MG   | Madagascar           | afrinic  | 5      |  28.1% |  52.9% |  -24.8pp
    IE   | Ireland              | ripencc  | 209    |  66.2% |  78.5% |  -12.3pp
    AO   | Angola               | afrinic  | 67     |  49.1% |  57.8% |   -8.7pp
    GT   | Guatemala            | lacnic   | 64     |  82.4% |  90.6% |   -8.2pp
    BF   | Burkina Faso         | afrinic  | 26     |  81.2% |  89.3% |   -8.1pp
    KY   | Cayman Islands       | arin     | 10     |  49.5% |  56.7% |   -7.2pp
    PY   | Paraguay             | lacnic   | 97     |  75.6% |  82.8% |   -7.2pp
    GL   | Greenland            | ripencc  | 1      |  77.1% |  83.3% |   -6.2pp
    KM   | Comoros              | afrinic  | 4      |  76.5% |  80.8% |   -4.3pp
    KN   | Saint Kitts and Nevi | arin     | 9      |  12.5% |  16.2% |   -3.7pp
    ME   | Montenegro           | ripencc  | 22     |  49.0% |  52.6% |   -3.6pp
    MP   | Northern Mariana Isl | apnic    | 1      |  94.7% |  98.3% |   -3.6pp
    UZ   | Uzbekistan           | ripencc  | 108    |  72.6% |  76.2% |   -3.6pp
    MU   | Mauritius            | afrinic  | 27     |  81.2% |  84.3% |   -3.1pp

    ====================================================================================================
     BIGGEST MOVERS — 24mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 24mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    CK   | Cook Islands         | apnic    | 2      | 100.0% |   3.7% |  +96.3pp
    DJ   | Djibouti             | afrinic  | 3      |  96.1% |   1.0% |  +95.1pp
    EG   | Egypt                | afrinic  | 74     |  95.5% |   7.7% |  +87.8pp
    CN   | China                | apnic    | 1341   |  89.4% |   2.9% |  +86.5pp
    CM   | Cameroon             | afrinic  | 21     |  94.9% |  13.8% |  +81.1pp
    FM   | Micronesia, Federate | apnic    | 5      |  85.0% |   4.8% |  +80.2pp
    PK   | Pakistan             | apnic    | 307    |  93.0% |  15.0% |  +78.0pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  76.9% |   0.0% |  +76.9pp
    CI   | Côte d'Ivoire        | afrinic  | 18     |  94.3% |  19.7% |  +74.6pp
    IS   | Iceland              | ripencc  | 72     |  75.7% |   1.7% |  +74.0pp
    SO   | Somalia              | afrinic  | 19     |  82.8% |  13.0% |  +69.8pp
    JE   | Jersey               | ripencc  | 9      |  92.1% |  25.0% |  +67.1pp
    BJ   | Benin                | afrinic  | 16     |  69.3% |   3.4% |  +65.9pp
    SL   | Sierra Leone         | afrinic  | 17     |  69.8% |   7.8% |  +62.0pp
    TJ   | Tajikistan           | ripencc  | 39     |  85.1% |  24.0% |  +61.1pp
    Decliners:
    CV   | Cabo Verde           | afrinic  | 7      |  35.4% |  83.0% |  -47.6pp
    SD   | Sudan                | afrinic  | 9      |  39.4% |  60.6% |  -21.2pp
    PE   | Peru                 | lacnic   | 190    |  35.5% |  52.4% |  -16.9pp
    KM   | Comoros              | afrinic  | 4      |  76.5% |  90.5% |  -14.0pp
    LY   | Libya                | afrinic  | 25     |  63.7% |  76.8% |  -13.1pp
    IE   | Ireland              | ripencc  | 209    |  66.2% |  75.4% |   -9.2pp
    SK   | Slovakia             | ripencc  | 199    |  44.4% |  52.5% |   -8.1pp
    AO   | Angola               | afrinic  | 67     |  49.1% |  56.6% |   -7.5pp
    PY   | Paraguay             | lacnic   | 97     |  75.6% |  82.6% |   -7.0pp
    MZ   | Mozambique           | afrinic  | 31     |  15.5% |  21.9% |   -6.4pp
    CG   | Congo                | afrinic  | 10     |  16.2% |  21.9% |   -5.7pp
    ME   | Montenegro           | ripencc  | 22     |  49.0% |  54.4% |   -5.4pp
    BF   | Burkina Faso         | afrinic  | 26     |  81.2% |  86.4% |   -5.2pp
    GL   | Greenland            | ripencc  | 1      |  77.1% |  80.6% |   -3.5pp
    VU   | Vanuatu              | apnic    | 11     |  91.5% |  94.9% |   -3.4pp

    ====================================================================================================
     BIGGEST MOVERS — 3mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 3mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    TJ   | Tajikistan           | ripencc  | 39     |  92.3% |  50.0% |  +42.3pp
    TH   | Thailand             | apnic    | 466    |  88.5% |  58.9% |  +29.6pp
    MA   | Morocco              | afrinic  | 29     |  44.4% |  21.6% |  +22.8pp
    MX   | Mexico               | lacnic   | 539    |  82.7% |  60.4% |  +22.3pp
    AZ   | Azerbaijan           | ripencc  | 99     |  87.8% |  72.7% |  +15.1pp
    SC   | Seychelles           | ripencc  | 68     |  83.2% |  68.3% |  +14.9pp
    VI   | Virgin Islands, U.S. | arin     | 6      |  73.8% |  62.1% |  +11.7pp
    MZ   | Mozambique           | afrinic  | 31     |  47.8% |  37.0% |  +10.8pp
    PH   | Philippines          | apnic    | 466    |  82.1% |  71.9% |  +10.2pp
    LK   | Sri Lanka            | apnic    | 23     |  89.7% |  81.1% |   +8.6pp
    NZ   | New Zealand          | apnic    | 428    |  73.2% |  64.7% |   +8.5pp
    MY   | Malaysia             | apnic    | 262    |  53.9% |  45.6% |   +8.3pp
    SD   | Sudan                | afrinic  | 9      |  73.9% |  66.7% |   +7.2pp
    KH   | Cambodia             | apnic    | 98     |  84.8% |  77.7% |   +7.1pp
    AR   | Argentina            | lacnic   | 1078   |  69.6% |  62.6% |   +7.0pp
    Decliners:
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  33.3% |  -25.6pp
    AL   | Albania              | ripencc  | 124    |  71.8% |  95.9% |  -24.1pp
    PR   | Puerto Rico          | arin     | 96     |  29.6% |  47.0% |  -17.4pp
    LA   | Laos                 | apnic    | 29     |  77.3% |  91.4% |  -14.1pp
    FJ   | Fiji                 | apnic    | 15     |  87.0% | 100.0% |  -13.0pp
    MM   | Myanmar              | apnic    | 132    |  90.3% |  99.2% |   -8.9pp
    AM   | Armenia              | ripencc  | 130    |  85.1% |  93.5% |   -8.4pp
    VE   | Venezuela            | lacnic   | 213    |  87.7% |  95.4% |   -7.7pp
    PT   | Portugal             | ripencc  | 144    |  87.2% |  93.5% |   -6.3pp
    UY   | Uruguay              | lacnic   | 30     |  43.1% |  49.3% |   -6.2pp
    RO   | Romania              | ripencc  | 925    |  64.2% |  69.3% |   -5.1pp
    ES   | Spain                | ripencc  | 965    |  81.1% |  85.9% |   -4.8pp
    BB   | Barbados             | arin     | 7      |  13.6% |  18.2% |   -4.6pp
    HN   | Honduras             | lacnic   | 100    |  91.6% |  95.7% |   -4.1pp
    MP   | Northern Mariana Isl | apnic    | 1      |  15.0% |  19.0% |   -4.0pp

    ====================================================================================================
     BIGGEST MOVERS — 6mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 6mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    CN   | China                | apnic    | 1341   |  96.9% |  13.1% |  +83.8pp
    TJ   | Tajikistan           | ripencc  | 39     |  92.3% |  50.0% |  +42.3pp
    RO   | Romania              | ripencc  | 925    |  64.2% |  25.1% |  +39.1pp
    TH   | Thailand             | apnic    | 466    |  88.5% |  57.2% |  +31.3pp
    MX   | Mexico               | lacnic   | 539    |  82.7% |  58.1% |  +24.6pp
    MA   | Morocco              | afrinic  | 29     |  44.4% |  21.1% |  +23.3pp
    ZM   | Zambia               | afrinic  | 18     | 100.0% |  80.0% |  +20.0pp
    PH   | Philippines          | apnic    | 466    |  82.1% |  63.3% |  +18.8pp
    SD   | Sudan                | afrinic  | 9      |  73.9% |  55.6% |  +18.3pp
    NI   | Nicaragua            | lacnic   | 23     |  98.7% |  82.6% |  +16.1pp
    UG   | Uganda               | afrinic  | 55     |  90.0% |  74.7% |  +15.3pp
    MZ   | Mozambique           | afrinic  | 31     |  47.8% |  33.3% |  +14.5pp
    AZ   | Azerbaijan           | ripencc  | 99     |  87.8% |  73.4% |  +14.4pp
    BD   | Bangladesh           | apnic    | 1552   |  85.6% |  71.7% |  +13.9pp
    KG   | Kyrgyzstan           | ripencc  | 61     |  92.9% |  81.8% |  +11.1pp
    Decliners:
    KE   | Kenya                | afrinic  | 229    |  31.8% |  81.4% |  -49.6pp
    AE   | United Arab Emirates | ripencc  | 165    |  48.3% |  95.4% |  -47.1pp
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  33.3% |  -25.6pp
    AL   | Albania              | ripencc  | 124    |  71.8% |  97.2% |  -25.4pp
    PR   | Puerto Rico          | arin     | 96     |  29.6% |  45.5% |  -15.9pp
    LA   | Laos                 | apnic    | 29     |  77.3% |  91.3% |  -14.0pp
    FJ   | Fiji                 | apnic    | 15     |  87.0% | 100.0% |  -13.0pp
    MO   | Macao                | apnic    | 11     |  65.2% |  76.6% |  -11.4pp
    PS   | Palestine, State of  | ripencc  | 45     |  86.4% |  95.2% |   -8.8pp
    UY   | Uruguay              | lacnic   | 30     |  43.1% |  51.2% |   -8.1pp
    NG   | Nigeria              | afrinic  | 232    |  42.6% |  50.0% |   -7.4pp
    VE   | Venezuela            | lacnic   | 213    |  87.7% |  94.0% |   -6.3pp
    LI   | Liechtenstein        | ripencc  | 26     |  79.2% |  85.4% |   -6.2pp
    MM   | Myanmar              | apnic    | 132    |  90.3% |  96.3% |   -6.0pp
    PK   | Pakistan             | apnic    | 307    |  91.2% |  96.8% |   -5.6pp

    ====================================================================================================
     BIGGEST MOVERS — 12mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 12mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    CN   | China                | apnic    | 1341   |  96.9% |   2.1% |  +94.8pp
    CH   | Switzerland          | ripencc  | 797    |  82.3% |  16.5% |  +65.8pp
    SO   | Somalia              | afrinic  | 19     |  82.1% |  21.4% |  +60.7pp
    SD   | Sudan                | afrinic  | 9      |  73.9% |  33.3% |  +40.6pp
    CM   | Cameroon             | afrinic  | 21     |  91.7% |  54.5% |  +37.2pp
    TJ   | Tajikistan           | ripencc  | 39     |  92.3% |  57.1% |  +35.2pp
    JM   | Jamaica              | arin     | 10     |  65.0% |  30.6% |  +34.4pp
    SI   | Slovenia             | ripencc  | 271    |  76.9% |  48.3% |  +28.6pp
    SC   | Seychelles           | ripencc  | 68     |  83.2% |  56.7% |  +26.5pp
    MA   | Morocco              | afrinic  | 29     |  44.4% |  18.4% |  +26.0pp
    MX   | Mexico               | lacnic   | 539    |  82.7% |  59.3% |  +23.4pp
    DE   | Germany              | ripencc  | 2614   |  82.2% |  62.2% |  +20.0pp
    PH   | Philippines          | apnic    | 466    |  82.1% |  63.8% |  +18.3pp
    CA   | Canada               | arin     | 1618   |  73.9% |  56.7% |  +17.2pp
    AZ   | Azerbaijan           | ripencc  | 99     |  87.8% |  70.8% |  +17.0pp
    Decliners:
    KE   | Kenya                | afrinic  | 229    |  31.8% |  77.4% |  -45.6pp
    AE   | United Arab Emirates | ripencc  | 165    |  48.3% |  90.5% |  -42.2pp
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  42.9% |  -35.2pp
    MO   | Macao                | apnic    | 11     |  65.2% |  95.8% |  -30.6pp
    RO   | Romania              | ripencc  | 925    |  64.2% |  94.5% |  -30.3pp
    BT   | Bhutan               | apnic    | 28     |  72.1% | 100.0% |  -27.9pp
    AL   | Albania              | ripencc  | 124    |  71.8% |  97.6% |  -25.8pp
    ZW   | Zimbabwe             | afrinic  | 27     |  14.4% |  36.8% |  -22.4pp
    IE   | Ireland              | ripencc  | 209    |  73.1% |  89.6% |  -16.5pp
    ZA   | South Africa         | afrinic  | 666    |  35.7% |  50.1% |  -14.4pp
    PR   | Puerto Rico          | arin     | 96     |  29.6% |  42.6% |  -13.0pp
    FJ   | Fiji                 | apnic    | 15     |  87.0% | 100.0% |  -13.0pp
    SA   | Saudi Arabia         | ripencc  | 166    |  86.3% |  98.5% |  -12.2pp
    LA   | Laos                 | apnic    | 29     |  77.3% |  89.1% |  -11.8pp
    NG   | Nigeria              | afrinic  | 232    |  42.6% |  52.5% |   -9.9pp

    ====================================================================================================
     BIGGEST MOVERS — 24mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 24mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    CN   | China                | apnic    | 1341   |  96.9% |   1.7% |  +95.2pp
    IS   | Iceland              | ripencc  | 72     |  93.8% |  24.8% |  +69.0pp
    JP   | Japan                | apnic    | 750    |  83.1% |  17.7% |  +65.4pp
    GH   | Ghana                | afrinic  | 94     |  91.0% |  38.5% |  +52.5pp
    JM   | Jamaica              | arin     | 10     |  65.0% |  14.3% |  +50.7pp
    SC   | Seychelles           | ripencc  | 68     |  83.2% |  40.4% |  +42.8pp
    UZ   | Uzbekistan           | ripencc  | 108    |  85.0% |  45.5% |  +39.5pp
    MC   | Monaco               | ripencc  | 4      |  90.9% |  56.2% |  +34.7pp
    AZ   | Azerbaijan           | ripencc  | 99     |  87.8% |  53.1% |  +34.7pp
    SD   | Sudan                | afrinic  | 9      |  73.9% |  40.0% |  +33.9pp
    TJ   | Tajikistan           | ripencc  | 39     |  92.3% |  60.0% |  +32.3pp
    SI   | Slovenia             | ripencc  | 271    |  76.9% |  46.0% |  +30.9pp
    TT   | Trinidad and Tobago  | lacnic   | 14     |  63.6% |  32.8% |  +30.8pp
    BM   | Bermuda              | arin     | 12     |  79.2% |  50.0% |  +29.2pp
    IN   | India                | apnic    | 2944   |  86.3% |  60.2% |  +26.1pp
    Decliners:
    TK   | Tokelau              | ripencc  | 3      |   7.7% | 100.0% |  -92.3pp
    CD   | Congo, The Democrati | afrinic  | 39     |  25.4% |  83.9% |  -58.5pp
    KE   | Kenya                | afrinic  | 229    |  31.8% |  82.3% |  -50.5pp
    ZW   | Zimbabwe             | afrinic  | 27     |  14.4% |  58.8% |  -44.4pp
    AE   | United Arab Emirates | ripencc  | 165    |  48.3% |  89.7% |  -41.4pp
    MZ   | Mozambique           | afrinic  | 31     |  47.8% |  86.7% |  -38.9pp
    MU   | Mauritius            | afrinic  | 27     |   2.6% |  40.6% |  -38.0pp
    MA   | Morocco              | afrinic  | 29     |  44.4% |  76.7% |  -32.3pp
    MO   | Macao                | apnic    | 11     |  65.2% |  96.4% |  -31.2pp
    BT   | Bhutan               | apnic    | 28     |  72.1% | 100.0% |  -27.9pp
    AL   | Albania              | ripencc  | 124    |  71.8% |  98.3% |  -26.5pp
    PR   | Puerto Rico          | arin     | 96     |  29.6% |  54.6% |  -25.0pp
    ZA   | South Africa         | afrinic  | 666    |  35.7% |  60.5% |  -24.8pp
    LA   | Laos                 | apnic    | 29     |  77.3% |  95.2% |  -17.9pp
    VI   | Virgin Islands, U.S. | arin     | 6      |  73.8% |  90.5% |  -16.7pp

    ====================================================================================================
     SPOTLIGHT: CHINA (CN)
    ====================================================================================================
    ASNs: 1341  |  RIR: apnic
    IPv4:
      Now  : 89.4% of IPv4 route objects covered by a valid ROA
      3mo  : 88.2% of IPv4 route objects covered by a valid ROA
      6mo  : 5.0% of IPv4 route objects covered by a valid ROA
      12mo : 3.8% of IPv4 route objects covered by a valid ROA
      24mo : 2.9% of IPv4 route objects covered by a valid ROA
    IPv6:
      Now  : 96.9% of IPv6 route objects covered by a valid ROA
      3mo  : 95.8% of IPv6 route objects covered by a valid ROA
      6mo  : 13.1% of IPv6 route objects covered by a valid ROA
      12mo : 2.1% of IPv6 route objects covered by a valid ROA
      24mo : 1.7% of IPv6 route objects covered by a valid ROA
