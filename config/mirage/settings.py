self.include_builtin("config/settings.py")

class General:
    close_to_tray: bool = False
    tooltips_delay: float = 0.5
    theme: str = "Glass.qpl"
    zoom: float = 1.0

class Notifications:
    # - "enable" (notifications will work normally)
    # - "highlights_only" (notify only for highlights, e.g. replies, keywords)
    # - "mute" (don't notify for anything)
    start_level: str = "enable"

class Scrolling:
    kinetic: bool = False
    non_kinetic_speed: float = 2.0

class Keys:
    compact = ["Alt+Ctrl+C"]

    zoom_in    = ["Ctrl++"]
    zoom_out   = ["Ctrl+-"]
    reset_zoom = ["Ctrl+="]

    notifications_highlights_only = ["Ctrl+Alt+H"]
    notifications_mute = ["Ctrl+Alt+M"]

    previous_tab = ["Alt+Shift+Left", "Alt+Shift+H"]
    next_tab     = ["Alt+Shift+Right", "Alt+Shift+L"]

    class Scrolling:
        up        = ["Alt+Ctrl+Up", "Alt+Ctrl+K"]
        down      = ["Alt+Ctrl+Down", "Alt+Ctrl+J"]
        page_up   = ["Alt+Up", "Alt+K", "PgUp"]
        page_down = ["Alt+Down", "Alt+J", "PgDown"]
        top       = ["Alt+G"]
        bottom    = ["Ctrl+G"]

    class Rooms:
        focus_filter = ["Ctrl+F"]
    
    class Chat:
        focus_room_pane = ["Alt+R"]
        hide_room_pane = ["Alt+Shift+R"]

        invite = ["Alt+I"]
        leave  = ["Alt+Escape"]
        forget = ["Alt+Shift+Escape"]

        send_file = ["Ctrl+Shift+S"]
        send_clipboard_path = ["Ctrl+S"]

    class Messages:
        previous = ["Ctrl+Up", "Ctrl+K"]
        next     = ["Ctrl+Down", "Ctrl+J"]

        select = ["Ctrl+Space"]
        select_until_here = ["Ctrl+Shift+Space"]
        unfocus_or_deselect = ["Ctrl+D"]

        reply = ["Ctrl+Q"]
        open_links_files = ["Ctrl+O"]
        open_links_files_externally = ["Ctrl+Shift+O"]
        copy_files_path = ["Ctrl+Shift+C"]
        clear_all = ["Ctrl+Shift+P"]

    class Security:
        refresh = ["F5"]
        sign_out = ["Alt+Delete"]

