# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os


# color shema 
color_light = "#eeeedd" 
color_black = "#111111"

color_primary = "#cc5555"
color_segundary = "#553333"
color_gray = "#888877"

color_segundary_dark = "#772222"
color_primary_dark = "#ff1111"

## parametros 
mod = "mod4"
terminal = "qterminal"


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),


    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes

    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # menu 
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Open Menu"),

    #screenshots 
    Key([mod],"s",lazy.spawn("scrot /home/nefasque/Imágenes/screenshots/%Y-%m-%d-%T-screenshot.png"), desc="Take screenshot"),
]

# group ----------------
__Groups = {
    1: Group(
        name ="term",
        layout = "MonadTall",
        label="",
    ), 
    2: Group(
        name = "www", 
        matches=[Match(wm_class=["firefox"])],
        label="󰀂"
    ), 
    3: Group(
        name = "dev", 
        label = ""
    ), 
    4: Group(
        name = "󰙯", 
        matches=[Match(wm_class=["discord"])],
        exclusive = True, 
        layout="max",
        persist=False, 
        init=False, 
    ),
    5: Group(
        name = "feh", 
        matches=[Match(wm_class=["feh"])],
        exclusive = True, 
        layout=max,
        persist=False, 
        init=False, 
        label = ""
    ),
    5: Group(
        name = "souns", 
        matches=[Match(wm_class=["audacious","shortwave"])],
        exclusive = True, 
        layout = "MonadTall",
        persist=False, 
        init=False, 
        label = ""
    )
}

# ---- regenarion de grupos 
groups = [ __Groups[i] for i in __Groups]

# ---- get la llave de grupo
def get_group_key(name): 
    return [k for k, g in __Groups.items() if g.name == name][0]

# ----> Key map Groups 
for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                 str(get_group_key(i.name)),
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),

            # mod1 + shift + letter of group = 
            # switch to & move focused window to group

            Key(
                [mod, "shift"],
                str(get_group_key(i.name)),
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

layouts = [
    layout.Columns(
        border_focus = color_segundary,
        border_focus_stack = color_primary_dark,
        border_normal = "#2f2f2f",
        border_width = 3,
        margin = 5,
        border_on_single = True, 
        grow_amount = 3,

    ),

    layout.Max(
        border_on_single = True, 
        border_focus = color_segundary,
        border_width = 3,
        margin = 5,
    ),

    layout.MonadTall(
        border_focus = color_segundary,
        border_width = 3,
        border_normal = "#2f2f2f", 
        margin = 5,
        border_on_single = True, 
        lower_right = False,
    ), 

    #layout.MonadWide(),
    #layout.RatioTile(),
    #layout.Tile(),
    #layout.TreeTab(),
    #layout.VerticalTile(),
    #layout.Zoomy(),
    #layout.Stack(num_stacks=2),
    #layout.Bsp(),
    #layout.Matrix(),
]

widget_defaults = dict(
    background= color_black,
    font="FiraCode Nerd Font",
    foregorund = color_light,
    fontsize=20,
    padding=5,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    borderwidth = 0,
                    padding = 20,
                    highlight_method="line",
                    highlight_color=["#000", "#000"],
                    block_highlight_text_color=color_primary,
                ),
                widget.Spacer(), 

                widget.Sep(padding = 20),
                widget.Systray(),
                widget.Volume(
                    fmt= '󰜟 {}',
                    fontsize = 18,
                    mouse_callbacks = {
                        "Button3": lazy.spawn("pavucontrol")  
                    }
                ),
                widget.Cmus(),
                widget.Clock(
                    font='Digital-7',
                    format="%I:%M",
                    fontsize = 24,
                    padding = 15, 
                ),
            ],
            24,
            # border_width=[10, 0, 10, 0],  # Draw top and bottom borders
            border_color=color_black, 
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"



# ---------- commands in init qtile 
autoStart = [
    "setxkbmap es", 
    "/home/nefasque/.config/qtile/ext_resolution.sh",
    "feh --bg-scale /home/nefasque/.config/qtile/wallpaper.jpg",
    "picom &",
    "sleep 1 && /usr/bin/lxpolkit &>/dev/null &"
]

for x in autoStart: 
    os.system(x)
