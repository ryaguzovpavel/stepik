"""Задание: работа с выпадающим списком (модуль 2).

pytest test_lesson_dropdown.py -v   # автотесты
python select_dropdown.py           # число из alert на selects1
"""
from __future__ import annotations

import time
from typing import TYPE_CHECKING

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

if TYPE_CHECKING:
    from selenium.webdriver.remote.webdriver import WebDriver

LINKS = (
    "https://suninjuly.github.io/selects1.html",
    "https://suninjuly.github.io/selects2.html",
)


def sum_numbers_on_page(driver: WebDriver) -> int:
    numbers = driver.find_elements(By.CSS_SELECTOR, "h1 .nowrap")
    return sum(int(span.text) for span in numbers)


def wait_for_select_options(driver: WebDriver, min_options: int = 6) -> None:
    WebDriverWait(driver, 12).until(
        lambda d: len(d.find_elements(By.CSS_SELECTOR, "select option")) >= min_options
    )


def submit_correct_sum(driver: WebDriver, link: str) -> str:
    driver.get(link)
    if "selects2" in link:
        wait_for_select_options(driver)
    total = sum_numbers_on_page(driver)
    Select(driver.find_element(By.TAG_NAME, "select")).select_by_value(str(total))
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    code = alert.text
    alert.accept()
    return code


def main() -> None:
    driver = webdriver.Chrome()
    try:
        for link in LINKS:
            code = submit_correct_sum(driver, link)
            print(f"{link} -> {code}")
            time.sleep(1)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
