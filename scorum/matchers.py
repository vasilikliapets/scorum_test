import allure
from hamcrest import has_entries, has_item, has_property, contains_string


@allure.step('response has successful result')
def has_successful_result():
    return has_property('ok', True)


@allure.step('response has unsuccessful result')
def has_unsuccessful_result():
    return has_property('ok', False)


@allure.step('response has error')
def has_error():
    return contains_string('error')
