# This script uses the 'pywhatkit' library to automate sending a single message
# to multiple WhatsApp numbers through the WhatsApp Web interface.
#
# PREREQUISITE:
# 1. You must have the 'pywhatkit' library installed: pip install pywhatkit
# 2. You must have WhatsApp Web logged in on your default web browser.
# 3. The script will wait 20 seconds for the WhatsApp Web page to load before attempting to send the message.

import pywhatkit
import time


def broadcast_whatsapp_message(phone_numbers, message):
    """
    Sends a message to a list of phone numbers using pywhatkit.

    NOTE: The script requires the phone numbers to be in international format
    (e.g., '+11234567890') and will open a new browser tab for each message.
    The message sending is timed (currently set to 20 seconds from execution).
    """
    print("--- Starting WhatsApp Broadcast ---")



    # Define the time delay (in seconds) to wait for WhatsApp Web to load.
    # Adjust this if your internet connection is slow.
    WAIT_TIME_SECONDS = 20

    # Store the count of successfully initiated messages
    success_count = 0

    for number in phone_numbers:
        try:
            print(f"Attempting to send message to: {number}")

            # Send the message.
            # The last argument (20) is the wait time in seconds before sending.
            # The arguments for time are (hour, minute). We use a time in the immediate future
            # of the current time plus a buffer for WhatsApp Web to open.

            # Since the script runs quickly, we add the current index to the wait time
            # to prevent multiple tabs from opening at the exact same second,
            # which can confuse the browser.

            # NOTE: pywhatkit uses the current system time. If the message time
            # is in the past, it sends immediately. We are using the 'wait_time' argument
            # to specify the delay.

            pywhatkit.sendwhatmsg_instantly(
                phone_no=number, message=message, wait_time=WAIT_TIME_SECONDS
            )

            print(
                f"Successfully initiated message for {number}. Please monitor your browser."
            )
            success_count += 1

            # Wait for the pywhatkit process to complete before moving to the next number.
            # This is crucial to avoid opening to
            # 
            # o many browser tabs at once.
            time.sleep(WAIT_TIME_SECONDS + 5)

        except Exception as e:
            print(f"ERROR sending to {number}: {e}")
            # Wait a short time before trying the next number
            time.sleep(5)

    print(f"--- Broadcast complete. {success_count} messages initiated. ---")
    print("Check your browser for final status and ensure messages were sent.")


if __name__ == "__main__":
    # --- CONFIGURATION ---

    # 1. LIST OF NUMBERS: Replace these with the actual WhatsApp numbers.
    #    MUST be in international format (e.g., '+19876543210').

    target_numbers = [+213698062454]

    # 2. MESSAGE CONTENT: Write your single message here.
    broadcast_message = (Bonjour,
J’espère que vous allez bien.
Je vous contacte via ce message pour vous informer / rester en contact.
Merci et excellente journée.)

    # --- EXECUTION ---
    broadcast_whatsapp_message(target_numbers, broadcast_message)
