# TO DO
# bulk model querying
##

import pyautogui
import time

# Used to improve response time
avg_times = []


def setup():
    return input("Are you using grok, chatgpt, or gemini?\n")


def queryLLM(model, query):
    """Accepts a LLM model and a single query."""
    if (model == "grok"):
        res = pyautogui.locateOnScreen("grok.png", confidence=0.5)
        center = pyautogui.center(res) if res else None
        pyautogui.moveTo(center)
        inputQuery(query)


def inputQuery(query):
    """Types and enters the query"""
    pyautogui.typewrite(query)
    pyautogui.press("enter")


def multiple_queries(model, queries):
    """Input a model and a list of queries"""
    if (model == "grok"):
        res = pyautogui.locateOnScreen("chat_boxes/grok.png", confidence=0.5)
    elif (model == "chatgpt"):
        res = pyautogui.locateOnScreen(
            "chat_boxes/chatgpt.png", confidence=0.5)
    elif (model == "gemini"):
        res = pyautogui.locateOnScreen("chat_boxes/gemini.png", confidence=0.5)
    else:
        pyautogui.screenshot("debug_screen.png")
    center = pyautogui.center(res) if res else None
    adjusted_center = pyautogui.Point(center.x, center.y - 10)
    pyautogui.moveTo(adjusted_center)
    pyautogui.leftClick()
    for query in queries:
        start = time.time()
        inputQuery(query)
        # Capture query result here
        end = time.time()
        avg_times.append(end - start)
        time.sleep(5)


def main():
    # queryLLM("grok", "Hello grok!")
    model = setup()
    multiple_queries(model, ["If the ancient Romans had access to a basic understanding of electricity (like static electricity) and could harness it, how might the trajectory of the Roman Empire and subsequent European history have been altered?",
                     "Imagine a scenario where a massive, previously unknown, highly fertile, and resource-rich continent suddenly emerged in the middle of the Pacific Ocean. How would the global geopolitical landscape, economic powers, and human migration patterns shift in the decades following its discovery?"])


if __name__ == "__main__":
    main()
