from melitk.restclient import new_restclient
from melitk import restclient_mock
from pytest_bdd import scenarios, given, when, then, parsers

scenarios("../restclient.feature")

# Given the url "www.google.com"
# When we mock the url to get the response "hoooola"
# Then the content of the response should be "hoooola"

@given(parsers.parse('the url "{url}"'), target_fixture="url")
def mocker_url(url):
    return url

@when(parsers.parse('we mock the url to get the response "{response}"'), target_fixture="mock")
def mocked(url, response):
    m = restclient_mock.Mocker()
    m.register_uri(restclient_mock.GET, url, text=response)
    return m


@then(parsers.parse('the content of the response should be "{response}"'))
def mok(mock, url, response):
    rc = new_restclient()
    with mock:
        resp = rc.get(url)
        assert resp.text == response
