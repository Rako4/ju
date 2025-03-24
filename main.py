Människa_väntar = 0
Människan_har_gått_förbi = 0
Bil_väntar = 0

def on_button_pressed_a():
    global Människa_väntar
    Människa_väntar = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Människa_väntar, Människan_har_gått_förbi
    Människa_väntar = 0
    Människan_har_gått_förbi = 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Bil_väntar
    Bil_väntar = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pins.digital_write_pin(DigitalPin.P0, 1)
    if Bil_väntar == 1:
        pins.digital_write_pin(DigitalPin.P0, 0)
        if Människa_väntar == 1:
            pins.digital_write_pin(DigitalPin.P0, 0)
            basic.pause(1000)
            pins.digital_write_pin(DigitalPin.P1, 1)
            basic.pause(2000)
            pins.digital_write_pin(DigitalPin.P1, 1)
            basic.pause(1000)
            pins.digital_write_pin(DigitalPin.P1, 0)
            basic.pause(1000)
            pins.digital_write_pin(DigitalPin.P2, 1)
            basic.pause(5000)
            if Människan_har_gått_förbi:
                pins.digital_write_pin(DigitalPin.P2, 0)
                basic.pause(1000)
                pins.digital_write_pin(DigitalPin.P1, 1)
                basic.pause(1000)
                pins.digital_write_pin(DigitalPin.P1, 0)
                basic.pause(1000)
                pins.digital_write_pin(DigitalPin.P0, 1)
        else:
            pins.digital_write_pin(DigitalPin.P0, 1)
basic.forever(on_forever)
