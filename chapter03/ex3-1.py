# tt = (1, 2, (30, 40))
# hash(tt)
#
# tt = (1, 2, frozenset([30, 40]))
# h = hash(tt)
# print(h)


DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
    ]

country_code = {country: code for code, country in DIAL_CODES}
print(country_code)

code_dict = {code: country for country, code in country_code.items() if code < 66}
print(code_dict)
