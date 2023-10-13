radio.set_group(xx)
radio.set_transmit_power(7)
input.set_accelerometer_range(AcceleratorRange.EIGHT_G)

#Set the radio group above. Use a number between 1-99

def on_forever():
    radio.send_number(input.acceleration(Dimension.Z))
    basic.pause(100)
basic.forever(on_forever)
