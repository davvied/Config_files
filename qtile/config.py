# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List  # noqa: F401

mod = "mod4"
# Terminal = guess_terminal()
Terminal = "alacritty"
Web_Browser = "firefox"
EmailClient = "thunderbird"
App_Launcher = "rofi -show-icons -show drun"
File_Manager = "nautilus"
Editer = "/usr/bin/emacsclient -c -a /usr/bin/emacs"
Display_Manager = "arandr"

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "control"], "h", lazy.layout.grow(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.shrink(), desc="Grow window to the left"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc='toggle floating'),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc='toggle fullscreen'),


    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "mod1"], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
    #     desc="Toggle between split and unsplit sides of stack",
    # ),
    # Key([mod], "w", lazy.to_screen(0), desc='Keyboard focus to monitor 1'),
    # Key([mod], "e", lazy.to_screen(1), desc='Keyboard focus to monitor 2'),
    # Key([mod], "r", lazy.to_screen(2), desc='Keyboard focus to monitor 3'),
         ### Switch focus of monitors
    Key([mod], "period", lazy.next_screen(), desc='Move focus to next monitor'),
    Key([mod], "comma", lazy.prev_screen(), desc='Move focus to prev monitor'),


    Key(["control", "shift"], "Left", lazy.spawn("amixer set Master 2%- -q"), desc="dec audio volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 2%- -q"), desc="dec audio volume"),
    Key(["control", "shift"], "Right", lazy.spawn("amixer set Master 2%+ -q"), desc="inc audio volume"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 2%+ -q"), desc="inc audio volume"),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle -q"), desc="Toggle audio on & off"),

    Key([mod], "Return", lazy.spawn(Terminal), desc="Launch terminal"),
    Key([mod], "t", lazy.spawn(Terminal), desc="Launch terminal"),

    Key([mod], "r", lazy.spawn(App_Launcher), desc="Spawn rofi app launcher"),
    Key([mod], "b", lazy.spawn(Web_Browser), desc="Spawn web browser"),
    Key([mod], "e", lazy.spawn(File_Manager), desc="Spawn file manager"),
    Key([mod], "w", lazy.spawn(Editer), desc="Spawn an editer"),
    Key([mod], "p", lazy.spawn("passmenu"), desc="password manager"),
    Key([mod, "shift"], "p", lazy.spawn(Display_Manager), desc="password manager"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

layouts = [
    layout.MonadTall(ratio=0.6,
                     **layout_theme),
    layout.Max(**layout_theme),
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.TreeTab(
         font = "Ubuntu",
         fontsize = 10,
         sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
         section_fontsize = 10,
         border_width = 2,
         bg_color = "1c1f24",
         active_bg = "c678dd",
         active_fg = "000000",
         inactive_bg = "a9a1e1",
         inactive_fg = "1c1f24",
         padding_left = 0,
         padding_x = 0,
         padding_y = 5,
         section_top = 10,
         section_bottom = 20,
         level_shift = 8,
         vspace = 3,
         panel_width = 200
         ),
    layout.Floating(**layout_theme)
]

colors = {"Black":         "#0c0c0d",
          "Gray":          "#282c34",
          "Dark_Red":      "#8C0102",
          "Red":           "#AE0505",
          "Light_Red":     "#E00506",
          "Blue_1":        "#1B788B",
          "Blue_2":        "#257D8D",
          "Blue_3":        "#208DA1",
          "Blue_Gray":     "#65959c",
          "Light_Blue":    "#91d5e0",
          }

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

widget_defaults = dict(
    # font="sans",
    font = "Ubuntu Bold",
    fontsize=14,
    padding=3,
    background = colors["Gray"],
    foreground = colors["Light_Blue"],
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.AGroupBox(
                    border = colors["Blue_1"],
                    borderwidth = 2,
                    center_aligned = True,
                    margin = 3,
                ),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.Bluetooth(),
                # widget.TextBox(
                #     "\ue0b6",
                #     fontsize = 18,
                #     padding = 0,
                # ),
                widget.CheckUpdates(
                    colour_have_updates = colors["Red"],
                    colour_no_updates = colors["Black"],
                    distro = 'Arch_paru',
                    no_update_string = 'Up to date',
                    update_interval = 600,
                    background = colors["Light_Blue"],
                ),
                # widget.TextBox(
                #     "\ue0b8",
                #     padding = 8,
                    # fontsize = 18,
                    # background = colors["Light_Blue"],
                    # foreground = colors["Gray"],
                # ),
                widget.OpenWeather(
                    cityid = 136256,
                ),
                # widget.TextBox(
                #     "\ue0bc",
                    # fontsize = 18,
                #     padding = 8,
                # ),
                widget.KeyboardLayout(
                    configured_keyboards = ['us', 'ir'],
                    background = colors["Light_Blue"],
                    foreground = colors["Black"],
                ),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.Systray(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        bottom=bar.Bar(
            [
                widget.GroupBox(
                    fontsize = 12,
                    active = colors["Red"],
                    block_highlight_text_color = colors["Blue_1"],
                ),
                # widget.Spacer(),
                widget.TaskList(
                    highlight_method = 'block',
                ),
            ],
            24,
        ),
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
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

@hook.subscribe.startup_once
def start_once():
# def autostart():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.local/Config_files/qtile/start_once.sh'])

@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.local/Config_files/qtile/autostart.sh'])

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
