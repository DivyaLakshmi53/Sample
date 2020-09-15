from selenium import webdriver
from ecommerce_common.common_configs.locators_config import locators_config
from ecommerce_common.common_configs.locators_config import url_config
import time
import logging as logger

def go_to(context, location, **kwargs):
    if not location.startswith('http'):
        _url = location
        base_url = url_config.URLCONFIG.get('base_url')
        url = base_url + _url



