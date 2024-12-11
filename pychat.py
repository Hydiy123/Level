import ctypes
from ctypes import wintypes

# Constants for window styles and show commands
WS_OVERLAPPEDWINDOW = 0x00CF0000
CW_USEDEFAULT = 0x80000000
SW_SHOW = 5

# Define the function prototype for the window procedure
WindowProc = ctypes.WINFUNCTYPE(
    ctypes.c_long,      # Return type
    wintypes.HWND,      # Handle to the window
    wintypes.UINT,      # Message ID
    wintypes.WPARAM,    # WPARAM (pointer-sized)
    wintypes.LPARAM,    # LPARAM (pointer-sized)
)

class PyChat:
    def __init__(self):
        self._title = "PyChat Window"  # Default title
        self._width = 800
        self._height = 600

        # Wrap the window_proc in the correct function type
        self.window_proc = WindowProc(self._window_proc)

    def title(self, title):  # Method to set the title
        """Set the window title."""
        self._title = title
        return self  # Enable chaining

    def size(self, width, height):
        """Set the window size."""
        self._width = width
        self._height = height
        return self  # Enable chaining

    def create_window(self):
        """Creates and displays the window."""
        hinstance = ctypes.windll.kernel32.GetModuleHandleW(None)

        # Define WNDCLASS structure using ctypes
        class WNDCLASS(ctypes.Structure):
            _fields_ = [
                ("style", wintypes.UINT),
                ("lpfnWndProc", WindowProc),
                ("cbClsExtra", wintypes.INT),
                ("cbWndExtra", wintypes.INT),
                ("hInstance", wintypes.HINSTANCE),
                ("hIcon", wintypes.HICON),
                ("hCursor", ctypes.POINTER(wintypes.HANDLE)),
                ("hbrBackground", wintypes.HBRUSH),
                ("lpszMenuName", wintypes.LPCWSTR),
                ("lpszClassName", wintypes.LPCWSTR),
            ]

        # Create the window class
        wndclass = WNDCLASS()
        wndclass.lpfnWndProc = self.window_proc  # Correctly set the function pointer
        wndclass.hInstance = hinstance
        wndclass.lpszClassName = "PyChatClass"
        wndclass.hbrBackground = ctypes.windll.user32.GetSysColorBrush(15)  # Corrected to use user32

        # Register the window class
        ctypes.windll.user32.RegisterClassW(ctypes.byref(wndclass))

        # Create the window
        hwnd = ctypes.windll.user32.CreateWindowExW(
            0,
            wndclass.lpszClassName,
            self._title,
            WS_OVERLAPPEDWINDOW,
            CW_USEDEFAULT,
            CW_USEDEFAULT,
            self._width,
            self._height,
            None,
            None,
            hinstance,
            None,
        )

        # Show the window
        ctypes.windll.user32.ShowWindow(hwnd, SW_SHOW)
        ctypes.windll.user32.UpdateWindow(hwnd)

        # Main message loop
        msg = wintypes.MSG()
        while ctypes.windll.user32.GetMessageW(ctypes.byref(msg), None, 0, 0) > 0:
            ctypes.windll.user32.TranslateMessage(ctypes.byref(msg))
            ctypes.windll.user32.DispatchMessageW(ctypes.byref(msg))

        return msg.wParam

    def _window_proc(self, hwnd, msg, wparam, lparam):
        """Callback function for handling window messages."""
        if msg == 0x0010:  # WM_CLOSE
            ctypes.windll.user32.PostQuitMessage(0)
            return 0

        # Explicitly cast wparam and lparam to ctypes-compatible types
        wparam = ctypes.c_void_p(wparam)  # WPARAM is a pointer-sized value
        lparam = ctypes.c_void_p(lparam)  # LPARAM is also a pointer-sized value

        return ctypes.windll.user32.DefWindowProcW(hwnd, msg, wparam, lparam)
