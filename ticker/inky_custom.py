<<<<<<< HEAD
import numpy
from inky.inky_ssd1608 import Inky, CS0_PIN, DC_PIN, RESET_PIN, BUSY_PIN
from inky import ssd1608


WHITE = 0
BLACK = 1
RED = YELLOW = 2

class Inky_SSD1608_Fast(Inky):
    """Inky pHAT V2 (250x122 pixel) e-Ink Display Driver."""
    WHITE = 0
    BLACK = 1
    RED = 2
    YELLOW = 2

    def __init__(
        self,
        resolution=(250, 122),
        colour="black",
        cs_pin=CS0_PIN,
        dc_pin=DC_PIN,
        reset_pin=RESET_PIN,
        busy_pin=BUSY_PIN,
        h_flip=False,
        v_flip=False,
        spi_bus=None,
        i2c_bus=None,
        gpio=None,
    ):

        super().__init__(
            resolution,
            colour,
            cs_pin,
            dc_pin,
            reset_pin,
            busy_pin,
            h_flip,
            v_flip,
            spi_bus,
            i2c_bus,
            gpio,
        )

        # Default
        self._luts = {
            "black": [
                0x02, 0x02, 0x01, 0x11, 0x12, 0x12, 0x22, 0x22, 0x66, 0x69,
                0x69, 0x59, 0x58, 0x99, 0x99, 0x88, 0x00, 0x00, 0x00, 0x00,
                0xF8, 0xB4, 0x13, 0x51, 0x35, 0x51, 0x51, 0x19, 0x01, 0x00,
            ],
            "red": [
                0x02, 0x02, 0x01, 0x11, 0x12, 0x12, 0x22, 0x22, 0x66, 0x69,
                0x69, 0x59, 0x58, 0x99, 0x99, 0x88, 0x00, 0x00, 0x00, 0x00,
                0xF8, 0xB4, 0x13, 0x51, 0x35, 0x51, 0x51, 0x19, 0x01, 0x00,
            ],
            "yellow": [
                0x02, 0x02, 0x01, 0x11, 0x12, 0x12, 0x22, 0x22, 0x66, 0x69,
                0x69, 0x59, 0x58, 0x99, 0x99, 0x88, 0x00, 0x00, 0x00, 0x00,
                0xF8, 0xB4, 0x13, 0x51, 0x35, 0x51, 0x51, 0x19, 0x01, 0x00,
            ],
        }
        # TODO: Find better values
        # TODO: Clean from time to time

    def show_stay_awake(self, busy_wait=True):
        """Show buffer on display.
        :param busy_wait: If True, wait for display update to finish before returning.
        """
        region = self.buf

        if self.v_flip:
            region = numpy.fliplr(region)

        if self.h_flip:
            region = numpy.flipud(region)

        if self.rotation:
            region = numpy.rot90(region, self.rotation // 90)

        buf_a = numpy.packbits(numpy.where(region == BLACK, 0, 1)).tolist()
        # buf_b = numpy.packbits(numpy.where(region == RED, 1, 0)).tolist()

        self._update_stay_awake(buf_a, busy_wait=busy_wait)


    def _update_stay_awake(self, buf_a, busy_wait=True):
        """Update display.
        Dispatches display update to correct driver.
        :param buf_a: Black/White pixels
        :param buf_b: Yellow/Red pixels
        """
        self.setup()

        self._send_command(ssd1608.DRIVER_CONTROL, [self.rows - 1, (self.rows - 1) >> 8, 0x00])
        # Set dummy line period
        self._send_command(ssd1608.WRITE_DUMMY, [0x1B])
        # Set Line Width
        self._send_command(ssd1608.WRITE_GATELINE, [0x0B])
        # Data entry squence (scan direction leftward and downward)
        self._send_command(ssd1608.DATA_MODE, [0x03])
        # Set ram X start and end position
        xposBuf = [0x00, self.cols // 8 - 1]
        self._send_command(ssd1608.SET_RAMXPOS, xposBuf)
        # Set ram Y start and end position
        yposBuf = [0x00, 0x00, (self.rows - 1) & 0xFF, (self.rows - 1) >> 8]
        self._send_command(ssd1608.SET_RAMYPOS, yposBuf)
        # VCOM Voltage
        self._send_command(ssd1608.WRITE_VCOM, [0x70])
        # Write LUT DATA
        self._send_command(ssd1608.WRITE_LUT, self._luts[self.lut])

        if self.border_colour == self.BLACK:
            self._send_command(ssd1608.WRITE_BORDER, 0b00000000)
            # GS Transition + Waveform 00 + GSA 0 + GSB 0
        elif self.border_colour == self.RED and self.colour == 'red':
            self._send_command(ssd1608.WRITE_BORDER, 0b00000110)
            # GS Transition + Waveform 01 + GSA 1 + GSB 0
        elif self.border_colour == self.YELLOW and self.colour == 'yellow':
            self._send_command(ssd1608.WRITE_BORDER, 0b00001111)
            # GS Transition + Waveform 11 + GSA 1 + GSB 1
        elif self.border_colour == self.WHITE:
            self._send_command(ssd1608.WRITE_BORDER, 0b00000001)
            # GS Transition + Waveform 00 + GSA 0 + GSB 1

        # Set RAM address to 0, 0
        self._send_command(ssd1608.SET_RAMXCOUNT, [0x00])
        self._send_command(ssd1608.SET_RAMYCOUNT, [0x00, 0x00])

        self._send_command(ssd1608.WRITE_RAM, buf_a)

        self._busy_wait()
        self._send_command(ssd1608.MASTER_ACTIVATE)
=======
from inky.inky_ssd1608 import Inky

>>>>>>> af9f8f8908e2a487b800f8f2d1de648dee0874cc
