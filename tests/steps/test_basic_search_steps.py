from pytest_bdd import scenarios, given, when, then


# Load the feature
scenarios("../features/basic_search.feature")


@given("As a not logged user navigate to homepage")
def navigate_to_homepage(home_page, common_actions):
    home_page.navigate_to_home_page()
    assert "kiwi.com" in home_page.page.url, "Homepage did not load successfully"
    common_actions.click_button(home_page.reject_all_btn)


@when("I select one-way trip type")
def select_one_way_trip(home_page, common_actions):
    common_actions.click_button(home_page.remove_option_btn)
    common_actions.click_button(home_page.trip_way_dropdown)
    common_actions.click_button(home_page.one_way_option)


@when('Set as departure airport "RTM"')
def set_departure_airport(home_page, common_actions):
    common_actions.input_text(home_page.location, "RTM")
    common_actions.click_button(home_page.get_place_picker_row("Rotterdam, Netherlands"))


@when('Set the arrival airport "MAD"')
def set_arrival_airport(home_page, common_actions):
    common_actions.input_text(home_page.location, "MAD", index=1)
    common_actions.click_button(home_page.get_place_picker_row("Madrid, Spain"))


@when('Uncheck the "Check accommodation with booking.com" option')
def uncheck_accommodation_option(home_page, common_actions):
    common_actions.click_button(home_page.booking_checkbox)


@when("Set the departure time 1 week in the future")
def set_departure_time(home_page, common_actions):
    common_actions.click_button(home_page.date_input_wrapper)
    home_page.select_week_in_future(weeks_in_future=1)
    common_actions.click_button(home_page.set_dates_btn)


@when("Click the search button")
def click_search_button(home_page, common_actions):
    common_actions.click_button(home_page.search_btn)


@then("I am redirected to search results page")
def validate_search_results(home_page, common_actions):
    common_actions.element_is_visible(home_page.search_page_header)
    print("User has landed on the search results page")
