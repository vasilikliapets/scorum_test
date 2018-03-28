import allure
import json
from jsonschema import validate
from hamcrest import assert_that, contains_string

from scorum.steps import get_dynamic_global_properties
from scorum.matchers import has_successful_result, has_error
from data.schemas import Schema
import data.input_data as data


@allure.feature('get_dynamic_global_properties')
def test_get_dynamic_global_properties(yaml_config):
    """
    :type yaml_config: dict
    """
    get_dynamic_global_properties_response = get_dynamic_global_properties(
        url=yaml_config['url'],
        data=data.dynamic_payload,
        headers=yaml_config['headers']
    )

    assert_that(get_dynamic_global_properties_response, has_successful_result())
    validate(get_dynamic_global_properties_response.json(), Schema.GET_DYNAMIC_GLOBAL_PROPERTIES)
    result_json = get_dynamic_global_properties_response.json()['result']

    assert_that(result_json['total_supply'], contains_string('SCR'))
    assert_that(result_json['registration_pool_balance'], contains_string('SCR'))
    assert_that(result_json['fund_budget_balance'], contains_string('SCR'))
    assert_that(result_json['content_reward_balance'], contains_string('SCR'))
    assert_that(result_json['circulating_capital'], contains_string('SCR'))
    assert_that(result_json['reward_pool_balance'], contains_string('SCR'))
    assert_that(result_json['total_scorumpower'], contains_string('SP'))


@allure.feature('get_dynamic_global_properties')
def test_get_dynamic_global_properties_bad_id(yaml_config):
    """
    :type yaml_config: dict
    """
    get_dynamic_global_properties_response = get_dynamic_global_properties(
        url=yaml_config['url'],
        data=data.dynamic_payload_bad_id,
        headers=yaml_config['headers']
    )

    assert_that(get_dynamic_global_properties_response, has_successful_result())
    assert_that(get_dynamic_global_properties_response.text, has_error())
    assert_that(get_dynamic_global_properties_response.text,
                contains_string(json.loads(data.dynamic_payload_bad_id)['id']))


@allure.feature('get_dynamic_global_properties')
def test_get_dynamic_global_properties_bad_method(yaml_config):
    """
    :type yaml_config: dict
    """
    get_dynamic_global_properties_response = get_dynamic_global_properties(
        url=yaml_config['url'],
        data=data.dynamic_payload_bad_method,
        headers=yaml_config['headers']
    )
    assert_that(get_dynamic_global_properties_response, has_successful_result())
    assert_that(get_dynamic_global_properties_response.text, has_error())
    assert_that(get_dynamic_global_properties_response.text,
                contains_string(json.loads(data.dynamic_payload_bad_method)['method']))


@allure.feature('get_dynamic_global_properties')
def test_get_dynamic_global_properties_bad_params(yaml_config):
    """
    :type yaml_config: dict
    """
    get_dynamic_global_properties_response = get_dynamic_global_properties(
        url=yaml_config['url'],
        data=data.dynamic_payload_bad_params,
        headers=yaml_config['headers']
    )
    assert_that(get_dynamic_global_properties_response, has_successful_result())
    assert_that(get_dynamic_global_properties_response.text, has_error())
    assert_that(get_dynamic_global_properties_response.text,
                contains_string(json.loads(data.dynamic_payload_bad_params)['params'][0]))
