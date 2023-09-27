﻿@given("Notepad++ is open")
def step_impl():
  TestedApps.notepad.Run(1, True)

@when("I add a note with the text {arg}")
def step_impl(param1):
  notepad_ = Aliases.notepad_
  win_notepad = notepad_.wndNotepad
  win_notepad.Scintilla.Keys(param1)
  win_notepad.Close()

@then("I should see the note in Notepad++")
def step_impl():
  expected_result = "Hello, Notepad++"
  TestedApps.notepad.Run(1, True)
  notepad_ = Aliases.notepad_
  win_notepad = notepad_.wndNotepad
  win_notepad.Scintilla.Keys("^a")
  win_notepad.Scintilla.Keys("^c")
  actual_result = Sys.Clipboard
  if actual_result == expected_result:
    Log.Message("Note is added succesfully, Test PASSED")
  else:
    message = "Actual Result: " + actual_result
    Log.Error("Note is not added, Test FAILED " + message)
  
  win_notepad.Tab.Click(89, 16)
  notepad_.dlgSave.btnNo.ClickButton()  
  win_notepad.Close()
