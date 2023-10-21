
import re
def is_valid_hex_color(color):
    return re.match(r'^#[0-9a-fA-f]{6}$', color) is not None

