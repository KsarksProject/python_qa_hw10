from selene import by, be
from selene.support.shared.jquery_style import s
from conftest import browser_management

REPO_NAME = "eroshenkoam/allure-example"
SEARCH_INPUT = '[class="search-input"]'
QUERY_INPUT = '[id="query-builder-test"]'
ISSUES_TAB = "#issues-tab"
ISSUE_TEXT = "One piece"


def test_selene(browser_management):
    s(SEARCH_INPUT).click()
    s(QUERY_INPUT).send_keys(REPO_NAME).submit()
    s(by.link_text(REPO_NAME)).should(be.visible).click()
    s(ISSUES_TAB).should(be.visible).click()
    s(by.partial_text(ISSUE_TEXT)).should(be.visible)
