import PySimpleGUIQt as sg
from loguru import logger
import time
from timeloop import Timeloop
from datetime import timedelta
from func import with_logging

tl = Timeloop()



@with_logging
@tl.job(interval=timedelta(seconds=30))
def MicroBreak():
    # TODO: If pause is pressed, don't show microbreaks
    # layout the Window
    layout = [[sg.Text('A MicroBreak')],
            [sg.ProgressBar(5, orientation='h', size=(20, 20), key='progbar')]]

    # create the Window
    window = sg.Window('Custom Progress Meter', layout)
    start = time.time()
    elapsed = 0
    while elapsed < 5:
        event, values = window.Read(timeout=0)
        if event == 'Cancel' or event is None:
            break
        end = time.time()
        elapsed = end - start
        window.Element('progbar').UpdateBar(elapsed)
    window.Close()    


menu = ['BLANK', ['&Pause', '---','E&xit']]
tray = sg.SystemTray(menu=menu, filename=r'tea.png')
tl.start(block=False) # Start all decorated functions in a thread


while True:  # The event loop
    menu_item = tray.Read()
    # logger.debug("Menu clicked: %s", menu_item)
    if menu_item == 'Exit':
        tl.stop()
        break
    elif menu_item == 'Pause':
        pass


