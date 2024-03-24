# DO NOT AUTOFORMAT THIS

"""
Country Alfa-2 codes as in ISO 3166.004-97.025-2001 (072021)
"""

__all__ = [
    # "COUNTRY_A2_TYPES",
    # "COUNTRY_A2_LIST",
    "CountryA2"
]

from typing import Literal  #, TypeAlias, get_args

from yoolib.customs import TypeTool


class CountryA2(TypeTool):
    type_alias = Literal[
    "AF", "AL", "AQ", "DZ", "AS", "AD", "AO", "AG", "AZ", "AR", "AU", "AT", "BS",
    "BH", "BD", "AM", "BB", "BE", "BM", "BT", "BO", "BA", "BW", "BV", "BR", "BZ",
    "IO", "SB", "VG", "BN", "BG", "MM", "BI", "BY", "KH", "CM", "CA", "CV", "KY",
    "CF", "LK", "TD", "CL", "CN", "TW", "CX", "CC", "CO", "KM", "YT", "CG", "CD",
    "CK", "CR", "HR", "CU", "CY", "CZ", "BJ", "DK", "DM", "DO", "EC", "SV", "GQ",
    "ET", "ER", "EE", "FO", "FK", "GS", "FJ", "FI", "АХ", "FR", "GF", "PF", "TF",
    "DJ", "GA", "GE", "GM", "PS", "DE", "GH", "GI", "KI", "GR", "GL", "GD", "GP",
    "GU", "GT", "GN", "GY", "HT", "HM", "VA", "HN", "HK", "HU", "IS", "IN", "ID",
    "IR", "IQ", "IE", "IL", "IT", "CI", "JM", "JP", "KZ", "JO", "KE", "KP", "KR",
    "KW", "KG", "LA", "LB", "LS", "LV", "LR", "LY", "LI", "LT", "LU", "MO", "MG",
    "MW", "MY", "MV", "ML", "MT", "MQ", "MR", "MU", "MX", "MC", "MN", "MD", "ME",
    "MS", "MA", "MZ", "OM", "NA", "NR", "NP", "NL", "CW", "AW", "SX", "BQ", "NC",
    "VU", "NZ", "NI", "NE", "NG", "NU", "NF", "NO", "MP", "UM", "FM", "MH", "PW",
    "PK", "PA", "PG", "PY", "PE", "PH", "PN", "PL", "PT", "GW", "TL", "PR", "QA",
    "RE", "RO", "RU", "RW", "BL", "SH", "KN", "AI", "LC", "MF", "PM", "VC", "SM",
    "ST", "SA", "SN", "RS", "SC", "SL", "SG", "SK", "VN", "SI", "SO", "ZA", "ZW",
    "ES", "EH", "SD", "SR", "SJ", "SZ", "SE", "CH", "SY", "TJ", "TH", "TG", "TK",
    "TO", "TT", "AE", "TN", "TR", "TM", "TC", "TV", "UG", "UA", "MK", "EG", "GB",
    "GG", "JE", "IM", "TZ", "US", "VI", "BF", "UY", "UZ", "VE", "WF", "WS", "YE",
    "ZM", "AB", "OS", "SS"
    ]

    def contains(self, value: str) -> bool:
        assert self.type_tuple
        return value in self.type_tuple

# COUNTRY_A2_TYPES: TypeAlias = Literal[
#     "AF", "AL", "AQ", "DZ", "AS", "AD", "AO", "AG", "AZ", "AR", "AU", "AT", "BS",
#     "BH", "BD", "AM", "BB", "BE", "BM", "BT", "BO", "BA", "BW", "BV", "BR", "BZ",
#     "IO", "SB", "VG", "BN", "BG", "MM", "BI", "BY", "KH", "CM", "CA", "CV", "KY",
#     "CF", "LK", "TD", "CL", "CN", "TW", "CX", "CC", "CO", "KM", "YT", "CG", "CD",
#     "CK", "CR", "HR", "CU", "CY", "CZ", "BJ", "DK", "DM", "DO", "EC", "SV", "GQ",
#     "ET", "ER", "EE", "FO", "FK", "GS", "FJ", "FI", "АХ", "FR", "GF", "PF", "TF",
#     "DJ", "GA", "GE", "GM", "PS", "DE", "GH", "GI", "KI", "GR", "GL", "GD", "GP",
#     "GU", "GT", "GN", "GY", "HT", "HM", "VA", "HN", "HK", "HU", "IS", "IN", "ID",
#     "IR", "IQ", "IE", "IL", "IT", "CI", "JM", "JP", "KZ", "JO", "KE", "KP", "KR",
#     "KW", "KG", "LA", "LB", "LS", "LV", "LR", "LY", "LI", "LT", "LU", "MO", "MG",
#     "MW", "MY", "MV", "ML", "MT", "MQ", "MR", "MU", "MX", "MC", "MN", "MD", "ME",
#     "MS", "MA", "MZ", "OM", "NA", "NR", "NP", "NL", "CW", "AW", "SX", "BQ", "NC",
#     "VU", "NZ", "NI", "NE", "NG", "NU", "NF", "NO", "MP", "UM", "FM", "MH", "PW",
#     "PK", "PA", "PG", "PY", "PE", "PH", "PN", "PL", "PT", "GW", "TL", "PR", "QA",
#     "RE", "RO", "RU", "RW", "BL", "SH", "KN", "AI", "LC", "MF", "PM", "VC", "SM",
#     "ST", "SA", "SN", "RS", "SC", "SL", "SG", "SK", "VN", "SI", "SO", "ZA", "ZW",
#     "ES", "EH", "SD", "SR", "SJ", "SZ", "SE", "CH", "SY", "TJ", "TH", "TG", "TK",
#     "TO", "TT", "AE", "TN", "TR", "TM", "TC", "TV", "UG", "UA", "MK", "EG", "GB",
#     "GG", "JE", "IM", "TZ", "US", "VI", "BF", "UY", "UZ", "VE", "WF", "WS", "YE",
#     "ZM", "AB", "OS", "SS"
# ]

# COUNTRY_A2_LIST = get_args(COUNTRY_A2_TYPES)
