import asyncio
from bleak import BleakScanner, BleakClient

# UUIDs for the LED service and characteristic
TARGET_ADDRESS = "8D1860A9-56E9-7C16-5881-6CAAA7106162"
RED_LED_UUID = '13012F01-F8C3-4F4A-A8F4-15CD926DA146'
GREEN_LED_UUID = '13012F02-F8C3-4F4A-A8F4-15CD926DA146'
BLUE_LED_UUID = '13012F03-F8C3-4F4A-A8F4-15CD926DA146'

on_value = bytearray([0x01])
off_value = bytearray([0x00])

RED = False
GREEN = False
BLUE = False


def getValue(on):
    if on:
        return on_value
    else:
        return off_value


async def setColor(client):
    global RED, GREEN, BLUE
    val = input('Enter rgb to toggle red, green and blue LEDs :')
    print(val)

    if 'r' in val:
        RED = not RED
        await client.write_gatt_char(RED_LED_UUID, getValue(RED))
    if 'g' in val:
        GREEN = not GREEN
        await client.write_gatt_char(GREEN_LED_UUID, getValue(GREEN))
    if 'b' in val:
        BLUE = not BLUE
        await client.write_gatt_char(BLUE_LED_UUID, getValue(BLUE))


async def connect_and_write_led_characteristic():
    global RED, GREEN, BLUE

    # Scan for BLE devices
    scanner = BleakScanner()

    await scanner.start()
    await asyncio.sleep(5)  # Scan for 5 seconds
    await scanner.stop()

    # Find the Arduino Nano 33 BLE Sense device
    device = await scanner.find_device_by_address(TARGET_ADDRESS)
    if not device:
        print("Device not found.")
        return

    async with BleakClient(device) as client:
        await client.is_connected()
        print(f"Connected to: {client.address}")

        val = await client.read_gatt_char(RED_LED_UUID)
        if val == on_value:
            print('RED ON')
            RED = True
        else:
            print('RED OFF')
            RED = False

        val = await client.read_gatt_char(GREEN_LED_UUID)
        if val == on_value:
            print('GREEN ON')
            GREEN = True
        else:
            print('GREEN OFF')
            GREEN = False

        val = await client.read_gatt_char(BLUE_LED_UUID)
        if val == on_value:
            print('BLUE ON')
            BLUE = True
        else:
            print('BLUE OFF')
            BLUE = False

        while True:
            try:
                await setColor(client)
            except KeyboardInterrupt:
                break


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(connect_and_write_led_characteristic())
