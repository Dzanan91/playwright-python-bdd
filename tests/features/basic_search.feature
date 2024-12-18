@T1
Feature: Basic search form

  Scenario: T1 - One way flight search
    Given As a not logged user navigate to homepage
    When I select one-way trip type
    And Set as departure airport "RTM"
    And Set the arrival airport "MAD"
    And Uncheck the "Check accommodation with booking.com" option
    And Set the departure time 1 week in the future
    And Click the search button
    Then I am redirected to search results page
