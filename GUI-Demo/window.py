import PySimpleGUI as sg

# windows - display the window of the content inside, two kinds of windows
# one shot - window displayed, event is read, window closes after 
# persistent - window stays open until the user takes the action to close the window or close the application

# creating a one shot window
layout = [[sg.Text('This is our one-shot window')],  # the layout displays what happens inside of our window
          [sg.Button('Ok')]]

window = sg.Window('Title', layout) # window holds the layout and the title of our window

event, values = window.read() # no clue what this does

window.close() # closes the window upon hitting the 'ok' button

# persistent window - more common due to hte user going to be interacting with them over an extended period of time
layout = [[sg.Text('This is our persistent window')],
          [sg.Button('1'), sg.Button('2'), sg.Button('Exit')]]

window = sg.Window('Title', layout)
# sets up the layout and the window

while True:         # The Event Looop, while true the window will remain open
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': # if we close the window or click the exit button
        break # this will end the program

    if event == '1':
        sg.popup('You clicked 1')
    elif event == '2':
        sg.popup('You clicked 2')

window.close() # closes the window

