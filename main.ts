radio.setGroup(45)
radio.setTransmitPower(7)
input.setAccelerometerRange(AcceleratorRange.EightG)
basic.forever(function on_forever() {
    radio.sendNumber(input.acceleration(Dimension.Z))
    basic.pause(100)
})
