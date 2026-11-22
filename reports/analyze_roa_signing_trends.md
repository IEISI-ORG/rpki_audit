    [*] Fetching APNIC Labs ROA-coverage snapshots...
        - Now   (reported date 21/11/2026): 278 countries/regions
        - 3mo   (reported date 22/08/2026): 278 countries/regions
        - 6mo   (reported date 22/05/2026): 279 countries/regions
        - 12mo  (reported date 22/11/2025): 279 countries/regions
        - 24mo  (reported date 22/11/2024): 279 countries/regions

    ====================================================================================================
     GLOBAL ROA COVERAGE TREND (IPv4 Route Objects, % Valid)
    ====================================================================================================
    Period   | Reported Date  | % Valid  | Total Route Objects
    ------------------------------------------------------------
    Now      | 21/11/2026     |   68.4% |  1,328,425
    3mo      | 22/08/2026     |   64.5% |  1,317,644
    6mo      | 22/05/2026     |   60.9% |  1,271,350
    12mo     | 22/11/2025     |   56.6% |  1,217,574
    24mo     | 22/11/2024     |   48.1% |  1,202,036

    ====================================================================================================
     GLOBAL ROA COVERAGE TREND (IPv6 Route Objects, % Valid)
    ====================================================================================================
    Period   | Reported Date  | % Valid  | Total Route Objects
    ------------------------------------------------------------
    Now      | 21/11/2026     |   76.9% |    326,140
    3mo      | 22/08/2026     |   75.1% |    309,166
    6mo      | 22/05/2026     |   68.9% |    307,637
    12mo     | 22/11/2025     |   60.4% |    293,120
    24mo     | 22/11/2024     |   55.4% |    262,373

    NOTE: IPv4 and IPv6 are reported separately because they are measured
    separately by APNIC and can diverge significantly per network — do not
    average or add them into one 'global ROA coverage' number.

    ====================================================================================================
     RIR ROA COVERAGE TREND (IPv4 Route Objects, % Valid, weighted by route-object count)
    ====================================================================================================
    RIR        | ASNs (now) |     Now |     3mo |     6mo |    12mo |    24mo
    -------------------------------------------------------------------------
    afrinic    | 2,474      |   66.2% |   60.9% |   61.4% |   38.5% |   16.9%
    apnic      | 31,505     |   76.8% |   72.1% |   59.6% |   54.4% |   51.3%
    arin       | 35,696     |   52.5% |   50.5% |   49.4% |   46.3% |   34.5%
    lacnic     | 13,889     |   72.1% |   65.4% |   60.9% |   60.0% |   52.3%
    ripencc    | 38,578     |   75.7% |   70.8% |   73.9% |   69.3% |   63.4%

    ====================================================================================================
     RIR ROA COVERAGE TREND (IPv6 Route Objects, % Valid, weighted by route-object count)
    ====================================================================================================
    RIR        | ASNs (now) |     Now |     3mo |     6mo |    12mo |    24mo
    -------------------------------------------------------------------------
    afrinic    | 2,474      |   41.8% |   40.2% |   38.5% |   35.4% |   54.5%
    apnic      | 31,505     |   84.1% |   83.5% |   68.0% |   49.2% |   40.6%
    arin       | 35,696     |   77.2% |   76.4% |   76.2% |   69.5% |   61.2%
    lacnic     | 13,889     |   68.0% |   62.6% |   60.6% |   57.1% |   54.1%
    ripencc    | 38,578     |   79.9% |   78.0% |   77.3% |   77.0% |   76.3%

    [+] Full per-country trend data (IPv4 + IPv6) saved to roa_signing_trends.csv

    ====================================================================================================
     BIGGEST MOVERS — 3mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 3mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    BS   | Bahamas              | arin     | 14     |  72.3% |  26.0% |  +46.3pp
    TJ   | Tajikistan           | ripencc  | 44     |  84.5% |  39.2% |  +45.3pp
    VG   | Virgin Islands, Brit | ripencc  | 51     |  77.7% |  45.7% |  +32.0pp
    PE   | Peru                 | lacnic   | 228    |  67.6% |  37.0% |  +30.6pp
    MG   | Madagascar           | afrinic  | 7      |  73.4% |  44.9% |  +28.5pp
    SL   | Sierra Leone         | afrinic  | 22     |  81.0% |  56.0% |  +25.0pp
    SK   | Slovakia             | ripencc  | 228    |  64.0% |  42.4% |  +21.6pp
    FI   | Finland              | ripencc  | 365    |  77.2% |  56.2% |  +21.0pp
    IT   | Italy                | ripencc  | 1320   |  69.5% |  48.9% |  +20.6pp
    AS   | American Samoa       | apnic    | 2      |  39.7% |  19.4% |  +20.3pp
    KE   | Kenya                | afrinic  | 250    |  76.7% |  56.5% |  +20.2pp
    PT   | Portugal             | ripencc  | 166    |  86.0% |  66.5% |  +19.5pp
    BJ   | Benin                | afrinic  | 16     |  72.9% |  54.2% |  +18.7pp
    UZ   | Uzbekistan           | ripencc  | 133    |  72.4% |  54.1% |  +18.3pp
    LR   | Liberia              | afrinic  | 15     |  59.6% |  41.7% |  +17.9pp
    Decliners:
    MH   | Marshall Islands     | ripencc  | 10     |  38.7% |  91.5% |  -52.8pp
    BQ   | Bonaire, Sint Eustat | lacnic   | 6      |  80.4% |  92.1% |  -11.7pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  76.2% |  83.3% |   -7.1pp
    SD   | Sudan                | afrinic  | 11     |  36.0% |  42.1% |   -6.1pp
    SC   | Seychelles           | ripencc  | 87     |  78.6% |  84.4% |   -5.8pp
    DK   | Denmark              | ripencc  | 468    |  55.9% |  61.2% |   -5.3pp
    DJ   | Djibouti             | afrinic  | 4      |  93.7% |  97.3% |   -3.6pp
    GD   | Grenada              | arin     | 11     |  31.1% |  34.6% |   -3.5pp
    PR   | Puerto Rico          | arin     | 124    |  26.4% |  29.0% |   -2.6pp
    AG   | Antigua and Barbuda  | arin     | 18     |  21.3% |  23.6% |   -2.3pp
    AW   | Aruba                | lacnic   | 3      |  97.8% | 100.0% |   -2.2pp
    BZ   | Belize               | lacnic   | 27     |  83.8% |  85.7% |   -1.9pp
    MP   | Northern Mariana Isl | apnic    | 2      |  92.7% |  94.4% |   -1.7pp
    MU   | Mauritius            | afrinic  | 42     |  79.5% |  80.8% |   -1.3pp
    KY   | Cayman Islands       | arin     | 18     |  47.3% |  48.2% |   -0.9pp

    ====================================================================================================
     BIGGEST MOVERS — 6mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 6mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    ST   | Sao Tome and Princip | afrinic  | 2      |  76.2% |   5.9% |  +70.3pp
    CN   | China                | apnic    | 6492   |  88.3% |  25.0% |  +63.3pp
    TJ   | Tajikistan           | ripencc  | 44     |  84.5% |  37.0% |  +47.5pp
    BS   | Bahamas              | arin     | 14     |  72.3% |  27.5% |  +44.8pp
    JE   | Jersey               | ripencc  | 13     |  92.2% |  54.6% |  +37.6pp
    TT   | Trinidad and Tobago  | lacnic   | 16     |  91.6% |  54.6% |  +37.0pp
    KI   | Kiribati             | apnic    | 6      | 100.0% |  63.2% |  +36.8pp
    MX   | Mexico               | lacnic   | 670    |  75.4% |  44.0% |  +31.4pp
    VG   | Virgin Islands, Brit | ripencc  | 51     |  77.7% |  46.7% |  +31.0pp
    MT   | Malta                | ripencc  | 52     |  55.4% |  25.1% |  +30.3pp
    PE   | Peru                 | lacnic   | 228    |  67.6% |  38.8% |  +28.8pp
    MG   | Madagascar           | afrinic  | 7      |  73.4% |  45.8% |  +27.6pp
    SL   | Sierra Leone         | afrinic  | 22     |  81.0% |  55.2% |  +25.8pp
    SO   | Somalia              | afrinic  | 22     |  84.5% |  59.9% |  +24.6pp
    GG   | Guernsey             | ripencc  | 10     |  71.4% |  49.3% |  +22.1pp
    Decliners:
    MH   | Marshall Islands     | ripencc  | 10     |  38.7% |  94.4% |  -55.7pp
    CV   | Cabo Verde           | afrinic  | 8      |  35.4% |  87.1% |  -51.7pp
    SD   | Sudan                | afrinic  | 11     |  36.0% |  45.6% |   -9.6pp
    SC   | Seychelles           | ripencc  | 87     |  78.6% |  87.6% |   -9.0pp
    MP   | Northern Mariana Isl | apnic    | 2      |  92.7% | 100.0% |   -7.3pp
    MK   | North Macedonia      | ripencc  | 69     |  44.8% |  51.8% |   -7.0pp
    KY   | Cayman Islands       | arin     | 18     |  47.3% |  54.2% |   -6.9pp
    DK   | Denmark              | ripencc  | 468    |  55.9% |  61.5% |   -5.6pp
    UZ   | Uzbekistan           | ripencc  | 133    |  72.4% |  77.1% |   -4.7pp
    VE   | Venezuela            | lacnic   | 265    |  89.8% |  94.4% |   -4.6pp
    TG   | Togo                 | afrinic  | 11     |  59.2% |  63.6% |   -4.4pp
    KM   | Comoros              | afrinic  | 4      |  74.3% |  78.6% |   -4.3pp
    MD   | Moldova              | ripencc  | 206    |  85.9% |  90.0% |   -4.1pp
    DJ   | Djibouti             | afrinic  | 4      |  93.7% |  97.2% |   -3.5pp
    IE   | Ireland              | ripencc  | 287    |  63.1% |  66.3% |   -3.2pp

    ====================================================================================================
     BIGGEST MOVERS — 12mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 12mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    DJ   | Djibouti             | afrinic  | 4      |  93.7% |   2.9% |  +90.8pp
    CK   | Cook Islands         | apnic    | 2      | 100.0% |   9.5% |  +90.5pp
    EG   | Egypt                | afrinic  | 86     |  95.7% |   9.6% |  +86.1pp
    CN   | China                | apnic    | 6492   |  88.3% |   3.9% |  +84.4pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  76.2% |   3.1% |  +73.1pp
    BJ   | Benin                | afrinic  | 16     |  72.9% |   5.7% |  +67.2pp
    SO   | Somalia              | afrinic  | 22     |  84.5% |  19.1% |  +65.4pp
    CM   | Cameroon             | afrinic  | 30     |  94.7% |  33.3% |  +61.4pp
    HT   | Haiti                | lacnic   | 11     |  59.8% |   3.6% |  +56.2pp
    TJ   | Tajikistan           | ripencc  | 44     |  84.5% |  30.9% |  +53.6pp
    JE   | Jersey               | ripencc  | 13     |  92.2% |  42.9% |  +49.3pp
    BS   | Bahamas              | arin     | 14     |  72.3% |  26.4% |  +45.9pp
    KI   | Kiribati             | apnic    | 6      | 100.0% |  56.2% |  +43.8pp
    TT   | Trinidad and Tobago  | lacnic   | 16     |  91.6% |  53.1% |  +38.5pp
    MX   | Mexico               | lacnic   | 670    |  75.4% |  41.4% |  +34.0pp
    Decliners:
    CV   | Cabo Verde           | afrinic  | 8      |  35.4% |  85.5% |  -50.1pp
    MH   | Marshall Islands     | ripencc  | 10     |  38.7% |  76.5% |  -37.8pp
    IE   | Ireland              | ripencc  | 287    |  63.1% |  78.4% |  -15.3pp
    AO   | Angola               | afrinic  | 70     |  50.7% |  60.8% |  -10.1pp
    KY   | Cayman Islands       | arin     | 18     |  47.3% |  56.7% |   -9.4pp
    GT   | Guatemala            | lacnic   | 79     |  81.1% |  90.3% |   -9.2pp
    BF   | Burkina Faso         | afrinic  | 30     |  81.5% |  90.3% |   -8.8pp
    PY   | Paraguay             | lacnic   | 117    |  75.8% |  83.7% |   -7.9pp
    MD   | Moldova              | ripencc  | 206    |  85.9% |  93.4% |   -7.5pp
    DK   | Denmark              | ripencc  | 468    |  55.9% |  63.1% |   -7.2pp
    GL   | Greenland            | ripencc  | 1      |  76.5% |  83.3% |   -6.8pp
    KM   | Comoros              | afrinic  | 4      |  74.3% |  80.8% |   -6.5pp
    MP   | Northern Mariana Isl | apnic    | 2      |  92.7% |  98.1% |   -5.4pp
    TG   | Togo                 | afrinic  | 11     |  59.2% |  64.1% |   -4.9pp
    AE   | United Arab Emirates | ripencc  | 219    |  81.7% |  86.0% |   -4.3pp

    ====================================================================================================
     BIGGEST MOVERS — 24mo WINDOW (IPv4, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 24mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    CK   | Cook Islands         | apnic    | 2      | 100.0% |   5.3% |  +94.7pp
    DJ   | Djibouti             | afrinic  | 4      |  93.7% |   1.0% |  +92.7pp
    EG   | Egypt                | afrinic  | 86     |  95.7% |   7.4% |  +88.3pp
    CN   | China                | apnic    | 6492   |  88.3% |   3.0% |  +85.3pp
    ST   | Sao Tome and Princip | afrinic  | 2      |  76.2% |   0.0% |  +76.2pp
    IS   | Iceland              | ripencc  | 87     |  75.8% |   1.7% |  +74.1pp
    CI   | Côte d'Ivoire        | afrinic  | 26     |  95.0% |  21.4% |  +73.6pp
    SO   | Somalia              | afrinic  | 22     |  84.5% |  13.0% |  +71.5pp
    BJ   | Benin                | afrinic  | 16     |  72.9% |   3.3% |  +69.6pp
    JE   | Jersey               | ripencc  | 13     |  92.2% |  25.3% |  +66.9pp
    TJ   | Tajikistan           | ripencc  | 44     |  84.5% |  23.9% |  +60.6pp
    ML   | Mali                 | afrinic  | 8      |  83.3% |  24.5% |  +58.8pp
    HT   | Haiti                | lacnic   | 11     |  59.8% |   2.3% |  +57.5pp
    ZA   | South Africa         | afrinic  | 751    |  67.4% |  10.2% |  +57.2pp
    LR   | Liberia              | afrinic  | 15     |  59.6% |   8.3% |  +51.3pp
    Decliners:
    CV   | Cabo Verde           | afrinic  | 8      |  35.4% |  83.0% |  -47.6pp
    MH   | Marshall Islands     | ripencc  | 10     |  38.7% |  82.4% |  -43.7pp
    SD   | Sudan                | afrinic  | 11     |  36.0% |  61.0% |  -25.0pp
    KM   | Comoros              | afrinic  | 4      |  74.3% |  90.5% |  -16.2pp
    IE   | Ireland              | ripencc  | 287    |  63.1% |  75.5% |  -12.4pp
    PY   | Paraguay             | lacnic   | 117    |  75.8% |  83.4% |   -7.6pp
    ME   | Montenegro           | ripencc  | 30     |  48.6% |  55.4% |   -6.8pp
    AO   | Angola               | afrinic  | 70     |  50.7% |  57.5% |   -6.8pp
    CG   | Congo                | afrinic  | 13     |  16.2% |  22.3% |   -6.1pp
    AE   | United Arab Emirates | ripencc  | 219    |  81.7% |  87.6% |   -5.9pp
    MD   | Moldova              | ripencc  | 206    |  85.9% |  91.0% |   -5.1pp
    BF   | Burkina Faso         | afrinic  | 30     |  81.5% |  86.1% |   -4.6pp
    VU   | Vanuatu              | apnic    | 14     |  91.5% |  95.8% |   -4.3pp
    TZ   | Tanzania             | afrinic  | 116    |  33.9% |  38.1% |   -4.2pp
    GL   | Greenland            | ripencc  | 1      |  76.5% |  80.6% |   -4.1pp

    ====================================================================================================
     BIGGEST MOVERS — 3mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 3mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    BS   | Bahamas              | arin     | 14     | 100.0% |   6.5% |  +93.5pp
    AE   | United Arab Emirates | ripencc  | 219    |  94.6% |  49.8% |  +44.8pp
    TJ   | Tajikistan           | ripencc  | 44     |  92.6% |  55.6% |  +37.0pp
    TH   | Thailand             | apnic    | 621    |  92.3% |  58.6% |  +33.7pp
    CL   | Chile                | lacnic   | 405    |  93.1% |  64.7% |  +28.4pp
    AZ   | Azerbaijan           | ripencc  | 122    |  89.2% |  70.8% |  +18.4pp
    MX   | Mexico               | lacnic   | 670    |  81.3% |  62.9% |  +18.4pp
    KH   | Cambodia             | apnic    | 143    |  96.5% |  85.0% |  +11.5pp
    PH   | Philippines          | apnic    | 677    |  84.2% |  72.8% |  +11.4pp
    VI   | Virgin Islands, U.S. | arin     | 12     |  73.7% |  62.5% |  +11.2pp
    RO   | Romania              | ripencc  | 1085   |  81.4% |  71.1% |  +10.3pp
    PS   | Palestine, State of  | ripencc  | 69     |  95.2% |  86.4% |   +8.8pp
    SA   | Saudi Arabia         | ripencc  | 201    |  94.5% |  85.7% |   +8.8pp
    MY   | Malaysia             | apnic    | 406    |  55.1% |  46.3% |   +8.8pp
    OM   | Oman                 | ripencc  | 26     |  59.3% |  50.8% |   +8.5pp
    Decliners:
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  33.3% |  -25.6pp
    BT   | Bhutan               | apnic    | 43     |  47.3% |  72.5% |  -25.2pp
    HK   | Hong Kong            | apnic    | 1403   |  48.3% |  70.7% |  -22.4pp
    AL   | Albania              | ripencc  | 133    |  74.5% |  96.2% |  -21.7pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  94.4% |  -17.1pp
    VG   | Virgin Islands, Brit | ripencc  | 51     |  74.4% |  88.8% |  -14.4pp
    KZ   | Kazakhstan           | ripencc  | 274    |  39.0% |  49.4% |  -10.4pp
    CM   | Cameroon             | afrinic  | 30     |  92.3% | 100.0% |   -7.7pp
    GE   | Georgia              | ripencc  | 177    |  83.6% |  90.9% |   -7.3pp
    PT   | Portugal             | ripencc  | 166    |  87.6% |  94.0% |   -6.4pp
    IL   | Israel               | ripencc  | 386    |  69.4% |  75.2% |   -5.8pp
    MW   | Malawi               | afrinic  | 30     |  79.4% |  84.8% |   -5.4pp
    BB   | Barbados             | arin     | 10     |  13.6% |  18.2% |   -4.6pp
    UZ   | Uzbekistan           | ripencc  | 133    |  82.0% |  86.2% |   -4.2pp
    MC   | Monaco               | ripencc  | 5      |  87.5% |  91.7% |   -4.2pp

    ====================================================================================================
     BIGGEST MOVERS — 6mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 6mo     | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    BS   | Bahamas              | arin     | 14     | 100.0% |   6.2% |  +93.8pp
    RO   | Romania              | ripencc  | 1085   |  81.4% |  31.0% |  +50.4pp
    TJ   | Tajikistan           | ripencc  | 44     |  92.6% |  47.8% |  +44.8pp
    CN   | China                | apnic    | 6492   |  96.9% |  62.5% |  +34.4pp
    TH   | Thailand             | apnic    | 621    |  92.3% |  58.8% |  +33.5pp
    CL   | Chile                | lacnic   | 405    |  93.1% |  65.7% |  +27.4pp
    BD   | Bangladesh           | apnic    | 2037   |  87.4% |  63.9% |  +23.5pp
    MX   | Mexico               | lacnic   | 670    |  81.3% |  59.5% |  +21.8pp
    MA   | Morocco              | afrinic  | 33     |  41.8% |  21.6% |  +20.2pp
    SD   | Sudan                | afrinic  | 11     |  80.0% |  63.6% |  +16.4pp
    AZ   | Azerbaijan           | ripencc  | 122    |  89.2% |  73.4% |  +15.8pp
    UG   | Uganda               | afrinic  | 59     |  90.0% |  75.3% |  +14.7pp
    KH   | Cambodia             | apnic    | 143    |  96.5% |  83.9% |  +12.6pp
    AO   | Angola               | afrinic  | 70     |  88.6% |  76.5% |  +12.1pp
    MZ   | Mozambique           | afrinic  | 31     |  47.8% |  37.0% |  +10.8pp
    Decliners:
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  33.3% |  -25.6pp
    BT   | Bhutan               | apnic    | 43     |  47.3% |  71.1% |  -23.8pp
    AL   | Albania              | ripencc  | 133    |  74.5% |  97.3% |  -22.8pp
    PR   | Puerto Rico          | arin     | 124    |  30.1% |  45.7% |  -15.6pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  92.9% |  -15.6pp
    FJ   | Fiji                 | apnic    | 20     |  87.0% | 100.0% |  -13.0pp
    SC   | Seychelles           | ripencc  | 87     |  83.3% |  94.8% |  -11.5pp
    MO   | Macao                | apnic    | 15     |  65.8% |  75.6% |   -9.8pp
    UZ   | Uzbekistan           | ripencc  | 133    |  82.0% |  88.9% |   -6.9pp
    GE   | Georgia              | ripencc  | 177    |  83.6% |  89.6% |   -6.0pp
    LI   | Liechtenstein        | ripencc  | 28     |  79.3% |  85.2% |   -5.9pp
    ES   | Spain                | ripencc  | 1169   |  80.4% |  85.8% |   -5.4pp
    IL   | Israel               | ripencc  | 386    |  69.4% |  74.7% |   -5.3pp
    PT   | Portugal             | ripencc  | 166    |  87.6% |  92.8% |   -5.2pp
    UY   | Uruguay              | lacnic   | 45     |  44.5% |  49.6% |   -5.1pp

    ====================================================================================================
     BIGGEST MOVERS — 12mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 12mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    CN   | China                | apnic    | 6492   |  96.9% |   2.3% |  +94.6pp
    BS   | Bahamas              | arin     | 14     | 100.0% |   5.5% |  +94.5pp
    SO   | Somalia              | afrinic  | 22     |  85.2% |  21.4% |  +63.8pp
    SD   | Sudan                | afrinic  | 11     |  80.0% |  27.3% |  +52.7pp
    TJ   | Tajikistan           | ripencc  | 44     |  92.6% |  43.5% |  +49.1pp
    JM   | Jamaica              | arin     | 15     |  66.7% |  34.3% |  +32.4pp
    CL   | Chile                | lacnic   | 405    |  93.1% |  66.5% |  +26.6pp
    MA   | Morocco              | afrinic  | 33     |  41.8% |  17.8% |  +24.0pp
    MX   | Mexico               | lacnic   | 670    |  81.3% |  59.3% |  +22.0pp
    AO   | Angola               | afrinic  | 70     |  88.6% |  67.6% |  +21.0pp
    CM   | Cameroon             | afrinic  | 30     |  92.3% |  71.4% |  +20.9pp
    PH   | Philippines          | apnic    | 677    |  84.2% |  64.7% |  +19.5pp
    SC   | Seychelles           | ripencc  | 87     |  83.3% |  64.6% |  +18.7pp
    AZ   | Azerbaijan           | ripencc  | 122    |  89.2% |  70.8% |  +18.4pp
    NI   | Nicaragua            | lacnic   | 30     |  98.7% |  83.0% |  +15.7pp
    Decliners:
    BT   | Bhutan               | apnic    | 43     |  47.3% | 100.0% |  -52.7pp
    KE   | Kenya                | afrinic  | 250    |  32.3% |  77.3% |  -45.0pp
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  42.9% |  -35.2pp
    AL   | Albania              | ripencc  | 133    |  74.5% |  98.4% |  -23.9pp
    ZA   | South Africa         | afrinic  | 751    |  36.3% |  50.9% |  -14.6pp
    RO   | Romania              | ripencc  | 1085   |  81.4% |  94.5% |  -13.1pp
    FJ   | Fiji                 | apnic    | 20     |  87.0% | 100.0% |  -13.0pp
    IE   | Ireland              | ripencc  | 287    |  71.5% |  84.3% |  -12.8pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  89.4% |  -12.1pp
    ES   | Spain                | ripencc  | 1169   |  80.4% |  91.4% |  -11.0pp
    MO   | Macao                | apnic    | 15     |  65.8% |  76.7% |  -10.9pp
    NG   | Nigeria              | afrinic  | 266    |  43.1% |  53.4% |  -10.3pp
    KR   | South Korea          | apnic    | 1087   |  11.2% |  19.8% |   -8.6pp
    HK   | Hong Kong            | apnic    | 1403   |  48.3% |  56.6% |   -8.3pp
    BB   | Barbados             | arin     | 10     |  13.6% |  21.7% |   -8.1pp

    ====================================================================================================
     BIGGEST MOVERS — 24mo WINDOW (IPv6, % Valid, ROA coverage)
    ====================================================================================================
    CC   | Country              | RIR      | ASNs   | Now     | 24mo    | Delta
    -------------------------------------------------------------------------------------
    Improvers:
    BS   | Bahamas              | arin     | 14     | 100.0% |   0.7% |  +99.3pp
    CN   | China                | apnic    | 6492   |  96.9% |   1.6% |  +95.3pp
    IS   | Iceland              | ripencc  | 87     |  92.4% |  24.5% |  +67.9pp
    JP   | Japan                | apnic    | 979    |  84.0% |  17.4% |  +66.6pp
    SD   | Sudan                | afrinic  | 11     |  80.0% |  14.3% |  +65.7pp
    JM   | Jamaica              | arin     | 15     |  66.7% |  10.7% |  +56.0pp
    GH   | Ghana                | afrinic  | 103    |  91.7% |  37.7% |  +54.0pp
    TJ   | Tajikistan           | ripencc  | 44     |  92.6% |  50.0% |  +42.6pp
    SC   | Seychelles           | ripencc  | 87     |  83.3% |  43.2% |  +40.1pp
    FJ   | Fiji                 | apnic    | 20     |  87.0% |  47.4% |  +39.6pp
    UZ   | Uzbekistan           | ripencc  | 133    |  82.0% |  43.2% |  +38.8pp
    AZ   | Azerbaijan           | ripencc  | 122    |  89.2% |  50.9% |  +38.3pp
    MC   | Monaco               | ripencc  | 5      |  87.5% |  50.0% |  +37.5pp
    BM   | Bermuda              | arin     | 23     |  78.3% |  41.7% |  +36.6pp
    SO   | Somalia              | afrinic  | 22     |  85.2% |  50.0% |  +35.2pp
    Decliners:
    CD   | Congo, The Democrati | afrinic  | 51     |  26.6% |  83.9% |  -57.3pp
    KE   | Kenya                | afrinic  | 250    |  32.3% |  84.9% |  -52.6pp
    BT   | Bhutan               | apnic    | 43     |  47.3% |  98.6% |  -51.3pp
    ZW   | Zimbabwe             | afrinic  | 27     |  13.6% |  58.8% |  -45.2pp
    TK   | Tokelau              | ripencc  | 3      |   7.7% |  50.0% |  -42.3pp
    MU   | Mauritius            | afrinic  | 42     |   2.0% |  36.8% |  -34.8pp
    MA   | Morocco              | afrinic  | 33     |  41.8% |  75.0% |  -33.2pp
    MO   | Macao                | apnic    | 15     |  65.8% |  89.3% |  -23.5pp
    AL   | Albania              | ripencc  | 133    |  74.5% |  97.6% |  -23.1pp
    PR   | Puerto Rico          | arin     | 124    |  30.1% |  52.9% |  -22.8pp
    TZ   | Tanzania             | afrinic  | 116    |  31.9% |  50.9% |  -19.0pp
    IL   | Israel               | ripencc  | 386    |  69.4% |  85.8% |  -16.4pp
    MZ   | Mozambique           | afrinic  | 31     |  47.8% |  63.6% |  -15.8pp
    LA   | Laos                 | apnic    | 42     |  77.3% |  92.9% |  -15.6pp
    NG   | Nigeria              | afrinic  | 266    |  43.1% |  57.5% |  -14.4pp

    ====================================================================================================
     SPOTLIGHT: CHINA (CN)
    ====================================================================================================
    ASNs: 6492  |  RIR: apnic
    IPv4:
      Now  : 88.3% of IPv4 route objects covered by a valid ROA
      3mo  : 81.7% of IPv4 route objects covered by a valid ROA
      6mo  : 25.0% of IPv4 route objects covered by a valid ROA
      12mo : 3.9% of IPv4 route objects covered by a valid ROA
      24mo : 3.0% of IPv4 route objects covered by a valid ROA
    IPv6:
      Now  : 96.9% of IPv6 route objects covered by a valid ROA
      3mo  : 97.4% of IPv6 route objects covered by a valid ROA
      6mo  : 62.5% of IPv6 route objects covered by a valid ROA
      12mo : 2.3% of IPv6 route objects covered by a valid ROA
      24mo : 1.6% of IPv6 route objects covered by a valid ROA
