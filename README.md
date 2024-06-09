# Window Blocker

Window Blocker is a quick and dirty Python script made by request which allows users to manage and block certain windows or Chrome tabs.

## Features

- Add Chrome tabs or apps to a list for automatic closure when they become active.
- Add specific windows to a list for automatic closure when they become active.
- Start and stop checking for active windows.

## Dependencies

- [pygetwindow](https://pypi.org/project/PyGetWindow/): For interacting with windows and getting active window information.
- [tkinter](https://docs.python.org/3/library/tkinter.html): For building the graphical user interface.
- [sv_ttk](https://pypi.org/project/sv-ttk/): A theme package for Tkinter.

## Usage

1. Install the dependencies by running:

   ```
   pip install -r requirements.txt
   ```

2. Run the script:

   ```
   python window_blocker.py
   ```

3. Use the GUI to add Chrome tabs/apps or specific windows to the block list.
4. Click "Start Checking Windows" to begin monitoring active windows.
5. Click "Stop Checking Windows" to stop monitoring.

## License

This project is licensed under the [MIT License](https://opensource.org/license/mit).
