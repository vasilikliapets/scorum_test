import allure
from hamcrest import has_entries, has_item, has_property, contains_string


def has_successful_result():
    return has_property('status_code', 200)


def has_error():
    return contains_string('error')
