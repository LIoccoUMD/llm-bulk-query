# TO DO
# bulk model querying
##

import pyautogui
import time

# Used to improve response time
avg_times = []

def queryLLM(model, query):
    """Accepts a LLM model and a single query."""
    if(model == "grok"):
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
    if(model == "grok"):
        pyautogui.screenshot("debug_screen.png")
        res = pyautogui.locateOnScreen("grok_1.png", confidence=0.5)
        center = pyautogui.center(res) if res else None
        pyautogui.moveTo(center)
        pyautogui.leftClick()
        for query in queries:
            start = time.time()
            inputQuery(query)
            # Capture query result
            end = time.time()
            avg_times.append(end - start)
            time.sleep(5)


def main():
    # queryLLM("grok", "Hello grok!")
    multiple_queries("grok", ["What kind of trees are most common in North Carolina?","Are there birds that fly around there?", "Is it possible to create a new color?"])

if __name__ == "__main__":
    main()
