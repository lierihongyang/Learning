# -*- coding: UTF-8 -*-
import pytest
import requests


@pytest.fixture()
def fixer1():
    print("fixture 1 前置")
    yield
    print("fixture 1 后置")


@pytest.mark.skip("test case 1 skip")
def test_case1():
    print("\ntest case 1")
    assert 1


def test_case2():
    print("\ntest case 2")
    assert 1


@pytest.mark.moke
def test_case3(fixer1):
    print("\ntest case 3")
    assert 1


class TestCase:
    @pytest.mark.skipif(4 == 4, reason="test case 4 skip")
    def test_case4(self):
        print("\ntest case 4")
        assert 0, "用例 test case 4 运行失败"

    def test_case5(self):
        print("\ntest case 5")
        assert 1

    def test_case6(self, fixer1):
        print("\ntest case 6")
        assert 1

    def test_case7(self):
        print("\ntest case 7")
        assert 1

    def test_case8(self):
        print("\ntest case 8")
        assert 1

    def test_case9(self):
        print("\ntest case 9")
        assert 1

    @pytest.mark.moke
    def test_case10(self):
        print("\ntest case 10")
        assert 1


from work_1 import ReadData


class TestInterface:
    rd = ReadData("data.xls")
    test_data = rd.read_xlsx()

    def test_login(self):
        interfaceUrl = self.test_data[0].get("interfaceUrl")
        method: str = self.test_data[0].get("method")
        value = self.test_data[0].get("value")
        expect = self.test_data[0].get("expect")

        value = eval(value)
        if method.lower() == "get":
            response = requests.get(interfaceUrl, params=value)
        if method.lower() == "post":
            response = requests.post(interfaceUrl, data=value)
        res_data = response.json()
        err_code = res_data.get("errorCode")
        assert str(err_code) == expect, f"实际结果: {err_code} 与 预期结果: {expect} 不符"


if __name__ == '__main__':
    # pytest.main(["-sv", "test_case.py"])
    # pytest.main(["-sv", "--reruns=2"])
    # pytest.main(["-sv", "-k=10"])
    # pytest.main(["-sv", "-n=5"])
    # pytest.main(["-sv", "-m=moke"])
    # pytest.main(["-sv", "--html=./resport.html"])
    pytest.main(["-sv", "test_case.py::TestInterface::test_login", "--html=./resport.html"])
