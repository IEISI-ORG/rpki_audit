    [*] Fetching APNIC Labs ROA-coverage snapshots...
        - Now   (reported date 15/10/2026): 278 countries/regions
        - 3mo   (reported date 18/07/2026): 278 countries/regions
        - 6mo   (reported date 18/04/2026): 279 countries/regions
        - 12mo  (reported date 18/10/2025): 280 countries/regions
        - 24mo  (reported date 18/10/2024): 279 countries/regions

    ====================================================================================================
     GLOBAL ROA COVERAGE TREND (IPv4 Route Objects, % Valid)
    ====================================================================================================
    Period   | Reported Date  | % Valid  | Total Route Objects
    ------------------------------------------------------------
    Now      | 15/10/2026     |   67.6% |  1,316,817
    3mo      | 18/07/2026     |   65.9% |  1,264,564
    6mo      | 18/04/2026     |   59.1% |  1,255,332
    12mo     | 18/10/2025     |   53.8% |  1,258,337
    24mo     | 18/10/2024     |   48.3% |  1,190,863

    ====================================================================================================
     GLOBAL ROA COVERAGE TREND (IPv6 Route Objects, % Valid)
    ====================================================================================================
    Period   | Reported Date  | % Valid  | Total Route Objects
    ------------------------------------------------------------
    Now      | 15/10/2026     |   76.0% |    318,358
    3mo      | 18/07/2026     |   74.1% |    314,307
    6mo      | 18/04/2026     |   62.7% |    302,145
    12mo     | 18/10/2025     |   57.5% |    296,773
    24mo     | 18/10/2024     |   55.6% |    259,929

    NOTE: IPv4 and IPv6 are reported separately because they are measured
    separately by APNIC and can diverge significantly per network — do not
    average or add them into one 'global ROA coverage' number.

    ====================================================================================================
     RIR ROA COVERAGE TREND (IPv4 Route Objects, % Valid, weighted by route-object count)
    ====================================================================================================
    RIR        | ASNs (now) |     Now |     3mo |     6mo |    12mo |    24mo
    -------------------------------------------------------------------------
    afrinic    | 2,471      |   65.4% |   61.6% |   58.7% |   37.9% |   32.3%
    apnic      | 31,425     |   76.3% |   74.3% |   55.5% |   49.0% |   45.9%
    arin       | 35,540     |   52.2% |   51.4% |   49.0% |   43.4% |   34.0%
    lacnic     | 13,817     |   69.2% |   63.4% |   58.4% |   59.2% |   54.8%
    ripencc    | 38,568     |   74.5% |   74.1% |   73.7% |   68.4% |   62.3%

    ====================================================================================================
     RIR ROA COVERAGE TREND (IPv6 Route Objects, % Valid, weighted by route-object count)
    ====================================================================================================
    RIR        | ASNs (now) |     Now |     3mo |     6mo |    12mo |    24mo
    -------------------------------------------------------------------------
    afrinic    | 2,471      |   41.7% |   39.5% |   41.0% |   35.2% |   65.4%
    apnic      | 31,425     |   83.4% |   81.7% |   51.6% |   48.7% |   39.4%
    arin       | 35,540     |   76.4% |   76.5% |   75.9% |   67.6% |   62.1%
    lacnic     | 13,817     |   67.7% |   61.2% |   59.7% |   56.1% |   56.3%
    ripencc    | 38,568     |   77.4% |   77.7% |   76.7% |   65.9% |   75.9%

    [+] Full per-country trend data (IPv4 + IPv6) saved to roa_signing_trends.csv

    ====================================================================================================
     BIGGEST MOVERS — 3mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 3mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    TG   | Togo                 | afrinic  | 11     |  57.0% |  10.2% |  +46.8pp
    TJ   | Tajikistan           | ripencc  | 43     |  82.3% |  37.4% |  +44.9pp
    MX   | Mexico               | lacnic   | 658    |  78.0% |  45.2% |  +32.8pp
    KI   | Kiribati             | apnic    | 5      |  92.0% |  63.2% |  +28.8pp
    SK   | Slovakia             | ripencc  | 229    |  65.1% |  42.9% |  +22.2pp
    CD   | Congo, The Democrati | afrinic  | 51     |  56.4% |  37.9% |  +18.5pp
    KE   | Kenya                | afrinic  | 247    |  77.1% |  59.5% |  +17.6pp
    SO   | Somalia              | afrinic  | 22     |  82.8% |  65.5% |  +17.3pp
    NG   | Nigeria              | afrinic  | 265    |  58.8% |  42.6% |  +16.2pp
    AU   | Australia            | apnic    | 3001   |  51.9% |  36.6% |  +15.3pp
    YT   | Mayotte              | afrinic  | 1      |  76.7% |  63.2% |  +13.5pp
    GQ   | Equatorial Guinea    | afrinic  | 7      |  58.5% |  45.7% |  +12.8pp
    SL   | Sierra Leone         | afrinic  | 22     |  69.4% |  58.6% |  +10.8pp
    BW   | Botswana             | afrinic  | 33     |  74.8% |  66.3% |   +8.5pp
    DO   | Dominican Republic   | lacnic   | 215    |  81.5% |  73.9% |   +7.6pp
    Decliners:
    MH   | Marshall Islands     | ripencc  | 11     |  52.0% |  94.2% |  -42.2pp
    IT   | Italy                | ripencc  | 1324   |  51.0% |  68.1% |  -17.1pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  75.0% |  83.8% |   -8.8pp
    KY   | Cayman Islands       | arin     | 18     |  49.1% |  55.2% |   -6.1pp
    CV   | Cabo Verde           | afrinic  | 8      |  35.4% |  40.6% |   -5.2pp
    VE   | Venezuela            | lacnic   | 261    |  90.1% |  94.7% |   -4.6pp
    SC   | Seychelles           | ripencc  | 87     |  81.6% |  85.9% |   -4.3pp
    MG   | Madagascar           | afrinic  | 7      |  39.0% |  42.0% |   -3.0pp
    BQ   | Bonaire, Sint Eustat | lacnic   | 6      |  80.4% |  83.3% |   -2.9pp
    SG   | Singapore            | apnic    | 729    |  77.7% |  80.5% |   -2.8pp
    BD   | Bangladesh           | apnic    | 2030   |  93.2% |  96.0% |   -2.8pp
    PE   | Peru                 | lacnic   | 226    |  35.6% |  38.3% |   -2.7pp
    PH   | Philippines          | apnic    | 674    |  88.4% |  91.1% |   -2.7pp
    MK   | North Macedonia      | ripencc  | 69     |  47.6% |  50.3% |   -2.7pp
    KN   | Saint Kitts and Nevi | arin     | 11     |  12.4% |  15.1% |   -2.7pp

    ====================================================================================================
     BIGGEST MOVERS — 6mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 6mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    DJ   | Djibouti             | afrinic  | 4      |  96.1% |   5.6% |  +90.5pp
    CN   | China                | apnic    | 6507   |  89.2% |   6.7% |  +82.5pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  75.0% |   5.9% |  +69.1pp
    CM   | Cameroon             | afrinic  | 30     |  94.5% |  35.8% |  +58.7pp
    TJ   | Tajikistan           | ripencc  | 43     |  82.3% |  37.0% |  +45.3pp
    JE   | Jersey               | ripencc  | 13     |  92.2% |  53.8% |  +38.4pp
    TT   | Trinidad and Tobago  | lacnic   | 16     |  91.8% |  54.6% |  +37.2pp
    MX   | Mexico               | lacnic   | 658    |  78.0% |  42.3% |  +35.7pp
    KI   | Kiribati             | apnic    | 5      |  92.0% |  63.2% |  +28.8pp
    MT   | Malta                | ripencc  | 55     |  53.7% |  25.3% |  +28.4pp
    SO   | Somalia              | afrinic  | 22     |  82.8% |  59.9% |  +22.9pp
    GG   | Guernsey             | ripencc  | 11     |  70.6% |  49.3% |  +21.3pp
    SK   | Slovakia             | ripencc  | 229    |  65.1% |  44.9% |  +20.2pp
    BW   | Botswana             | afrinic  | 33     |  74.8% |  55.0% |  +19.8pp
    KE   | Kenya                | afrinic  | 247    |  77.1% |  57.7% |  +19.4pp
    Decliners:
    CV   | Cabo Verde           | afrinic  | 8      |  35.4% |  86.9% |  -51.5pp
    MH   | Marshall Islands     | ripencc  | 11     |  52.0% |  91.7% |  -39.7pp
    IT   | Italy                | ripencc  | 1324   |  51.0% |  66.5% |  -15.5pp
    SD   | Sudan                | afrinic  | 11     |  38.9% |  46.0% |   -7.1pp
    MG   | Madagascar           | afrinic  | 7      |  39.0% |  45.9% |   -6.9pp
    KY   | Cayman Islands       | arin     | 18     |  49.1% |  55.2% |   -6.1pp
    SC   | Seychelles           | ripencc  | 87     |  81.6% |  87.4% |   -5.8pp
    NE   | Niger                | afrinic  | 7      |  16.4% |  21.4% |   -5.0pp
    MP   | Northern Mariana Isl | apnic    | 2      |  93.3% |  98.2% |   -4.9pp
    UZ   | Uzbekistan           | ripencc  | 129    |  72.7% |  77.5% |   -4.8pp
    TG   | Togo                 | afrinic  | 11     |  57.0% |  61.7% |   -4.7pp
    KM   | Comoros              | afrinic  | 4      |  74.3% |  78.6% |   -4.3pp
    AE   | United Arab Emirates | ripencc  | 216    |  81.4% |  85.5% |   -4.1pp
    MK   | North Macedonia      | ripencc  | 69     |  47.6% |  51.7% |   -4.1pp
    LY   | Libya                | afrinic  | 27     |  68.5% |  71.5% |   -3.0pp

    ====================================================================================================
     BIGGEST MOVERS — 12mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 12mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    DJ   | Djibouti             | afrinic  | 4      |  96.1% |   2.9% |  +93.2pp
    EG   | Egypt                | afrinic  | 86     |  95.5% |   7.6% |  +87.9pp
    CN   | China                | apnic    | 6507   |  89.2% |   3.9% |  +85.3pp
    PK   | Pakistan             | apnic    | 473    |  92.5% |  15.4% |  +77.1pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  75.0% |   3.1% |  +71.9pp
    BJ   | Benin                | afrinic  | 16     |  72.5% |   5.7% |  +66.8pp
    SO   | Somalia              | afrinic  | 22     |  82.8% |  19.7% |  +63.1pp
    CM   | Cameroon             | afrinic  | 30     |  94.5% |  31.9% |  +62.6pp
    TJ   | Tajikistan           | ripencc  | 43     |  82.3% |  27.1% |  +55.2pp
    HT   | Haiti                | lacnic   | 11     |  56.7% |   3.0% |  +53.7pp
    JE   | Jersey               | ripencc  | 13     |  92.2% |  42.4% |  +49.8pp
    KI   | Kiribati             | apnic    | 5      |  92.0% |  42.9% |  +49.1pp
    LS   | Lesotho              | afrinic  | 9      |  72.1% |  30.1% |  +42.0pp
    KZ   | Kazakhstan           | ripencc  | 266    |  80.3% |  39.6% |  +40.7pp
    TT   | Trinidad and Tobago  | lacnic   | 16     |  91.8% |  52.2% |  +39.6pp
    Decliners:
    CV   | Cabo Verde           | afrinic  | 8      |  35.4% |  84.9% |  -49.5pp
    MH   | Marshall Islands     | ripencc  | 11     |  52.0% |  76.5% |  -24.5pp
    MG   | Madagascar           | afrinic  | 7      |  39.0% |  52.5% |  -13.5pp
    IE   | Ireland              | ripencc  | 287    |  65.2% |  78.5% |  -13.3pp
    GT   | Guatemala            | lacnic   | 79     |  81.4% |  90.5% |   -9.1pp
    AO   | Angola               | afrinic  | 70     |  49.4% |  58.0% |   -8.6pp
    BF   | Burkina Faso         | afrinic  | 30     |  81.3% |  89.5% |   -8.2pp
    KY   | Cayman Islands       | arin     | 18     |  49.1% |  56.7% |   -7.6pp
    PY   | Paraguay             | lacnic   | 115    |  75.4% |  82.7% |   -7.3pp
    TG   | Togo                 | afrinic  | 11     |  57.0% |  64.2% |   -7.2pp
    KM   | Comoros              | afrinic  | 4      |  74.3% |  80.8% |   -6.5pp
    GL   | Greenland            | ripencc  | 1      |  77.1% |  83.3% |   -6.2pp
    MP   | Northern Mariana Isl | apnic    | 2      |  93.3% |  98.3% |   -5.0pp
    MU   | Mauritius            | afrinic  | 42     |  80.7% |  85.3% |   -4.6pp
    AE   | United Arab Emirates | ripencc  | 216    |  81.4% |  85.4% |   -4.0pp

    ====================================================================================================
     BIGGEST MOVERS — 24mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 24mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    DJ   | Djibouti             | afrinic  | 4      |  96.1% |   1.0% |  +95.1pp
    EG   | Egypt                | afrinic  | 86     |  95.5% |   7.6% |  +87.9pp
    CN   | China                | apnic    | 6507   |  89.2% |   2.9% |  +86.3pp
    CM   | Cameroon             | afrinic  | 30     |  94.5% |  13.9% |  +80.6pp
    FM   | Micronesia, Federate | apnic    | 6      |  85.0% |   4.8% |  +80.2pp
    PK   | Pakistan             | apnic    | 473    |  92.5% |  15.3% |  +77.2pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  75.0% |   0.0% |  +75.0pp
    CI   | Côte d'Ivoire        | afrinic  | 25     |  94.5% |  19.7% |  +74.8pp
    IS   | Iceland              | ripencc  | 87     |  75.8% |   1.7% |  +74.1pp
    SO   | Somalia              | afrinic  | 22     |  82.8% |  13.3% |  +69.5pp
    BJ   | Benin                | afrinic  | 16     |  72.5% |   3.4% |  +69.1pp
    JE   | Jersey               | ripencc  | 13     |  92.2% |  25.0% |  +67.2pp
    ML   | Mali                 | afrinic  | 8      |  83.4% |  25.1% |  +58.3pp
    TJ   | Tajikistan           | ripencc  | 43     |  82.3% |  24.1% |  +58.2pp
    HT   | Haiti                | lacnic   | 11     |  56.7% |   1.9% |  +54.8pp
    Decliners:
    CV   | Cabo Verde           | afrinic  | 8      |  35.4% |  83.0% |  -47.6pp
    MH   | Marshall Islands     | ripencc  | 11     |  52.0% |  82.4% |  -30.4pp
    SD   | Sudan                | afrinic  | 11     |  38.9% |  59.1% |  -20.2pp
    PE   | Peru                 | lacnic   | 226    |  35.6% |  52.2% |  -16.6pp
    KM   | Comoros              | afrinic  | 4      |  74.3% |  90.5% |  -16.2pp
    IE   | Ireland              | ripencc  | 287    |  65.2% |  75.4% |  -10.2pp
    AO   | Angola               | afrinic  | 70     |  49.4% |  57.7% |   -8.3pp
    PY   | Paraguay             | lacnic   | 115    |  75.4% |  83.2% |   -7.8pp
    LY   | Libya                | afrinic  | 27     |  68.5% |  76.1% |   -7.6pp
    MZ   | Mozambique           | afrinic  | 31     |  16.0% |  21.9% |   -5.9pp
    CG   | Congo                | afrinic  | 13     |  16.3% |  21.9% |   -5.6pp
    TZ   | Tanzania             | afrinic  | 116    |  33.7% |  39.3% |   -5.6pp
    ME   | Montenegro           | ripencc  | 31     |  49.2% |  54.4% |   -5.2pp
    BF   | Burkina Faso         | afrinic  | 30     |  81.3% |  86.4% |   -5.1pp
    AE   | United Arab Emirates | ripencc  | 216    |  81.4% |  85.6% |   -4.2pp

    ====================================================================================================
     BIGGEST MOVERS — 3mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 3mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    TJ   | Tajikistan           | ripencc  | 43     |  91.7% |  50.0% |  +41.7pp
    MT   | Malta                | ripencc  | 55     |  79.4% |  45.8% |  +33.6pp
    TH   | Thailand             | apnic    | 620    |  89.1% |  59.0% |  +30.1pp
    CL   | Chile                | lacnic   | 401    |  93.1% |  64.5% |  +28.6pp
    MX   | Mexico               | lacnic   | 658    |  82.7% |  60.4% |  +22.3pp
    KZ   | Kazakhstan           | ripencc  | 266    |  54.0% |  37.5% |  +16.5pp
    AZ   | Azerbaijan           | ripencc  | 121    |  89.0% |  72.7% |  +16.3pp
    PH   | Philippines          | apnic    | 674    |  84.3% |  72.0% |  +12.3pp
    SD   | Sudan                | afrinic  | 11     |  77.3% |  65.2% |  +12.1pp
    SC   | Seychelles           | ripencc  | 87     |  75.6% |  66.4% |   +9.2pp
    MC   | Monaco               | ripencc  | 5      | 100.0% |  91.3% |   +8.7pp
    MY   | Malaysia             | apnic    | 406    |  54.1% |  45.7% |   +8.4pp
    PK   | Pakistan             | apnic    | 473    |  97.8% |  89.5% |   +8.3pp
    LK   | Sri Lanka            | apnic    | 32     |  89.3% |  81.1% |   +8.2pp
    NZ   | New Zealand          | apnic    | 701    |  73.3% |  65.1% |   +8.2pp
    Decliners:
    RW   | Rwanda               | afrinic  | 28     |  15.3% |  78.6% |  -63.3pp
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  33.3% |  -25.6pp
    AL   | Albania              | ripencc  | 132    |  73.4% |  96.3% |  -22.9pp
    PR   | Puerto Rico          | arin     | 124    |  30.6% |  47.0% |  -16.4pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  91.4% |  -14.1pp
    FJ   | Fiji                 | apnic    | 20     |  87.0% | 100.0% |  -13.0pp
    VE   | Venezuela            | lacnic   | 261    |  86.6% |  95.6% |   -9.0pp
    AM   | Armenia              | ripencc  | 155    |  86.2% |  93.5% |   -7.3pp
    ES   | Spain                | ripencc  | 1172   |  79.7% |  86.1% |   -6.4pp
    PT   | Portugal             | ripencc  | 167    |  87.3% |  93.5% |   -6.2pp
    GE   | Georgia              | ripencc  | 174    |  85.5% |  91.2% |   -5.7pp
    PY   | Paraguay             | lacnic   | 115    |  54.8% |  59.7% |   -4.9pp
    BB   | Barbados             | arin     | 10     |  13.6% |  18.2% |   -4.6pp
    RO   | Romania              | ripencc  | 1085   |  65.5% |  69.7% |   -4.2pp
    HN   | Honduras             | lacnic   | 110    |  91.6% |  95.7% |   -4.1pp

    ====================================================================================================
     BIGGEST MOVERS — 6mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 6mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    CN   | China                | apnic    | 6507   |  97.0% |  15.5% |  +81.5pp
    TJ   | Tajikistan           | ripencc  | 43     |  91.7% |  50.0% |  +41.7pp
    RO   | Romania              | ripencc  | 1085   |  65.5% |  25.2% |  +40.3pp
    MT   | Malta                | ripencc  | 55     |  79.4% |  40.4% |  +39.0pp
    TH   | Thailand             | apnic    | 620    |  89.1% |  58.2% |  +30.9pp
    CL   | Chile                | lacnic   | 401    |  93.1% |  65.6% |  +27.5pp
    SD   | Sudan                | afrinic  | 11     |  77.3% |  50.0% |  +27.3pp
    MX   | Mexico               | lacnic   | 658    |  82.7% |  57.0% |  +25.7pp
    MA   | Morocco              | afrinic  | 33     |  43.9% |  21.1% |  +22.8pp
    KZ   | Kazakhstan           | ripencc  | 266    |  54.0% |  32.5% |  +21.5pp
    PH   | Philippines          | apnic    | 674    |  84.3% |  63.3% |  +21.0pp
    BD   | Bangladesh           | apnic    | 2030   |  85.9% |  65.2% |  +20.7pp
    UG   | Uganda               | afrinic  | 59     |  90.0% |  74.2% |  +15.8pp
    AZ   | Azerbaijan           | ripencc  | 121    |  89.0% |  73.4% |  +15.6pp
    KG   | Kyrgyzstan           | ripencc  | 71     |  95.2% |  81.8% |  +13.4pp
    Decliners:
    AE   | United Arab Emirates | ripencc  | 216    |  49.3% |  95.4% |  -46.1pp
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  33.3% |  -25.6pp
    AL   | Albania              | ripencc  | 132    |  73.4% |  97.3% |  -23.9pp
    PR   | Puerto Rico          | arin     | 124    |  30.6% |  46.1% |  -15.5pp
    FJ   | Fiji                 | apnic    | 20     |  87.0% | 100.0% |  -13.0pp
    SA   | Saudi Arabia         | ripencc  | 200    |  80.6% |  92.1% |  -11.5pp
    MO   | Macao                | apnic    | 15     |  65.5% |  76.3% |  -10.8pp
    PS   | Palestine, State of  | ripencc  | 69     |  86.4% |  95.2% |   -8.8pp
    VE   | Venezuela            | lacnic   | 261    |  86.6% |  93.6% |   -7.0pp
    LI   | Liechtenstein        | ripencc  | 29     |  79.2% |  85.6% |   -6.4pp
    ES   | Spain                | ripencc  | 1172   |  79.7% |  85.5% |   -5.8pp
    UY   | Uruguay              | lacnic   | 45     |  45.2% |  50.8% |   -5.6pp
    MM   | Myanmar              | apnic    | 172    |  90.9% |  96.3% |   -5.4pp
    MW   | Malawi               | afrinic  | 30     |  78.8% |  84.0% |   -5.2pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  82.4% |   -5.1pp

    ====================================================================================================
     BIGGEST MOVERS — 12mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 12mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    CN   | China                | apnic    | 6507   |  97.0% |   2.1% |  +94.9pp
    CH   | Switzerland          | ripencc  | 1063   |  82.1% |  16.3% |  +65.8pp
    SO   | Somalia              | afrinic  | 22     |  85.2% |  21.4% |  +63.8pp
    TJ   | Tajikistan           | ripencc  | 43     |  91.7% |  40.9% |  +50.8pp
    SD   | Sudan                | afrinic  | 11     |  77.3% |  33.3% |  +44.0pp
    CM   | Cameroon             | afrinic  | 30     |  91.7% |  54.5% |  +37.2pp
    JM   | Jamaica              | arin     | 15     |  66.7% |  30.6% |  +36.1pp
    MT   | Malta                | ripencc  | 55     |  79.4% |  51.6% |  +27.8pp
    CL   | Chile                | lacnic   | 401    |  93.1% |  65.3% |  +27.8pp
    MA   | Morocco              | afrinic  | 33     |  43.9% |  17.8% |  +26.1pp
    KZ   | Kazakhstan           | ripencc  | 266    |  54.0% |  29.5% |  +24.5pp
    MX   | Mexico               | lacnic   | 658    |  82.7% |  59.1% |  +23.6pp
    SC   | Seychelles           | ripencc  | 87     |  75.6% |  54.8% |  +20.8pp
    DE   | Germany              | ripencc  | 3276   |  82.4% |  62.0% |  +20.4pp
    PH   | Philippines          | apnic    | 674    |  84.3% |  64.0% |  +20.3pp
    Decliners:
    KE   | Kenya                | afrinic  | 247    |  31.6% |  77.0% |  -45.4pp
    AE   | United Arab Emirates | ripencc  | 216    |  49.3% |  90.7% |  -41.4pp
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  42.9% |  -35.2pp
    RO   | Romania              | ripencc  | 1085   |  65.5% |  94.6% |  -29.1pp
    BT   | Bhutan               | apnic    | 43     |  73.0% | 100.0% |  -27.0pp
    AL   | Albania              | ripencc  | 132    |  73.4% |  98.2% |  -24.8pp
    ZW   | Zimbabwe             | afrinic  | 28     |  13.6% |  36.8% |  -23.2pp
    SA   | Saudi Arabia         | ripencc  | 200    |  80.6% |  98.3% |  -17.7pp
    IE   | Ireland              | ripencc  | 287    |  73.0% |  88.6% |  -15.6pp
    ZA   | South Africa         | afrinic  | 751    |  35.8% |  50.2% |  -14.4pp
    FJ   | Fiji                 | apnic    | 20     |  87.0% | 100.0% |  -13.0pp
    PR   | Puerto Rico          | arin     | 124    |  30.6% |  42.9% |  -12.3pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  89.1% |  -11.8pp
    MO   | Macao                | apnic    | 15     |  65.5% |  76.7% |  -11.2pp
    ES   | Spain                | ripencc  | 1172   |  79.7% |  90.4% |  -10.7pp

    ====================================================================================================
     BIGGEST MOVERS — 24mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 24mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    CN   | China                | apnic    | 6507   |  97.0% |   1.7% |  +95.3pp
    IS   | Iceland              | ripencc  | 87     |  93.8% |  24.6% |  +69.2pp
    JP   | Japan                | apnic    | 983    |  83.5% |  17.8% |  +65.7pp
    SD   | Sudan                | afrinic  | 11     |  77.3% |  20.0% |  +57.3pp
    JM   | Jamaica              | arin     | 15     |  66.7% |  10.7% |  +56.0pp
    GH   | Ghana                | afrinic  | 104    |  90.9% |  36.5% |  +54.4pp
    MC   | Monaco               | ripencc  | 5      | 100.0% |  50.0% |  +50.0pp
    MT   | Malta                | ripencc  | 55     |  79.4% |  38.2% |  +41.2pp
    UZ   | Uzbekistan           | ripencc  | 129    |  84.7% |  44.4% |  +40.3pp
    AZ   | Azerbaijan           | ripencc  | 121    |  89.0% |  50.0% |  +39.0pp
    TJ   | Tajikistan           | ripencc  | 43     |  91.7% |  53.3% |  +38.4pp
    BM   | Bermuda              | arin     | 23     |  79.2% |  41.7% |  +37.5pp
    CL   | Chile                | lacnic   | 401    |  93.1% |  57.1% |  +36.0pp
    SO   | Somalia              | afrinic  | 22     |  85.2% |  50.0% |  +35.2pp
    SI   | Slovenia             | ripencc  | 306    |  79.4% |  45.1% |  +34.3pp
    Decliners:
    CD   | Congo, The Democrati | afrinic  | 51     |  27.0% |  82.1% |  -55.1pp
    KE   | Kenya                | afrinic  | 247    |  31.6% |  82.2% |  -50.6pp
    ZW   | Zimbabwe             | afrinic  | 28     |  13.6% |  62.5% |  -48.9pp
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  50.0% |  -42.3pp
    AE   | United Arab Emirates | ripencc  | 216    |  49.3% |  89.5% |  -40.2pp
    MU   | Mauritius            | afrinic  | 42     |   2.5% |  36.8% |  -34.3pp
    MA   | Morocco              | afrinic  | 33     |  43.9% |  75.0% |  -31.1pp
    MZ   | Mozambique           | afrinic  | 31     |  47.8% |  76.5% |  -28.7pp
    MO   | Macao                | apnic    | 15     |  65.5% |  92.9% |  -27.4pp
    BT   | Bhutan               | apnic    | 43     |  73.0% |  98.6% |  -25.6pp
    ZA   | South Africa         | afrinic  | 751    |  35.8% |  60.9% |  -25.1pp
    AL   | Albania              | ripencc  | 132    |  73.4% |  96.7% |  -23.3pp
    PR   | Puerto Rico          | arin     | 124    |  30.6% |  53.4% |  -22.8pp
    TZ   | Tanzania             | afrinic  | 116    |  33.3% |  50.0% |  -16.7pp
    NG   | Nigeria              | afrinic  | 265    |  42.4% |  58.5% |  -16.1pp

    ====================================================================================================
     SPOTLIGHT: CHINA (CN)
    ====================================================================================================
    ASNs: 6507  |  RIR: apnic
    IPv4:
      Now  : 89.2% of IPv4 route objects covered by a valid ROA
      3mo  : 88.3% of IPv4 route objects covered by a valid ROA
      6mo  : 6.7% of IPv4 route objects covered by a valid ROA
      12mo : 3.9% of IPv4 route objects covered by a valid ROA
      24mo : 2.9% of IPv4 route objects covered by a valid ROA
    IPv6:
      Now  : 97.0% of IPv6 route objects covered by a valid ROA
      3mo  : 96.1% of IPv6 route objects covered by a valid ROA
      6mo  : 15.5% of IPv6 route objects covered by a valid ROA
      12mo : 2.1% of IPv6 route objects covered by a valid ROA
      24mo : 1.7% of IPv6 route objects covered by a valid ROA
