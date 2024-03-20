# pylint: disable=too-many-lines

__all__ = [
    "CountriesNum",
    "CountriesA2",
    "CountriesA3",
    "Countries",
]

from dataclasses import dataclass
from enum import Enum, IntEnum, StrEnum


class CountriesNum(IntEnum):
    AFGHANISTAN = 4
    ALAND_ISLANDS = 248
    ALBANIA = 8
    ALGERIA = 12
    AMERICAN_SAMOA = 16
    ANDORRA = 20
    ANGOLA = 24
    ANGUILLA = 660
    ANTARCTICA = 10
    ANTIGUA_AND_BARBUDA = 28
    ARGENTINA = 32
    ARMENIA = 51
    ARUBA = 533
    AUSTRALIA = 36
    AUSTRIA = 40
    AZERBAIJAN = 31
    BAHAMAS = 44
    BAHRAIN = 48
    BANGLADESH = 50
    BARBADOS = 52
    BELARUS = 112
    BELGIUM = 56
    BELIZE = 84
    BENIN = 204
    BERMUDA = 60
    BHUTAN = 64
    BOLIVIA = 68
    BONAIRE = 535
    BOSNIA_AND_HERZEGOVINA = 70
    BOTSWANA = 72
    BOUVET_ISLAND = 74
    BRAZIL = 76
    BRITISH_INDIAN_OCEAN_TERRITORY = 86
    BRUNEI_DARUSSALAM = 96
    BULGARIA = 100
    BURKINA_FASO = 854
    BURUNDI = 108
    CABO_VERDE = 132
    CAMBODIA = 116
    CAMEROON = 120
    CANADA = 124
    CAYMAN_ISLANDS = 136
    CENTRAL_AFRICAN_REPUBLIC = 140
    CHAD = 148
    CHILE = 152
    CHINA = 156
    CHRISTMAS_ISLAND = 162
    COCOS_KEELING_ISLANDS = 166
    COLOMBIA = 170
    COMOROS = 174
    CONGO_DEMOCRATIC_REPUBLIC = 180
    CONGO = 178
    COOK_ISLANDS = 184
    COSTA_RICA = 188
    COTE_DIVOIRE = 384
    CROATIA = 191
    CUBA = 192
    CURACAO = 531
    CYPRUS = 196
    CZECHIA = 203
    DENMARK = 208
    DJIBOUTI = 262
    DOMINICA = 212
    DOMINICAN_REPUBLIC = 214
    ECUADOR = 218
    EGYPT = 818
    EL_SALVADOR = 222
    EQUATORIAL_GUINEA = 226
    ERITREA = 232
    ESTONIA = 233
    ESWATINI = 748
    ETHIOPIA = 231
    FALKLAND_ISLANDS = 238
    FAROE_ISLANDS = 234
    FIJI = 242
    FINLAND = 246
    FRANCE = 250
    FRENCH_GUIANA = 254
    FRENCH_POLYNESIA = 258
    FRENCH_SOUTHERN_TERRITORIES = 260
    GABON = 266
    GAMBIA = 270
    GEORGIA = 268
    GERMANY = 276
    GHANA = 288
    GIBRALTAR = 292
    GREECE = 300
    GREENLAND = 304
    GRENADA = 308
    GUADELOUPE = 312
    GUAM = 316
    GUATEMALA = 320
    GUERNSEY = 831
    GUINEA = 324
    GUINEA_BISSAU = 624
    GUYANA = 328
    HAITI = 332
    HEARD_ISLAND_AND_MCDONALD_ISLANDS = 334
    HOLY_SEE = 336
    HONDURAS = 340
    HONG_KONG = 344
    HUNGARY = 348
    ICELAND = 352
    INDIA = 356
    INDONESIA = 360
    IRAN = 364
    IRAQ = 368
    IRELAND = 372
    ISLE_OF_MAN = 833
    ISRAEL = 376
    ITALY = 380
    JAMAICA = 388
    JAPAN = 392
    JERSEY = 832
    JORDAN = 400
    KAZAKHSTAN = 398
    KENYA = 404
    KIRIBATI = 296
    KOREA_DEMOCRATIC_PEOPLES_REPUBLIC = 408
    KOREA_REPUBLIC = 410
    KUWAIT = 414
    KYRGYZSTAN = 417
    LAO_PEOPLES_DEMOCRATIC_REPUBLIC = 418
    LATVIA = 428
    LEBANON = 422
    LESOTHO = 426
    LIBERIA = 430
    LIBYA = 434
    LIECHTENSTEIN = 438
    LITHUANIA = 440
    LUXEMBOURG = 442
    MACAO = 446
    MADAGASCAR = 450
    MALAWI = 454
    MALAYSIA = 458
    MALDIVES = 462
    MALI = 466
    MALTA = 470
    MARSHALL_ISLANDS = 584
    MARTINIQUE = 474
    MAURITANIA = 478
    MAURITIUS = 480
    MAYOTTE = 175
    MEXICO = 484
    MICRONESIA = 583
    MOLDOVA = 498
    MONACO = 492
    MONGOLIA = 496
    MONTENEGRO = 499
    MONTSERRAT = 500
    MOROCCO = 504
    MOZAMBIQUE = 508
    MYANMAR = 104
    NAMIBIA = 516
    NAURU = 520
    NEPAL = 524
    NETHERLANDS = 528
    NEW_CALEDONIA = 540
    NEW_ZEALAND = 554
    NICARAGUA = 558
    NIGER = 562
    NIGERIA = 566
    NIUE = 570
    NORFOLK_ISLAND = 574
    NORTH_MACEDONIA = 807
    NORTHERN_MARIANA_ISLANDS = 580
    NORWAY = 578
    OMAN = 512
    PAKISTAN = 586
    PALAU = 585
    PALESTINE = 275
    PANAMA = 591
    PAPUA_NEW_GUINEA = 598
    PARAGUAY = 600
    PERU = 604
    PHILIPPINES = 608
    PITCAIRN = 612
    POLAND = 616
    PORTUGAL = 620
    PUERTO_RICO = 630
    QATAR = 634
    REUNION = 638
    ROMANIA = 642
    RUSSIA = 643
    RWANDA = 646
    SAINT_BARTHELEMY = 652
    SAINT_HELENA = 654
    SAINT_KITTS_AND_NEVIS = 659
    SAINT_LUCIA = 662
    SAINT_MARTIN_FRENCH_PART = 663
    SAINT_PIERRE_AND_MIQUELON = 666
    SAINT_VINCENT_AND_THE_GRENADINES = 670
    SAMOA = 882
    SAN_MARINO = 674
    SAO_TOME_AND_PRINCIPE = 678
    SAUDI_ARABIA = 682
    SENEGAL = 686
    SERBIA = 688
    SEYCHELLES = 690
    SIERRA_LEONE = 694
    SINGAPORE = 702
    SINT_MAARTEN_DUTCH_PART = 534
    SLOVAKIA = 703
    SLOVENIA = 705
    SOLOMON_ISLANDS = 90
    SOMALIA = 706
    SOUTH_AFRICA = 710
    SOUTH_GEORGIA_AND_THE_SOUTH_SANDWICH_ISLANDS = 239
    SOUTH_SUDAN = 728
    SPAIN = 724
    SRI_LANKA = 144
    SUDAN = 729
    SURINAME = 740
    SVALBARD = 744
    SWEDEN = 752
    SWITZERLAND = 756
    SYRIAN_ARAB_REPUBLIC = 760
    TAIWAN_PROVINCE_OF_CHINA = 158
    TAJIKISTAN = 762
    TANZANIA = 834
    THAILAND = 764
    TIMOR_LESTE = 626
    TOGO = 768
    TOKELAU = 772
    TONGA = 776
    TRINIDAD_AND_TOBAGO = 780
    TUNISIA = 788
    TURKIYE = 792
    TURKMENISTAN = 795
    TURKS_AND_CAICOS_ISLANDS = 796
    TUVALU = 798
    UGANDA = 800
    UKRAINE = 804
    UNITED_ARAB_EMIRATES = 784
    GREAT_BRITAIN = 826
    UNITED_STATES_MINOR_OUTLYING_ISLANDS = 581
    USA = 840
    URUGUAY = 858
    UZBEKISTAN = 860
    VANUATU = 548
    VENEZUELA = 862
    VIET_NAM = 704
    VIRGIN_ISLANDS_BRITISH = 92
    VIRGIN_ISLANDS_US = 850
    WALLIS_AND_FUTUNA = 876
    WESTERN_SAHARA = 732
    YEMEN = 887
    ZAMBIA = 894
    ZIMBABWE = 716



class CountriesA2(StrEnum):
    """ISO 3166 alpha-2"""

    AFGHANISTAN = 'AF'
    ALAND_ISLANDS = 'AX'
    ALBANIA = 'AL'
    ALGERIA = 'DZ'
    AMERICAN_SAMOA = 'AS'
    ANDORRA = 'AD'
    ANGOLA = 'AO'
    ANGUILLA = 'AI'
    ANTARCTICA = 'AQ'
    ANTIGUA_AND_BARBUDA = 'AG'
    ARGENTINA = 'AR'
    ARMENIA = 'AM'
    ARUBA = 'AW'
    AUSTRALIA = 'AU'
    AUSTRIA = 'AT'
    AZERBAIJAN = 'AZ'
    BAHAMAS = 'BS'
    BAHRAIN = 'BH'
    BANGLADESH = 'BD'
    BARBADOS = 'BB'
    BELARUS = 'BY'
    BELGIUM = 'BE'
    BELIZE = 'BZ'
    BENIN = 'BJ'
    BERMUDA = 'BM'
    BHUTAN = 'BT'
    BOLIVIA = 'BO'
    BONAIRE = 'BQ'
    BOSNIA_AND_HERZEGOVINA = 'BA'
    BOTSWANA = 'BW'
    BOUVET_ISLAND = 'BV'
    BRAZIL = 'BR'
    BRITISH_INDIAN_OCEAN_TERRITORY = 'IO'
    BRUNEI_DARUSSALAM = 'BN'
    BULGARIA = 'BG'
    BURKINA_FASO = 'BF'
    BURUNDI = 'BI'
    CABO_VERDE = 'CV'
    CAMBODIA = 'KH'
    CAMEROON = 'CM'
    CANADA = 'CA'
    CAYMAN_ISLANDS = 'KY'
    CENTRAL_AFRICAN_REPUBLIC = 'CF'
    CHAD = 'TD'
    CHILE = 'CL'
    CHINA = 'CN'
    CHRISTMAS_ISLAND = 'CX'
    COCOS_KEELING_ISLANDS = 'CC'
    COLOMBIA = 'CO'
    COMOROS = 'KM'
    CONGO = 'CG'
    CONGO_DEMOCRATIC_REPUBLIC = 'CD'
    COOK_ISLANDS = 'CK'
    COSTA_RICA = 'CR'
    COTE_DIVOIRE = 'CI'
    CROATIA = 'HR'
    CUBA = 'CU'
    CURACAO = 'CW'
    CYPRUS = 'CY'
    CZECHIA = 'CZ'
    DENMARK = 'DK'
    DJIBOUTI = 'DJ'
    DOMINICA = 'DM'
    DOMINICAN_REPUBLIC = 'DO'
    ECUADOR = 'EC'
    EGYPT = 'EG'
    EL_SALVADOR = 'SV'
    EQUATORIAL_GUINEA = 'GQ'
    ERITREA = 'ER'
    ESTONIA = 'EE'
    ESWATINI = 'SZ'
    ETHIOPIA = 'ET'
    FALKLAND_ISLANDS = 'FK'
    FAROE_ISLANDS = 'FO'
    FIJI = 'FJ'
    FINLAND = 'FI'
    FRANCE = 'FR'
    FRENCH_GUIANA = 'GF'
    FRENCH_POLYNESIA = 'PF'
    FRENCH_SOUTHERN_TERRITORIES = 'TF'
    GABON = 'GA'
    GAMBIA = 'GM'
    GEORGIA = 'GE'
    GERMANY = 'DE'
    GHANA = 'GH'
    GIBRALTAR = 'GI'
    GREAT_BRITAIN = 'GB'
    GREECE = 'GR'
    GREENLAND = 'GL'
    GRENADA = 'GD'
    GUADELOUPE = 'GP'
    GUAM = 'GU'
    GUATEMALA = 'GT'
    GUERNSEY = 'GG'
    GUINEA = 'GN'
    GUINEA_BISSAU = 'GW'
    GUYANA = 'GY'
    HAITI = 'HT'
    HEARD_ISLAND_AND_MCDONALD_ISLANDS = 'HM'
    HOLY_SEE = 'VA'
    HONDURAS = 'HN'
    HONG_KONG = 'HK'
    HUNGARY = 'HU'
    ICELAND = 'IS'
    INDIA = 'IN'
    INDONESIA = 'ID'
    IRAN = 'IR'
    IRAQ = 'IQ'
    IRELAND = 'IE'
    ISLE_OF_MAN = 'IM'
    ISRAEL = 'IL'
    ITALY = 'IT'
    JAMAICA = 'JM'
    JAPAN = 'JP'
    JERSEY = 'JE'
    JORDAN = 'JO'
    KAZAKHSTAN = 'KZ'
    KENYA = 'KE'
    KIRIBATI = 'KI'
    KOREA_DEMOCRATIC_PEOPLES_REPUBLIC = 'KP'
    KOREA_REPUBLIC = 'KR'
    KUWAIT = 'KW'
    KYRGYZSTAN = 'KG'
    LAO_PEOPLES_DEMOCRATIC_REPUBLIC = 'LA'
    LATVIA = 'LV'
    LEBANON = 'LB'
    LESOTHO = 'LS'
    LIBERIA = 'LR'
    LIBYA = 'LY'
    LIECHTENSTEIN = 'LI'
    LITHUANIA = 'LT'
    LUXEMBOURG = 'LU'
    MACAO = 'MO'
    MADAGASCAR = 'MG'
    MALAWI = 'MW'
    MALAYSIA = 'MY'
    MALDIVES = 'MV'
    MALI = 'ML'
    MALTA = 'MT'
    MARSHALL_ISLANDS = 'MH'
    MARTINIQUE = 'MQ'
    MAURITANIA = 'MR'
    MAURITIUS = 'MU'
    MAYOTTE = 'YT'
    MEXICO = 'MX'
    MICRONESIA = 'FM'
    MOLDOVA = 'MD'
    MONACO = 'MC'
    MONGOLIA = 'MN'
    MONTENEGRO = 'ME'
    MONTSERRAT = 'MS'
    MOROCCO = 'MA'
    MOZAMBIQUE = 'MZ'
    MYANMAR = 'MM'
    NAMIBIA = 'NA'
    NAURU = 'NR'
    NEPAL = 'NP'
    NETHERLANDS = 'NL'
    NEW_CALEDONIA = 'NC'
    NEW_ZEALAND = 'NZ'
    NICARAGUA = 'NI'
    NIGER = 'NE'
    NIGERIA = 'NG'
    NIUE = 'NU'
    NORFOLK_ISLAND = 'NF'
    NORTH_MACEDONIA = 'MK'
    NORTHERN_MARIANA_ISLANDS = 'MP'
    NORWAY = 'NO'
    OMAN = 'OM'
    PAKISTAN = 'PK'
    PALAU = 'PW'
    PALESTINE = 'PS'
    PANAMA = 'PA'
    PAPUA_NEW_GUINEA = 'PG'
    PARAGUAY = 'PY'
    PERU = 'PE'
    PHILIPPINES = 'PH'
    PITCAIRN = 'PN'
    POLAND = 'PL'
    PORTUGAL = 'PT'
    PUERTO_RICO = 'PR'
    QATAR = 'QA'
    REUNION = 'RE'
    ROMANIA = 'RO'
    RUSSIA = 'RU'
    RWANDA = 'RW'
    SAINT_BARTHELEMY = 'BL'
    SAINT_HELENA = 'SH'
    SAINT_KITTS_AND_NEVIS = 'KN'
    SAINT_LUCIA = 'LC'
    SAINT_MARTIN_FRENCH_PART = 'MF'
    SAINT_PIERRE_AND_MIQUELON = 'PM'
    SAINT_VINCENT_AND_THE_GRENADINES = 'VC'
    SAMOA = 'WS'
    SAN_MARINO = 'SM'
    SAO_TOME_AND_PRINCIPE = 'ST'
    SAUDI_ARABIA = 'SA'
    SENEGAL = 'SN'
    SERBIA = 'RS'
    SEYCHELLES = 'SC'
    SIERRA_LEONE = 'SL'
    SINGAPORE = 'SG'
    SINT_MAARTEN_DUTCH_PART = 'SX'
    SLOVAKIA = 'SK'
    SLOVENIA = 'SI'
    SOLOMON_ISLANDS = 'SB'
    SOMALIA = 'SO'
    SOUTH_AFRICA = 'ZA'
    SOUTH_GEORGIA_AND_THE_SOUTH_SANDWICH_ISLANDS = 'GS'
    SOUTH_SUDAN = 'SS'
    SPAIN = 'ES'
    SRI_LANKA = 'LK'
    SUDAN = 'SD'
    SURINAME = 'SR'
    SVALBARD = 'SJ'
    SWEDEN = 'SE'
    SWITZERLAND = 'CH'
    SYRIAN_ARAB_REPUBLIC = 'SY'
    TAIWAN_PROVINCE_OF_CHINA = 'TW'
    TAJIKISTAN = 'TJ'
    TANZANIA = 'TZ'
    THAILAND = 'TH'
    TIMOR_LESTE = 'TL'
    TOGO = 'TG'
    TOKELAU = 'TK'
    TONGA = 'TO'
    TRINIDAD_AND_TOBAGO = 'TT'
    TUNISIA = 'TN'
    TURKIYE = 'TR'
    TURKMENISTAN = 'TM'
    TURKS_AND_CAICOS_ISLANDS = 'TC'
    TUVALU = 'TV'
    UGANDA = 'UG'
    UKRAINE = 'UA'
    UNITED_ARAB_EMIRATES = 'AE'
    UNITED_STATES_MINOR_OUTLYING_ISLANDS = 'UM'
    URUGUAY = 'UY'
    USA = 'US'
    UZBEKISTAN = 'UZ'
    VANUATU = 'VU'
    VENEZUELA = 'VE'
    VIET_NAM = 'VN'
    VIRGIN_ISLANDS_BRITISH = 'VG'
    VIRGIN_ISLANDS_US = 'VI'
    WALLIS_AND_FUTUNA = 'WF'
    WESTERN_SAHARA = 'EH'
    YEMEN = 'YE'
    ZAMBIA = 'ZM'
    ZIMBABWE = 'ZW'


class CountriesA3(StrEnum):
    """ISO-3166 alpha-3"""

    AFGHANISTAN = 'AFG'
    ALAND_ISLANDS = 'ALA'
    ALBANIA = 'ALB'
    ALGERIA = 'DZA'
    AMERICAN_SAMOA = 'ASM'
    ANDORRA = 'AND'
    ANGOLA = 'AGO'
    ANGUILLA = 'AIA'
    ANTARCTICA = 'ATA'
    ANTIGUA_AND_BARBUDA = 'ATG'
    ARGENTINA = 'ARG'
    ARMENIA = 'ARM'
    ARUBA = 'ABW'
    AUSTRALIA = 'AUS'
    AUSTRIA = 'AUT'
    AZERBAIJAN = 'AZE'
    BAHAMAS = 'BHS'
    BAHRAIN = 'BHR'
    BANGLADESH = 'BGD'
    BARBADOS = 'BRB'
    BELARUS = 'BLR'
    BELGIUM = 'BEL'
    BELIZE = 'BLZ'
    BENIN = 'BEN'
    BERMUDA = 'BMU'
    BHUTAN = 'BTN'
    BOLIVIA = 'BOL'
    BONAIRE = 'BES'
    BOSNIA_AND_HERZEGOVINA = 'BIH'
    BOTSWANA = 'BWA'
    BOUVET_ISLAND = 'BVT'
    BRAZIL = 'BRA'
    BRITISH_INDIAN_OCEAN_TERRITORY = 'IOT'
    BRUNEI_DARUSSALAM = 'BRN'
    BULGARIA = 'BGR'
    BURKINA_FASO = 'BFA'
    BURUNDI = 'BDI'
    CABO_VERDE = 'CPV'
    CAMBODIA = 'KHM'
    CAMEROON = 'CMR'
    CANADA = 'CAN'
    CAYMAN_ISLANDS = 'CYM'
    CENTRAL_AFRICAN_REPUBLIC = 'CAF'
    CHAD = 'TCD'
    CHILE = 'CHL'
    CHINA = 'CHN'
    CHRISTMAS_ISLAND = 'CXR'
    COCOS_KEELING_ISLANDS = 'CCK'
    COLOMBIA = 'COL'
    COMOROS = 'COM'
    CONGO = 'COG'
    CONGO_DEMOCRATIC_REPUBLIC = 'COD'
    COOK_ISLANDS = 'COK'
    COSTA_RICA = 'CRI'
    COTE_DIVOIRE = 'CIV'
    CROATIA = 'HRV'
    CUBA = 'CUB'
    CURACAO = 'CUW'
    CYPRUS = 'CYP'
    CZECHIA = 'CZE'
    DENMARK = 'DNK'
    DJIBOUTI = 'DJI'
    DOMINICA = 'DMA'
    DOMINICAN_REPUBLIC = 'DOM'
    ECUADOR = 'ECU'
    EGYPT = 'EGY'
    EL_SALVADOR = 'SLV'
    EQUATORIAL_GUINEA = 'GNQ'
    ERITREA = 'ERI'
    ESTONIA = 'EST'
    ESWATINI = 'SWZ'
    ETHIOPIA = 'ETH'
    FALKLAND_ISLANDS = 'FLK'
    FAROE_ISLANDS = 'FRO'
    FIJI = 'FJI'
    FINLAND = 'FIN'
    FRANCE = 'FRA'
    FRENCH_GUIANA = 'GUF'
    FRENCH_POLYNESIA = 'PYF'
    FRENCH_SOUTHERN_TERRITORIES = 'ATF'
    GABON = 'GAB'
    GAMBIA = 'GMB'
    GEORGIA = 'GEO'
    GERMANY = 'DEU'
    GHANA = 'GHA'
    GIBRALTAR = 'GIB'
    GREAT_BRITAIN = 'GBR'
    GREECE = 'GRC'
    GREENLAND = 'GRL'
    GRENADA = 'GRD'
    GUADELOUPE = 'GLP'
    GUAM = 'GUM'
    GUATEMALA = 'GTM'
    GUERNSEY = 'GGY'
    GUINEA = 'GIN'
    GUINEA_BISSAU = 'GNB'
    GUYANA = 'GUY'
    HAITI = 'HTI'
    HEARD_ISLAND_AND_MCDONALD_ISLANDS = 'HMD'
    HOLY_SEE = 'VAT'
    HONDURAS = 'HND'
    HONG_KONG = 'HKG'
    HUNGARY = 'HUN'
    ICELAND = 'ISL'
    INDIA = 'IND'
    INDONESIA = 'IDN'
    IRAN = 'IRN'
    IRAQ = 'IRQ'
    IRELAND = 'IRL'
    ISLE_OF_MAN = 'IMN'
    ISRAEL = 'ISR'
    ITALY = 'ITA'
    JAMAICA = 'JAM'
    JAPAN = 'JPN'
    JERSEY = 'JEY'
    JORDAN = 'JOR'
    KAZAKHSTAN = 'KAZ'
    KENYA = 'KEN'
    KIRIBATI = 'KIR'
    KOREA_DEMOCRATIC_PEOPLES_REPUBLIC = 'PRK'
    KOREA_REPUBLIC = 'KOR'
    KUWAIT = 'KWT'
    KYRGYZSTAN = 'KGZ'
    LAO_PEOPLES_DEMOCRATIC_REPUBLIC = 'LAO'
    LATVIA = 'LVA'
    LEBANON = 'LBN'
    LESOTHO = 'LSO'
    LIBERIA = 'LBR'
    LIBYA = 'LBY'
    LIECHTENSTEIN = 'LIE'
    LITHUANIA = 'LTU'
    LUXEMBOURG = 'LUX'
    MACAO = 'MAC'
    MADAGASCAR = 'MDG'
    MALAWI = 'MWI'
    MALAYSIA = 'MYS'
    MALDIVES = 'MDV'
    MALI = 'MLI'
    MALTA = 'MLT'
    MARSHALL_ISLANDS = 'MHL'
    MARTINIQUE = 'MTQ'
    MAURITANIA = 'MRT'
    MAURITIUS = 'MUS'
    MAYOTTE = 'MYT'
    MEXICO = 'MEX'
    MICRONESIA = 'FSM'
    MOLDOVA = 'MDA'
    MONACO = 'MCO'
    MONGOLIA = 'MNG'
    MONTENEGRO = 'MNE'
    MONTSERRAT = 'MSR'
    MOROCCO = 'MAR'
    MOZAMBIQUE = 'MOZ'
    MYANMAR = 'MMR'
    NAMIBIA = 'NAM'
    NAURU = 'NRU'
    NEPAL = 'NPL'
    NETHERLANDS = 'NLD'
    NEW_CALEDONIA = 'NCL'
    NEW_ZEALAND = 'NZL'
    NICARAGUA = 'NIC'
    NIGER = 'NER'
    NIGERIA = 'NGA'
    NIUE = 'NIU'
    NORFOLK_ISLAND = 'NFK'
    NORTH_MACEDONIA = 'MKD'
    NORTHERN_MARIANA_ISLANDS = 'MNP'
    NORWAY = 'NOR'
    OMAN = 'OMN'
    PAKISTAN = 'PAK'
    PALAU = 'PLW'
    PALESTINE = 'PSE'
    PANAMA = 'PAN'
    PAPUA_NEW_GUINEA = 'PNG'
    PARAGUAY = 'PRY'
    PERU = 'PER'
    PHILIPPINES = 'PHL'
    PITCAIRN = 'PCN'
    POLAND = 'POL'
    PORTUGAL = 'PRT'
    PUERTO_RICO = 'PRI'
    QATAR = 'QAT'
    REUNION = 'REU'
    ROMANIA = 'ROU'
    RUSSIA = 'RUS'
    RWANDA = 'RWA'
    SAINT_BARTHELEMY = 'BLM'
    SAINT_HELENA = 'SHN'
    SAINT_KITTS_AND_NEVIS = 'KNA'
    SAINT_LUCIA = 'LCA'
    SAINT_MARTIN_FRENCH_PART = 'MAF'
    SAINT_PIERRE_AND_MIQUELON = 'SPM'
    SAINT_VINCENT_AND_THE_GRENADINES = 'VCT'
    SAMOA = 'WSM'
    SAN_MARINO = 'SMR'
    SAO_TOME_AND_PRINCIPE = 'STP'
    SAUDI_ARABIA = 'SAU'
    SENEGAL = 'SEN'
    SERBIA = 'SRB'
    SEYCHELLES = 'SYC'
    SIERRA_LEONE = 'SLE'
    SINGAPORE = 'SGP'
    SINT_MAARTEN_DUTCH_PART = 'SXM'
    SLOVAKIA = 'SVK'
    SLOVENIA = 'SVN'
    SOLOMON_ISLANDS = 'SLB'
    SOMALIA = 'SOM'
    SOUTH_AFRICA = 'ZAF'
    SOUTH_GEORGIA_AND_THE_SOUTH_SANDWICH_ISLANDS = 'SGS'
    SOUTH_SUDAN = 'SSD'
    SPAIN = 'ESP'
    SRI_LANKA = 'LKA'
    SUDAN = 'SDN'
    SURINAME = 'SUR'
    SVALBARD = 'SJM'
    SWEDEN = 'SWE'
    SWITZERLAND = 'CHE'
    SYRIAN_ARAB_REPUBLIC = 'SYR'
    TAIWAN_PROVINCE_OF_CHINA = 'TWN'
    TAJIKISTAN = 'TJK'
    TANZANIA = 'TZA'
    THAILAND = 'THA'
    TIMOR_LESTE = 'TLS'
    TOGO = 'TGO'
    TOKELAU = 'TKL'
    TONGA = 'TON'
    TRINIDAD_AND_TOBAGO = 'TTO'
    TUNISIA = 'TUN'
    TURKIYE = 'TUR'
    TURKMENISTAN = 'TKM'
    TURKS_AND_CAICOS_ISLANDS = 'TCA'
    TUVALU = 'TUV'
    UGANDA = 'UGA'
    UKRAINE = 'UKR'
    UNITED_ARAB_EMIRATES = 'ARE'
    UNITED_STATES_MINOR_OUTLYING_ISLANDS = 'UMI'
    URUGUAY = 'URY'
    USA = 'USA'
    UZBEKISTAN = 'UZB'
    VANUATU = 'VUT'
    VENEZUELA = 'VEN'
    VIET_NAM = 'VNM'
    VIRGIN_ISLANDS_BRITISH = 'VGB'
    VIRGIN_ISLANDS_US = 'VIR'
    WALLIS_AND_FUTUNA = 'WLF'
    WESTERN_SAHARA = 'ESH'
    YEMEN = 'YEM'
    ZAMBIA = 'ZMB'
    ZIMBABWE = 'ZWE'


@dataclass
class CountriesMixin:
    # pylint: disable=too-many-instance-attributes
    short_en: str
    long_en: str
    short_ru: str
    long_ru: str
    a2: str
    a3: str
    num: int
    tld: str


class Countries(CountriesMixin, Enum):
    AFGHANISTAN = (
        'Afghanistan',
        'The Islamic Republic of Afghanistan',
        'Афганистан',
        'Переходное Исламское Государство Афганистан',
        'AF',
        'AFG',
        4,
        '.af',
    )
    ALAND_ISLANDS = (
        'Åland Islands',
        'Åland',
        'Эландские Острова',
        'Эландские Острова',
        'AX',
        'ALA',
        248,
        '.ax',
    )
    ALBANIA = (
        'Albania',
        'The Republic of Albania',
        'Албания',
        'Республика Албания',
        'AL',
        'ALB',
        8,
        '.al',
    )
    ALGERIA = (
        'Algeria',
        "The People's Democratic Republic of Algeria",
        'Алжир',
        'Алжирская Народная Демократическая Республика',
        'DZ',
        'DZA',
        12,
        '.dz',
    )
    AMERICAN_SAMOA = (
        'American Samoa',
        'The Territory of American Samoa',
        'Американское Самоа',
        'Американское Самоа',
        'AS',
        'ASM',
        16,
        '.as',
    )
    ANDORRA = (
        'Andorra',
        'The Principality of Andorra',
        'Андорра',
        'Княжество Андорра',
        'AD',
        'AND',
        20,
        '.ad',
    )
    ANGOLA = (
        'Angola',
        'The Republic of Angola',
        'Ангола',
        'Республика Ангола',
        'AO',
        'AGO',
        24,
        '.ao',
    )
    ANGUILLA = ('Anguilla', 'Anguilla', 'Ангилья', 'Ангилья', 'AI', 'AIA', 660, '.ai')
    ANTARCTICA = (
        'Antarctica',
        'Antarctica (all land and ice shelves south of the 60th parallel south)',
        'Антарктида',
        'Антарктида',
        'AQ',
        'ATA',
        10,
        '.aq',
    )
    ANTIGUA_AND_BARBUDA = (
        'Antigua and Barbuda',
        'Antigua and Barbuda',
        'Антигуа и Барбуда',
        'Антигуа и Барбуда',
        'AG',
        'ATG',
        28,
        '.ag',
    )
    ARGENTINA = (
        'Argentina',
        'The Argentine Republic',
        'Аргентина',
        'Аргентинская Республика',
        'AR',
        'ARG',
        32,
        '.ar',
    )
    ARMENIA = (
        'Armenia',
        'The Republic of Armenia',
        'Армения',
        'Республика Армения',
        'AM',
        'ARM',
        51,
        '.am',
    )
    ARUBA = ('Aruba', 'Aruba', 'Аруба', 'Аруба', 'AW', 'ABW', 533, '.aw')
    AUSTRALIA = (
        'Australia',
        'The Commonwealth of Australia',
        'Австралия',
        'Австралия',
        'AU',
        'AUS',
        36,
        '.au',
    )
    AUSTRIA = (
        'Austria',
        'The Republic of Austria',
        'Австрия',
        'Австрийская Республика',
        'AT',
        'AUT',
        40,
        '.at',
    )
    AZERBAIJAN = (
        'Azerbaijan',
        'The Republic of Azerbaijan',
        'Азербайджан',
        'Республика Азербайджан',
        'AZ',
        'AZE',
        31,
        '.az',
    )
    BAHAMAS = (
        'Bahamas',
        'The Commonwealth of The Bahamas',
        'Багамы',
        'Содружество Багамы',
        'BS',
        'BHS',
        44,
        '.bs',
    )
    BAHRAIN = (
        'Bahrain',
        'The Kingdom of Bahrain',
        'Бахрейн',
        'Королевство Бахрейн',
        'BH',
        'BHR',
        48,
        '.bh',
    )
    BANGLADESH = (
        'Bangladesh',
        "The People's Republic of Bangladesh",
        'Бангладеш',
        'Народная Республика Бангладеш',
        'BD',
        'BGD',
        50,
        '.bd',
    )
    BARBADOS = ('Barbados', 'Barbados', 'Барбадос', 'Барбадос', 'BB', 'BRB', 52, '.bb')
    BELARUS = (
        'Belarus',
        'The Republic of Belarus',
        'Беларусь',
        'Республика Беларусь',
        'BY',
        'BLR',
        112,
        '.by',
    )
    BELGIUM = (
        'Belgium',
        'The Kingdom of Belgium',
        'Бельгия',
        'Королевство Бельгия',
        'BE',
        'BEL',
        56,
        '.be',
    )
    BELIZE = ('Belize', 'Belize', 'Белиз', 'Белиз', 'BZ', 'BLZ', 84, '.bz')
    BENIN = (
        'Benin',
        'The Republic of Benin',
        'Бенин',
        'Республика Бенин',
        'BJ',
        'BEN',
        204,
        '.bj',
    )
    BERMUDA = ('Bermuda', 'Bermuda', 'Бермуды', 'Бермуды', 'BM', 'BMU', 60, '.bm')
    BHUTAN = (
        'Bhutan',
        'The Kingdom of Bhutan',
        'Бутан',
        'Королевство Бутан',
        'BT',
        'BTN',
        64,
        '.bt',
    )
    BOLIVIA = (
        'Bolivia (Plurinational State of)',
        'The Plurinational State of Bolivia',
        'Боливия, Многонациональное Государство',
        'Многонациональное Государство Боливия',
        'BO',
        'BOL',
        68,
        '.bo',
    )
    BONAIRE = (
        'Bonaire',
        'Bonaire, Sint Eustatius and Saba',
        'Бонэйр, Синт-Эстатиус и Саба',
        'Бонэйр, Синт-Эстатиус и Саба',
        'BQ',
        'BES',
        535,
        '.bq.nl',
    )
    BOSNIA_AND_HERZEGOVINA = (
        'Bosnia and Herzegovina',
        'Bosnia and Herzegovina',
        'Босния и Герцеговина',
        'Босния и Герцеговина',
        'BA',
        'BIH',
        70,
        '.ba',
    )
    BOTSWANA = (
        'Botswana',
        'The Republic of Botswana',
        'Ботсвана',
        'Республика Ботсвана',
        'BW',
        'BWA',
        72,
        '.bw',
    )
    BOUVET_ISLAND = (
        'Bouvet Island',
        'Bouvet Island',
        'Остров Буве',
        'Остров Буве',
        'BV',
        'BVT',
        74,
        '',
    )
    BRAZIL = (
        'Brazil',
        'The Federative Republic of Brazil',
        'Бразилия',
        'Федеративная Республика Бразилия',
        'BR',
        'BRA',
        76,
        '.br',
    )
    BRITISH_INDIAN_OCEAN_TERRITORY = (
        'British Indian Ocean Territory',
        'The British Indian Ocean Territory',
        'Британская Территория В Индийском Океане',
        'Британская Территория В Индийском Океане',
        'IO',
        'IOT',
        86,
        '.io',
    )
    BRUNEI_DARUSSALAM = (
        'Brunei Darussalam',
        'The Nation of Brunei, the Abode of Peace',
        'Бруней-Даруссалам',
        'Бруней-Даруссалам',
        'BN',
        'BRN',
        96,
        '.bn',
    )
    BULGARIA = (
        'Bulgaria',
        'The Republic of Bulgaria',
        'Болгария',
        'Республика Болгария',
        'BG',
        'BGR',
        100,
        '.bg',
    )
    BURKINA_FASO = (
        'Burkina Faso',
        'Burkina Faso',
        'Буркина-Фасо',
        'Буркина-Фасо',
        'BF',
        'BFA',
        854,
        '.bf',
    )
    BURUNDI = (
        'Burundi',
        'The Republic of Burundi',
        'Бурунди',
        'Республика Бурунди',
        'BI',
        'BDI',
        108,
        '.bi',
    )
    CABO_VERDE = (
        'Cabo Verde',
        'The Republic of Cabo Verde',
        'Кабо-Верде',
        'Республика Кабо-Верде',
        'CV',
        'CPV',
        132,
        '.cv',
    )
    CAMBODIA = (
        'Cambodia',
        'The Kingdom of Cambodia',
        'Камбоджа',
        'Королевство Камбоджа',
        'KH',
        'KHM',
        116,
        '.kh',
    )
    CAMEROON = (
        'Cameroon',
        'The Republic of Cameroon',
        'Камерун',
        'Республика Камерун',
        'CM',
        'CMR',
        120,
        '.cm',
    )
    CANADA = ('Canada', 'Canada', 'Канада', 'Канада', 'CA', 'CAN', 124, '.ca')
    CAYMAN_ISLANDS = (
        'Cayman Islands',
        'The Cayman Islands',
        'Острова Кайман',
        'Острова Кайман',
        'KY',
        'CYM',
        136,
        '.ky',
    )
    CENTRAL_AFRICAN_REPUBLIC = (
        'Central African Republic',
        'The Central African Republic',
        'Центрально-Африканская Республика',
        'Центрально-Африканская Республика',
        'CF',
        'CAF',
        140,
        '.cf',
    )
    CHAD = (
        'Chad',
        'The Republic of Chad',
        'Чад',
        'Республика Чад',
        'TD',
        'TCD',
        148,
        '.td',
    )
    CHILE = (
        'Chile',
        'The Republic of Chile',
        'Чили',
        'Республика Чили',
        'CL',
        'CHL',
        152,
        '.cl',
    )
    CHINA = (
        'China',
        "The People's Republic of China",
        'Китай',
        'Китайская Народная Республика',
        'CN',
        'CHN',
        156,
        '.cn',
    )
    CHRISTMAS_ISLAND = (
        'Christmas Island',
        'The Territory of Christmas Island',
        'Остров Рождества',
        'Остров Рождества',
        'CX',
        'CXR',
        162,
        '.cx',
    )
    COCOS_KEELING_ISLANDS = (
        'Cocos (Keeling) Islands',
        'The Territory of Cocos (Keeling) Islands',
        'Кокосовые (Килинг) Острова',
        'Кокосовые (Килинг) Острова',
        'CC',
        'CCK',
        166,
        '.cc',
    )
    COLOMBIA = (
        'Colombia',
        'The Republic of Colombia',
        'Колумбия',
        'Республика Колумбия',
        'CO',
        'COL',
        170,
        '.co',
    )
    COMOROS = (
        'Comoros',
        'The Union of the Comoros',
        'Коморы',
        'Союз Коморы',
        'KM',
        'COM',
        174,
        '.km',
    )
    CONGO_DEMOCRATIC_REPUBLIC = (
        'Congo (the Democratic Republic of the)',
        'The Democratic Republic of the Congo',
        'Конго, Демократическая Республика',
        'Демократическая Республика Конго',
        'CD',
        'COD',
        180,
        '.cd',
    )
    CONGO = (
        'Congo',
        'The Republic of the Congo',
        'Конго',
        'Республика Конго',
        'CG',
        'COG',
        178,
        '.cg',
    )
    COOK_ISLANDS = (
        'Cook Islands',
        'The Cook Islands',
        'Острова Кука',
        'Острова Кука',
        'CK',
        'COK',
        184,
        '.ck',
    )
    COSTA_RICA = (
        'Costa Rica',
        'The Republic of Costa Rica',
        'Коста-Рика',
        'Республика Коста-Рика',
        'CR',
        'CRI',
        188,
        '.cr',
    )
    COTE_DIVOIRE = (
        "Côte d'Ivoire",
        "The Republic of Côte d'Ivoire",
        "Кот Д'Ивуар",
        "Республика Кот Д'Ивуар",
        'CI',
        'CIV',
        384,
        '.ci',
    )
    CROATIA = (
        'Croatia',
        'The Republic of Croatia',
        'Хорватия',
        'Республика Хорватия',
        'HR',
        'HRV',
        191,
        '.hr',
    )
    CUBA = (
        'Cuba',
        'The Republic of Cuba',
        'Куба',
        'Республика Куба',
        'CU',
        'CUB',
        192,
        '.cu',
    )
    CURACAO = (
        'Curaçao',
        'The Country of Curaçao',
        'Кюрасао',
        'Кюрасао',
        'CW',
        'CUW',
        531,
        '.cw',
    )
    CYPRUS = (
        'Cyprus',
        'The Republic of Cyprus',
        'Кипр',
        'Республика Кипр',
        'CY',
        'CYP',
        196,
        '.cy',
    )
    CZECHIA = (
        'Czechia',
        'The Czech Republic',
        'Чехия',
        'Чешская Республика',
        'CZ',
        'CZE',
        203,
        '.cz',
    )
    DENMARK = (
        'Denmark',
        'The Kingdom of Denmark',
        'Дания',
        'Королевство Дания',
        'DK',
        'DNK',
        208,
        '.dk',
    )
    DJIBOUTI = (
        'Djibouti',
        'The Republic of Djibouti',
        'Джибути',
        'Республика Джибути',
        'DJ',
        'DJI',
        262,
        '.dj',
    )
    DOMINICA = (
        'Dominica',
        'The Commonwealth of Dominica',
        'Доминика',
        'Содружество Доминики',
        'DM',
        'DMA',
        212,
        '.dm',
    )
    DOMINICAN_REPUBLIC = (
        'Dominican Republic',
        'The Dominican Republic',
        'Доминиканская Республика',
        'Доминиканская Республика',
        'DO',
        'DOM',
        214,
        '.do',
    )
    ECUADOR = (
        'Ecuador',
        'The Republic of Ecuador',
        'Эквадор',
        'Республика Эквадор',
        'EC',
        'ECU',
        218,
        '.ec',
    )
    EGYPT = (
        'Egypt',
        'The Arab Republic of Egypt',
        'Египет',
        'Арабская Республика Египет',
        'EG',
        'EGY',
        818,
        '.eg',
    )
    EL_SALVADOR = (
        'El Salvador',
        'The Republic of El Salvador',
        'Эль-Сальвадор',
        'Республика Эль-Сальвадор',
        'SV',
        'SLV',
        222,
        '.sv',
    )
    EQUATORIAL_GUINEA = (
        'Equatorial Guinea',
        'The Republic of Equatorial Guinea',
        'Экваториальная Гвинея',
        'Республика Экваториальная Гвинея',
        'GQ',
        'GNQ',
        226,
        '.gq',
    )
    ERITREA = (
        'Eritrea',
        'The State of Eritrea',
        'Эритрея',
        'Государство Эритрея',
        'ER',
        'ERI',
        232,
        '.er',
    )
    ESTONIA = (
        'Estonia',
        'The Republic of Estonia',
        'Эстония',
        'Эстонская Республика',
        'EE',
        'EST',
        233,
        '.ee',
    )
    ESWATINI = (
        'Eswatini',
        'The Kingdom of Eswatini',
        'Эсватини',
        'Королевство Эсватини',
        'SZ',
        'SWZ',
        748,
        '.sz',
    )
    ETHIOPIA = (
        'Ethiopia',
        'The Federal Democratic Republic of Ethiopia',
        'Эфиопия',
        'Федеративная Демократическая Республика Эфиопия',
        'ET',
        'ETH',
        231,
        '.et',
    )
    FALKLAND_ISLANDS = (
        'Falkland Islands',
        'The Falkland Islands',
        'Фолклендские Острова (Мальвинские)',
        'Фолклендские Острова (Мальвинские)',
        'FK',
        'FLK',
        238,
        '.fk',
    )
    FAROE_ISLANDS = (
        'Faroe Islands',
        'The Faroe Islands',
        'Фарерские Острова',
        'Фарерские Острова',
        'FO',
        'FRO',
        234,
        '.fo',
    )
    FIJI = (
        'Fiji',
        'The Republic of Fiji',
        'Фиджи',
        'Республика Фиджи',
        'FJ',
        'FJI',
        242,
        '.fj',
    )
    FINLAND = (
        'Finland',
        'The Republic of Finland',
        'Финляндия',
        'Финляндская Республика',
        'FI',
        'FIN',
        246,
        '.fi',
    )
    FRANCE = (
        'France',
        'The French Republic',
        'Франция',
        'Французская Республика',
        'FR',
        'FRA',
        250,
        '.fr',
    )
    FRENCH_GUIANA = (
        'French Guiana',
        'Guyane',
        'Французская Гвиана',
        'Французская Гвиана',
        'GF',
        'GUF',
        254,
        '.gf',
    )
    FRENCH_POLYNESIA = (
        'French Polynesia',
        'French Polynesia',
        'Французская Полинезия',
        'Французская Полинезия',
        'PF',
        'PYF',
        258,
        '.pf',
    )
    FRENCH_SOUTHERN_TERRITORIES = (
        'French Southern Territories',
        'The French Southern and Antarctic Lands',
        'Французские Южные Территории',
        'Французские Южные Территории',
        'TF',
        'ATF',
        260,
        '.tf',
    )
    GABON = (
        'Gabon',
        'The Gabonese Republic',
        'Габон',
        'Габонская Республика',
        'GA',
        'GAB',
        266,
        '.ga',
    )
    GAMBIA = (
        'Gambia',
        'The Republic of The Gambia',
        'Гамбия',
        'Республика Гамбия',
        'GM',
        'GMB',
        270,
        '.gm',
    )
    GEORGIA = ('Georgia', 'Georgia', 'Грузия', 'Грузия', 'GE', 'GEO', 268, '.ge')
    GERMANY = (
        'Germany',
        'The Federal Republic of Germany',
        'Германия',
        'Федеративная Республика Германия',
        'DE',
        'DEU',
        276,
        '.de',
    )
    GHANA = (
        'Ghana',
        'The Republic of Ghana',
        'Гана',
        'Республика Гана',
        'GH',
        'GHA',
        288,
        '.gh',
    )
    GIBRALTAR = (
        'Gibraltar',
        'Gibraltar',
        'Гибралтар',
        'Гибралтар',
        'GI',
        'GIB',
        292,
        '.gi',
    )
    GREECE = (
        'Greece',
        'The Hellenic Republic',
        'Греция',
        'Греческая Республика',
        'GR',
        'GRC',
        300,
        '.gr',
    )
    GREENLAND = (
        'Greenland',
        'Kalaallit Nunaat',
        'Гренландия',
        'Гренландия',
        'GL',
        'GRL',
        304,
        '.gl',
    )
    GRENADA = ('Grenada', 'Grenada', 'Гренада', 'Гренада', 'GD', 'GRD', 308, '.gd')
    GUADELOUPE = (
        'Guadeloupe',
        'Guadeloupe',
        'Гваделупа',
        'Гваделупа',
        'GP',
        'GLP',
        312,
        '.gp',
    )
    GUAM = ('Guam', 'The Territory of Guam', 'Гуам', 'Гуам', 'GU', 'GUM', 316, '.gu')
    GUATEMALA = (
        'Guatemala',
        'The Republic of Guatemala',
        'Гватемала',
        'Республика Гватемала',
        'GT',
        'GTM',
        320,
        '.gt',
    )
    GUERNSEY = (
        'Guernsey',
        'The Bailiwick of Guernsey',
        'Гернси',
        'Гернси',
        'GG',
        'GGY',
        831,
        '.gg',
    )
    GUINEA = (
        'Guinea',
        'The Republic of Guinea',
        'Гвинея',
        'Гвинейская Республика',
        'GN',
        'GIN',
        324,
        '.gn',
    )
    GUINEA_BISSAU = (
        'Guinea-Bissau',
        'The Republic of Guinea-Bissau',
        'Гвинея-Бисау',
        'Республика Гвинея-Бисау',
        'GW',
        'GNB',
        624,
        '.gw',
    )
    GUYANA = (
        'Guyana',
        'The Co-operative Republic of Guyana',
        'Гайана',
        'Республика Гайана',
        'GY',
        'GUY',
        328,
        '.gy',
    )
    HAITI = (
        'Haiti',
        'The Republic of Haiti',
        'Гаити',
        'Республика Гаити',
        'HT',
        'HTI',
        332,
        '.ht',
    )
    HEARD_ISLAND_AND_MCDONALD_ISLANDS = (
        'Heard Island and McDonald Islands',
        'The Territory of Heard Island and McDonald Islands',
        'Остров Херд и Острова Макдональд',
        'Остров Херд и Острова Макдональд',
        'HM',
        'HMD',
        334,
        '.hm',
    )
    HOLY_SEE = (
        'Holy See',
        'The Holy See',
        'Папский Престол (Государство - Город Ватикан)',
        'Папский Престол (Государство - Город Ватикан)',
        'VA',
        'VAT',
        336,
        '.va',
    )
    HONDURAS = (
        'Honduras',
        'The Republic of Honduras',
        'Гондурас',
        'Республика Гондурас',
        'HN',
        'HND',
        340,
        '.hn',
    )
    HONG_KONG = (
        'Hong Kong',
        'The Hong Kong Special Administrative Region of China',
        'Гонконг',
        'Специальный Административный Район Гонконг Китайской Народной Республики',
        'HK',
        'HKG',
        344,
        '.hk',
    )
    HUNGARY = ('Hungary', 'Hungary', 'Венгрия', 'Венгрия', 'HU', 'HUN', 348, '.hu')
    ICELAND = (
        'Iceland',
        'Iceland',
        'Исландия',
        'Республика Исландия',
        'IS',
        'ISL',
        352,
        '.is',
    )
    INDIA = (
        'India',
        'The Republic of India',
        'Индия',
        'Республика Индия',
        'IN',
        'IND',
        356,
        '.in',
    )
    INDONESIA = (
        'Indonesia',
        'The Republic of Indonesia',
        'Индонезия',
        'Республика Индонезия',
        'ID',
        'IDN',
        360,
        '.id',
    )
    IRAN = (
        'Iran (Islamic Republic of)',
        'The Islamic Republic of Iran',
        'Иран',
        'Исламская республика Иран',
        'IR',
        'IRN',
        364,
        '.ir',
    )
    IRAQ = (
        'Iraq',
        'The Republic of Iraq',
        'Ирак',
        'Республика Ирак',
        'IQ',
        'IRQ',
        368,
        '.iq',
    )
    IRELAND = ('Ireland', 'Ireland', 'Ирландия', 'Ирландия', 'IE', 'IRL', 372, '.ie')
    ISLE_OF_MAN = (
        'Isle of Man',
        'The Isle of Man',
        'Остров Мэн',
        'Остров Мэн',
        'IM',
        'IMN',
        833,
        '.im',
    )
    ISRAEL = (
        'Israel',
        'The State of Israel',
        'Израиль',
        'Государство Израиль',
        'IL',
        'ISR',
        376,
        '.il',
    )
    ITALY = (
        'Italy',
        'The Italian Republic',
        'Италия',
        'Итальянская Республика',
        'IT',
        'ITA',
        380,
        '.it',
    )
    JAMAICA = ('Jamaica', 'Jamaica', 'Ямайка', 'Ямайка', 'JM', 'JAM', 388, '.jm')
    JAPAN = ('Japan', 'Japan', 'Япония', 'Япония', 'JP', 'JPN', 392, '.jp')
    JERSEY = (
        'Jersey',
        'The Bailiwick of Jersey',
        'Джерси',
        'Джерси',
        'JE',
        'JEY',
        832,
        '.je',
    )
    JORDAN = (
        'Jordan',
        'The Hashemite Kingdom of Jordan',
        'Иордания',
        'Иорданское Хашимитское Королевство',
        'JO',
        'JOR',
        400,
        '.jo',
    )
    KAZAKHSTAN = (
        'Kazakhstan',
        'The Republic of Kazakhstan',
        'Казахстан',
        'Республика Казахстан',
        'KZ',
        'KAZ',
        398,
        '.kz',
    )
    KENYA = (
        'Kenya',
        'The Republic of Kenya',
        'Кения',
        'Республика Кения',
        'KE',
        'KEN',
        404,
        '.ke',
    )
    KIRIBATI = (
        'Kiribati',
        'The Republic of Kiribati',
        'Кирибати',
        'Республика Кирибати',
        'KI',
        'KIR',
        296,
        '.ki',
    )
    KOREA_DEMOCRATIC_PEOPLES_REPUBLIC = (
        "Korea (the Democratic People's Republic of)",
        "The Democratic People's Republic of Korea",
        'Корея, Народно-Демократическая Республика',
        'Корейская Народно-Демократическая Республика',
        'KP',
        'PRK',
        408,
        '.kp',
    )
    KOREA_REPUBLIC = (
        'Korea (the Republic of)',
        'The Republic of Korea',
        'Корея, Республика',
        'Республика Корея',
        'KR',
        'KOR',
        410,
        '.kr',
    )
    KUWAIT = (
        'Kuwait',
        'The State of Kuwait',
        'Кувейт',
        'Государство Кувейт',
        'KW',
        'KWT',
        414,
        '.kw',
    )
    KYRGYZSTAN = (
        'Kyrgyzstan',
        'The Kyrgyz Republic',
        'Киргизия',
        'Киргизская Республика',
        'KG',
        'KGZ',
        417,
        '.kg',
    )
    LAO_PEOPLES_DEMOCRATIC_REPUBLIC = (
        "Lao People's Democratic Republic",
        "The Lao People's Democratic Republic",
        'Лаос',
        'Лаосская Народно-Демократическая Республика',
        'LA',
        'LAO',
        418,
        '.la',
    )
    LATVIA = (
        'Latvia',
        'The Republic of Latvia',
        'Латвия',
        'Латвийская Республика',
        'LV',
        'LVA',
        428,
        '.lv',
    )
    LEBANON = (
        'Lebanon',
        'The Lebanese Republic',
        'Ливан',
        'Ливанская Республика',
        'LB',
        'LBN',
        422,
        '.lb',
    )
    LESOTHO = (
        'Lesotho',
        'The Kingdom of Lesotho',
        'Лесото',
        'Королевство Лесото',
        'LS',
        'LSO',
        426,
        '.ls',
    )
    LIBERIA = (
        'Liberia',
        'The Republic of Liberia',
        'Либерия',
        'Республика Либерия',
        'LR',
        'LBR',
        430,
        '.lr',
    )
    LIBYA = (
        'Libya',
        'The State of Libya',
        'Ливия',
        'Государство Ливия',
        'LY',
        'LBY',
        434,
        '.ly',
    )
    LIECHTENSTEIN = (
        'Liechtenstein',
        'The Principality of Liechtenstein',
        'Лихтенштейн',
        'Княжество Лихтенштейн',
        'LI',
        'LIE',
        438,
        '.li',
    )
    LITHUANIA = (
        'Lithuania',
        'The Republic of Lithuania',
        'Литва',
        'Литовская Республика',
        'LT',
        'LTU',
        440,
        '.lt',
    )
    LUXEMBOURG = (
        'Luxembourg',
        'The Grand Duchy of Luxembourg',
        'Люксембург',
        'Великое Герцогство Люксембург',
        'LU',
        'LUX',
        442,
        '.lu',
    )
    MACAO = (
        'Macao',
        'The Macao Special Administrative Region of China',
        'Макао',
        'Специальный Административный Район Макао Китайской Народной Республики',
        'MO',
        'MAC',
        446,
        '.mo',
    )
    MADAGASCAR = (
        'Madagascar',
        'The Republic of Madagascar',
        'Мадагаскар',
        'Республика Мадагаскар',
        'MG',
        'MDG',
        450,
        '.mg',
    )
    MALAWI = (
        'Malawi',
        'The Republic of Malawi',
        'Малави',
        'Республика Малави',
        'MW',
        'MWI',
        454,
        '.mw',
    )
    MALAYSIA = (
        'Malaysia',
        'Malaysia',
        'Малайзия',
        'Малайзия',
        'MY',
        'MYS',
        458,
        '.my',
    )
    MALDIVES = (
        'Maldives',
        'The Republic of Maldives',
        'Мальдивы',
        'Мальдивская Республика',
        'MV',
        'MDV',
        462,
        '.mv',
    )
    MALI = (
        'Mali',
        'The Republic of Mali',
        'Мали',
        'Республика Мали',
        'ML',
        'MLI',
        466,
        '.ml',
    )
    MALTA = (
        'Malta',
        'The Republic of Malta',
        'Мальта',
        'Республика Мальта',
        'MT',
        'MLT',
        470,
        '.mt',
    )
    MARSHALL_ISLANDS = (
        'Marshall Islands',
        'The Republic of the Marshall Islands',
        'Маршалловы Острова',
        'Республика Маршалловы Острова',
        'MH',
        'MHL',
        584,
        '.mh',
    )
    MARTINIQUE = (
        'Martinique',
        'Martinique',
        'Мартиника',
        'Мартиника',
        'MQ',
        'MTQ',
        474,
        '.mq',
    )
    MAURITANIA = (
        'Mauritania',
        'The Islamic Republic of Mauritania',
        'Мавритания',
        'Исламская Республика Мавритания',
        'MR',
        'MRT',
        478,
        '.mr',
    )
    MAURITIUS = (
        'Mauritius',
        'The Republic of Mauritius',
        'Маврикий',
        'Республика Маврикий',
        'MU',
        'MUS',
        480,
        '.mu',
    )
    MAYOTTE = (
        'Mayotte',
        'The Department of Mayotte',
        'Майотта',
        'Майотта',
        'YT',
        'MYT',
        175,
        '.yt',
    )
    MEXICO = (
        'Mexico',
        'The United Mexican States',
        'Мексика',
        'Мексиканские Соединенные Штаты',
        'MX',
        'MEX',
        484,
        '.mx',
    )
    MICRONESIA = (
        'Micronesia (Federated States of)',
        'The Federated States of Micronesia',
        'Микронезия',
        'Федеративные Штаты Микронезии',
        'FM',
        'FSM',
        583,
        '.fm',
    )
    MOLDOVA = (
        'Moldova (the Republic of)',
        'The Republic of Moldova',
        'Молдова',
        'Республика Молдова',
        'MD',
        'MDA',
        498,
        '.md',
    )
    MONACO = (
        'Monaco',
        'The Principality of Monaco',
        'Монако',
        'Княжество Монако',
        'MC',
        'MCO',
        492,
        '.mc',
    )
    MONGOLIA = (
        'Mongolia',
        'Mongolia',
        'Монголия',
        'Монголия',
        'MN',
        'MNG',
        496,
        '.mn',
    )
    MONTENEGRO = (
        'Montenegro',
        'Montenegro',
        'Черногория',
        'Черногория',
        'ME',
        'MNE',
        499,
        '.me',
    )
    MONTSERRAT = (
        'Montserrat',
        'Montserrat',
        'Монтсеррат',
        'Монтсеррат',
        'MS',
        'MSR',
        500,
        '.ms',
    )
    MOROCCO = (
        'Morocco',
        'The Kingdom of Morocco',
        'Марокко',
        'Королевство Марокко',
        'MA',
        'MAR',
        504,
        '.ma',
    )
    MOZAMBIQUE = (
        'Mozambique',
        'The Republic of Mozambique',
        'Мозамбик',
        'Республика Мозамбик',
        'MZ',
        'MOZ',
        508,
        '.mz',
    )
    MYANMAR = (
        'Myanmar',
        'The Republic of the Union of Myanmar',
        'Мьянма',
        'Республика Союза Мьянма',
        'MM',
        'MMR',
        104,
        '.mm',
    )
    NAMIBIA = (
        'Namibia',
        'The Republic of Namibia',
        'Намибия',
        'Республика Намибия',
        'NA',
        'NAM',
        516,
        '.na',
    )
    NAURU = (
        'Nauru',
        'The Republic of Nauru',
        'Науру',
        'Республика Науру',
        'NR',
        'NRU',
        520,
        '.nr',
    )
    NEPAL = (
        'Nepal',
        'The Federal Democratic Republic of Nepal',
        'Непал',
        'Федеративная Демократическая Республика Непал',
        'NP',
        'NPL',
        524,
        '.np',
    )
    NETHERLANDS = (
        'Netherlands, Kingdom of the',
        'The Kingdom of the Netherlands',
        'Нидерланды',
        'Королевство Нидерландов',
        'NL',
        'NLD',
        528,
        '.nl',
    )
    NEW_CALEDONIA = (
        'New Caledonia',
        'New Caledonia',
        'Новая Каледония',
        'Новая Каледония',
        'NC',
        'NCL',
        540,
        '.nc',
    )
    NEW_ZEALAND = (
        'New Zealand',
        'New Zealand',
        'Новая Зеландия',
        'Новая Зеландия',
        'NZ',
        'NZL',
        554,
        '.nz',
    )
    NICARAGUA = (
        'Nicaragua',
        'The Republic of Nicaragua',
        'Никарагуа',
        'Республика Никарагуа',
        'NI',
        'NIC',
        558,
        '.ni',
    )
    NIGER = (
        'Niger',
        'The Republic of the Niger',
        'Нигер',
        'Республика Нигер',
        'NE',
        'NER',
        562,
        '.ne',
    )
    NIGERIA = (
        'Nigeria',
        'The Federal Republic of Nigeria',
        'Нигерия',
        'Федеративная Республика Нигерия',
        'NG',
        'NGA',
        566,
        '.ng',
    )
    NIUE = ('Niue', 'Niue', 'Ниуэ', 'Республика Ниуэ', 'NU', 'NIU', 570, '.nu')
    NORFOLK_ISLAND = (
        'Norfolk Island',
        'The Territory of Norfolk Island',
        'Остров Норфолк',
        'Остров Норфолк',
        'NF',
        'NFK',
        574,
        '.nf',
    )
    NORTH_MACEDONIA = (
        'North Macedonia',
        'The Republic of North Macedonia',
        'Северная Македония',
        'Республика Северная Македония',
        'MK',
        'MKD',
        807,
        '.mk',
    )
    NORTHERN_MARIANA_ISLANDS = (
        'Northern Mariana Islands',
        'The Commonwealth of the Northern Mariana Islands',
        'Северные Марианские Острова',
        'Содружество Северных Марианских Островов',
        'MP',
        'MNP',
        580,
        '.mp',
    )
    NORWAY = (
        'Norway',
        'The Kingdom of Norway',
        'Норвегия',
        'Королевство Норвегия',
        'NO',
        'NOR',
        578,
        '.no',
    )
    OMAN = (
        'Oman',
        'The Sultanate of Oman',
        'Оман',
        'Султанат Оман',
        'OM',
        'OMN',
        512,
        '.om',
    )
    PAKISTAN = (
        'Pakistan',
        'The Islamic Republic of Pakistan',
        'Пакистан',
        'Исламская Республика Пакистан',
        'PK',
        'PAK',
        586,
        '.pk',
    )
    PALAU = (
        'Palau',
        'The Republic of Palau',
        'Палау',
        'Республика Палау',
        'PW',
        'PLW',
        585,
        '.pw',
    )
    PALESTINE = (
        'Palestine, State of',
        'The State of Palestine',
        'Палестина',
        'Государство Палестина',
        'PS',
        'PSE',
        275,
        '.ps',
    )
    PANAMA = (
        'Panama',
        'The Republic of Panamá',
        'Панама',
        'Республика Панама',
        'PA',
        'PAN',
        591,
        '.pa',
    )
    PAPUA_NEW_GUINEA = (
        'Papua New Guinea',
        'The Independent State of Papua New Guinea',
        'Папуа-Новая Гвинея',
        'Независимое Государство  Папуа Новая Гвинея',
        'PG',
        'PNG',
        598,
        '.pg',
    )
    PARAGUAY = (
        'Paraguay',
        'The Republic of Paraguay',
        'Парагвай',
        'Республика Парагвай',
        'PY',
        'PRY',
        600,
        '.py',
    )
    PERU = (
        'Peru',
        'The Republic of Perú',
        'Перу',
        'Республика Перу',
        'PE',
        'PER',
        604,
        '.pe',
    )
    PHILIPPINES = (
        'Philippines',
        'The Republic of the Philippines',
        'Филиппины',
        'Республика Филиппины',
        'PH',
        'PHL',
        608,
        '.ph',
    )
    PITCAIRN = (
        'Pitcairn',
        'The Pitcairn, Henderson, Ducie and Oeno Islands',
        'Питкерн',
        'Питкерн',
        'PN',
        'PCN',
        612,
        '.pn',
    )
    POLAND = (
        'Poland',
        'The Republic of Poland',
        'Польша',
        'Республика Польша',
        'PL',
        'POL',
        616,
        '.pl',
    )
    PORTUGAL = (
        'Portugal',
        'The Portuguese Republic',
        'Португалия',
        'Португальская Республика',
        'PT',
        'PRT',
        620,
        '.pt',
    )
    PUERTO_RICO = (
        'Puerto Rico',
        'The Commonwealth of Puerto Rico',
        'Пуэрто-Рико',
        'Пуэрто-Рико',
        'PR',
        'PRI',
        630,
        '.pr',
    )
    QATAR = (
        'Qatar',
        'The State of Qatar',
        'Катар',
        'Государство Катар',
        'QA',
        'QAT',
        634,
        '.qa',
    )
    REUNION = ('Réunion', 'Réunion', 'Реюньон', 'Реюньон', 'RE', 'REU', 638, '.re')
    ROMANIA = ('Romania', 'Romania', 'Румыния', 'Румыния', 'RO', 'ROU', 642, '.ro')
    RUSSIA = (
        'Russian Federation',
        'The Russian Federation',
        'Россия',
        'Российская Федерация',
        'RU',
        'RUS',
        643,
        '.ru',
    )
    RWANDA = (
        'Rwanda',
        'The Republic of Rwanda',
        'Руанда',
        'Руандийская Республика',
        'RW',
        'RWA',
        646,
        '.rw',
    )
    SAINT_BARTHELEMY = (
        'Saint Barthélemy',
        'The Collectivity of Saint-Barthélemy',
        'Сен-Бартелеми',
        'Сен-Бартелеми',
        'BL',
        'BLM',
        652,
        '.bl',
    )
    SAINT_HELENA = (
        'Saint Helena',
        'Saint Helena, Ascension and Tristan da Cunha',
        'Святая Елена, Остров Вознесения, Тристан-Да-Кунья',
        'Святая Елена, Остров Вознесения, Тристан-Да-Кунья',
        'SH',
        'SHN',
        654,
        '.sh',
    )
    SAINT_KITTS_AND_NEVIS = (
        'Saint Kitts and Nevis',
        'Saint Kitts and Nevis',
        'Сент-Китс и Невис',
        'Сент-Китс и Невис',
        'KN',
        'KNA',
        659,
        '.kn',
    )
    SAINT_LUCIA = (
        'Saint Lucia',
        'Saint Lucia',
        'Сент-Люсия',
        'Сент-Люсия',
        'LC',
        'LCA',
        662,
        '.lc',
    )
    SAINT_MARTIN_FRENCH_PART = (
        'Saint Martin (French part)',
        'The Collectivity of Saint-Martin',
        'Сен-Мартен (Французская Часть)',
        'Сен-Мартен (Французская Часть)',
        'MF',
        'MAF',
        663,
        '.mf',
    )
    SAINT_PIERRE_AND_MIQUELON = (
        'Saint Pierre and Miquelon',
        'The Overseas Collectivity of Saint-Pierre and Miquelon',
        'Сен-Пьер и Микелон',
        'Сен-Пьер и Микелон',
        'PM',
        'SPM',
        666,
        '.pm',
    )
    SAINT_VINCENT_AND_THE_GRENADINES = (
        'Saint Vincent and the Grenadines',
        'Saint Vincent and the Grenadines',
        'Сент-Винсент и Гренадины',
        'Сент-Винсент и Гренадины',
        'VC',
        'VCT',
        670,
        '.vc',
    )
    SAMOA = (
        'Samoa',
        'The Independent State of Samoa',
        'Самоа',
        'Независимое Государство Самоа',
        'WS',
        'WSM',
        882,
        '.ws',
    )
    SAN_MARINO = (
        'San Marino',
        'The Republic of San Marino',
        'Сан-Марино',
        'Республика Сан-Марино',
        'SM',
        'SMR',
        674,
        '.sm',
    )
    SAO_TOME_AND_PRINCIPE = (
        'Sao Tome and Principe',
        'The Democratic Republic of São Tomé and Príncipe',
        'Сан-Томе и Принсипи',
        'Демократическая Республика Сан-Томе и Принсипи',
        'ST',
        'STP',
        678,
        '.st',
    )
    SAUDI_ARABIA = (
        'Saudi Arabia',
        'The Kingdom of Saudi Arabia',
        'Саудовская Аравия',
        'Королевство Саудовская Аравия',
        'SA',
        'SAU',
        682,
        '.sa',
    )
    SENEGAL = (
        'Senegal',
        'The Republic of Senegal',
        'Сенегал',
        'Республика Сенегал',
        'SN',
        'SEN',
        686,
        '.sn',
    )
    SERBIA = (
        'Serbia',
        'The Republic of Serbia',
        'Сербия',
        'Республика Сербия',
        'RS',
        'SRB',
        688,
        '.rs',
    )
    SEYCHELLES = (
        'Seychelles',
        'The Republic of Seychelles',
        'Сейшелы',
        'Республика Сейшелы',
        'SC',
        'SYC',
        690,
        '.sc',
    )
    SIERRA_LEONE = (
        'Sierra Leone',
        'The Republic of Sierra Leone',
        'Сьерра-Леоне',
        'Республика Сьерра-Леоне',
        'SL',
        'SLE',
        694,
        '.sl',
    )
    SINGAPORE = (
        'Singapore',
        'The Republic of Singapore',
        'Сингапур',
        'Республика Сингапур',
        'SG',
        'SGP',
        702,
        '.sg',
    )
    SINT_MAARTEN_DUTCH_PART = (
        'Sint Maarten (Dutch part)',
        'Sint Maarten',
        'Сен-Мартен (Нидерландская Часть)',
        'Сен-Мартен (Нидерландская Часть)',
        'SX',
        'SXM',
        534,
        '.sx',
    )
    SLOVAKIA = (
        'Slovakia',
        'The Slovak Republic',
        'Словакия',
        'Словацкая Республика',
        'SK',
        'SVK',
        703,
        '.sk',
    )
    SLOVENIA = (
        'Slovenia',
        'The Republic of Slovenia',
        'Словения',
        'Республика Словения',
        'SI',
        'SVN',
        705,
        '.si',
    )
    SOLOMON_ISLANDS = (
        'Solomon Islands',
        'The Solomon Islands',
        'Соломоновы Острова',
        'Соломоновы Острова',
        'SB',
        'SLB',
        90,
        '.sb',
    )
    SOMALIA = (
        'Somalia',
        'The Federal Republic of Somalia',
        'Сомали',
        'Федеративная Республика Сомали',
        'SO',
        'SOM',
        706,
        '.so',
    )
    SOUTH_AFRICA = (
        'South Africa',
        'The Republic of South Africa',
        'Южная Африка',
        'Южно-Африканская Республика',
        'ZA',
        'ZAF',
        710,
        '.za',
    )
    SOUTH_GEORGIA_AND_THE_SOUTH_SANDWICH_ISLANDS = (
        'South Georgia and the South Sandwich Islands',
        'South Georgia and the South Sandwich Islands',
        'Южная Джорджия и Южные Сандвичевы Острова',
        'Южная Джорджия и Южные Сандвичевы Острова',
        'GS',
        'SGS',
        239,
        '.gs',
    )
    SOUTH_SUDAN = (
        'South Sudan',
        'The Republic of South Sudan',
        'Южный Судан',
        'Республика Южный Судан',
        'SS',
        'SSD',
        728,
        '.ss',
    )
    SPAIN = (
        'Spain',
        'The Kingdom of Spain',
        'Испания',
        'Королевство Испания',
        'ES',
        'ESP',
        724,
        '.es',
    )
    SRI_LANKA = (
        'Sri Lanka',
        'The Democratic Socialist Republic of Sri Lanka',
        'Шри-Ланка',
        'Демократическая Социалистическая Республика Шри-Ланка',
        'LK',
        'LKA',
        144,
        '.lk',
    )
    SUDAN = (
        'Sudan',
        'The Republic of the Sudan',
        'Судан',
        'Республика Судан',
        'SD',
        'SDN',
        729,
        '.sd',
    )
    SURINAME = (
        'Suriname',
        'The Republic of Suriname',
        'Суринам',
        'Республика Суринам',
        'SR',
        'SUR',
        740,
        '.sr',
    )
    SVALBARD = (
        'Svalbard',
        'Svalbard and Jan Mayen',
        'Шпицберген и Ян Майен',
        'Шпицберген и Ян Майен',
        'SJ',
        'SJM',
        744,
        '',
    )
    SWEDEN = (
        'Sweden',
        'The Kingdom of Sweden',
        'Швеция',
        'Королевство Швеция',
        'SE',
        'SWE',
        752,
        '.se',
    )
    SWITZERLAND = (
        'Switzerland',
        'The Swiss Confederation',
        'Швейцария',
        'Швейцарская Конфедерация',
        'CH',
        'CHE',
        756,
        '.ch',
    )
    SYRIAN_ARAB_REPUBLIC = (
        'Syrian Arab Republic',
        'The Syrian Arab Republic',
        'Сирийская Арабская Республика',
        'Сирийская Арабская Республика',
        'SY',
        'SYR',
        760,
        '.sy',
    )
    TAIWAN_PROVINCE_OF_CHINA = (
        'Taiwan (Province of China)',
        'The Republic of China',
        'Тайвань (Китай)',
        'Тайвань (Китай)',
        'TW',
        'TWN',
        158,
        '.tw',
    )
    TAJIKISTAN = (
        'Tajikistan',
        'The Republic of Tajikistan',
        'Таджикистан',
        'Республика Таджикистан',
        'TJ',
        'TJK',
        762,
        '.tj',
    )
    TANZANIA = (
        'Tanzania, the United Republic of',
        'The United Republic of Tanzania',
        'Танзания, Объединенная Республика',
        'Объединенная Республика Танзания',
        'TZ',
        'TZA',
        834,
        '.tz',
    )
    THAILAND = (
        'Thailand',
        'The Kingdom of Thailand',
        'Таиланд',
        'Королевство Таиланд',
        'TH',
        'THA',
        764,
        '.th',
    )
    TIMOR_LESTE = (
        'Timor-Leste',
        'The Democratic Republic of Timor-Leste',
        'Тимор-Лесте',
        'Демократическая Республика Тимор-Лесте',
        'TL',
        'TLS',
        626,
        '.tl',
    )
    TOGO = (
        'Togo',
        'The Togolese Republic',
        'Того',
        'Тоголезская Республика',
        'TG',
        'TGO',
        768,
        '.tg',
    )
    TOKELAU = ('Tokelau', 'Tokelau', 'Токелау', 'Токелау', 'TK', 'TKL', 772, '.tk')
    TONGA = (
        'Tonga',
        'The Kingdom of Tonga',
        'Тонга',
        'Королевство Тонга',
        'TO',
        'TON',
        776,
        '.to',
    )
    TRINIDAD_AND_TOBAGO = (
        'Trinidad and Tobago',
        'The Republic of Trinidad and Tobago',
        'Тринидад и Тобаго',
        'Республика Тринидад и Тобаго',
        'TT',
        'TTO',
        780,
        '.tt',
    )
    TUNISIA = (
        'Tunisia',
        'The Republic of Tunisia',
        'Тунис',
        'Тунисская Республика',
        'TN',
        'TUN',
        788,
        '.tn',
    )
    TURKIYE = (
        'Türkiye',
        'The Republic of Türkiye',
        'Турция',
        'Турецкая Республика',
        'TR',
        'TUR',
        792,
        '.tr',
    )
    TURKMENISTAN = (
        'Turkmenistan',
        'Turkmenistan',
        'Туркменистан',
        'Туркменистан',
        'TM',
        'TKM',
        795,
        '.tm',
    )
    TURKS_AND_CAICOS_ISLANDS = (
        'Turks and Caicos Islands',
        'The Turks and Caicos Islands',
        'Острова Теркс и Кайкос',
        'Острова Теркс и Кайкос',
        'TC',
        'TCA',
        796,
        '.tc',
    )
    TUVALU = ('Tuvalu', 'Tuvalu', 'Тувалу', 'Тувалу', 'TV', 'TUV', 798, '.tv')
    UGANDA = (
        'Uganda',
        'The Republic of Uganda',
        'Уганда',
        'Республика Уганда',
        'UG',
        'UGA',
        800,
        '.ug',
    )
    UKRAINE = ('Ukraine', 'Ukraine', 'Украина', 'Украина', 'UA', 'UKR', 804, '.ua')
    UNITED_ARAB_EMIRATES = (
        'United Arab Emirates',
        'The United Arab Emirates',
        'Объединенные Арабские Эмираты',
        'Объединенные Арабские Эмираты',
        'AE',
        'ARE',
        784,
        '.ae',
    )
    GREAT_BRITAIN = (
        'United Kingdom of Great Britain and Northern Ireland',
        'The United Kingdom of Great Britain and Northern Ireland',
        'Соединенное Королевство',
        'Соединенное Королевство Великобритании и Северной Ирландии',
        'GB',
        'GBR',
        826,
        '.gb.uk',
    )
    UNITED_STATES_MINOR_OUTLYING_ISLANDS = (
        'United States Minor Outlying Islands',
        'BakerIsland, HowlandIsland, JarvisIsland, JohnstonAtoll, KingmanReef, '
        'MidwayAtoll, NavassaIsland, PalmyraAtoll, and WakeIsland',
        'Малые Тихоокеанские Отдаленные Острова США',
        'Малые Тихоокеанские Отдаленные Острова Соединенных Штатов',
        'UM',
        'UMI',
        581,
        '',
    )
    USA = (
        'United States of America',
        'The United States of America',
        'США',
        'Соединенные Штаты Америки',
        'US',
        'USA',
        840,
        '.us',
    )
    URUGUAY = (
        'Uruguay',
        'The Oriental Republic of Uruguay',
        'Уругвай',
        'Восточная Республика Уругвай',
        'UY',
        'URY',
        858,
        '.uy',
    )
    UZBEKISTAN = (
        'Uzbekistan',
        'The Republic of Uzbekistan',
        'Узбекистан',
        'Республика Узбекистан',
        'UZ',
        'UZB',
        860,
        '.uz',
    )
    VANUATU = (
        'Vanuatu',
        'The Republic of Vanuatu',
        'Вануату',
        'Республика Вануату',
        'VU',
        'VUT',
        548,
        '.vu',
    )
    VENEZUELA = (
        'Venezuela (Bolivarian Republic of)',
        'The Bolivarian Republic of Venezuela',
        'Венесуэла',
        'Боливарианская Республика Венесуэла',
        'VE',
        'VEN',
        862,
        '.ve',
    )
    VIET_NAM = (
        'Viet Nam',
        'The Socialist Republic of Viet Nam',
        'Вьетнам',
        'Социалистическая Республика Вьетнам',
        'VN',
        'VNM',
        704,
        '.vn',
    )
    VIRGIN_ISLANDS_BRITISH = (
        'Virgin Islands (British)',
        'The Virgin Islands',
        'Виргинские Острова (Британские)',
        'Британские Виргинские Острова',
        'VG',
        'VGB',
        92,
        '.vg',
    )
    VIRGIN_ISLANDS_US = (
        'Virgin Islands (U.S.)',
        'The Virgin Islands of the United States',
        'Виргинские Острова (США)',
        'Виргинские Острова Соединенных Штатов',
        'VI',
        'VIR',
        850,
        '.vi',
    )
    WALLIS_AND_FUTUNA = (
        'Wallis and Futuna',
        'The Territory of the Wallis and Futuna Islands',
        'Уоллис и Футуна',
        'Уоллис и Футуна',
        'WF',
        'WLF',
        876,
        '.wf',
    )
    WESTERN_SAHARA = (
        'Western Sahara',
        'The Sahrawi Arab Democratic Republic',
        'Западная Сахара',
        'Западная Сахара',
        'EH',
        'ESH',
        732,
        '',
    )
    YEMEN = (
        'Yemen',
        'The Republic of Yemen',
        'Йемен',
        'Йеменская Республика',
        'YE',
        'YEM',
        887,
        '.ye',
    )
    ZAMBIA = (
        'Zambia',
        'The Republic of Zambia',
        'Замбия',
        'Республика Замбия',
        'ZM',
        'ZMB',
        894,
        '.zm',
    )
    ZIMBABWE = (
        'Zimbabwe',
        'The Republic of Zimbabwe',
        'Зимбабве',
        'Республика Зимбабве',
        'ZW',
        'ZWE',
        716,
        '.zw',
    )
