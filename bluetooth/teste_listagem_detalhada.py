import bluetooth

nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True,
                                            flush_cache=True, lookup_class=False)

print("Achado {} dispositivos".format(len(nearby_devices)))

services = []

for addr, name in nearby_devices:
    try:
        services.append(bluetooth.find_service(address=addr))
    except UnicodeEncodeError:
        continue
        
for s in services:
    for svc in s:
        try:
            print("\nService Name:", svc["name"])
        except UnicodeEncodeError:
            print("Erro")
        try:
            print("    Host:       ", svc["host"])
        except UnicodeEncodeError:
            print("Erro")
        try:
            print("    Description:", svc["description"])
        except UnicodeEncodeError:
            print("Erro")
        try:
            print("    Provided By:", svc["provider"])
        except UnicodeEncodeError:
            print("Erro")
        try:
            print("    Protocol:   ", svc["protocol"])
        except UnicodeEncodeError:
            print("Erro")
        try:
            print("    channel/PSM:", svc["port"])
        except UnicodeEncodeError:
            print("Erro")
        try:
            print("    svc classes:", svc["service-classes"])
        except UnicodeEncodeError:
            print("Erro")
        try:
            print("    profiles:   ", svc["profiles"])
        except UnicodeEncodeError:
            print("Erro")
        try:
            print("    service id: ", svc["service-id"])
        except UnicodeEncodeError:
            print("Erro")

        
        
        
        
        
        
        
        