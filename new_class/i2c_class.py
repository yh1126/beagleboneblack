import smbus

class I2cClass(object):

    def __init__(self, address, bus=1):
        self.i2c = smbus.SMBus(bus)
        self.address = address

    def read_byte(self):
        return self.i2c.read_byte(address)

    def read_byte_data(self, cmd):
        return self.i2c.read_byte_data(self.address, cmd)

    def read_block_data(self, cmd, blocks):
        return self.i2c.read_block_data(self.address, cmd, blocks)

    def write_quick(self):
        self.i2c.write_quick()

    def write_byte(self, value):
        self.i2c.write_byte(self.address, value)

    def write_byte_data(self, cmd, value):
        self.i2c.write_byte_data(self.address, cmd, value)

    def write_word_data(self, cmd, value):
        self.i2c.write_word_data(self.address, cmd, value)

    def process_call(self, cmd, value):
        self.i2c.process_call(self.address, cmd, value)

    def exception_method(self):
        print("exception_method")
