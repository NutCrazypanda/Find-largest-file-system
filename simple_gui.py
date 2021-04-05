import os
import fnmatch
import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your creations colorful

layout = [  [sg.Text('Filename'),sg.Input(), sg.FolderBrowse()],
            [sg.Text('Enter File size (GB)'), sg.InputText()],
            [sg.OK('Search'),sg.Button('Clear')],
            [sg.Text(size=(100,20),key='-RESULT-')]]

window = sg.Window('Get filename example', layout)

while True:
    event, values = window.read()
    if event == 'Clear':
        text = window['-RESULT-']
        text.update('')
    else:
        path = os.path.abspath(str(values[0]))
        max_size = float(values[1])*1024*1024*1024
        max_file =""
        for folder, subfolders, files in os.walk(path):
            try:
                for file in files:
                    size = os.stat(os.path.join( folder, file )).st_size
                    if size>max_size:
                        max_file = os.path.join( folder, file )
                        text = window['-RESULT-']
                        text.update(text.get()+max_file+' Size:'+str(size/1024/1024/1024)+' GB \n')
            except :
                pass
window.close()
