'''
notes
two types of api that are used - one for visuals and one for the backend



'''

import PySimpleGUI as sg

sg.popup('Hello') # pop up window that displays the text
# can pass in more parameters to customize how the window shows
# ex. sg.popup('Hello', no_titlebar = True) # makes a popup window without the titlebar

'''
popup
popup_animated
popup_annoying
popup_auto_close
popup_cancel
popup_error
popup_error_with_traceback
popup_get_date
popup_get_file
popup_get_folder
popup_get_text
popup_menu
popup_no_border
popup_no_buttons
popup_no_frame
popup_no_titlebar
popup_no_wait
popup_non_blocking
popup_notify
popup_ok
popup_ok_cancel
popup_quick
popup_quick_message
popup_scrolled
popup_timed
popup_yes_no

'''

name = sg.popup_get_text('What is your name?') # pop up window that saves the entered string into a variable
# pop up text cna take in four different kinds of information
# popup_get_[text, file, folder, date]

sg.Print('Hello', colors = 'white on red') # highlighting/debug screen

for i in range(0, 100): # progress bar
    sg.one_line_progress_meter("Just as the name says", i, 99)
# has only three parameters for teh title, counter, max value

