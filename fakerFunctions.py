from faker import Faker
fake = Faker()

fake.address()
# '76930 Murray Bypass Apt. 764\nBrownland, AL 01638'

fake.building_number()
# '2110'

fake.city()
# 'South Melvintown'

fake.city_prefix()
# 'New'

fake.city_suffix()
# 'burgh'

fake.country()
# 'Macao'

fake.country_code(representation='alpha-2')
# 'LI'

fake.military_apo()
# 'PSC 5079, Box 8281'

fake.military_dpo()
# 'Unit 7218 Box 4143'

fake.military_ship()
# 'USNV'

fake.military_state()
# 'AP'

fake.postalcode()
# '93010'

fake.postalcode_in_state(state_abbr=None)
# '31508'

fake.postalcode_plus4()
# '09451-2611'

fake.postcode()
# '63621'

fake.postcode_in_state(state_abbr=None)
# '20331'

fake.secondary_address()
# 'Apt. 821'

fake.state()
# 'Tennessee'

fake.state_abbr(include_territories=True)
# 'ME'

fake.street_address()
# '0094 Bell Plains Apt. 228'

fake.street_name()
# 'Castro Spring'

fake.street_suffix()
# 'Estate'

fake.zipcode()
# '37422'

fake.zipcode_in_state(state_abbr=None)
# '84527'

fake.zipcode_plus4()
# '81677-2914'

fake.license_plate()
# '504 JTZ'

fake.bank_country()
# 'GB'

fake.bban()
# 'PSQK33805839960667'

fake.iban()
# 'GB25YUDD30055481604751'

fake.ean(length=13)
# '9886213654091'

fake.ean13(leading_zero=None)
# '3592901083420'

fake.ean8()
# '29701407'

fake.upc_a(upc_ae_mode=False, base=None, number_system_digit=None)
# '074609662310'

fake.upc_e(base=None, number_system_digit=None, safe_mode=True)
# '14240485'

fake.color(hue=None, luminosity=None, color_format='hex')
# '#3f41cc'

fake.color_name()
# 'DarkSlateBlue'

fake.hex_color()
# '#cf3784'

fake.rgb_color()
# '207,102,78'

fake.rgb_css_color()
# 'rgb(164,67,175)'

fake.safe_color_name()
# 'purple'

fake.safe_hex_color()
# '#22bb00'

fake.bs()
# 'aggregate next-generation solutions'

fake.catch_phrase()
# 'Switchable uniform conglomeration'

fake.company()
# 'Morrison, Martin and Jones'

fake.company_suffix()
# 'LLC'

fake.credit_card_expire(start='now', end='+10y', date_format='%m/%y')
# '02/28'

fake.credit_card_full(card_type=None)
# 'JCB 16 digit\nLarry Aguirre\n3531967866124946 12/25\nCVC: 834\n'

fake.credit_card_number(card_type=None)
# '4953630407768558'

fake.credit_card_provider(card_type=None)
# 'JCB 15 digit'

fake.credit_card_security_code(card_type=None)
# '814'

fake.cryptocurrency()
# ('FTH', 'Feathercoin')

fake.cryptocurrency_code()
# 'MSC'

fake.cryptocurrency_name()
# 'Lisk'

fake.currency()
# ('KYD', 'Cayman Islands dollar')

fake.currency_code()
# 'BTN'

fake.currency_name()
# 'Cayman Islands dollar'

#fake.currency_symbol()
# '$'

fake.am_pm()
# 'AM'

fake.century()
# 'XX'

fake.date(pattern='%Y-%m-%d', end_datetime=None)
# '1995-04-28'

fake.date_between(start_date='-30y', end_date='today')
# datetime.date(2006, 7, 20)

fake.date_between_dates(date_start=None, date_end=None)
# datetime.date(2020, 1, 29)

fake.date_object(end_datetime=None)
# datetime.date(2008, 9, 16)

fake.date_of_birth(tzinfo=None, minimum_age=0, maximum_age=115)
# datetime.date(1911, 4, 11)

fake.date_this_century(before_today=True, after_today=False)
# datetime.date(2009, 11, 2)

fake.date_this_decade(before_today=True, after_today=False)
# datetime.date(2020, 1, 11)

fake.date_this_month(before_today=True, after_today=False)
# datetime.date(2020, 1, 22)

fake.date_this_year(before_today=True, after_today=False)
# datetime.date(2020, 1, 21)

fake.date_time(tzinfo=None, end_datetime=None)
# datetime.datetime(1976, 6, 29, 14, 15, 29)

fake.date_time_ad(tzinfo=None, end_datetime=None, start_datetime=None)
# datetime.datetime(1329, 6, 19, 6, 37, 27)

fake.date_time_between(start_date='-30y', end_date='now', tzinfo=None)
# datetime.datetime(1994, 2, 21, 15, 43, 49)

fake.date_time_between_dates(datetime_start=None, datetime_end=None, tzinfo=None)
# datetime.datetime(2020, 1, 29, 15, 52, 47)

fake.date_time_this_century(before_now=True, after_now=False, tzinfo=None)
# datetime.datetime(2000, 7, 8, 1, 26, 8)

fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None)
# datetime.datetime(2020, 1, 4, 11, 14, 41)

fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)
# datetime.datetime(2020, 1, 22, 0, 7, 48)

fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)
# datetime.datetime(2020, 1, 1, 19, 30, 27)

fake.day_of_month()
# '19'

fake.day_of_week()
# 'Wednesday'

fake.future_date(end_date='+30d', tzinfo=None)
# datetime.date(2020, 2, 4)

fake.future_datetime(end_date='+30d', tzinfo=None)
# datetime.datetime(2020, 2, 1, 6, 23, 39)

fake.iso8601(tzinfo=None, end_datetime=None)
# '2019-02-09T01:32:11'

fake.month()
# '03'

fake.month_name()
# 'October'

fake.past_date(start_date='-30d', tzinfo=None)
# datetime.date(2020, 1, 25)

fake.past_datetime(start_date='-30d', tzinfo=None)
# datetime.datetime(2020, 1, 7, 10, 32, 17)

fake.time(pattern='%H:%M:%S', end_datetime=None)
# '17:17:18'

fake.time_delta(end_datetime=None)
# datetime.timedelta(0)

fake.time_object(end_datetime=None)
# datetime.time(1, 34, 22)

fake.time_series(start_date='-30d', end_date='now', precision=None, distrib=None, tzinfo=None)
# <generator object Provider.time_series at 0x7f9c69afd2a0>

fake.timezone()
# 'America/Guatemala'

fake.unix_time(end_datetime=None, start_datetime=None)
# 1112744199

fake.year()
# '2017'

fake.file_extension(category=None)
# 'js'

fake.file_name(category=None, extension=None)
# 'draw.avi'

fake.file_path(depth=1, category=None, extension=None)
# '/sense/visit.flac'

fake.mime_type(category=None)
# 'application/xml-dtd'

fake.unix_device(prefix=None)
# '/dev/sdt'

fake.unix_partition(prefix=None)
# '/dev/sdr9'

fake.coordinate(center=None, radius=0.001)
# Decimal('-103.656529')

fake.latitude()
# Decimal('-10.7490995')

fake.latlng()
# (Decimal('-52.518457'), Decimal('13.683455'))

fake.local_latlng(country_code='US', coords_only=False)
# ('44.27804', '-88.27205', 'Kaukauna', 'US', 'America/Chicago')

fake.location_on_land(coords_only=False)
# ('50.72043', '11.34046', 'Rudolstadt', 'DE', 'Europe/Berlin')

fake.longitude()
# Decimal('-163.031168')

fake.ascii_company_email()
# 'icook@odonnell.info'

fake.ascii_email()
# 'ambermurphy@yahoo.com'

fake.ascii_free_email()
# 'rwhitehead@hotmail.com'

fake.ascii_safe_email()
# 'mitchellsusan@example.net'

fake.company_email()
# 'xlamb@lamb.org'

fake.domain_name()
# 'pierce.com'

fake.domain_word()
# 'smith-anderson'

fake.email()
# 'larsenpaul@yahoo.com'

fake.free_email()
# 'piercekatherine@gmail.com'

fake.free_email_domain()
# 'gmail.com'

fake.hostname()
# 'web-30.osborne.com'

fake.image_url(width=None, height=None)
# 'https://dummyimage.com/850x818'

fake.ipv4(network=False, address_class=None, private=None)
# '3.20.151.164'

fake.ipv4_network_class()
# 'b'

fake.ipv4_private(network=False, address_class=None)
# '172.17.215.231'

fake.ipv4_public(network=False, address_class=None)
# '86.164.16.152'

fake.ipv6(network=False)
# '6d1:d6cf:b431:60c9:e823:9314:2c2d:180c'

fake.mac_address()
# 'c7:98:37:64:8d:d1'

fake.safe_email()
# 'kristinaporter@example.net'

fake.slug()
# 'happen-ten-mother'

fake.tld()
# 'biz'

fake.uri()
# 'http://winters.com/index.htm'

fake.uri_extension()
# '.asp'

fake.uri_page()
# 'faq'

fake.uri_path(deep=None)
# 'posts'

fake.url(schemes=None)
# 'https://woodard.biz/'

fake.user_name()
# 'colealexander'

fake.isbn10(separator='-')
# '0-595-77935-2'

fake.isbn13(separator='-')
# '978-1-246-27007-5'

fake.job()
# 'Museum/gallery curator'

fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
# 'Until one chair available drive. Color a buy represent lead sure sign.'

fake.paragraphs(nb=3, ext_word_list=None)
# [   'Property agree ground art. Various such follow information painting. '
#     'Decision Congress everybody television.',
#     'Rich star than poor mention eight. Quite number program his how watch.',
#     'When human stay medical conference find consumer play. White institution '
#     'attorney defense stay professor majority.']

fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
# 'Page beyond success continue camera six.'

fake.sentences(nb=3, ext_word_list=None)
# [   'Local west official be size.',
#     'Voice economic mission approach force.',
#     'Bad international behavior dream yourself.']

fake.text(max_nb_chars=200, ext_word_list=None)
# ('Explain wear represent expect successful free although. Charge quickly '
#  'standard trouble. Around population simply list then executive go.')

fake.texts(nb_texts=3, max_nb_chars=200, ext_word_list=None)
# [   'Ready concern pattern rate. New star who order threat develop could born. '
#     'Ahead city age.',
#     'Ever free color future. Population major price.\n'
#     'Able whole movement night. Education have floor land agency small. '
#     'Authority in financial decision probably anything.',
#     'Red form sometimes guy use. Candidate two chair trouble amount sort '
#     'seven.\n'
#     'Arm win against example mission. Reason stuff among range. Window step '
#     'share imagine future practice four common.']

fake.word(ext_word_list=None)
# 'tonight'

fake.words(nb=3, ext_word_list=None, unique=False)
# ['perhaps', 'attention', 'each']

fake.binary(length=1048576)

fake.boolean(chance_of_getting_true=50)
# True

fake.csv(header=None, data_columns=('{{name}}', '{{address}}'), num_rows=10, include_row_ids=False)
# ('"Amanda Miranda","2582 West Fields Apt. 216\n'
#  'South Tanyaberg, NM 09568"\r\n')

fake.dsv(dialect='faker-csv', header=None, data_columns=('{{name}}', '{{address}}'), num_rows=10, include_row_ids=False)
# ('"Christopher Maynard","8581 Joseph Station Apt. 254\n'
#  'Portershire, OH 73939"\r\n')

fake.md5(raw_output=False)
# 'b55c742294e9c41f9822aba6145b8001'

fake.null_boolean()
# True

fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
# 'evSF6Qpq#N'

fake.psv(header=None, data_columns=('{{name}}', '{{address}}'), num_rows=10, include_row_ids=False)
# ('"Lori Matthews"|"9661 Ryan Bypass Apt. 156\n'
#  'New Suzanneberg, OH 41489"\r\n')

fake.sha1(raw_output=False)
# '5b9b06e30a84dbf6a7516dc5fb399eaaeade6397'

fake.sha256(raw_output=False)
# '79af8ba5c3aa01c0f99e483a1c2ed0a2d1333422e4abba7ac88becd52d45b0eb'

fake.tar(uncompressed_size=65536, num_files=1, min_file_size=4096, compression=None)
# (b'gTuFDGUGCKoQgWHCBGoB1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
#  b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

fake.tsv(header=None, data_columns=('{{name}}', '{{address}}'), num_rows=10, include_row_ids=False)
# ('"Jenny Brooks"\t"342 Howard Isle\n'
#  'Frostborough, NJ 06167"\r\n')

fake.uuid4()
# 'f2c2eb43-7402-4857-a10e-52dc8231dc0c'

fake.zip(uncompressed_size=65536, num_files=1, min_file_size=4096, compression=None)
# (b'PK\x03\x04\x14\x00\x00\x00\x00\x00\x98~=P~M\x95\xdd\x00\x04\x00\x00\x00\x04'
#  b'\x00\x00\x01\x00\x01\x00C\x00\x00\x003\x04\x00\x00\x00\x00')

fake.first_name()
# 'David'

fake.first_name_female()
# 'Dawn'

fake.first_name_male()
# 'Adam'

fake.last_name()
# 'Santos'

fake.last_name_female()
# 'Barnes'

fake.last_name_male()
# 'Brown'

fake.name()
# 'Christine Fuentes'

fake.name_female()
# 'Erin Friedman'

fake.name_male()
# 'Nicholas Wong'

fake.prefix()
# 'Mr.'

fake.prefix_female()
# 'Mrs.'

fake.prefix_male()
# 'Dr.'

fake.suffix()
# 'Jr.'

fake.suffix_female()
# 'MD'

fake.suffix_male()
# 'DVM'

fake.msisdn()
# '6156139955822'

fake.phone_number()
# '331-486-7899'

fake.profile(fields=None, sex=None)
# {   'address': '2084 Tom Stravenue Apt. 952\nLake Kaitlyn, NJ 34201',
#     'birthdate': datetime.date(1929, 2, 26),
#     'blood_group': 'O-',
#     'company': 'Dunn-Garrison',
#     'current_location': (Decimal('37.508178'), Decimal('-7.724199')),
#     'job': 'Sports development officer',
#     'mail': 'kristen35@gmail.com',
#     'name': 'Jodi Diaz',
#     'residence': '446 Morales Grove\nSouth Brandon, DC 33012',
#     'sex': 'F',
#     'ssn': '054-05-3711',
#     'username': 'matthew41',
#     'website': ['http://www.mcmahon-cooper.info/']}

fake.simple_profile(sex=None)
# {   'address': '769 James Ports\nSnyderberg, AZ 01472',
#     'birthdate': datetime.date(1948, 1, 7),
#     'mail': 'christopherpotter@hotmail.com',
#     'name': 'Stacy Gutierrez',
#     'sex': 'F',
#     'username': 'iperez'}

fake.pybool()
# True

fake.pydecimal(left_digits=None, right_digits=None, positive=False, min_value=None, max_value=None)
# Decimal('435.906123178')

fake.pydict(nb_elements=10, variable_nb_elements=True)
# {   'alone': 'pgarrett@khan-massey.com',
#     'enjoy': 'https://www.perry.info/author.html',
#     'house': 'ucxyXziGvPFovlgHzqYd',
#     'open': datetime.datetime(1995, 5, 13, 22, 23, 8),
#     'start': 'esmith@butler.com',
#     'support': Decimal('5.35308')}

fake.pyfloat(left_digits=None, right_digits=None, positive=False, min_value=None, max_value=None)
# 7132794.32308

fake.pyint(min_value=0, max_value=9999, step=1)
# 1395

fake.pyiterable(nb_elements=10, variable_nb_elements=True)
# {datetime.datetime(2010, 5, 26, 23, 39, 52), 'dtJBDEppINynSzrQyUVq', 'bxMSncTboCbADtzEOWSL', 'qIGeHOpuSyIWruoJImGt', 4305, Decimal('-529.909858'), -7660.3011, 2294, 'IcflQnsmJqdsvyqMtAQL', 'https://www.reed.com/terms.htm', 'VgxvHEBcSEtWmeBNTIYi', 'IdiIGWZHidNFZewCygjD'}

fake.pylist(nb_elements=10, variable_nb_elements=True)
# [   49,
#     'ERhTsVcjMrRVJWtQMppK',
#     datetime.datetime(1986, 11, 8, 15, 52, 44),
#     27653245640.14,
#     'RqnzwQlPghCtXBfZkApT',
#     'jGqaWUykJejMFmsYQtiv',
#     Decimal('-600968029491762.0'),
#     -49290.8461]

fake.pyset(nb_elements=10, variable_nb_elements=True)
# {'hijqjeWSbVMFgCZVMSey', 'TQytUxQkxdzftjWldooc', Decimal('60160737782622.4'), datetime.datetime(1982, 4, 22, 14, 57, 25), 'IboCVjtlRzmWiWDMoapN', 8792, 'emilyweber@mccoy.com'}

fake.pystr(min_chars=None, max_chars=20)
# 'zKyHOdVXYsouMnaCaYMG'

fake.pystr_format(string_format='?#-###{{random_int}}{{random_letter}}', letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
# 'S1-0342811q'

fake.pystruct(count=10)
# (   [   'hpReNStWoJwCcUMlqbqK',
# ...
#                                     datetime.datetime(1975, 12, 6, 5, 41, 33)]}}})

fake.pytuple(nb_elements=10, variable_nb_elements=True)
# (   'AyhgbCDKnVfQfaejfDFg',
#     2373,
#     'QDgoJaFrxqlyczLjVZTh',
#     'bstrong@hotmail.com',
#     'jyCNjwPvBjlkjlIoSJls',
#     503,
#     'http://acosta-smith.com/blog/privacy/',
#     1627,
#     -87642395043.0)

fake.ein()
# '90-2312290'

fake.invalid_ssn()
# '873-00-9685'

fake.itin()
# '953-99-6330'

fake.ssn(taxpayer_identification_number_type='SSN')
# '631-43-9018'

fake.android_platform_token()
# 'Android 8.0.0'

fake.chrome(version_from=13, version_to=63, build_from=800, build_to=899)
# ('Mozilla/5.0 (iPad; CPU iPad OS 10_3_4 like Mac OS X) AppleWebKit/532.0 '
#  '(KHTML, like Gecko) CriOS/46.0.804.0 Mobile/39D864 Safari/532.0')

fake.firefox()
# ('Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/531.0 '
#  '(KHTML, like Gecko) FxiOS/9.1w2715.0 Mobile/57E877 Safari/531.0')

fake.internet_explorer()
# 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.0; Trident/5.0)'

fake.ios_platform_token()
# 'iPhone; CPU iPhone OS 7_1_2 like Mac OS X'

fake.linux_platform_token()
# 'X11; Linux x86_64'

fake.linux_processor()
# 'i686'

fake.mac_platform_token()
# 'Macintosh; PPC Mac OS X 10_6_3'

fake.mac_processor()
# 'U; PPC'

fake.opera()
# 'Opera/8.82.(X11; Linux x86_64; gez-ER) Presto/2.9.181 Version/10.00'

fake.safari()
# ('Mozilla/5.0 (Windows; U; Windows 98) AppleWebKit/532.23.3 (KHTML, like '
#  'Gecko) Version/5.0.1 Safari/532.23.3')

fake.user_agent()
# 'Opera/8.68.(X11; Linux x86_64; ug-CN) Presto/2.9.188 Version/10.00'

fake.windows_platform_token()
# 'Windows CE'
