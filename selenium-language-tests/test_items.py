def test_add_to_cart_button_is_present(browser):
    browser.get(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    )
    button = browser.find_element("css selector", ".btn-add-to-basket")
    assert button.is_displayed()
