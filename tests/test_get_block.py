import allure
import json
from jsonschema import validate
from hamcrest import assert_that, equal_to, contains_string

from scorum.steps import get_block
from scorum.matchers import has_successful_result, has_error
from data.input_data import get_block_payload, get_block_payload_bad_id, get_block_payload_bad_method, \
    get_block_payload_bad_params
from data.schemas import Schema


@allure.feature('get_block')
def test_get_block(yaml_config):
    """
    :type yaml_config: dict
    """
    get_block_response = get_block(
        url=yaml_config['url'],
        data=get_block_payload,
        headers=yaml_config['headers']
    )

    assert_that(get_block_response, has_successful_result())
    assert_that(get_block_response.json()['id'], equal_to(json.loads(get_block_payload)['id']))
    validate(get_block_response.json(), Schema.GET_BLOCK)
    assert_that(get_block_response, has_successful_result())


@allure.feature('get_block')
def test_get_block_bad_id(yaml_config):
    """
    :type yaml_config: dict
    """
    get_block_response = get_block(
        url=yaml_config['url'],
        data=get_block_payload_bad_id,
        headers=yaml_config['headers']
    )

    # assert_that(get_block_response, has_unsuccessful_result())
    assert_that(get_block_response.text, has_error())
    assert_that(get_block_response.text,
                contains_string(json.loads(get_block_payload_bad_id)['id']))


@allure.feature('get_block')
def test_get_block_bad_method(yaml_config):
    """
    :type yaml_config: dict
    """
    get_block_response = get_block(
        url=yaml_config['url'],
        data=get_block_payload_bad_method,
        headers=yaml_config['headers']
    )

    # assert_that(get_block_response, has_unsuccessful_result())
    assert_that(get_block_response.text, has_error())
    assert_that(get_block_response.text,
                contains_string(json.loads(get_block_payload_bad_method)['method']))


@allure.feature('get_block')
def test_get_block_bad_params(yaml_config):
    """
    :type yaml_config: dict
    """
    get_block_response = get_block(
        url=yaml_config['url'],
        data=get_block_payload_bad_params,
        headers=yaml_config['headers']
    )

    # assert_that(get_block_response, has_unsuccessful_result())
    assert_that(get_block_response.text, has_error())
    assert_that(get_block_response.text,
                contains_string(json.loads(get_block_payload_bad_params)['params'][0]))
