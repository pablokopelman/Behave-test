Feature: trying pytest-bdd

    Scenario: testting with restclient mock

        Given the url "www.google.com"
        When we mock the url to get the response "hoooola"
        Then the content of the response should be "hoooola"
