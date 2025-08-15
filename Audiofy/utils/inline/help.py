# ---------------------------------------------------------
# Audify Bot - All rights reserved
# ---------------------------------------------------------
# This code is part of the Audify Bot project.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.
# ---------------------------------------------------------

from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Audify import app

# First help panel with page 1
def help_pannel(_, START: Union[bool, int] = None):
    nav_footer = [
        InlineKeyboardButton(text=_["H_B_N"], callback_data="help_callback page2"),
        InlineKeyboardButton(
            text=_["BACK_BUTTON"] if START else _["CLOSE_BUTTON"],
            callback_data="settingsback_helper" if START else "close"
        )
    ]
    buttons = [
        [InlineKeyboardButton(text=_["H_B_1"], callback_data="help_callback hb1"),
         InlineKeyboardButton(text=_["H_B_2"], callback_data="help_callback hb2"),
         InlineKeyboardButton(text=_["H_B_3"], callback_data="help_callback hb3")],
        [InlineKeyboardButton(text=_["H_B_4"], callback_data="help_callback hb4"),
         InlineKeyboardButton(text=_["H_B_5"], callback_data="help_callback hb5"),
         InlineKeyboardButton(text=_["H_B_6"], callback_data="help_callback hb6")],
        [InlineKeyboardButton(text=_["H_B_7"], callback_data="help_callback hb7"),
         InlineKeyboardButton(text=_["H_B_8"], callback_data="help_callback hb8"),
         InlineKeyboardButton(text=_["H_B_9"], callback_data="help_callback hb9")],
        [InlineKeyboardButton(text=_["H_B_10"], callback_data="help_callback hb10"),
         InlineKeyboardButton(text=_["H_B_11"], callback_data="help_callback hb11"),
         InlineKeyboardButton(text=_["H_B_12"], callback_data="help_callback hb12")],
        [InlineKeyboardButton(text=_["H_B_13"], callback_data="help_callback hb13"),
         InlineKeyboardButton(text=_["H_B_14"], callback_data="help_callback hb14"),
         InlineKeyboardButton(text=_["H_B_15"], callback_data="help_callback hb15")],
        nav_footer
    ]
    return InlineKeyboardMarkup(buttons)

# Page 2 help panel
def help_pannel_page2(_):
    nav_footer = [
        InlineKeyboardButton(text=_["H_B_P"], callback_data="help_callback page1"),
        InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="settingsback_helper"),
        InlineKeyboardButton(text=_["H_B_N"], callback_data="help_callback page3"),
    ]
    buttons = [
        [InlineKeyboardButton(text=_["H_B_16"], callback_data="help_callback hb16"),
         InlineKeyboardButton(text=_["H_B_17"], callback_data="help_callback hb17"),
         InlineKeyboardButton(text=_["H_B_18"], callback_data="help_callback hb18")],
        [InlineKeyboardButton(text=_["H_B_19"], callback_data="help_callback hb19"),
         InlineKeyboardButton(text=_["H_B_20"], callback_data="help_callback hb20"),
         InlineKeyboardButton(text=_["H_B_21"], callback_data="help_callback hb21")],
        [InlineKeyboardButton(text=_["H_B_22"], callback_data="help_callback hb22"),
         InlineKeyboardButton(text=_["H_B_23"], callback_data="help_callback hb23"),
         InlineKeyboardButton(text=_["H_B_24"], callback_data="help_callback hb24")],
        [InlineKeyboardButton(text=_["H_B_25"], callback_data="help_callback hb25"),
         InlineKeyboardButton(text=_["H_B_26"], callback_data="help_callback hb26"),
         InlineKeyboardButton(text=_["H_B_27"], callback_data="help_callback hb27")],
        [InlineKeyboardButton(text=_["H_B_28"], callback_data="help_callback hb28"),
         InlineKeyboardButton(text=_["H_B_29"], callback_data="help_callback hb29"),
         InlineKeyboardButton(text=_["H_B_30"], callback_data="help_callback hb30")],
        nav_footer
    ]
    return InlineKeyboardMarkup(buttons)

# Page 3 help panel
def help_pannel_page3(_):
    nav_footer = [
        InlineKeyboardButton(text=_["H_B_P"], callback_data="help_callback page2"),
        InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="settingsback_helper"),
        InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
    ]
    buttons = [
        [InlineKeyboardButton(text=_["H_B_31"], callback_data="help_callback hb31"),
         InlineKeyboardButton(text=_["H_B_32"], callback_data="help_callback hb32"),
         InlineKeyboardButton(text=_["H_B_33"], callback_data="help_callback hb33")],
        [InlineKeyboardButton(text=_["H_B_34"], callback_data="help_callback hb34"),
         InlineKeyboardButton(text=_["H_B_35"], callback_data="help_callback hb35"),
         InlineKeyboardButton(text=_["H_B_36"], callback_data="help_callback hb36")],
        [InlineKeyboardButton(text=_["H_B_37"], callback_data="help_callback hb37"),
         InlineKeyboardButton(text=_["H_B_38"], callback_data="help_callback hb38"),
         InlineKeyboardButton(text=_["H_B_39"], callback_data="help_callback hb39")],
        [InlineKeyboardButton(text=_["H_B_40"], callback_data="help_callback hb40"),
         InlineKeyboardButton(text=_["H_B_41"], callback_data="help_callback hb41"),
         InlineKeyboardButton(text=_["H_B_42"], callback_data="help_callback hb42")],
        [InlineKeyboardButton(text=_["H_B_43"], callback_data="help_callback hb43"),
         InlineKeyboardButton(text=_["H_B_44"], callback_data="help_callback hb44"),
         InlineKeyboardButton(text=_["H_B_45"], callback_data="help_callback hb45")],
        [InlineKeyboardButton(text=_["H_B_46"], callback_data="help_callback hb46"),
         InlineKeyboardButton(text=_["H_B_47"], callback_data="help_callback hb47"),
         InlineKeyboardButton(text=_["H_B_48"], callback_data="help_callback hb48")],
        nav_footer
    ]
    return InlineKeyboardMarkup(buttons)

# ✅ FIXED: Back button for help submenus (handles string input like 'hb23')
def help_back_markup(_, module_number: str):
    try:
        # Extract number from string like 'hb23'
        num = int(''.join(filter(str.isdigit, str(module_number))))
    except ValueError:
        num = 1  # fallback default

    if 1 <= num <= 15:
        callback = "help_callback page1"
    elif 16 <= num <= 30:
        callback = "help_callback page2"
    elif 31 <= num <= 50:
        callback = "help_callback page3"
    else:
        callback = "help_callback page1"

    return InlineKeyboardMarkup([
        [InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data=callback)]
    ])

# Private help panel button
def private_help_panel(_):
    return [[
        InlineKeyboardButton(text=_["S_B_4"], url=f"https://t.me/{app.username}?start=help")
    ]]
