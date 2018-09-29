import bluetooth
import select


class MyDiscoverer(bluetooth.DeviceDiscoverer):

    def pre_inquiry(self):
        self.done = False

    def device_discovered(self, address, device_class, rssi, name):
        print("%s - %s" % (address, name))

        # get some information out of the device class and display it.
        # voodoo magic specified at:
        #
        # https://www.bluetooth.org/foundry/assignnumb/document/baseband
        major_classes = ("Miscellaneous",
                         "Computer",
                         "Phone",
                         "LAN/Network Access point",
                         "Audio/Video",
                         "Peripheral",
                         "Imaging")
        print("major_classes", major_classes)
        major_class = (device_class >> 8) & 0xf
        print("major_class", major_class)
        if major_class < 7:
            print("  %s" % major_classes[major_class])
        else:
            print("  Uncategorized")

        print("  services:")
        service_classes = ((16, "positioning"),
                           (17, "networking"),
                           (18, "rendering"),
                           (19, "capturing"),
                           (20, "object transfer"),
                           (21, "audio"),
                           (22, "telephony"),
                           (23, "information"))

        for bitpos, classname in service_classes:
            if device_class & (1 << (bitpos-1)):
                print("    %s" % classname)
        print("  RSSI: " + str(rssi))

    def inquiry_complete(self):
        self.done = True


d = MyDiscoverer()
d.find_devices(lookup_names=True)

readfiles = [d, ]

while True:
    rfds = select.select(readfiles, [], [])[0]

    if d in rfds:
        d.process_event()

    if d.done:
        break
