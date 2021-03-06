# -*- coding: utf-8 -*-
"""Unit test for case-conversion
"""

import case_conversion
from unittest import TestCase
from parameterized import parameterized

ACRONYMS = ['HTTP']
ACRONYMS_UNICODE = [u'HÉÉP']

CASES = [
    'camelcase',
    'pascalcase',
    'snakecase',
    'dashcase',
    'spinalcase',
    'kebabcase',
    'constcase',
    'screaming_snakecase',
    'dotcase',
]

CASES_PRESERVE = [
    'separate_words',
    'slashcase',
    'backslashcase',
]

VALUES = {
    'camelcase': 'fooBarString',
    'pascalcase': 'FooBarString',
    'snakecase': 'foo_bar_string',
    'dashcase': 'foo-bar-string',
    'spinalcase': 'foo-bar-string',
    'kebabcase': 'foo-bar-string',
    'constcase': 'FOO_BAR_STRING',
    'screaming_snakecase': 'FOO_BAR_STRING',
    'dotcase': 'foo.bar.string',
    'separate_words': 'foo bar string',
    'slashcase': 'foo/bar/string',
    'backslashcase': 'foo\\bar\\string',
}

VALUES_UNICODE = {
    'camelcase': u'fóoBarString',
    'pascalcase': u'FóoBarString',
    'snakecase': u'fóo_bar_string',
    'dashcase': u'fóo-bar-string',
    'spinalcase': u'fóo-bar-string',
    'kebabcase': u'fóo-bar-string',
    'constcase': u'FÓO_BAR_STRING',
    'screaming_snakecase': u'FÓO_BAR_STRING',
    'dotcase': u'fóo.bar.string',
    'separate_words': u'fóo bar string',
    'slashcase': u'fóo/bar/string',
    'backslashcase': u'fóo\\bar\\string',
}

VALUES_SINGLE = {
    'camelcase': 'foo',
    'pascalcase': 'Foo',
    'snakecase': 'foo',
    'dashcase': 'foo',
    'spinalcase': 'foo',
    'kebabcase': 'foo',
    'constcase': 'FOO',
    'screaming_snakecase': 'FOO',
    'dotcase': 'foo',
    'separate_words': 'foo',
    'slashcase': 'foo',
    'backslashcase': 'foo',
}

VALUES_SINGLE_UNICODE = {
    'camelcase': u'fóo',
    'pascalcase': u'Fóo',
    'snakecase': u'fóo',
    'dashcase': u'fóo',
    'spinalcase': u'fóo',
    'kebabcase': u'fóo',
    'constcase': u'FÓO',
    'screaming_snakecase': u'FÓO',
    'dotcase': u'fóo',
    'separate_words': u'fóo',
    'slashcase': u'fóo',
    'backslashcase': u'fóo',
}

VALUES_ACRONYM = {
    'camelcase': 'fooHTTPBarString',
    'pascalcase': 'FooHTTPBarString',
    'snakecase': 'foo_http_bar_string',
    'dashcase': 'foo-http-bar-string',
    'spinalcase': 'foo-http-bar-string',
    'kebabcase': 'foo-http-bar-string',
    'constcase': 'FOO_HTTP_BAR_STRING',
    'screaming_snakecase': 'FOO_HTTP_BAR_STRING',
    'dotcase': 'foo.http.bar.string',
    'separate_words': 'foo http bar string',
    'slashcase': 'foo/http/bar/string',
    'backslashcase': 'foo\\http\\bar\\string',
}

VALUES_ACRONYM_UNICODE = {
    'camelcase': u'fooHÉÉPBarString',
    'pascalcase': u'FooHÉÉPBarString',
    'snakecase': u'foo_héép_bar_string',
    'dashcase': u'foo-héép-bar-string',
    'spinalcase': u'foo-héép-bar-string',
    'kebabcase': u'foo-héép-bar-string',
    'constcase': u'FOO_HÉÉP_BAR_STRING',
    'screaming_snakecase': u'FOO_HÉÉP_BAR_STRING',
    'dotcase': u'foo.héép.bar.string',
    'separate_words': u'foo héép bar string',
    'slashcase': u'foo/héép/bar/string',
    'backslashcase': u'foo\\héép\\bar\\string',
}

PRESERVE_VALUES = {
    'separate_words': {'camelcase': 'foo Bar String',
                       'pascalcase': 'Foo Bar String',
                       'constcase': 'FOO BAR STRING',
                       'screaming_snakecase': 'FOO BAR STRING',
                       'default': 'foo bar string'},
    'slashcase': {'camelcase': 'foo/Bar/String',
                  'pascalcase': 'Foo/Bar/String',
                  'constcase': 'FOO/BAR/STRING',
                  'screaming_snakecase': 'FOO/BAR/STRING',
                  'default': 'foo/bar/string'},
    'backslashcase': {'camelcase': 'foo\\Bar\\String',
                      'pascalcase': 'Foo\\Bar\\String',
                      'constcase': 'FOO\\BAR\\STRING',
                      'screaming_snakecase': 'FOO\\BAR\\STRING',
                      'default': 'foo\\bar\\string'},
}

PRESERVE_VALUES_UNICODE = {
    'separate_words': {'camelcase': u'fóo Bar String',
                       'pascalcase': u'Fóo Bar String',
                       'constcase': u'FÓO BAR STRING',
                       'screaming_snakecase': u'FÓO BAR STRING',
                       'default': u'fóo bar string'},
    'slashcase': {'camelcase': u'fóo/Bar/String',
                  'pascalcase': u'Fóo/Bar/String',
                  'constcase': u'FÓO/BAR/STRING',
                  'screaming_snakecase': u'FÓO/BAR/STRING',
                  'default': u'fóo/bar/string'},
    'backslashcase': {'camelcase': u'fóo\\Bar\\String',
                      'pascalcase': u'Fóo\\Bar\\String',
                      'constcase': u'FÓO\\BAR\\STRING',
                      'screaming_snakecase': u'FÓO\\BAR\\STRING',
                      'default': u'fóo\\bar\\string'},
}

PRESERVE_VALUES_SINGLE = {
    'separate_words': {'camelcase': 'foo',
                       'pascalcase': 'Foo',
                       'constcase': 'FOO',
                       'screaming_snakecase': 'FOO',
                       'default': 'foo'},
    'slashcase': {'camelcase': 'foo',
                  'pascalcase': 'Foo',
                  'constcase': 'FOO',
                  'screaming_snakecase': 'FOO',
                  'default': 'foo'},
    'backslashcase': {'camelcase': 'foo',
                      'pascalcase': 'Foo',
                      'constcase': 'FOO',
                      'screaming_snakecase': 'FOO',
                      'default': 'foo'},
}

PRESERVE_VALUES_SINGLE_UNICODE = {
    'separate_words': {'camelcase': u'fóo',
                       'pascalcase': u'Fóo',
                       'constcase': u'FÓO',
                       'screaming_snakecase': u'FÓO',
                       'default': u'fóo'},
    'slashcase': {'camelcase': u'fóo',
                  'pascalcase': u'Fóo',
                  'constcase': u'FÓO',
                  'screaming_snakecase': u'FÓO',
                  'default': u'fóo'},
    'backslashcase': {'camelcase': u'fóo',
                      'pascalcase': u'Fóo',
                      'constcase': u'FÓO',
                      'screaming_snakecase': u'FÓO',
                      'default': u'fóo'},
}

PRESERVE_VALUES_ACRONYM = {
    'separate_words': {'camelcase': 'foo HTTP Bar String',
                       'pascalcase': 'Foo HTTP Bar String',
                       'constcase': 'FOO HTTP BAR STRING',
                       'screaming_snakecase': 'FOO HTTP BAR STRING',
                       'default': 'foo http bar string'},
    'slashcase': {'camelcase': 'foo/HTTP/Bar/String',
                  'pascalcase': 'Foo/HTTP/Bar/String',
                  'constcase': 'FOO/HTTP/BAR/STRING',
                  'screaming_snakecase': 'FOO/HTTP/BAR/STRING',
                  'default': 'foo/http/bar/string'},
    'backslashcase': {'camelcase': 'foo\\HTTP\\Bar\\String',
                      'pascalcase': 'Foo\\HTTP\\Bar\\String',
                      'constcase': 'FOO\\HTTP\\BAR\\STRING',
                      'screaming_snakecase': 'FOO\\HTTP\\BAR\\STRING',
                      'default': 'foo\\http\\bar\\string'},
}

PRESERVE_VALUES_ACRONYM_UNICODE = {
    'separate_words': {'camelcase': u'foo HÉÉP Bar String',
                       'pascalcase': u'Foo HÉÉP Bar String',
                       'constcase': u'FOO HÉÉP BAR STRING',
                       'screaming_snakecase': u'FOO HÉÉP BAR STRING',
                       'default': u'foo héép bar string'},
    'slashcase': {'camelcase': u'foo/HÉÉP/Bar/String',
                  'pascalcase': u'Foo/HÉÉP/Bar/String',
                  'constcase': u'FOO/HÉÉP/BAR/STRING',
                  'screaming_snakecase': u'FOO/HÉÉP/BAR/STRING',
                  'default': u'foo/héép/bar/string'},
    'backslashcase': {'camelcase': u'foo\\HÉÉP\\Bar\\String',
                      'pascalcase': u'Foo\\HÉÉP\\Bar\\String',
                      'constcase': u'FOO\\HÉÉP\\BAR\\STRING',
                      'screaming_snakecase': u'FOO\\HÉÉP\\BAR\\STRING',
                      'default': u'foo\\héép\\bar\\string'},
}


PRESERVE_VALUES_ACRONYM_SINGLE = {
    'separate_words': {'camelcase': 'HTTP',
                       'pascalcase': 'HTTP',
                       'constcase': 'HTTP',
                       'screaming_snakecase': 'HTTP',
                       'default': 'http'},
    'slashcase': {'camelcase': 'HTTP',
                  'pascalcase': 'HTTP',
                  'constcase': 'HTTP',
                  'screaming_snakecase': 'HTTP',
                  'default': 'http'},
    'backslashcase': {'camelcase': 'HTTP',
                      'pascalcase': 'HTTP',
                      'constcase': 'HTTP',
                      'screaming_snakecase': 'HTTP',
                      'default': 'http'},
}

CAPITAL_CASES = [
    'camelcase',
    'pascalcase',
    'constcase',
    'screaming_snakecase',
]


def _expand_values(values):
    test_params = []
    for case in CASES:
        test_params.extend([
            (name + '2' + case,
             case,
             value,
             values[case]) for name, value in values.items()
        ])
        test_params.append((case + '_empty', case, '', ''))
    return test_params


def _expand_values_preserve(preserve_values, values):
    test_params = []
    for case in CASES_PRESERVE:
        test_params.extend([
            (name + '2' + case,
             case,
             value,
             preserve_values[case][name if name in CAPITAL_CASES else 'default'])  # nopep8
            for name, value in values.items()
        ])
        test_params.append((case + '_empty', case, '', ''))
    return test_params


class CaseConversionTest(TestCase):
    @parameterized.expand(_expand_values(VALUES))
    def test(self, _, case, value, expected):
        """
        Test conversions from all cases to all cases that don't preserve
        capital/lower case letters.
        """
        case_converter = getattr(case_conversion, case)
        self.assertEqual(case_converter(value), expected)

    @parameterized.expand(_expand_values(VALUES_UNICODE))
    def test_unicode(self, _, case, value, expected):
        """
        Test conversions from all cases to all cases that don't preserve
        capital/lower case letters (with unicode characters).
        """
        case_converter = getattr(case_conversion, case)
        self.assertEqual(case_converter(value), expected)

    @parameterized.expand(_expand_values(VALUES_SINGLE))
    def test_single(self, _, case, value, expected):
        """
        Test conversions of single words from all cases to all cases that
        don't preserve capital/lower case letters.
        """
        case_converter = getattr(case_conversion, case)
        self.assertEqual(case_converter(value), expected)

    @parameterized.expand(_expand_values(VALUES_SINGLE_UNICODE))
    def test_single_unicode(self, _, case, value, expected):
        """
        Test conversions of single words from all cases to all cases that
        don't preserve capital/lower case letters (with unicode characters).
        """
        case_converter = getattr(case_conversion, case)
        self.assertEqual(case_converter(value), expected)

    @parameterized.expand(_expand_values_preserve(PRESERVE_VALUES, VALUES))
    def test_preserve_case(self, _, case, value, expected):
        """
        Test conversions from all cases to all cases that do preserve
        capital/lower case letters.
        """
        case_converter = getattr(case_conversion, case)
        self.assertEqual(case_converter(value), expected)

    @parameterized.expand(
        _expand_values_preserve(PRESERVE_VALUES_UNICODE, VALUES_UNICODE))
    def test_preserve_case_unicode(self, _, case, value, expected):
        """
        Test conversions from all cases to all cases that do preserve
        capital/lower case letters (with unicode characters).
        """
        case_converter = getattr(case_conversion, case)
        self.assertEqual(case_converter(value), expected)

    @parameterized.expand(
        _expand_values_preserve(PRESERVE_VALUES_SINGLE, VALUES_SINGLE))
    def test_preserve_case_single(self, _, case, value, expected):
        """
        Test conversions of single words from all cases to all cases that do
        preserve capital/lower case letters.
        """
        case_converter = getattr(case_conversion, case)
        self.assertEqual(case_converter(value), expected)

    @parameterized.expand(
        _expand_values_preserve(PRESERVE_VALUES_SINGLE_UNICODE,
                                VALUES_SINGLE_UNICODE))
    def test_preserve_case_single_unicode(self, _, case, value, expected):
        """
        Test conversions of single words from all cases to all cases that do
        preserve capital/lower case letters (with unicode characters).
        """
        case_converter = getattr(case_conversion, case)
        self.assertEqual(case_converter(value), expected)

    @parameterized.expand(_expand_values(VALUES_ACRONYM))
    def test_acronyms(self, _, case, value, expected):
        """
        Test conversions from all cases to all cases that don't preserve
        capital/lower case letters (with acronym detection).
        """
        case_converter = getattr(case_conversion, case)
        result = case_converter(value, acronyms=ACRONYMS)
        self.assertEqual(result, expected)

    @parameterized.expand(_expand_values(VALUES_ACRONYM_UNICODE))
    def test_acronyms_unicode(self, _, case, value, expected):
        """
        Test conversions from all cases to all cases that don't preserve
        capital/lower case letters (with acronym detection and unicode
        characters).
        """
        case_converter = getattr(case_conversion, case)
        result = case_converter(value, acronyms=ACRONYMS_UNICODE)
        self.assertEqual(result, expected)

    @parameterized.expand(
        _expand_values_preserve(PRESERVE_VALUES_ACRONYM, VALUES_ACRONYM))
    def test_acronyms_preserve_case(self, _, case, value, expected):
        """
        Test conversions from all cases to all cases that do preserve
        capital/lower case letters (with acronym detection).
        """
        case_converter = getattr(case_conversion, case)
        result = case_converter(value, acronyms=ACRONYMS)
        self.assertEqual(result, expected)

    @parameterized.expand(
        _expand_values_preserve(PRESERVE_VALUES_ACRONYM_UNICODE,
                                VALUES_ACRONYM_UNICODE))
    def test_acronyms_preserve_case_unicode(self, _, case, value, expected):
        """
        Test conversions from all cases to all cases that do preserve
        capital/lower case letters (with acronym detection and unicode
        characters).
        """
        case_converter = getattr(case_conversion, case)
        result = case_converter(value, acronyms=ACRONYMS_UNICODE)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    from unittest import main

    main()
