@given("Notepad++ is open")
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

@when("I save the text as {arg} in the path {arg}")
def step_impl(param1, param2):
  TestedApps.notepad.Run(1, True)
  notepad_ = Aliases.notepad_
  wndNotepad = notepad_.wndNotepad
  wndNotepad.Scintilla.Keys("^s")
  dlgSaveAs = notepad_.dlgSaveAs
  progress = dlgSaveAs.WorkerW.ReBarWindow32.AddressBandRoot.progress
  progress.BreadcrumbParent.toolbar.Click(281, 21)
  comboBox = progress.comboBox
  comboBox.SetText(param2)
  comboBox.ComboBox.Edit.Keys("[Enter]")
  comboBox = dlgSaveAs.DUIViewWndClassName.Explorer_Pane.FloatNotifySink2.ComboBox
  comboBox.Edit.Click(120, 3)
  comboBox.SetText(param1)
  dlgSaveAs.btnSave.ClickButton()
  wndNotepad.Click(259, 70)
  wndNotepad.Tab.Click(94, 18)
  wndNotepad.Close()

@then("I should open the file {arg}")
def step_impl(param1):
  explorer = Aliases.explorer
  explorer.wndShell_TrayWnd.DesktopWindowXamlSource.Click(791, 36)
  wndCabinetWClass = explorer.wndCabinetWClass
  progress = wndCabinetWClass.WorkerW.ReBarWindow32.AddressBandRoot.progress
  progress.BreadcrumbParent.toolbarAddressThisPC.Click(255, 20)
  comboBox = progress.comboBox
  comboBox.SetText(param1)
  comboBox.ComboBox.Edit.Keys("[Enter]")
  wndNotepad = Aliases.Notepad.wndNotepad
  if wndNotepad.Exists:
    Log.Message("File is opened Successfully, Test PASSED")
  else:
    Log.Error("File does not exists, Test FAILED ")
    explorer.dlgFileExplorer.File_Explorer2.CtrlNotifySink.btnOK.ClickButton()
    wndCabinetWClass.Close()

@then("I should see the text in Notepad")
def step_impl():
  expected_result = "task1"
  explorer = Aliases.explorer  
  wndNotepad = Aliases.Notepad.wndNotepad
  richEditD2DPT = wndNotepad.RichEditD2DPT
  richEditD2DPT.Drag(108, 38, -97, -1)
  richEditD2DPT.Keys("^c")
  actual_result = Sys.Clipboard
  if actual_result == expected_result:
    Log.Message("Note is added succesfully, Test PASSED")
  else:
    message = "Actual Result: " + actual_result
    Log.Error("Note is not added, Test FAILED " + message)

  wndNotepad.Close()
  explorer.wndCabinetWClass.Close()
