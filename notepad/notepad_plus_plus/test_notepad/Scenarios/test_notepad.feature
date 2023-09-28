Feature: Adding a note to Notepad++

Scenario: Add a note to Notepad++
    Given Notepad++ is open
    When  I add a note with the text "Hello, Notepad++"
    Then  I should see the note in Notepad++


Scenario: Save a text in a file
    Given Notepad++ is open
    When  I add a note with the text "task1"
    And   I save the text as "text1.txt" in the path "C:\Users\dennis.gamboa\Desktop"
    Then  I should open the file "C:\Users\dennis.gamboa\Desktop\text1.txt"
    And   I should see the text in Notepad
