import allure
from selene import by, be
from selene.support.shared.jquery_style import s
from conftest import browser_management

REPO_NAME = "eroshenkoam/allure-example"
SEARCH_INPUT = '[class="search-input"]'
QUERY_INPUT = '[id="query-builder-test"]'
ISSUES_TAB = "#issues-tab"
ISSUE_TEXT = "One piece"


@allure.tag('web')
@allure.feature("Задачи в репозитории")
@allure.story("Проверка Issue")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Aleksandr Bardashevich")
@allure.description("Тест для проверки поиска текста на странице")
@allure.link("https://github.com", name="Testing")
def test_labels(browser_management):
    expected_result = ISSUE_TEXT

    @allure.step("Поиск репозитория: {repo}")
    def search_for_repository(repo: str):
        s(SEARCH_INPUT).click()
        s(QUERY_INPUT).send_keys(repo).submit()

    @allure.step("Клик на репозиторий: {repo}")
    def open_repository(repo: str):
        s(by.link_text(repo)).should(be.visible).click()

    @allure.step("Клик на вкладку Issues")
    def open_issue_tab():
        s(ISSUES_TAB).should(be.visible).click()

    @allure.step(f"Проверка отображения текста: {expected_result}")
    def should_display_text(name: str):
        s(by.partial_text(name)).should(be.visible)

    search_for_repository(REPO_NAME)
    open_repository(REPO_NAME)
    open_issue_tab()
    should_display_text(expected_result)
