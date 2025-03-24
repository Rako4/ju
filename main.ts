let Människa_väntar = 0
let Människan_har_gått_förbi = 0
let Bil_väntar = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    Människa_väntar = 1
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    Människa_väntar = 0
    Människan_har_gått_förbi = 1
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    Bil_väntar = 1
})
basic.forever(function on_forever() {
    pins.digitalWritePin(DigitalPin.P0, 1)
    if (Bil_väntar == 1) {
        pins.digitalWritePin(DigitalPin.P0, 0)
        if (Människa_väntar == 1) {
            pins.digitalWritePin(DigitalPin.P0, 0)
            basic.pause(1000)
            pins.digitalWritePin(DigitalPin.P1, 1)
            basic.pause(2000)
            pins.digitalWritePin(DigitalPin.P1, 1)
            basic.pause(1000)
            pins.digitalWritePin(DigitalPin.P1, 0)
            basic.pause(1000)
            pins.digitalWritePin(DigitalPin.P2, 1)
            basic.pause(5000)
            if (Människan_har_gått_förbi) {
                pins.digitalWritePin(DigitalPin.P2, 0)
                basic.pause(1000)
                pins.digitalWritePin(DigitalPin.P1, 1)
                basic.pause(1000)
                pins.digitalWritePin(DigitalPin.P1, 0)
                basic.pause(1000)
                pins.digitalWritePin(DigitalPin.P0, 1)
            }
            
        } else {
            pins.digitalWritePin(DigitalPin.P0, 1)
        }
        
    }
    
})
