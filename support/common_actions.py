from playwright.sync_api import Page, Locator, expect

class CommonActions:
    def __init__(self, page: Page):
        self.page = page

    def click_button(self, locator: Locator, index: int = 0) -> None:
        """Scroll to and click a button or element."""
        element = locator.nth(index)
        element.scroll_into_view_if_needed()
        element.click()

    def click_element_by_text(self, base_locator: str, text: str) -> None:
        """
        Clicks on an element based on the base locator and text content.
        :param base_locator: Base locator (e.g., 'button', 'div').
        :param text: Text content of the element to match.
        """
        target_element = self.page.locator(f"{base_locator}:has-text('{text}')")
        expect(target_element).to_be_visible(timeout=5000)
        target_element.click()


    def input_text(self, locator: Locator, text: str, index: int = 0) -> None:
        """Input text into a given element."""
        element = locator.nth(index)
        element.fill(text)

    def element_is_visible(self, locator: Locator) -> bool:
        """Check if an element is visible."""
        expect(locator).to_be_visible()
        return locator.is_visible()

    def get_text(self, selector: str) -> str:
        """Retrieve the text of an element by selector."""
        return self.page.locator(selector).inner_text()

    def wait_for_element(self, selector: str, timeout: int = 5000) -> None:
        """Wait for an element to appear with a timeout."""
        self.page.locator(selector).wait_for(timeout=timeout)

    def hover_over_element(self, locator: Locator) -> None:
        """Hover over an element."""
        locator.hover()

    def is_text_visible(self, locator: Locator, expected_text: str, index: int = 0, timeout: int = 5000) -> None:
        """
        Verify if a text is visible in a specific element.
        :param locator: The Playwright locator object.
        :param expected_text: The expected text.
        :param index: Index if there are multiple matches.
        :param timeout: Timeout for waiting.
        """
        element = locator.nth(index)
        element.wait_for(state="visible", timeout=timeout)
        actual_text = element.inner_text()
        assert actual_text.strip() == expected_text.strip(), f"Expected: '{expected_text}', but got: '{actual_text}'"

    def validate_url(self, expected_url: str, match_type: str = "exact") -> None:
        """
        Validates the current URL.
        :param expected_url: The expected URL or part of the URL.
        :param match_type: 'exact' for exact match, 'contains' for partial match.
        """
        current_url = self.page.url
        if match_type == "exact":
            assert current_url == expected_url, f"Expected URL: '{expected_url}', but got: '{current_url}'"
        elif match_type == "contains":
            assert expected_url in current_url, f"URL does not contain: '{expected_url}'"
        else:
            raise ValueError(f"Invalid match type: {match_type}")
