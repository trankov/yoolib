# The Package

A base difference of `isoworld` from another similar packages is focus on typing and validation puproses. It includes Enums, tuples and dictionaries, containing ISO-based info about countries and currencies.

# Countries

## Predefined dicts and tuples

A `countries` module implements ISO 3166 standard. The predefined declarations are:

- `countydict.COUNTRIES`: a list of dictionaries
- `countrytuples.COUNTRYTUPLES`: a tuples where the values only
- `countrytuples.COUNTRYKEYS`: a tuple of keys, `zip`-compatible with these values tuples

Use `.get(**kwargs)` and `.find(*args)` for seek in countries. They returns first found dictionary matched with parameters passed. A first one looks matches by keys/values, and a second only by values. If nothing was found,  you'll get`None`.

*For authors's needs countries also include a Russian forms. Maybe it also will be useful for somebody else.*

```python
from isoworld import countries


countries.get(short_en='American Samoa')
countries.find('American Samoa')
```

Result:

```python
{
	'short_en': 'American Samoa',
	'long_en': 'The Territory of American Samoa',
	'short_ru': 'Американское Самоа',
	'long_ru': 'Американское Самоа',
	'a2': 'AS',
	'a3': 'ASM',
	'num': 16,
	'tld': '.as',
}
```

## Pydantic 2 support

```python
countries.CountryModel.find('USA')
```

Result:

```python
CountryModel(short_en='United States of America', long_en='The United States of America', short_ru='США', long_ru='Соединенные Штаты Америки', a2=<CountriesA2.USA: 'US'>, a3=<CountriesA3.USA: 'USA'>, num=<CountriesNum.USA: 840>, tld='.us')
```

Also there is `countries.CountryModel.get()` similar to `countries.get()`
## Ready to use Enums

```python
countries.CountriesA2 # 2-letter codes
countries.CountriesA3 # 3-letter codes
countries.CountriesNum # Numeric codes
countries.Countries # full-info dataclasses
```

Examples:

```python
countries.Countries.ROMANIA.tld      # '.ro'
countries.CountriesA2.BELIZE         # <CountriesA2.BELIZE: 'BZ'>
countries.CountriesA3.LIECHTENSTEIN  # <CountriesA3.LIECHTENSTEIN: 'LIE'>
countries.CountriesNum.PUERTO_RICO   # <CountriesNum.PUERTO_RICO: 630>
```


# Currencies

## Predefined dicts and tuples

A `currencies` module implements ISO 4217 standard. The predefined declarations are:

- `currencydict.CURRENCIES`: a list of dictionaries
- `currencytuples.CURRENCYTUPLES`: a tuples where the values only
- `currencytuples.CURRENCYKEYS`: a tuple of keys, `zip`-compatible with these values tuples

You also use `.get(**kwargs)` and `.find(**kwargs)` for seek in currencies, but their work is a bit different. Both of them looks matches by keys/values, so a first one returns first match found, **but** a second one returns list of all matches found. If nothing was found,  you'll still get`None`.

```python
from isoworld import currencies

currencies.get(code='USD')
```

It returns:

```python
{'entity': 'American Samoa', 'currency': 'US Dollar', 'code': 'USD', 'num': 840, 'minors': 2, 'fund': False}
```

But:

```python
currencies.find(code='USD')
```

Returns:

```python
[
	{
		'entity': 'American Samoa',
		'currency': 'US Dollar',
		'code': 'USD',
		'num': 840,
		'minors': 2,
		'fund': False,
	},
	{
		'entity': 'Bonaire, Sint Eustatius And Saba',
		'currency': 'US Dollar',
		'code': 'USD',
		'num': 840,
		'minors': 2,
		'fund': False,
	},
	{
		'entity': 'British Indian Ocean Territory (The)',
		'currency': 'US Dollar',
		'code': 'USD',
		'num': 840,
		'minors': 2,
		'fund': False,
	},
	{
		'entity': 'Ecuador',
		'currency': 'US Dollar',
		'code': 'USD',
		'num': 840,
		'minors': 2,
		'fund': False,
	},
	{
		'entity': 'El Salvador',
		'currency': 'US Dollar',
		'code': 'USD',
		'num': 840,
		'minors': 2,
		'fund': False,
	},
	{
		'entity': 'Guam',
		'currency': 'US Dollar',
		'code': 'USD',
		'num': 840,
		'minors': 2,
		'fund': False,
	},
	{
		'entity': 'Haiti',
		'currency': 'US Dollar',
		'code': 'USD',
		'num': 840,
		'minors': 2,
		'fund': False,
	},
	{
		'entity': 'Marshall Islands (The)',
		'currency': 'US Dollar',
		'code': 'USD',
		'num': 840,
		'minors': 2,
		'fund': False,
	},
	{
		'entity': 'Micronesia (Federated States Of)',
		'currency': 'US Dollar',
		'code': 'USD',
		'num': 840,
		'minors': 2,
		'fund': False,
	},
	{
		'entity': 'Northern Mariana Islands (The)',
		'currency': 'US Dollar',
		'code': 'USD',
		'num': 840,
		'minors': 2,
		'fund': False,
	},
	{
		'entity': 'Palau',
		'currency': 'US Dollar',
		'code': 'USD',
		'num': 840,
		'minors': 2,
		'fund': False,
	},
	{
		'entity': 'Panama',
		'currency': 'US Dollar',
		'code': 'USD',
		'num': 840,
		'minors': 2,
		'fund': False,
	},
	{
		'entity': 'Puerto Rico',
		'currency': 'US Dollar',
		'code': 'USD',
		'num': 840,
		'minors': 2,
		'fund': False,
	},
	{
		'entity': 'Timor-leste',
		'currency': 'US Dollar',
		'code': 'USD',
		'num': 840,
		'minors': 2,
		'fund': False,
	},
	{
		'entity': 'Turks And Caicos Islands (The)',
		'currency': 'US Dollar',
		'code': 'USD',
		'num': 840,
		'minors': 2,
		'fund': False,
	},
	{
		'entity': 'United States Minor Outlying Islands (The)',
		'currency': 'US Dollar',
		'code': 'USD',
		'num': 840,
		'minors': 2,
		'fund': False,
	},
	{
		'entity': 'United States Of America (The)',
		'currency': 'US Dollar',
		'code': 'USD',
		'num': 840,
		'minors': 2,
		'fund': False,
	},
	{
		'entity': 'Virgin Islands (British)',
		'currency': 'US Dollar',
		'code': 'USD',
		'num': 840,
		'minors': 2,
		'fund': False,
	},
	{
		'entity': 'Virgin Islands (U.s.)',
		'currency': 'US Dollar',
		'code': 'USD',
		'num': 840,
		'minors': 2,
		'fund': False,
	},
]
```

## Pydantic 2 support:

```python
currencies.CurrencyModel.find(code='GBP')
```

Result:

```python
[
	 CurrencyModel(
		 entity='Guernsey',
		 currency='Pound Sterling',
		 code=<CurrencyCode.GBP: 'GBP'>,
		 num=<CurrencyNum.GBP: 826>,
		 minors=2
	),
	 CurrencyModel(
		 entity='Isle Of Man',
		 currency='Pound Sterling',
		 code=<CurrencyCode.GBP: 'GBP'>,
		 num=<CurrencyNum.GBP: 826>,
		 minors=2
	),
	 CurrencyModel(
		 entity='Jersey',
		 currency='Pound Sterling',
		 code=<CurrencyCode.GBP: 'GBP'>,
		 num=<CurrencyNum.GBP: 826>,
		 minors=2
	),
	 CurrencyModel(
		 entity='United Kingdom Of Great Britain And Northern Ireland (The)',
		 currency='Pound Sterling',
		 code=<CurrencyCode.GBP: 'GBP'>,
		 num=<CurrencyNum.GBP: 826>,
		 minors=2
	)
]
```

Also `currencies.CurrencyModel.get()` is awailable.

## Ready to use Enums

```python
currencies.CurrencyCode      # 3-letters code
currencies.CurrencyNum       # Numeric code
currencies.CurrencyEntity    # 3-letters code
currencies.CurrencyName      # 3-letters code
currencies.CurrencyCodeNum   # (alphabetic_code: str, numeric_code: int)
```

Examples:

```python
currencies.CurrencyCode.LSL
# <CurrencyCode.LSL: 'LSL'>

currencies.CurrencyNum.RON
# <CurrencyNum.RON: 946>

currencies.CurrencyEntity.TRINIDAD_AND_TOBAGO
# <CurrencyEntity.TRINIDAD_AND_TOBAGO: 'TTD'>

currencies.CurrencyName.INDIAN_RUPEE
# <CurrencyName.INDIAN_RUPEE: 'INR'>

currencies.CurrencyCodeNum.SHP
# <CurrencyCodeNum.SHP: alphabetic_code='SHP', numeric_code=654>

currencies.CurrencyCodeNum.RUB.numeric_code
# 643

currencies.CurrencyCodeNum.RUB.alphabetic_code
# 'RUB'
```
