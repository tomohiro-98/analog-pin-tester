reading = 0

def on_forever():
    global reading
    reading = pins.analog_read_pin(AnalogPin.P0)
    led.plot_bar_graph(reading, 1023)
    if input.button_is_pressed(Button.A):
        basic.show_number(reading)
basic.forever(on_forever)
