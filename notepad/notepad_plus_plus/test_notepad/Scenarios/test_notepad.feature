Feature: Adding a note to Notepad++

Scenario: Add a note to Notepad++
    Given Notepad++ is open
    When I add a note with the text "Hello, Notepad++"
    Then I should see the note in Notepad++
