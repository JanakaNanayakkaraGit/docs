# Restricting Text Responses With Regular Expressions

**Last updated:**
<a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/restrict_responses.md" class="reference">15
Feb 2022</a>

A regular expression, or regex, is a search pattern used for matching specific
characters and ranges of characters within a string. It is widely used to
validate, search, extract, and restrict text in most programming languages.
KoboToolbox supports regex to control the length and characters during data
entry to a particular question _(e.g. controlling the entry of mobile number to
exactly 10 digits, controlling the entry of a valid email id etc.)_.

## To use a regex in KoboToolbox, follow these steps

1. Prepare a _Text_ question type.

2. Go to the question's _Settings_.

3. Go to _Validation Criteria_ and choose the _Manually enter your validation
   logic in XLSForm_ code option.

4. In the _Validation Code_ box, enter your regex formula between the quotation
   marks `(' ')` of the `regex(., ' ')` format. For reference, the period (`.`)
   refers to _'this question'_, while the regular expression inside the
   quotation marks (`' '`) needs to conform to the established regex rules.

5. (Optional) Add a custom _Error Message_ for the person entering data to see
   when they don't meet the regex criteria.

![image](/images/restrict_responses/regrex.jpg)

Regex can also be coded in XLSForm, under the _constraint_ column:

| type | name | label                       | appearance | constraint              | constraint_message                |
| :--- | :--- | :-------------------------- | :--------- | :---------------------- | :-------------------------------- |
| text | q1   | Mobile number of respondent | numbers    | regex(., '^[0-9]{10}$') | This value must be only 10 digits |

Alternatively, you can create a `calculate` question type and then define the
regex code under the _calculation_ column. You could then use this variable as
many times as needed in the survey:

| type      | name | label                  | calculation                              | constraint      | constraint_message                  |
| :-------- | :--- | :--------------------- | :--------------------------------------- | :-------------- | :---------------------------------- |
| calculate | q0   |                        | '^[A-Z]{1}[a-z]{1,}\s[A-Z]{1}[a-z]{1,}$' |                 |                                     |
| text      | q1   | Name of the Enumerator |                                          | regex(., ${q0}) | Please use this format: Kobe Bryant |
| text      | q2   | Name of the Respondent |                                          | regex(., ${q0}) | Please use this format: Kobe Bryant |
| integer   | q3   | Age of the Respondent  |                                          |                 |                                     |

## How do I build the regex that I need?

In addition to the examples and tips provided below, please visit
[this website](http://www.regexr.com) for more help and examples.

<p class="note">Regex in KoboToolbox should always be written in-between the apostrophes <code>regex(., ' ')</code> as shown in the examples.</p>

| Regex               | Description                                                                                                                                                                                 |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `^`                 | The caret symbol matches the start of a string without consuming any character.                                                                                                             |
| `$`                 | The dollar symbol matches the end of a string without consuming any character.                                                                                                              |
| `[abc]`             | Matches either `a`, `b` or `c` from within the square brackets `[ ]`.                                                                                                                       |
| `[a-z]`             | Matches any lowercase character from `a` to `z`.                                                                                                                                            |
| `[A-Z]`             | Matches any uppercase character from `A` to `Z`.                                                                                                                                            |
| `[0-9]`             | Matches any whole numbers from `0` to `9`.                                                                                                                                                  |
| `[a-zA-Z0-9]`       | Matches any character from `a` to `z` or `A` to `Z` or `0` to `9`.                                                                                                                          |
| `[^abc]`            | Matches any character _except_ `a`, `b` or `c`.                                                                                                                                             |
| `[^A-Z]`            | Matches any characters _except_ those in the range `A` to `Z`.                                                                                                                              |
| `(apple)`           | The grouping character `( )` matches anything that is within the parenthesis.                                                                                                               |
| <code>&#x7c;</code> | A vertical bar matches any element separated.                                                                                                                                               |
| `\`                 | A back slash is used to match the literal value of any metacharacter (e.g. try using `\.` or `\@` or `\$` while building regex).                                                            |
| `\number`           | Matches the same character as most recently matched by the n<sup>th</sup> (number used) capturing group.                                                                                    |
| `\s`                | Matches any _space_ or _tab_.                                                                                                                                                               |
| `\b`                | Matches, without consuming any characters immediately between a character matched by `\w` and a character not matched by `\w` (in either order). `\b` is also known as the _word boundary_. |
| `\d`                | Matches any equivalent numbers `[0-9]`                                                                                                                                                      |
| `\D`                | Matches anything other than numbers `(0 to 9)`.                                                                                                                                             |
| `\w`                | Matches any word character (i.e. `a` to `z` or `A` to `Z` or `0` to `9` or `_`).                                                                                                            |
| `\W`                | Matches anything other than what `\w` matches (i.e. it matches wild cards and spaces).                                                                                                      |
| `?`                 | A question mark used just behind a character matches or skips (if not required) a character match.                                                                                          |
| `*`                 | An asterisk symbol used just behind a character matches zero or more consecutive character.                                                                                                 |
| `+`                 | The plus symbol used just behind a character matches one or more consecutive character.                                                                                                     |
| `{x}`               | Matches exactly `x` consecutive characters.                                                                                                                                                 |
| `{x,}`              | Matches at least `x` consecutive characters (or more).                                                                                                                                      |
| `{x,y}`             | Matches between `x` and `y` consecutive characters.                                                                                                                                         |

## Examples related to use of numbers

<p class="note">For all <code>text</code> type questions that use numbers, do not forget to type <code>numbers</code> under the <code>appearance</code> column.</p>

| XLSForm Regex                                                                     | Description                                                                                                        |
| :-------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| `regex(., '^[0-9]{10}$')` or `regex(., '^\d{10}$')`                               | Restrict mobile number to ten digits                                                                               |
| `regex(., '^[0-9]{4}.[0-9]{2}.[0-9]{2}$')` or `regex(., '^\d{4}\.\d{2}\.\d{2}$')` | Restrict an input to `1234.56.78`                                                                                  |
| `regex(., '^[01-99]{2}$') and (. >= 01)`                                          | Restrict an input between `01` to `99` digits where input format of a _single number_ (like 1 or 2) is not allowed |
| <code>regex(., '^(12&#x7c;345)$')</code>                                          | Restrict an input to either to `12` or `345`                                                                       |
| `regex(., '^[1-9][0-9]{8}$')` or `regex(., '^[^0][0-9]{8}$')`                     | Restrict an input of _nine digits_ where the first number can't be `0`                                             |
| `regex(., '^\d$')`                                                                | Restrict an input to _one digit_ in between `0` to `9`                                                             |
| `regex(., '^\d{5}$')`                                                             | Restrict an input to _five digits_ in between `0` to `9`                                                           |
| `regex(., '^\d{2}\.\d{3}$')`                                                      | Restrict an input to _two digits and three decimals_ (e.g. `12.345`)                                               |
| `regex(., '^\d{2}(\.\d{3})?$')`                                                   | Restrict an input to _two digits and three decimals_ (while the decimals are optional) (e.g. `12` or `12.345`)     |

## Examples related to use of letters

| XLSForm Regex                                                  | Description                                                                                                                                                                                                                                                                                                                             |
| :------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `regex(., '^[a-z]{1,6}$')`                                     | Restrict an input to any lowercase letters (_up to 6 characters long_)                                                                                                                                                                                                                                                                  |
| `regex(., '^[A-Z]{1,10}$')`                                    | Restrict an input to any uppercase letters (_up to 10 characters long_)                                                                                                                                                                                                                                                                 |
| <code>regex(., '^(Apple&#x7c;Orange&#x7c;Banana)$')</code>     | Restrict an input to only either to `Apple` or `Orange` or `Banana`                                                                                                                                                                                                                                                                     |
| <code>regex(., '^p(ea&#x7c;ai)r$')</code>                      | Restrict an input to only `pear` or `pair`                                                                                                                                                                                                                                                                                              |
| `regex(., '^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+[.][A-Za-z]{2,}$')` | Restrict an input with a _valid email address_                                                                                                                                                                                                                                                                                          |
| `regex(., '^[A-Z]{1}[a-z]{1,}[ ]{1}[A-Z]{1}[a-z]{1,}$')`       | Restrict an input of the beneficiaries name where the _initials of the first name and last name are uppercase_ e.g. `Kobe Bryant`                                                                                                                                                                                                       |
| `regex(., '^\w{1,}\s(\w{1,})?(\s)?\w{1,}$')`                   | Restrict an input of the beneficiaries name with _first name, middle name (if any) and last name_ e.g. `Kobe Bean Bryant`                                                                                                                                                                                                               |
| `regex(., '^([A-Z]{1}[a-z]{1,}\s)([A-Z]{1}[a-z]{1,}\s?)+$')`   | Restrict an input of the beneficiaries' full name where the _initials of the names are in uppercase_ and the name are quite long (often greater than 3 words) e.g. `Samayamantri Venkata Rama Naga Butchi Anjaneya Satya Krishna Vijay` (this is an example of south Indian names)                                                      |
| `regex(., '^(\D+)\s(\D+)\s?\1$')`                              | Restrict an input of the beneficiaries' first name (so that you are able to capture the exact spelling) where the _enumerators are forced to enter the beneficiaries first name twice_ e.g. `Kobe Bryant Kobe`. (This could be helpful when you are trying to document beneficiaries details where a typo error could cost you heavy)   |
| `regex(., '^(\D+)\s(\D+)\s?\2$')`                              | Restrict an input of the beneficiaries' last name (so that you are able to capture the exact spelling) where the _enumerators are forced to enter the beneficiaries last name twice_ e.g. `Kobe Bryant Bryant`. _(This could be helpful when you are trying to document beneficiaries details where a typo error could cost you heavy)_ |
| `regex(., '^colou?r$')`                                        | Restrict a character within a word by using the `?` (quantifier) e.g. allow either `color` or `colour` as an input                                                                                                                                                                                                                      |
| `regex(., '^ah*!$')`                                           | Restrict a character within a word by using the `*` (quantifier) e.g. allow either `a!` or `ah!` or `ahh!` or `ahhh!` and so on as an input                                                                                                                                                                                             |
| `regex(., '^ah+!$')`                                           | Restrict a character within a word by using the `+` (quantifier) e.g. allow either `ah!` or `ahh!` or `ahhh!` and so on as an input                                                                                                                                                                                                     |
| `regex(., '^\D$')`                                             | Restrict an input to a _non-digit character_ (e.g. `a` or `c` or `!` or `#` or `%` etc.)                                                                                                                                                                                                                                                |
| `regex(., '^\D{5 }$')`                                         | Restrict an input to _five non-digit character_ (e.g. `aZcB!#%` etc.)                                                                                                                                                                                                                                                                   |

## Examples related to use of a combination of letters and numbers

| XLSForm Regex                                             | Description                                                                                                                                                                                                     |
| :-------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `regex(., '^\w$')`                                        | Restrict one character which matches between `a` to `z` or `A` to `Z` or `0` to `9` or `_` (i.e. match one character from `[a-zA-Z0-9_]`)                                                                       |
| `regex(., '^\w{3}$')`                                     | Restrict three character which matches between `a` to `z` or `A` to `Z` or `0` to `9` or `_` (i.e. match one character from `[a-zA-Z0-9_]`)                                                                     |
| `regex(., '^[A-Z]{3}[_][A-Z]{3}[_][0-9]{4}[_][0-9]{4}$')` | Restrict your beneficiary ID to a specific format e.g. `CAR_PRC_2020_0048`                                                                                                                                      |
| `regex(., '^CAR-PRC-2020-[0-9]{4}$')`                     | Restrict your beneficiary ID to a specific format e.g. `CAR-PRC-2020-0048` (_where the enumerators should enter an exact match from `CAR` to `-` i.e. `CAR-PRC-2020-` and can enter any 4 digit serial number_) |
| <code>regex(., '^[\$&#x7c;\£]\d{3}$')</code>              | Restrict a currency input of _three digits_ with a currency sign (either `dollar` or `pound`) in front (e.g. `$999` or `£500`)                                                                                  |
| `regex(., '^\W*(\w+\b\W*){3}$')`                          | Restrict an exact input of number of words (e.g. to restrict exactly 3 words `I love you.`)                                                                                                                     |
| `regex(., '^\W*(\w+\b\W*){3,5}$')`                        | Restrict an input of number of words (e.g. to restrict a range of words say `3` to `5`)                                                                                                                         |

## Considerations when using regex

-   If you wish to use a regex constraint on a number in a `text` type question,
    make sure you _always_ have the value `numbers` under the `appearance`
    column. This restricts the display of alphabets, making only numbers visible
    for inputs.

-   The Collect Android app and Enketo behave differently with their handling of
    regex expressions. Collect behaves as if you have used the anchors `^` and
    `$` around the expression (even if you have not used them), while Enketo
    requires the anchors as mandatory for an exact match.
