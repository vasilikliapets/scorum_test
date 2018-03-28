import allure
import requests


@allure.step('get_dynamic_global_properties')
def get_dynamic_global_properties(url, data, **kwargs):
    return requests.post(url=url, data=data, **kwargs)


@allure.step('get_existed_block')
def get_block(url, data, **kwargs):
    return requests.get(url=url, data=data, **kwargs)
