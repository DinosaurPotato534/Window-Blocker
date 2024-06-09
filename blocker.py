import time
import tkinter as tk
from tkinter import ttk
import pygetwindow as gw
import threading
import sv_ttk

chrome_apps_to_close = []
windows_to_close = []

keep_running = False
thread = None

def add_chrome_tab():
    tab = chrome_entry.get()
    if tab:
        chrome_apps_to_close.append(tab.lower())
        chrome_listbox.insert(tk.END, tab)
        chrome_entry.delete(0, tk.END)

def remove_chrome_tab():
    selected_index = chrome_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        chrome_apps_to_close.pop(index)
        chrome_listbox.delete(index)

def add_window():
    window_name = window_entry.get()
    if window_name:
        windows_to_close.append(window_name.lower())
        window_listbox.insert(tk.END, window_name)
        window_entry.delete(0, tk.END)

def remove_window():
    selected_index = window_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        windows_to_close.pop(index)
        window_listbox.delete(index)

def toggle_checking_windows():
    global keep_running, thread
    if not keep_running:
        keep_running = True
        start_button.config(state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL)
        thread = threading.Thread(target=check_windows)
        thread.start()
    else:
        keep_running = False
        start_button.config(state=tk.NORMAL)
        stop_button.config(state=tk.DISABLED)

def check_windows():
    try:
        while keep_running:
            active_window = gw.getActiveWindow()
            active_window_title = active_window.title.lower() if active_window else None
            print("Active Window:", active_window_title)

            if active_window_title is not None and "chrome" in active_window_title:
                for app in chrome_apps_to_close:
                    if app in active_window_title:
                        chrome_windows = [window for window in gw.getWindowsWithTitle(app)]
                        for chrome_window in chrome_windows:
                            chrome_window.close()
            elif active_window_title is not None:
                for window_name in windows_to_close:
                    if window_name in active_window_title:
                        print("Closing window:", active_window.title)
                        keyboard.send_keys("%{F4}")

            time.sleep(1)
    except KeyboardInterrupt:
        print("\nScript terminated by user.")

root = tk.Tk()
root.title("Window Blocker")

sv_ttk.set_theme("dark")

chrome_frame = ttk.Frame(root)
chrome_frame.pack(padx=10, pady=5, fill=tk.BOTH)

window_frame = ttk.Frame(root)
window_frame.pack(padx=10, pady=5, fill=tk.BOTH)

chrome_label = ttk.Label(chrome_frame, text="Chrome Tabs/Apps:")
chrome_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

chrome_entry = ttk.Entry(chrome_frame, width=40)
chrome_entry.grid(row=0, column=1, padx=5, pady=5)

add_chrome_button = ttk.Button(chrome_frame, text="Add", command=add_chrome_tab)
add_chrome_button.grid(row=0, column=2, padx=5, pady=5)

chrome_listbox = tk.Listbox(chrome_frame, width=50)
chrome_listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

remove_chrome_button = ttk.Button(chrome_frame, text="Remove", command=remove_chrome_tab)
remove_chrome_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

window_label = ttk.Label(window_frame, text="Windows to Close:")
window_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

window_entry = ttk.Entry(window_frame, width=40)
window_entry.grid(row=0, column=1, padx=5, pady=5)

add_window_button = ttk.Button(window_frame, text="Add", command=add_window)
add_window_button.grid(row=0, column=2, padx=5, pady=5)

window_listbox = tk.Listbox(window_frame, width=50)
window_listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

remove_window_button = ttk.Button(window_frame, text="Remove", command=remove_window)
remove_window_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

start_button = ttk.Button(root, text="Start Checking Windows", command=toggle_checking_windows)
start_button.pack(padx=10, pady=5)

stop_button = ttk.Button(root, text="Stop Checking Windows", command=toggle_checking_windows, state=tk.DISABLED)
stop_button.pack(padx=10, pady=5)

root.mainloop()
