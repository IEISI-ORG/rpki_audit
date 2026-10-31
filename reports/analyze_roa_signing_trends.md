    [*] Fetching APNIC Labs ROA-coverage snapshots...
        - Now   (reported date 29/10/2026): 278 countries/regions
        - 3mo   (reported date 01/08/2026): 278 countries/regions
        - 6mo   (reported date 01/05/2026): 279 countries/regions
        - 12mo  (reported date 01/11/2025): 280 countries/regions
        - 24mo  (reported date 01/11/2024): 279 countries/regions

    ====================================================================================================
     GLOBAL ROA COVERAGE TREND (IPv4 Route Objects, % Valid)
    ====================================================================================================
    Period   | Reported Date  | % Valid  | Total Route Objects
    ------------------------------------------------------------
    Now      | 29/10/2026     |   67.8% |  1,328,458
    3mo      | 01/08/2026     |   66.0% |  1,275,752
    6mo      | 01/05/2026     |   59.4% |  1,259,668
    12mo     | 01/11/2025     |   55.5% |  1,223,854
    24mo     | 01/11/2024     |   48.5% |  1,193,484

    ====================================================================================================
     GLOBAL ROA COVERAGE TREND (IPv6 Route Objects, % Valid)
    ====================================================================================================
    Period   | Reported Date  | % Valid  | Total Route Objects
    ------------------------------------------------------------
    Now      | 29/10/2026     |   76.4% |    323,147
    3mo      | 01/08/2026     |   74.2% |    314,953
    6mo      | 01/05/2026     |   63.9% |    304,899
    12mo     | 01/11/2025     |   57.7% |    299,517
    24mo     | 01/11/2024     |   55.3% |    261,900

    NOTE: IPv4 and IPv6 are reported separately because they are measured
    separately by APNIC and can diverge significantly per network — do not
    average or add them into one 'global ROA coverage' number.

    ====================================================================================================
     RIR ROA COVERAGE TREND (IPv4 Route Objects, % Valid, weighted by route-object count)
    ====================================================================================================
    RIR        | ASNs (now) |     Now |     3mo |     6mo |    12mo |    24mo
    -------------------------------------------------------------------------
    afrinic    | 2,477      |   65.6% |   61.4% |   58.3% |   37.5% |   33.5%
    apnic      | 31,467     |   76.3% |   74.2% |   54.5% |   54.1% |   46.0%
    arin       | 35,594     |   52.9% |   51.6% |   49.2% |   43.8% |   34.0%
    lacnic     | 13,850     |   69.6% |   63.2% |   61.1% |   59.7% |   54.9%
    ripencc    | 38,650     |   74.6% |   74.5% |   73.9% |   68.7% |   62.3%

    ====================================================================================================
     RIR ROA COVERAGE TREND (IPv6 Route Objects, % Valid, weighted by route-object count)
    ====================================================================================================
    RIR        | ASNs (now) |     Now |     3mo |     6mo |    12mo |    24mo
    -------------------------------------------------------------------------
    afrinic    | 2,477      |   42.1% |   39.8% |   40.9% |   35.4% |   61.5%
    apnic      | 31,467     |   83.6% |   81.8% |   54.2% |   48.8% |   39.7%
    arin       | 35,594     |   77.3% |   76.2% |   76.4% |   67.8% |   61.7%
    lacnic     | 13,850     |   68.3% |   61.8% |   60.2% |   56.7% |   55.7%
    ripencc    | 38,650     |   77.5% |   77.7% |   76.5% |   65.8% |   76.1%

    [+] Full per-country trend data (IPv4 + IPv6) saved to roa_signing_trends.csv

    ====================================================================================================
     BIGGEST MOVERS — 3mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 3mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    TG   | Togo                 | afrinic  | 11     |  60.9% |  10.2% |  +50.7pp
    BS   | Bahamas              | arin     | 13     |  72.9% |  26.2% |  +46.7pp
    TJ   | Tajikistan           | ripencc  | 44     |  82.0% |  38.3% |  +43.7pp
    MX   | Mexico               | lacnic   | 664    |  78.1% |  45.2% |  +32.9pp
    VG   | Virgin Islands, Brit | ripencc  | 51     |  77.4% |  48.3% |  +29.1pp
    KI   | Kiribati             | apnic    | 6      |  92.0% |  63.2% |  +28.8pp
    SK   | Slovakia             | ripencc  | 231    |  65.0% |  43.0% |  +22.0pp
    SL   | Sierra Leone         | afrinic  | 22     |  79.8% |  58.6% |  +21.2pp
    SO   | Somalia              | afrinic  | 22     |  85.0% |  65.5% |  +19.5pp
    CD   | Congo, The Democrati | afrinic  | 51     |  54.1% |  37.4% |  +16.7pp
    KE   | Kenya                | afrinic  | 250    |  77.0% |  60.4% |  +16.6pp
    NG   | Nigeria              | afrinic  | 266    |  59.1% |  42.7% |  +16.4pp
    AU   | Australia            | apnic    | 3001   |  53.1% |  36.8% |  +16.3pp
    YT   | Mayotte              | afrinic  | 1      |  78.1% |  63.2% |  +14.9pp
    GQ   | Equatorial Guinea    | afrinic  | 7      |  59.5% |  45.7% |  +13.8pp
    Decliners:
    MH   | Marshall Islands     | ripencc  | 11     |  36.2% |  91.7% |  -55.5pp
    BQ   | Bonaire, Sint Eustat | lacnic   | 6      |  80.4% |  97.2% |  -16.8pp
    IT   | Italy                | ripencc  | 1325   |  51.3% |  67.9% |  -16.6pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  76.2% |  83.8% |   -7.6pp
    VE   | Venezuela            | lacnic   | 261    |  90.0% |  95.3% |   -5.3pp
    CV   | Cabo Verde           | afrinic  | 8      |  35.4% |  40.6% |   -5.2pp
    SD   | Sudan                | afrinic  | 11     |  37.6% |  41.4% |   -3.8pp
    SC   | Seychelles           | ripencc  | 87     |  82.1% |  85.8% |   -3.7pp
    SG   | Singapore            | apnic    | 728    |  77.6% |  81.1% |   -3.5pp
    DK   | Denmark              | ripencc  | 470    |  58.4% |  61.4% |   -3.0pp
    MC   | Monaco               | ripencc  | 5      |  55.3% |  58.3% |   -3.0pp
    AI   | Anguilla             | arin     | 4      |   8.6% |  11.5% |   -2.9pp
    MU   | Mauritius            | afrinic  | 41     |  80.1% |  82.6% |   -2.5pp
    PE   | Peru                 | lacnic   | 226    |  35.6% |  38.1% |   -2.5pp
    PH   | Philippines          | apnic    | 675    |  88.6% |  91.0% |   -2.4pp

    ====================================================================================================
     BIGGEST MOVERS — 6mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 6mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    DJ   | Djibouti             | afrinic  | 4      |  94.9% |   5.6% |  +89.3pp
    CN   | China                | apnic    | 6505   |  87.7% |   8.5% |  +79.2pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  76.2% |   5.9% |  +70.3pp
    CM   | Cameroon             | afrinic  | 30     |  94.6% |  36.7% |  +57.9pp
    BS   | Bahamas              | arin     | 13     |  72.9% |  27.3% |  +45.6pp
    TJ   | Tajikistan           | ripencc  | 44     |  82.0% |  37.3% |  +44.7pp
    JE   | Jersey               | ripencc  | 13     |  92.3% |  53.8% |  +38.5pp
    TT   | Trinidad and Tobago  | lacnic   | 16     |  91.7% |  54.5% |  +37.2pp
    MX   | Mexico               | lacnic   | 664    |  78.1% |  42.5% |  +35.6pp
    VG   | Virgin Islands, Brit | ripencc  | 51     |  77.4% |  45.7% |  +31.7pp
    MT   | Malta                | ripencc  | 53     |  54.4% |  25.2% |  +29.2pp
    KI   | Kiribati             | apnic    | 6      |  92.0% |  63.2% |  +28.8pp
    SO   | Somalia              | afrinic  | 22     |  85.0% |  60.1% |  +24.9pp
    SL   | Sierra Leone         | afrinic  | 22     |  79.8% |  55.2% |  +24.6pp
    ID   | Indonesia            | apnic    | 4082   |  88.3% |  65.7% |  +22.6pp
    Decliners:
    MH   | Marshall Islands     | ripencc  | 11     |  36.2% |  91.8% |  -55.6pp
    CV   | Cabo Verde           | afrinic  | 8      |  35.4% |  87.1% |  -51.7pp
    IT   | Italy                | ripencc  | 1325   |  51.3% |  67.6% |  -16.3pp
    SD   | Sudan                | afrinic  | 11     |  37.6% |  46.1% |   -8.5pp
    KM   | Comoros              | afrinic  | 4      |  71.4% |  79.3% |   -7.9pp
    KY   | Cayman Islands       | arin     | 18     |  48.6% |  55.2% |   -6.6pp
    MP   | Northern Mariana Isl | apnic    | 2      |  94.3% | 100.0% |   -5.7pp
    MG   | Madagascar           | afrinic  | 7      |  40.4% |  45.5% |   -5.1pp
    UZ   | Uzbekistan           | ripencc  | 131    |  72.4% |  77.4% |   -5.0pp
    MD   | Moldova              | ripencc  | 207    |  86.2% |  91.1% |   -4.9pp
    AE   | United Arab Emirates | ripencc  | 217    |  81.1% |  85.4% |   -4.3pp
    MK   | North Macedonia      | ripencc  | 69     |  47.6% |  51.4% |   -3.8pp
    VE   | Venezuela            | lacnic   | 261    |  90.0% |  93.6% |   -3.6pp
    DK   | Denmark              | ripencc  | 470    |  58.4% |  62.0% |   -3.6pp
    SC   | Seychelles           | ripencc  | 87     |  82.1% |  85.6% |   -3.5pp

    ====================================================================================================
     BIGGEST MOVERS — 12mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 12mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    DJ   | Djibouti             | afrinic  | 4      |  94.9% |   1.9% |  +93.0pp
    EG   | Egypt                | afrinic  | 86     |  95.5% |   7.4% |  +88.1pp
    CN   | China                | apnic    | 6505   |  87.7% |   3.9% |  +83.8pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  76.2% |   3.1% |  +73.1pp
    BJ   | Benin                | afrinic  | 16     |  73.0% |   5.7% |  +67.3pp
    SO   | Somalia              | afrinic  | 22     |  85.0% |  19.1% |  +65.9pp
    CM   | Cameroon             | afrinic  | 30     |  94.6% |  31.6% |  +63.0pp
    HT   | Haiti                | lacnic   | 11     |  56.7% |   3.6% |  +53.1pp
    TJ   | Tajikistan           | ripencc  | 44     |  82.0% |  30.2% |  +51.8pp
    JE   | Jersey               | ripencc  | 13     |  92.3% |  42.4% |  +49.9pp
    BS   | Bahamas              | arin     | 13     |  72.9% |  25.4% |  +47.5pp
    KI   | Kiribati             | apnic    | 6      |  92.0% |  50.0% |  +42.0pp
    LS   | Lesotho              | afrinic  | 9      |  72.1% |  30.1% |  +42.0pp
    TT   | Trinidad and Tobago  | lacnic   | 16     |  91.7% |  52.8% |  +38.9pp
    MX   | Mexico               | lacnic   | 664    |  78.1% |  41.4% |  +36.7pp
    Decliners:
    CV   | Cabo Verde           | afrinic  | 8      |  35.4% |  85.5% |  -50.1pp
    MH   | Marshall Islands     | ripencc  | 11     |  36.2% |  75.0% |  -38.8pp
    IE   | Ireland              | ripencc  | 287    |  64.3% |  78.1% |  -13.8pp
    MG   | Madagascar           | afrinic  | 7      |  40.4% |  52.6% |  -12.2pp
    KM   | Comoros              | afrinic  | 4      |  71.4% |  80.8% |   -9.4pp
    GT   | Guatemala            | lacnic   | 79     |  81.6% |  90.6% |   -9.0pp
    KY   | Cayman Islands       | arin     | 18     |  48.6% |  56.7% |   -8.1pp
    BF   | Burkina Faso         | afrinic  | 30     |  81.4% |  89.5% |   -8.1pp
    AO   | Angola               | afrinic  | 70     |  49.9% |  57.2% |   -7.3pp
    GL   | Greenland            | ripencc  | 1      |  76.5% |  83.3% |   -6.8pp
    PY   | Paraguay             | lacnic   | 115    |  75.7% |  82.2% |   -6.5pp
    MU   | Mauritius            | afrinic  | 41     |  80.1% |  86.4% |   -6.3pp
    AE   | United Arab Emirates | ripencc  | 217    |  81.1% |  86.6% |   -5.5pp
    MD   | Moldova              | ripencc  | 207    |  86.2% |  91.7% |   -5.5pp
    MP   | Northern Mariana Isl | apnic    | 2      |  94.3% |  98.2% |   -3.9pp

    ====================================================================================================
     BIGGEST MOVERS — 24mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 24mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    DJ   | Djibouti             | afrinic  | 4      |  94.9% |   1.0% |  +93.9pp
    EG   | Egypt                | afrinic  | 86     |  95.5% |   7.8% |  +87.7pp
    CN   | China                | apnic    | 6505   |  87.7% |   3.0% |  +84.7pp
    FM   | Micronesia, Federate | apnic    | 6      |  85.0% |   4.8% |  +80.2pp
    PK   | Pakistan             | apnic    | 473    |  91.9% |  15.5% |  +76.4pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  76.2% |   0.0% |  +76.2pp
    IS   | Iceland              | ripencc  | 87     |  76.0% |   1.7% |  +74.3pp
    CI   | Côte d'Ivoire        | afrinic  | 26     |  94.7% |  21.4% |  +73.3pp
    SO   | Somalia              | afrinic  | 22     |  85.0% |  13.0% |  +72.0pp
    BJ   | Benin                | afrinic  | 16     |  73.0% |   3.4% |  +69.6pp
    JE   | Jersey               | ripencc  | 13     |  92.3% |  25.0% |  +67.3pp
    ML   | Mali                 | afrinic  | 8      |  83.0% |  24.6% |  +58.4pp
    TJ   | Tajikistan           | ripencc  | 44     |  82.0% |  24.0% |  +58.0pp
    HT   | Haiti                | lacnic   | 11     |  56.7% |   2.1% |  +54.6pp
    BS   | Bahamas              | arin     | 13     |  72.9% |  22.7% |  +50.2pp
    Decliners:
    CV   | Cabo Verde           | afrinic  | 8      |  35.4% |  83.0% |  -47.6pp
    MH   | Marshall Islands     | ripencc  | 11     |  36.2% |  82.4% |  -46.2pp
    SD   | Sudan                | afrinic  | 11     |  37.6% |  60.0% |  -22.4pp
    KM   | Comoros              | afrinic  | 4      |  71.4% |  90.5% |  -19.1pp
    PE   | Peru                 | lacnic   | 226    |  35.6% |  52.0% |  -16.4pp
    IE   | Ireland              | ripencc  | 287    |  64.3% |  74.8% |  -10.5pp
    PY   | Paraguay             | lacnic   | 115    |  75.7% |  83.0% |   -7.3pp
    AE   | United Arab Emirates | ripencc  | 217    |  81.1% |  88.4% |   -7.3pp
    AO   | Angola               | afrinic  | 70     |  49.9% |  56.4% |   -6.5pp
    CG   | Congo                | afrinic  | 13     |  16.3% |  22.1% |   -5.8pp
    MF   | Saint Martin (French | arin     | 6      |  40.0% |  45.0% |   -5.0pp
    ME   | Montenegro           | ripencc  | 31     |  48.8% |  53.7% |   -4.9pp
    BF   | Burkina Faso         | afrinic  | 30     |  81.4% |  86.2% |   -4.8pp
    MD   | Moldova              | ripencc  | 207    |  86.2% |  90.8% |   -4.6pp
    TZ   | Tanzania             | afrinic  | 116    |  33.4% |  37.8% |   -4.4pp

    ====================================================================================================
     BIGGEST MOVERS — 3mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 3mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    BS   | Bahamas              | arin     | 13     | 100.0% |   6.5% |  +93.5pp
    TJ   | Tajikistan           | ripencc  | 44     |  91.7% |  55.6% |  +36.1pp
    TH   | Thailand             | apnic    | 621    |  90.0% |  58.9% |  +31.1pp
    CL   | Chile                | lacnic   | 403    |  92.8% |  64.6% |  +28.2pp
    MX   | Mexico               | lacnic   | 664    |  82.4% |  60.3% |  +22.1pp
    AZ   | Azerbaijan           | ripencc  | 122    |  89.0% |  71.8% |  +17.2pp
    SD   | Sudan                | afrinic  | 11     |  80.0% |  63.6% |  +16.4pp
    AO   | Angola               | afrinic  | 70     |  91.2% |  77.1% |  +14.1pp
    VI   | Virgin Islands, U.S. | arin     | 12     |  73.0% |  60.7% |  +12.3pp
    PH   | Philippines          | apnic    | 675    |  84.6% |  72.3% |  +12.3pp
    LK   | Sri Lanka            | apnic    | 32     |  91.1% |  80.5% |  +10.6pp
    MM   | Myanmar              | apnic    | 172    |  99.2% |  90.6% |   +8.6pp
    MZ   | Mozambique           | afrinic  | 31     |  47.8% |  39.3% |   +8.5pp
    MY   | Malaysia             | apnic    | 406    |  54.5% |  46.4% |   +8.1pp
    SC   | Seychelles           | ripencc  | 87     |  79.3% |  72.1% |   +7.2pp
    Decliners:
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  33.3% |  -25.6pp
    AL   | Albania              | ripencc  | 133    |  72.7% |  95.7% |  -23.0pp
    PR   | Puerto Rico          | arin     | 124    |  30.6% |  47.3% |  -16.7pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  91.4% |  -14.1pp
    ES   | Spain                | ripencc  | 1174   |  79.8% |  92.9% |  -13.1pp
    AM   | Armenia              | ripencc  | 155    |  85.1% |  94.1% |   -9.0pp
    PT   | Portugal             | ripencc  | 167    |  88.1% |  94.0% |   -5.9pp
    GE   | Georgia              | ripencc  | 175    |  85.9% |  91.2% |   -5.3pp
    RO   | Romania              | ripencc  | 1086   |  65.6% |  70.3% |   -4.7pp
    MC   | Monaco               | ripencc  | 5      |  87.0% |  91.7% |   -4.7pp
    BB   | Barbados             | arin     | 10     |  13.6% |  18.2% |   -4.6pp
    UZ   | Uzbekistan           | ripencc  | 131    |  82.0% |  86.4% |   -4.4pp
    PY   | Paraguay             | lacnic   | 115    |  54.4% |  58.4% |   -4.0pp
    MP   | Northern Mariana Isl | apnic    | 2      |  15.0% |  19.0% |   -4.0pp
    HN   | Honduras             | lacnic   | 110    |  91.7% |  95.6% |   -3.9pp

    ====================================================================================================
     BIGGEST MOVERS — 6mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 6mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    BS   | Bahamas              | arin     | 13     | 100.0% |   6.2% |  +93.8pp
    CN   | China                | apnic    | 6505   |  96.9% |  25.6% |  +71.3pp
    TJ   | Tajikistan           | ripencc  | 44     |  91.7% |  50.0% |  +41.7pp
    RO   | Romania              | ripencc  | 1086   |  65.6% |  24.7% |  +40.9pp
    TH   | Thailand             | apnic    | 621    |  90.0% |  58.3% |  +31.7pp
    CL   | Chile                | lacnic   | 403    |  92.8% |  65.5% |  +27.3pp
    MX   | Mexico               | lacnic   | 664    |  82.4% |  57.0% |  +25.4pp
    SD   | Sudan                | afrinic  | 11     |  80.0% |  55.6% |  +24.4pp
    MA   | Morocco              | afrinic  | 33     |  45.1% |  21.6% |  +23.5pp
    PH   | Philippines          | apnic    | 675    |  84.6% |  62.9% |  +21.7pp
    BD   | Bangladesh           | apnic    | 2032   |  84.2% |  65.4% |  +18.8pp
    ID   | Indonesia            | apnic    | 4082   |  58.6% |  40.7% |  +17.9pp
    AZ   | Azerbaijan           | ripencc  | 122    |  89.0% |  73.4% |  +15.6pp
    AO   | Angola               | afrinic  | 70     |  91.2% |  75.8% |  +15.4pp
    UG   | Uganda               | afrinic  | 59     |  90.1% |  75.0% |  +15.1pp
    Decliners:
    AE   | United Arab Emirates | ripencc  | 217    |  49.7% |  95.4% |  -45.7pp
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  33.3% |  -25.6pp
    AL   | Albania              | ripencc  | 133    |  72.7% |  97.3% |  -24.6pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  92.6% |  -15.3pp
    PR   | Puerto Rico          | arin     | 124    |  30.6% |  45.7% |  -15.1pp
    SA   | Saudi Arabia         | ripencc  | 201    |  83.4% |  92.3% |   -8.9pp
    PS   | Palestine, State of  | ripencc  | 69     |  86.4% |  95.0% |   -8.6pp
    UZ   | Uzbekistan           | ripencc  | 131    |  82.0% |  89.1% |   -7.1pp
    PK   | Pakistan             | apnic    | 473    |  90.4% |  97.1% |   -6.7pp
    LI   | Liechtenstein        | ripencc  | 29     |  79.2% |  85.8% |   -6.6pp
    MO   | Macao                | apnic    | 15     |  65.8% |  72.3% |   -6.5pp
    ES   | Spain                | ripencc  | 1174   |  79.8% |  85.7% |   -5.9pp
    AM   | Armenia              | ripencc  | 155    |  85.1% |  90.4% |   -5.3pp
    PT   | Portugal             | ripencc  | 167    |  88.1% |  92.7% |   -4.6pp
    BB   | Barbados             | arin     | 10     |  13.6% |  18.2% |   -4.6pp

    ====================================================================================================
     BIGGEST MOVERS — 12mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 12mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    BS   | Bahamas              | arin     | 13     | 100.0% |   5.2% |  +94.8pp
    CN   | China                | apnic    | 6505   |  96.9% |   2.1% |  +94.8pp
    CH   | Switzerland          | ripencc  | 1066   |  81.3% |  16.1% |  +65.2pp
    SO   | Somalia              | afrinic  | 22     |  85.2% |  21.4% |  +63.8pp
    TJ   | Tajikistan           | ripencc  | 44     |  91.7% |  39.1% |  +52.6pp
    SD   | Sudan                | afrinic  | 11     |  80.0% |  33.3% |  +46.7pp
    JM   | Jamaica              | arin     | 15     |  66.7% |  32.4% |  +34.3pp
    MA   | Morocco              | afrinic  | 33     |  45.1% |  17.8% |  +27.3pp
    CL   | Chile                | lacnic   | 403    |  92.8% |  66.8% |  +26.0pp
    MX   | Mexico               | lacnic   | 664    |  82.4% |  59.3% |  +23.1pp
    DE   | Germany              | ripencc  | 3285   |  82.7% |  61.6% |  +21.1pp
    PH   | Philippines          | apnic    | 675    |  84.6% |  63.6% |  +21.0pp
    AZ   | Azerbaijan           | ripencc  | 122    |  89.0% |  69.7% |  +19.3pp
    CA   | Canada               | arin     | 2543   |  75.3% |  56.9% |  +18.4pp
    AO   | Angola               | afrinic  | 70     |  91.2% |  75.0% |  +16.2pp
    Decliners:
    KE   | Kenya                | afrinic  | 250    |  32.3% |  77.1% |  -44.8pp
    AE   | United Arab Emirates | ripencc  | 217    |  49.7% |  91.1% |  -41.4pp
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  42.9% |  -35.2pp
    RO   | Romania              | ripencc  | 1086   |  65.6% |  94.7% |  -29.1pp
    BT   | Bhutan               | apnic    | 43     |  73.0% | 100.0% |  -27.0pp
    AL   | Albania              | ripencc  | 133    |  72.7% |  98.3% |  -25.6pp
    ZW   | Zimbabwe             | afrinic  | 29     |  13.9% |  36.8% |  -22.9pp
    ZA   | South Africa         | afrinic  | 752    |  35.7% |  50.5% |  -14.8pp
    SA   | Saudi Arabia         | ripencc  | 201    |  83.4% |  98.0% |  -14.6pp
    IE   | Ireland              | ripencc  | 287    |  73.2% |  86.1% |  -12.9pp
    PR   | Puerto Rico          | arin     | 124    |  30.6% |  43.3% |  -12.7pp
    MO   | Macao                | apnic    | 15     |  65.8% |  76.7% |  -10.9pp
    ES   | Spain                | ripencc  | 1174   |  79.8% |  90.6% |  -10.8pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  87.2% |   -9.9pp
    KR   | South Korea          | apnic    | 1084   |  11.1% |  19.8% |   -8.7pp

    ====================================================================================================
     BIGGEST MOVERS — 24mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 24mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    BS   | Bahamas              | arin     | 13     | 100.0% |   0.7% |  +99.3pp
    CN   | China                | apnic    | 6505   |  96.9% |   1.6% |  +95.3pp
    IS   | Iceland              | ripencc  | 87     |  93.8% |  25.8% |  +68.0pp
    JP   | Japan                | apnic    | 982    |  83.6% |  17.8% |  +65.8pp
    SD   | Sudan                | afrinic  | 11     |  80.0% |  14.3% |  +65.7pp
    JM   | Jamaica              | arin     | 15     |  66.7% |  10.7% |  +56.0pp
    GH   | Ghana                | afrinic  | 104    |  91.0% |  36.5% |  +54.5pp
    TJ   | Tajikistan           | ripencc  | 44     |  91.7% |  53.3% |  +38.4pp
    AZ   | Azerbaijan           | ripencc  | 122    |  89.0% |  50.9% |  +38.1pp
    SC   | Seychelles           | ripencc  | 87     |  79.3% |  41.6% |  +37.7pp
    UZ   | Uzbekistan           | ripencc  | 131    |  82.0% |  44.4% |  +37.6pp
    BM   | Bermuda              | arin     | 23     |  79.2% |  41.7% |  +37.5pp
    MC   | Monaco               | ripencc  | 5      |  87.0% |  50.0% |  +37.0pp
    SO   | Somalia              | afrinic  | 22     |  85.2% |  50.0% |  +35.2pp
    CL   | Chile                | lacnic   | 403    |  92.8% |  58.4% |  +34.4pp
    Decliners:
    CD   | Congo, The Democrati | afrinic  | 51     |  25.0% |  83.9% |  -58.9pp
    KE   | Kenya                | afrinic  | 250    |  32.3% |  84.1% |  -51.8pp
    ZW   | Zimbabwe             | afrinic  | 29     |  13.9% |  62.5% |  -48.6pp
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  50.0% |  -42.3pp
    AE   | United Arab Emirates | ripencc  | 217    |  49.7% |  90.3% |  -40.6pp
    MU   | Mauritius            | afrinic  | 41     |   2.3% |  36.8% |  -34.5pp
    MA   | Morocco              | afrinic  | 33     |  45.1% |  74.6% |  -29.5pp
    MO   | Macao                | apnic    | 15     |  65.8% |  92.9% |  -27.1pp
    BT   | Bhutan               | apnic    | 43     |  73.0% |  98.6% |  -25.6pp
    ZA   | South Africa         | afrinic  | 752    |  35.7% |  60.9% |  -25.2pp
    AL   | Albania              | ripencc  | 133    |  72.7% |  97.5% |  -24.8pp
    PR   | Puerto Rico          | arin     | 124    |  30.6% |  53.1% |  -22.5pp
    MZ   | Mozambique           | afrinic  | 31     |  47.8% |  63.6% |  -15.8pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  92.9% |  -15.6pp
    TZ   | Tanzania             | afrinic  | 116    |  34.8% |  50.0% |  -15.2pp

    ====================================================================================================
     SPOTLIGHT: CHINA (CN)
    ====================================================================================================
    ASNs: 6505  |  RIR: apnic
    IPv4:
      Now  : 87.7% of IPv4 route objects covered by a valid ROA
      3mo  : 88.3% of IPv4 route objects covered by a valid ROA
      6mo  : 8.5% of IPv4 route objects covered by a valid ROA
      12mo : 3.9% of IPv4 route objects covered by a valid ROA
      24mo : 3.0% of IPv4 route objects covered by a valid ROA
    IPv6:
      Now  : 96.9% of IPv6 route objects covered by a valid ROA
      3mo  : 96.1% of IPv6 route objects covered by a valid ROA
      6mo  : 25.6% of IPv6 route objects covered by a valid ROA
      12mo : 2.1% of IPv6 route objects covered by a valid ROA
      24mo : 1.6% of IPv6 route objects covered by a valid ROA
