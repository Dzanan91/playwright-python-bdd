from playwright.sync_api import Page, BrowserContext, Locator
from datetime import datetime, timedelta
from playwright.sync_api import expect


class HomePage:
    def __init__(self, page: Page, context: BrowserContext, base_url: str):
        self.page = page
        self.context = context
        self.base_url = base_url  # Initialize the base URL

        # Locators
        self.reject_all_btn: Locator = page.locator('button div:has-text("Reject all")')
        self.remove_option_btn: Locator = page.locator('div[data-test="PlacePickerInputPlace-close"]')
        self.trip_way_dropdown: Locator = page.locator('div[data-test="SearchFormModesPicker-active-return"]')
        self.one_way_option: Locator = page.locator('a[data-test="ModePopupOption-oneWay"]')
        self.location: Locator = page.locator('input[data-test="SearchField-input"]')
        self.arrival_location: Locator = page.locator('div[data-test="PlacePickerInput-destination"]')
        self.search_result_option: Locator = page.locator('div[data-test="PlacePickerRow-wrapper"]')
        self.booking_checkbox: Locator = page.locator('div[data-test="bookingCheckbox"]')
        self.date_input_wrapper: Locator = page.locator('input[data-test="SearchFieldDateInput"]')
        self.day_locator_template = 'div[data-value="{date}"]'
        self.drag_arrow_locator_template = 'div[data-value="{date}"] div[data-test="DayDragArrowRight"]'
        self.set_dates_btn: Locator = page.locator('button[data-test="SearchFormDoneButton"]')
        self.search_btn: Locator = page.locator('a[data-test="LandingSearchButton"]')
        self.search_page_header: Locator = page.locator('div[data-test="SearchForm-wrapper"]')



        
    def navigate_to_home_page(self) -> None:
        """Navigate to the homepage."""
        self.page.goto(self.base_url)
    
    
    def get_place_picker_row(self, text: str) -> Locator:
        """
        Dynamically generates a locator for a PlacePickerRow based on text.
        :param text: Text to match within the PlacePickerRow.
        :return: Locator for the element.
        """
        return self.page.locator(f'div[data-test="PlacePickerRow-wrapper"] div:has-text("{text}")')
    
    def select_week_in_future(self, weeks_in_future: int = 1) -> None:
        """
        Selects a full week in the future by interacting with the drag arrows.
        :param weeks_in_future: Number of weeks into the future to start.
        """
        # Calculate the start date
        start_date = datetime.now() + timedelta(weeks=weeks_in_future)
        current_date = start_date

        # Click on the starting date
        start_date_str = current_date.strftime("%Y-%m-%d")
        start_day_locator = self.page.locator(self.day_locator_template.format(date=start_date_str))
        expect(start_day_locator).to_be_visible(timeout=3000)
        start_day_locator.click()
        print(f"Clicked on the start date: {start_date_str}")

        # Click the drag arrow dynamically for 6 days
        for _ in range(6):
            # Wait for the current drag arrow to appear
            drag_arrow_locator = self.page.locator(
                self.drag_arrow_locator_template.format(date=current_date.strftime("%Y-%m-%d"))
            )
            expect(drag_arrow_locator).to_be_visible(timeout=3000)

            # Click the drag arrow
            drag_arrow_locator.click()
            print(f"Clicked on drag arrow for date: {current_date.strftime('%Y-%m-%d')}")

            # Increment to the next date
            current_date += timedelta(days=1)