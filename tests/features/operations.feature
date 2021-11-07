Feature: showing off behave

    @string
    Scenario: Test if first is not a number
        Given a number and a letter
        Then result will be the integer

    Scenario Outline: Simple numbers
        Given two numbers <first> and <second>
        When first is a number
        And second is a number
        Then result will be <result> of type integer

        Examples: numbers
        | first  | second | result |
        | 1      | 2      | 3      |
        | 2      | 3      | 5      |
        | 0      | 0      | 0      |
        | -1     | -1     | -2     |
        | -1     | 1      | 0      |

    Scenario: Test simple sum
        Given two numbers
        When first is a string
        Then result will be an integer

    @string
    Scenario: Test number and a string
        Given a number and a string
        When first is a string
        Then result will be an integer

    @string
    Scenario Outline: Simple numbers with strings
        Given two numbers <first> and <second>
        When first is a number
        And second is a string
        Then result will be <result> of type integer

        Examples:
            | first | second | result |
            | 1     | 2      | 3      |
            | 2     | 3      | 5      |
