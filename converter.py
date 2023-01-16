import PySimpleGUI as sg

  #  [sg.Text("Text", enable_events = True, key="Text"), sg.Spin(["item","item2"])], #
#[sg.Button("Button", key = "Button1")],
#[sg.Input(key ="Input")],
#[sg.Text("Test"), sg.Button("Test Button",key = "Button2")]
layout = [
    [
        sg.Input(key = 'Input'),
        sg.Spin(['km to meters','kg to grams','sec to min','meters to seconds', 'grams to kgs','mins to sec'], key = 'Units'), 
        sg.Button('Convert', key = 'Convert')
    ],
    [sg.Text('Output', key = 'Output')]
]
#  mejor nombrarlos con keys para buscarlos luego en el codido

# Creamos una tabla con los arrows especificos

window = sg.Window('Converter',layout)# llamamos a window con el read pero si agregamos eventos colocarlo en el while

while True:
#Recordar que win_closed debe estar en Mayusc """

    event, values = window.read()
 
    if event == sg.WIN_CLOSED:
        break
 
    if event == 'Convert':
        input_value = values['Input']
        if input_value.isnumeric():
            match values['Units']:
                case 'km to meters':
                    output = round(float(input_value) * 1000,2)
                    output_string = f'{input_value} km are {output} meters.'
                case 'kg to grams':
                    output = round(float(input_value) * 1000,2)
                    output_string = f'{input_value} kg are {output} grams.'
                case 'sec to min':
                    output = round(float(input_value) / 60,2)
                    output_string = f'{input_value} seconds are {output} minutes.'
                case 'meters to seconds':
                    output = round(float(input_value) / 0.01,2)
                    output_string = f'{input_value} meters are {output} kms.'
                case 'grams to kgs':
                    output = round(float(input_value) / 0.0,2)
                    output_string = f'{input_value}  grams {output} kgs.'
                case 'mins to sec':
                    output = round(float(input_value) * 60,2)
                    output_string = f'{input_value} mins are {output} secs.'
            window['Output'].update(output_string)
        else:
            window['Output'].update('Please enter a number')
    #if event == "Button1":
        #window["Text"].update(values["Input" ])
       #print("values"["Input"]) 
#Se puede colocar el corchete input para obviar los primeros dos datos
  #  if event == "Button2":
       # print("test pressed")


   # if event == "Text":
     #   print("Text pressed")

window.close()

# No se cerrara hasta no salir especificamente.Eventos se activan con una accion.- Al cerrar se actrivaria el window.close  """

