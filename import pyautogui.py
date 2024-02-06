import pyautogui
import time

time.sleep(7)

# Constants
OPENAI_URL = "https://chat.openai.com/"
TREE_OF_THOUGHTS_STEPS = [
    "Explore and generate information about each idea.",
    "Rank all three ideas according to 5 criteria that are selected by the AI.",
    "Drop the lowest two and declare a sub winner and give executive summary of the winner."
]
LOOP_ITERATIONS = 2  # Change this for more/less cycles

# Function to open OpenAI website and focus on input box
def open_oa_chat():
    pyautogui.hotkey("ctrl", "t")  # Open new tab
    pyautogui.write(OPENAI_URL)
    pyautogui.press("enter")
    # Wait for page to load; modify as needed for your connection
    for _ in range(50):  # Check every 0.1 seconds for up to 5 seconds
        if pyautogui.locateOnScreen('image_of_input_box.png'):  # Image of the input box to confirm page load
            break
        time.sleep(0.1)
    pyautogui.press("tab")  # Focus on input box

# Function to process Tree of Thoughts steps
def process_tree_of_thoughts(steps):
    for step in steps:
        pyautogui.write(step + "\n", interval=0.1)
        time.sleep(3)  # Wait for processing

# Main Loop
open_oa_chat()

for i in range(LOOP_ITERATIONS):  # Enter Tree of Thoughts steps
    pyautogui.write("Tree of Thoughts steps: \n", interval=0.1)
    process_tree_of_thoughts(TREE_OF_THOUGHTS_STEPS)

    # Additional steps as per your instructions (modify these as needed)
    # STEP Generate two new alternate competing ideas...
    # STEP Explore information, rank, drop, declare sub-winner...
    # STEP Retake a screenshot

    # Take screenshot at the end of each loop
    image_name = f"screenshot_{i+1}.png"
    pyautogui.screenshot(image_name)

# Final steps (modify based on your desired ending)
# Generate Pros and Cons, counterarguments, etc.

print("Process completed!")  # Confirmation message