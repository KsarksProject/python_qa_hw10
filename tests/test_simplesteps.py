import allure
from selene import by, be
from selene.support.shared.jquery_style import s
from conftest import browser_management

REPO_NAME = "eroshenkoam/allure-example"
SEARCH_INPUT = '[class="search-input"]'
QUERY_INPUT = '[id="query-builder-test"]'
ISSUES_TAB = "#issues-tab"
ISSUE_TEXT = "One piece"

def test_steps(browser_management):
    expected_result = ISSUE_TEXT

    with allure.step("Клик на инпут ввода"):
        s(SEARCH_INPUT).click()

    with allure.step("Поиск репозитория"):
        s(QUERY_INPUT).send_keys(REPO_NAME).press_enter()

    with allure.step("Клик на найденный репозиторий"):
        s(by.link_text(REPO_NAME)).should(be.visible).click()

    with allure.step("Клик на таб issues"):
        s(ISSUES_TAB).should(be.visible).click()

    with allure.step(f"Проверка отображения {expected_result} на странице"):
        s(by.partial_text(expected_result)).should(be.visible)
