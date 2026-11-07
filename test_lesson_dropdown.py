"""Автотест: сумма на странице и выбор в выпадающем списке."""
import pytest

from select_dropdown import LINKS, submit_correct_sum


@pytest.fixture
def browser():
    from selenium import webdriver

    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.parametrize("link", LINKS)
def test_select_sum_and_submit(browser, link):
    code = submit_correct_sum(browser, link)
    assert code.isdigit(), f"Ожидалось число в alert, получено: {code!r}"
