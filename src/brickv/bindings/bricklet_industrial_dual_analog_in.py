# -*- coding: utf-8 -*-
#############################################################
# This file was automatically generated on 2016-05-31.      #
#                                                           #
# Python Bindings Version 2.1.9                             #
#                                                           #
# If you have a bugfix for this file and want to commit it, #
# please fix the bug in the generator. You can find a link  #
# to the generators git repository on tinkerforge.com       #
#############################################################

try:
    from collections import namedtuple
except ImportError:
    try:
        from .ip_connection import namedtuple
    except ValueError:
        from ip_connection import namedtuple

try:
    from .ip_connection import Device, IPConnection, Error
except ValueError:
    from ip_connection import Device, IPConnection, Error

GetVoltageCallbackThreshold = namedtuple('VoltageCallbackThreshold', ['option', 'min', 'max'])
GetCalibration = namedtuple('Calibration', ['offset', 'gain'])
GetIdentity = namedtuple('Identity', ['uid', 'connected_uid', 'position', 'hardware_version', 'firmware_version', 'device_identifier'])

class BrickletIndustrialDualAnalogIn(Device):
    """
    Measures two DC voltages between -35V and +35V with 24bit resolution each
    """

    DEVICE_IDENTIFIER = 249
    DEVICE_DISPLAY_NAME = 'Industrial Dual Analog In Bricklet'

    CALLBACK_VOLTAGE = 13
    CALLBACK_VOLTAGE_REACHED = 14

    FUNCTION_GET_VOLTAGE = 1
    FUNCTION_SET_VOLTAGE_CALLBACK_PERIOD = 2
    FUNCTION_GET_VOLTAGE_CALLBACK_PERIOD = 3
    FUNCTION_SET_VOLTAGE_CALLBACK_THRESHOLD = 4
    FUNCTION_GET_VOLTAGE_CALLBACK_THRESHOLD = 5
    FUNCTION_SET_DEBOUNCE_PERIOD = 6
    FUNCTION_GET_DEBOUNCE_PERIOD = 7
    FUNCTION_SET_SAMPLE_RATE = 8
    FUNCTION_GET_SAMPLE_RATE = 9
    FUNCTION_SET_CALIBRATION = 10
    FUNCTION_GET_CALIBRATION = 11
    FUNCTION_GET_ADC_VALUES = 12
    FUNCTION_GET_IDENTITY = 255

    THRESHOLD_OPTION_OFF = 'x'
    THRESHOLD_OPTION_OUTSIDE = 'o'
    THRESHOLD_OPTION_INSIDE = 'i'
    THRESHOLD_OPTION_SMALLER = '<'
    THRESHOLD_OPTION_GREATER = '>'
    SAMPLE_RATE_976_SPS = 0
    SAMPLE_RATE_488_SPS = 1
    SAMPLE_RATE_244_SPS = 2
    SAMPLE_RATE_122_SPS = 3
    SAMPLE_RATE_61_SPS = 4
    SAMPLE_RATE_4_SPS = 5
    SAMPLE_RATE_2_SPS = 6
    SAMPLE_RATE_1_SPS = 7

    def __init__(self, uid, ipcon):
        """
        Creates an object with the unique device ID *uid* and adds it to
        the IP Connection *ipcon*.
        """
        Device.__init__(self, uid, ipcon)

        self.api_version = (2, 0, 0)

        self.response_expected[BrickletIndustrialDualAnalogIn.FUNCTION_GET_VOLTAGE] = BrickletIndustrialDualAnalogIn.RESPONSE_EXPECTED_ALWAYS_TRUE
        self.response_expected[BrickletIndustrialDualAnalogIn.FUNCTION_SET_VOLTAGE_CALLBACK_PERIOD] = BrickletIndustrialDualAnalogIn.RESPONSE_EXPECTED_TRUE
        self.response_expected[BrickletIndustrialDualAnalogIn.FUNCTION_GET_VOLTAGE_CALLBACK_PERIOD] = BrickletIndustrialDualAnalogIn.RESPONSE_EXPECTED_ALWAYS_TRUE
        self.response_expected[BrickletIndustrialDualAnalogIn.FUNCTION_SET_VOLTAGE_CALLBACK_THRESHOLD] = BrickletIndustrialDualAnalogIn.RESPONSE_EXPECTED_TRUE
        self.response_expected[BrickletIndustrialDualAnalogIn.FUNCTION_GET_VOLTAGE_CALLBACK_THRESHOLD] = BrickletIndustrialDualAnalogIn.RESPONSE_EXPECTED_ALWAYS_TRUE
        self.response_expected[BrickletIndustrialDualAnalogIn.FUNCTION_SET_DEBOUNCE_PERIOD] = BrickletIndustrialDualAnalogIn.RESPONSE_EXPECTED_TRUE
        self.response_expected[BrickletIndustrialDualAnalogIn.FUNCTION_GET_DEBOUNCE_PERIOD] = BrickletIndustrialDualAnalogIn.RESPONSE_EXPECTED_ALWAYS_TRUE
        self.response_expected[BrickletIndustrialDualAnalogIn.FUNCTION_SET_SAMPLE_RATE] = BrickletIndustrialDualAnalogIn.RESPONSE_EXPECTED_FALSE
        self.response_expected[BrickletIndustrialDualAnalogIn.FUNCTION_GET_SAMPLE_RATE] = BrickletIndustrialDualAnalogIn.RESPONSE_EXPECTED_ALWAYS_TRUE
        self.response_expected[BrickletIndustrialDualAnalogIn.FUNCTION_SET_CALIBRATION] = BrickletIndustrialDualAnalogIn.RESPONSE_EXPECTED_FALSE
        self.response_expected[BrickletIndustrialDualAnalogIn.FUNCTION_GET_CALIBRATION] = BrickletIndustrialDualAnalogIn.RESPONSE_EXPECTED_ALWAYS_TRUE
        self.response_expected[BrickletIndustrialDualAnalogIn.FUNCTION_GET_ADC_VALUES] = BrickletIndustrialDualAnalogIn.RESPONSE_EXPECTED_ALWAYS_TRUE
        self.response_expected[BrickletIndustrialDualAnalogIn.CALLBACK_VOLTAGE] = BrickletIndustrialDualAnalogIn.RESPONSE_EXPECTED_ALWAYS_FALSE
        self.response_expected[BrickletIndustrialDualAnalogIn.CALLBACK_VOLTAGE_REACHED] = BrickletIndustrialDualAnalogIn.RESPONSE_EXPECTED_ALWAYS_FALSE
        self.response_expected[BrickletIndustrialDualAnalogIn.FUNCTION_GET_IDENTITY] = BrickletIndustrialDualAnalogIn.RESPONSE_EXPECTED_ALWAYS_TRUE

        self.callback_formats[BrickletIndustrialDualAnalogIn.CALLBACK_VOLTAGE] = 'B i'
        self.callback_formats[BrickletIndustrialDualAnalogIn.CALLBACK_VOLTAGE_REACHED] = 'B i'

    def get_voltage(self, channel):
        """
        Returns the voltage for the given channel in mV.
        
        If you want to get the voltage periodically, it is recommended to use the
        callback :func:`Voltage` and set the period with 
        :func:`SetVoltageCallbackPeriod`.
        """
        return self.ipcon.send_request(self, BrickletIndustrialDualAnalogIn.FUNCTION_GET_VOLTAGE, (channel,), 'B', 'i')

    def set_voltage_callback_period(self, channel, period):
        """
        Sets the period in ms with which the :func:`Voltage` callback is triggered
        periodically for the given channel. A value of 0 turns the callback off.
        
        :func:`Voltage` is only triggered if the voltage has changed since the
        last triggering.
        
        The default value is 0.
        """
        self.ipcon.send_request(self, BrickletIndustrialDualAnalogIn.FUNCTION_SET_VOLTAGE_CALLBACK_PERIOD, (channel, period), 'B I', '')

    def get_voltage_callback_period(self, channel):
        """
        Returns the period as set by :func:`SetVoltageCallbackPeriod`.
        """
        return self.ipcon.send_request(self, BrickletIndustrialDualAnalogIn.FUNCTION_GET_VOLTAGE_CALLBACK_PERIOD, (channel,), 'B', 'I')

    def set_voltage_callback_threshold(self, channel, option, min, max):
        """
        Sets the thresholds for the :func:`VoltageReached` callback for the given
        channel.
        
        The following options are possible:
        
        .. csv-table::
         :header: "Option", "Description"
         :widths: 10, 100
        
         "'x'",    "Callback is turned off"
         "'o'",    "Callback is triggered when the voltage is *outside* the min and max values"
         "'i'",    "Callback is triggered when the voltage is *inside* the min and max values"
         "'<'",    "Callback is triggered when the voltage is smaller than the min value (max is ignored)"
         "'>'",    "Callback is triggered when the voltage is greater than the min value (max is ignored)"
        
        The default value is ('x', 0, 0).
        """
        self.ipcon.send_request(self, BrickletIndustrialDualAnalogIn.FUNCTION_SET_VOLTAGE_CALLBACK_THRESHOLD, (channel, option, min, max), 'B c i i', '')

    def get_voltage_callback_threshold(self, channel):
        """
        Returns the threshold as set by :func:`SetVoltageCallbackThreshold`.
        """
        return GetVoltageCallbackThreshold(*self.ipcon.send_request(self, BrickletIndustrialDualAnalogIn.FUNCTION_GET_VOLTAGE_CALLBACK_THRESHOLD, (channel,), 'B', 'c i i'))

    def set_debounce_period(self, debounce):
        """
        Sets the period in ms with which the threshold callback
        
        * :func:`VoltageReached`
        
        is triggered, if the threshold
        
        * :func:`SetVoltageCallbackThreshold`
        
        keeps being reached.
        
        The default value is 100.
        """
        self.ipcon.send_request(self, BrickletIndustrialDualAnalogIn.FUNCTION_SET_DEBOUNCE_PERIOD, (debounce,), 'I', '')

    def get_debounce_period(self):
        """
        Returns the debounce period as set by :func:`SetDebouncePeriod`.
        """
        return self.ipcon.send_request(self, BrickletIndustrialDualAnalogIn.FUNCTION_GET_DEBOUNCE_PERIOD, (), '', 'I')

    def set_sample_rate(self, rate):
        """
        Sets the sample rate. The sample rate can be between 1 sample per second
        and 976 samples per second. Decreasing the sample rate will also decrease the
        noise on the data.
        
        The default value is 6 (2 samples per second).
        """
        self.ipcon.send_request(self, BrickletIndustrialDualAnalogIn.FUNCTION_SET_SAMPLE_RATE, (rate,), 'B', '')

    def get_sample_rate(self):
        """
        Returns the sample rate as set by :func:`SetSampleRate`.
        """
        return self.ipcon.send_request(self, BrickletIndustrialDualAnalogIn.FUNCTION_GET_SAMPLE_RATE, (), '', 'B')

    def set_calibration(self, offset, gain):
        """
        Sets offset and gain of MCP3911 internal calibration registers.
        
        See MCP3911 datasheet 7.7 and 7.8. The Industrial Dual Analog In Bricklet
        is already factory calibrated by Tinkerforge. It should not be necessary
        for you to use this function
        """
        self.ipcon.send_request(self, BrickletIndustrialDualAnalogIn.FUNCTION_SET_CALIBRATION, (offset, gain), '2i 2i', '')

    def get_calibration(self):
        """
        Returns the calibration as set by :func:`SetCalibration`.
        """
        return GetCalibration(*self.ipcon.send_request(self, BrickletIndustrialDualAnalogIn.FUNCTION_GET_CALIBRATION, (), '', '2i 2i'))

    def get_adc_values(self):
        """
        Returns the ADC values as given by the MCP3911 IC. This function
        is needed for proper calibration, see :func:`SetCalibration`.
        """
        return self.ipcon.send_request(self, BrickletIndustrialDualAnalogIn.FUNCTION_GET_ADC_VALUES, (), '', '2i')

    def get_identity(self):
        """
        Returns the UID, the UID where the Bricklet is connected to, 
        the position, the hardware and firmware version as well as the
        device identifier.
        
        The position can be 'a', 'b', 'c' or 'd'.
        
        The device identifier numbers can be found :ref:`here <device_identifier>`.
        |device_identifier_constant|
        """
        return GetIdentity(*self.ipcon.send_request(self, BrickletIndustrialDualAnalogIn.FUNCTION_GET_IDENTITY, (), '', '8s 8s c 3B 3B H'))

    def register_callback(self, id, callback):
        """
        Registers a callback with ID *id* to the function *callback*.
        """
        self.registered_callbacks[id] = callback

IndustrialDualAnalogIn = BrickletIndustrialDualAnalogIn # for backward compatibility
