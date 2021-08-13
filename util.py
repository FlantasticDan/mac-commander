def normalize_mac_address(mac_address: str, display=True) -> str:
    mac_address = mac_address.lower()
    if display:
        return mac_address.replace('-', ":")
    return mac_address.replace(':', '-')
