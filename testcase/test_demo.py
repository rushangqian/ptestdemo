import re
import time

import pytest
import requests


class TestDemo:
    def test_demo1(self, my_fixture):
        t = '打哈萨克都好看就华东数控'
        s = re.search('克都(.*?)数控', t)
        print(s.group())
        requests.get()

    @pytest.mark.smokers
    @pytest.mark.lock
    def test_demo_h(self):
        print("hello,h")
