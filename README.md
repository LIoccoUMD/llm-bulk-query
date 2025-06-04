# LLM GUI Bulk Query Inputs

Automates the process of sending queries to a GUI-based LLM interface (e.g., Grok) using PyAutoGUI. This tool simulates human interaction by detecting the input box on-screen and typing in queries from a provided list.

## Features

- Visual query box detection via screenshot matching
- Simulated typing and submission of queries
- Batch querying support with average timing logs (WIP)
- Debug screenshots for troubleshooting [optional]

## Requirements

- Python 3.x
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
- OpenCV support (for confidence matching):
  ```pip install opencv-python```

## Usage

1. Capture a screenshot of the query input box and name it *"grok.png"* or *"grok_1.png"*
2. Ensure the target LLM window is visible on the screen
3. Run ```py main.py```

 ## Notes
 - Make sure display scaling is set to 100%
 - Adjust the confidence level in locateOnScreen() if matching fails.
