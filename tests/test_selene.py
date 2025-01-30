from selene import be, have, by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_clean_issue():
    browser.open("https://github.com")

    s('[data-target="qbsearch-input.inputButton"]').click()
    s('#query-builder-test').should(be.visible).send_keys("eroshenkoam/allure-example").press_enter()

    s(by.link_text("eroshenkoam/allure-example")).should(be.visible).click()

    s("#issues-tab").should(be.visible).click()

    print("Текущий URL:", browser.driver.current_url)

    issue = s('a[href="/eroshenkoam/allure-example/issues/94"] span')
    issue.should(be.visible).should(have.text("One piece"))
