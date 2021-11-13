from behave import fixture
from melitk.restclient_mock import Mocker
from behave.fixture import use_fixture_by_tag, fixture_call_params


# -- FIXTURE-VARIANT 1: Use generator-function
@fixture
def restclient_mock(context, **kwargs):
    # -- SETUP-FIXTURE PART:
    context.restclient_mock = Mocker
    yield context.restclient_mock
    # -- CLEANUP-FIXTURE PART:
    context.restclient_mock = None


fixture_registry1 = {
    "fixture.restclient_mock": restclient_mock,
}

def before_tag(context, tag):
    if tag.startswith("fixture."):
        return use_fixture_by_tag(tag, context, fixture_registry1)
