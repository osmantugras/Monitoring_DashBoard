# Server Status Dashboard

This is a server status dashboard application built with Python and Tkinter. It allows you to monitor the status of multiple servers by pinging their IP addresses.

## Requirements

- Python 3.x
- Tkinter library

## Getting Started

1. Clone the repository or download the source code.
2. Make sure you have Python 3.x installed on your system.
3. Run the following command to install the required dependencies:


4. Run the script by executing the following command:

```
pip install -r subprocess
pip install -r tkinter
pip install -r platform
```

5. The application will open a window to select the operating system. Choose the appropriate option (Windows, MacOS, or Linux) and click the "Start" button.

6. In the login window, enter the IP address and name of each server you want to monitor. Click the "Add" button to add the server.

7. After adding the servers, click the "Run" button to open the server status dashboard.

8. The dashboard will display the server names, IP addresses, and their current status (reachable or unreachable). The status will be updated periodically by pinging the servers.

9. To stop the application, simply close the dashboard window.

## Customization

- To customize the appearance or layout of the dashboard, you can modify the code in the `open_dashboard()` function of the script.

- To change the icons used for server status, replace the existing image files with your own images and update the image file paths in the code accordingly.
