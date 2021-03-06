# -*- coding: utf-8 -*-
"""
Master Plugin
Copyright (C) 2010-2012 Olaf Lüke <olaf@tinkerforge.com>
Copyright (C) 2014-2016 Matthias Bolte <matthias@tinkerforge.com>

master.py: Master Plugin implementation

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public
License along with this program; if not, write to the
Free Software Foundation, Inc., 59 Temple Place - Suite 330,
Boston, MA 02111-1307, USA.
"""

from PyQt4.QtCore import QTimer
from PyQt4.QtGui import QAction

from brickv.plugin_system.plugin_base import PluginBase
from brickv.plugin_system.plugins.master.ui_master import Ui_Master
from brickv.plugin_system.plugins.master.extension_type import ExtensionType
from brickv.plugin_system.plugins.master.chibi import Chibi
from brickv.plugin_system.plugins.master.rs485 import RS485
from brickv.plugin_system.plugins.master.wifi import Wifi
from brickv.plugin_system.plugins.master.ethernet import Ethernet
from brickv.plugin_system.plugins.master.wifi2 import Wifi2
from brickv.bindings.brick_master import BrickMaster
from brickv.async_call import async_call
from brickv import infos
from brickv.utils import get_main_window, format_current

class Master(PluginBase, Ui_Master):
    def __init__(self, *args):
        PluginBase.__init__(self, BrickMaster, *args)

        self.setupUi(self)

        self.master = self.device

        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_data)

        self.extension_type = None

        self.extensions = []
        self.num_extensions = 0

        self.extension_label.setText("None Present")
        self.tab_widget.removeTab(0)
        self.tab_widget.hide()

        if self.firmware_version >= (1, 1, 0):
            self.check_extensions = True
            self.extension_type_button.clicked.connect(self.extension_clicked)
        else:
            self.check_extensions = False
            self.extension_type_button.setEnabled(False)

        if self.firmware_version >= (1, 2, 1):
            reset = QAction('Reset', self)
            reset.triggered.connect(lambda: self.master.reset())
            self.set_actions(reset)

        self.extension_type_preset = [None, False, False, False, False, False]
        self.update_extensions_in_device_info()

    def update_extensions_in_device_info(self):
        def is_present_async(present, extension_type, name):
            self.extension_type_preset[extension_type] = present

            if present:
                if self.device_info.extensions['ext0'] == None:
                    ext = 'ext0'
                elif self.device_info.extensions['ext1'] == None:
                    ext = 'ext1'
                else:
                    return # This should never be the case

                self.device_info.extensions[ext] = infos.ExtensionInfo()
                self.device_info.extensions[ext].name = name
                self.device_info.extensions[ext].extension_type = extension_type
                self.device_info.extensions[ext].position = ext
                self.device_info.extensions[ext].master_info = self.device_info
                infos.update_info(self.uid)

                def get_wifi2_firmware_version_async(version, ext):
                    self.device_info.extensions[ext].firmware_version_installed = version
                    infos.update_info(self.uid)

                if extension_type == self.master.EXTENSION_TYPE_WIFI2:
                    self.device_info.extensions[ext].url_part = 'wifi_v2'
                    async_call(self.master.get_wifi2_firmware_version, None, lambda v: get_wifi2_firmware_version_async(v, ext), self.increase_error_count)

        def get_connection_type_async(connection_type):
            self.device_info.connection_type = connection_type
            infos.update_info(self.uid)

        if self.firmware_version >= (1, 1, 0):
            async_call(self.master.is_chibi_present, None, lambda p: is_present_async(p, self.master.EXTENSION_TYPE_CHIBI, 'Chibi Extension'), self.increase_error_count)

        if self.firmware_version >= (1, 2, 0):
            async_call(self.master.is_rs485_present, None, lambda p: is_present_async(p, self.master.EXTENSION_TYPE_RS485, 'RS485 Extension'), self.increase_error_count)

        if self.firmware_version >= (1, 3, 0):
            async_call(self.master.is_wifi_present, None, lambda p: is_present_async(p, self.master.EXTENSION_TYPE_WIFI, 'WIFI Extension'), self.increase_error_count)

        if self.firmware_version >= (2, 1, 0):
            async_call(self.master.is_ethernet_present, None, lambda p: is_present_async(p, self.master.EXTENSION_TYPE_ETHERNET, 'Ethernet Extension'), self.increase_error_count)

        if self.firmware_version >= (2, 4, 0):
            async_call(self.master.is_wifi2_present, None, lambda p: is_present_async(p, self.master.EXTENSION_TYPE_WIFI2, 'WIFI Extension 2.0'), self.increase_error_count)
            async_call(self.master.get_connection_type, None, get_connection_type_async, self.increase_error_count)

        async_call(lambda: None, None, lambda: get_main_window().update_tree_view(), None)

    def is_wifi2_present_async(self, present):
        if present:
            wifi2 = Wifi2(self)
            self.extensions.append(wifi2)
            self.tab_widget.addTab(wifi2, 'WIFI 2.0')
            self.tab_widget.show()
            self.num_extensions += 1
            self.extension_label.setText(str(self.num_extensions) + " Present")
            self.label_no_extension.hide()

    def is_ethernet_present_async(self, present):
        if present:
            ethernet = Ethernet(self)
            self.extensions.append(ethernet)
            self.tab_widget.addTab(ethernet, 'Ethernet')
            self.tab_widget.show()
            self.num_extensions += 1
            self.extension_label.setText(str(self.num_extensions) + " Present")
            self.label_no_extension.hide()

    def is_wifi_present_async(self, present):
        if present:
            wifi = Wifi(self)
            self.extensions.append(wifi)
            self.tab_widget.addTab(wifi, 'WIFI')
            self.tab_widget.show()
            self.num_extensions += 1
            self.extension_label.setText(str(self.num_extensions) + " Present")
            self.label_no_extension.hide()

    def is_rs485_present_async(self, present):
        if present:
            rs485 = RS485(self)
            self.extensions.append(rs485)
            self.tab_widget.addTab(rs485, 'RS485')
            self.tab_widget.show()
            self.num_extensions += 1
            self.extension_label.setText(str(self.num_extensions) + " Present")
            self.label_no_extension.hide()

    def is_chibi_present_async(self, present):
        if present:
            chibi = Chibi(self)
            self.extensions.append(chibi)
            self.tab_widget.addTab(chibi, 'Chibi')
            self.tab_widget.show()
            self.num_extensions += 1
            self.extension_label.setText(str(self.num_extensions) + " Present")
            self.label_no_extension.hide()

    def start(self):
        if self.check_extensions:
            self.check_extensions = False

            self.is_chibi_present_async(self.extension_type_preset[self.master.EXTENSION_TYPE_CHIBI])
            self.is_rs485_present_async(self.extension_type_preset[self.master.EXTENSION_TYPE_RS485])
            self.is_wifi_present_async(self.extension_type_preset[self.master.EXTENSION_TYPE_WIFI])
            self.is_ethernet_present_async(self.extension_type_preset[self.master.EXTENSION_TYPE_ETHERNET])
            self.is_wifi2_present_async(self.extension_type_preset[self.master.EXTENSION_TYPE_WIFI2])

        self.update_timer.start(1000)

    def stop(self):
        self.update_timer.stop()

    def destroy(self):
        for extension in self.extensions:
            extension.destroy()
            extension.hide()
            extension.setParent(None)

        self.extensions = []

        if self.extension_type:
            self.extension_type.close()

    def is_hardware_version_relevant(self):
        return True

    def get_url_part(self):
        return 'master'

    @staticmethod
    def has_device_identifier(device_identifier):
        return device_identifier == BrickMaster.DEVICE_IDENTIFIER

    def update_data(self):
        async_call(self.master.get_stack_voltage, None, self.get_stack_voltage_async, self.increase_error_count)
        async_call(self.master.get_stack_current, None, self.get_stack_current_async, self.increase_error_count)

        for extension in self.extensions:
            extension.update_data()

    def get_stack_voltage_async(self, voltage):
        self.stack_voltage_label.setText('{:g} V'.format(round(voltage / 1000.0, 1)))

    def get_stack_current_async(self, current):
        self.stack_current_label.setText(format_current(current / 1000.0))

    def extension_clicked(self):
        if self.extension_type is None:
            self.extension_type = ExtensionType(self)

        self.extension_type.show()
