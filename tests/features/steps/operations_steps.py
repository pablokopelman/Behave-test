"""Behave tests."""
from behave import given, when, then
from operations.simple import Simple


@given('two numbers')
def step_givenInts(context) -> None:
    """Given."""
    context.first_number = 1
    context.second_number = 2


@given('a number and a string')
def step_givenIntStr(context) -> None:
    """Given."""
    context.first_number = "1"
    context.second_number = 2


@when('first is a string')
def step_when(context) -> None:
    """When."""
    context.first_number = str(context.first_number)


@then('result will be an integer')
def step_then(context) -> int:
    """Then."""
    ret = Simple.sum(context.first_number, context.second_number)
    assert type(ret) is int
    return ret


@given("a number and a letter")
def step_givenLetter(context) -> None:
    """Given."""
    context.first_number = "a"
    context.second_number = "1"


@then('result will be the integer')
def step_impl(context) -> int:
    ret = Simple.sum(context.first_number, context.second_number)
    assert type(ret) is int
    return ret


@given("two numbers {first} and {second}")
def step_implTwo(context, first, second) -> None:
    """Given."""
    context.first_number = first
    context.second_number = second


@when("first is a number")
def step_first_Int(context) -> None:
    """When."""
    context.first_number = int(context.first_number)


@when("second is a number")
def step_second_int(context) -> None:
    """When."""
    context.second_number = int(context.second_number)


@when("second is a string")
def stepTwoStr(context) -> None:
    """When."""
    context.second_number = str(context.second_number)


@then("result will be {result:d} of type integer")
def step_impl_result(context, result) -> None:
    """Then."""
    ret = Simple.sum(context.first_number, context.second_number)

    assert type(ret) is int
    assert ret == result
