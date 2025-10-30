import bluetooth
# pip install git+https://github.com/pybluez/pybluez.git#egg=pybluez

print("Performing inquiry...")

nearby_devices = bluetooth.discover_devices(duration=15, lookup_names=True,
                                            flush_cache=True, lookup_class=False)

print("Found {} devices".format(len(nearby_devices)))

for addr, name in nearby_devices:
    try:
        print("   {} - {}".format(addr, name))
    except UnicodeEncodeError:
        print("   {} - {}".format(addr, name.encode("utf-8", "replace")))