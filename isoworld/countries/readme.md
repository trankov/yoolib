# Countries section

These classes and utilities have been designed to work with country data in accordance with ISO 3166.

The **Repository** allows users to search for countries based on the value of specific attributes and provides information about the countries that match the search criteria.

**Enums** allow you to access country data using predefined constants.

## Repository

The repository contains unified country data. You can retrieve the country you need based on the value of one of its attributes.

The country data is stored in a literal dictionary format, as it is one of the most fundamental and optimized data structures in Python.

## Enums

Enums are useful for typehinting, validation and IDE auto suggestions. Each Enum here contains the same set of names for constants (see below).

Despite the fact that Enum is a compact and efficient data format, it still requires more resources than a dictionary. Therefore, it is not advisable to import more classes into your project than necessary.

Here is a four types of Enum:

### CountriesNum

A numeric codes of countries as `int` values. Inherits `IntEnum` type.

```python
from isoworld.countries.enums import CountriesNum


>>> CountriesNum.THAILAND
>>> 764
```

### CountriesA2

A two-letter country codes according to ISO 3166 alpha-2. Inherits `StrEnum` type.

```python
from isoworld.countries.enums import CountriesA2


>>> CountriesA2.MADAGASCAR
>>> 'MG'
```

### CountriesA3

A three-letter country codes according to ISO 3166 alpha-3. Inherits `StrEnum` type.

```python
from isoworld.countries.enums import CountriesA3


>>> CountriesA3.GUINEA_BISSAU
>>> 'GNB'
```

### Countries

Each country constant in this Enum is a dataclass. The fields are the same as for Repository.

```python
from isoworld.countries.enums import Countries


>>> Countries.EGYPT.long_en
>>> 'The Arab Republic of Egypt'

>>> Countries.ITALY.short_ru
>>> 'Италия'

>>> Countries.MEXICO.tld
>>> '.mx'

>>> Countries.RUSSIA
>>> <Countries.RUSSIA: short_en='Russian Federation', long_en='The Russian Federation', short_ru='Россия', long_ru='Российская Федерация', a2='RU', a3='RUS', num=643, tld='.ru'>
```

### Constants names for Enums

`AFGHANISTAN`, `ALAND_ISLANDS`, `ALBANIA`, `ALGERIA`, `AMERICAN_SAMOA`, `ANDORRA`, `ANGOLA`, `ANGUILLA`, `ANTARCTICA`, `ANTIGUA_AND_BARBUDA`, `ARGENTINA`, `ARMENIA`, `ARUBA`, `AUSTRALIA`, `AUSTRIA`, `AZERBAIJAN`, `BAHAMAS`, `BAHRAIN`, `BANGLADESH`, `BARBADOS`, `BELARUS`, `BELGIUM`, `BELIZE`, `BENIN`, `BERMUDA`, `BHUTAN`, `BOLIVIA`, `BONAIRE`, `BOSNIA_AND_HERZEGOVINA`, `BOTSWANA`, `BOUVET_ISLAND`, `BRAZIL`, `BRITISH_INDIAN_OCEAN_TERRITORY`, `BRUNEI_DARUSSALAM`, `BULGARIA`, `BURKINA_FASO`, `BURUNDI`, `CABO_VERDE`, `CAMBODIA`, `CAMEROON`, `CANADA`, `CAYMAN_ISLANDS`, `CENTRAL_AFRICAN_REPUBLIC`, `CHAD`, `CHILE`, `CHINA`, `CHRISTMAS_ISLAND`, `COCOS_KEELING_ISLANDS`, `COLOMBIA`, `COMOROS`, `CONGO_DEMOCRATIC_REPUBLIC`, `CONGO`, `COOK_ISLANDS`, `COSTA_RICA`, `COTE_DIVOIRE`, `CROATIA`, `CUBA`, `CURACAO`, `CYPRUS`, `CZECHIA`, `DENMARK`, `DJIBOUTI`, `DOMINICA`, `DOMINICAN_REPUBLIC`, `ECUADOR`, `EGYPT`, `EL_SALVADOR`, `EQUATORIAL_GUINEA`, `ERITREA`, `ESTONIA`, `ESWATINI`, `ETHIOPIA`, `FALKLAND_ISLANDS`, `FAROE_ISLANDS`, `FIJI`, `FINLAND`, `FRANCE`, `FRENCH_GUIANA`, `FRENCH_POLYNESIA`, `FRENCH_SOUTHERN_TERRITORIES`, `GABON`, `GAMBIA`, `GEORGIA`, `GERMANY`, `GHANA`, `GIBRALTAR`, `GREECE`, `GREENLAND`, `GRENADA`, `GUADELOUPE`, `GUAM`, `GUATEMALA`, `GUERNSEY`, `GUINEA`, `GUINEA_BISSAU`, `GUYANA`, `HAITI`, `HEARD_ISLAND_AND_MCDONALD_ISLANDS`, `HOLY_SEE`, `HONDURAS`, `HONG_KONG`, `HUNGARY`, `ICELAND`, `INDIA`, `INDONESIA`, `IRAN`, `IRAQ`, `IRELAND`, `ISLE_OF_MAN`, `ISRAEL`, `ITALY`, `JAMAICA`, `JAPAN`, `JERSEY`, `JORDAN`, `KAZAKHSTAN`, `KENYA`, `KIRIBATI`, `KOREA_DEMOCRATIC_PEOPLES_REPUBLIC`, `KOREA_REPUBLIC`, `KUWAIT`, `KYRGYZSTAN`, `LAO_PEOPLES_DEMOCRATIC_REPUBLIC`, `LATVIA`, `LEBANON`, `LESOTHO`, `LIBERIA`, `LIBYA`, `LIECHTENSTEIN`, `LITHUANIA`, `LUXEMBOURG`, `MACAO`, `MADAGASCAR`, `MALAWI`, `MALAYSIA`, `MALDIVES`, `MALI`, `MALTA`, `MARSHALL_ISLANDS`, `MARTINIQUE`, `MAURITANIA`, `MAURITIUS`, `MAYOTTE`, `MEXICO`, `MICRONESIA`, `MOLDOVA`, `MONACO`, `MONGOLIA`, `MONTENEGRO`, `MONTSERRAT`, `MOROCCO`, `MOZAMBIQUE`, `MYANMAR`, `NAMIBIA`, `NAURU`, `NEPAL`, `NETHERLANDS`, `NEW_CALEDONIA`, `NEW_ZEALAND`, `NICARAGUA`, `NIGER`, `NIGERIA`, `NIUE`, `NORFOLK_ISLAND`, `NORTH_MACEDONIA`, `NORTHERN_MARIANA_ISLANDS`, `NORWAY`, `OMAN`, `PAKISTAN`, `PALAU`, `PALESTINE`, `PANAMA`, `PAPUA_NEW_GUINEA`, `PARAGUAY`, `PERU`, `PHILIPPINES`, `PITCAIRN`, `POLAND`, `PORTUGAL`, `PUERTO_RICO`, `QATAR`, `REUNION`, `ROMANIA`, `RUSSIA`, `RWANDA`, `SAINT_BARTHELEMY`, `SAINT_HELENA`, `SAINT_KITTS_AND_NEVIS`, `SAINT_LUCIA`, `SAINT_MARTIN_FRENCH_PART`, `SAINT_PIERRE_AND_MIQUELON`, `SAINT_VINCENT_AND_THE_GRENADINES`, `SAMOA`, `SAN_MARINO`, `SAO_TOME_AND_PRINCIPE`, `SAUDI_ARABIA`, `SENEGAL`, `SERBIA`, `SEYCHELLES`, `SIERRA_LEONE`, `SINGAPORE`, `SINT_MAARTEN_DUTCH_PART`, `SLOVAKIA`, `SLOVENIA`, `SOLOMON_ISLANDS`, `SOMALIA`, `SOUTH_AFRICA`, `SOUTH_GEORGIA_AND_THE_SOUTH_SANDWICH_ISLANDS`, `SOUTH_SUDAN`, `SPAIN`, `SRI_LANKA`, `SUDAN`, `SURINAME`, `SVALBARD`, `SWEDEN`, `SWITZERLAND`, `SYRIAN_ARAB_REPUBLIC`, `TAIWAN_PROVINCE_OF_CHINA`, `TAJIKISTAN`, `TANZANIA`, `THAILAND`, `TIMOR_LESTE`, `TOGO`, `TOKELAU`, `TONGA`, `TRINIDAD_AND_TOBAGO`, `TUNISIA`, `TURKIYE`, `TURKMENISTAN`, `TURKS_AND_CAICOS_ISLANDS`, `TUVALU`, `UGANDA`, `UKRAINE`, `UNITED_ARAB_EMIRATES`, `GREAT_BRITAIN`, `UNITED_STATES_MINOR_OUTLYING_ISLANDS`, `USA`, `URUGUAY`, `UZBEKISTAN`, `VANUATU`, `VENEZUELA`, `VIET_NAM`, `VIRGIN_ISLANDS_BRITISH`, `VIRGIN_ISLANDS_US`, `WALLIS_AND_FUTUNA`, `WESTERN_SAHARA`, `YEMEN`, `ZAMBIA`, `ZIMBABWE`
