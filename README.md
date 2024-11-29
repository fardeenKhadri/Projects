AI Voice Assistant with Pyttsx3 and OpenAI

This is a Python-based voice assistant script that integrates with OpenAI's GPT model to provide natural language responses, interact with users via speech, and perform various tasks like opening websites, playing music, and checking the time. It is designed to act as a virtual assistant, responding to commands and queries efficiently.


**Features**
1. _Voice Interaction_:
   - Uses `pyttsx3` for text-to-speech output.
   - Uses `speech_recognition` for capturing and recognizing user speech input.
   
2. _AI-Driven Responses_:
   - Integrates OpenAI's GPT-3.5 Turbo for generating intelligent responses to user queries.

3. _Task Automation_:
   - Opens predefined websites like YouTube, Google, Wikipedia, and Instagram.
   - Plays music from a specified folder.
   - Opens Visual Studio Code or any other application (path needs to be set).
   - Announces the current time on request.
   - Checks Gmail inbox for updates.

4. _Customizable Voice_:
   - Can be configured to use a female voice or any other voice available in the system.

5. _Secure Access_:
   - Ensures access is only provided to authorized users by verifying a specific keyword.

---

**Requirements**
Python Libraries
- `pyttsx3` (for text-to-speech)
- `speech_recognition` (for voice recognition)
- `openai` (for AI-driven responses)
- `webbrowser` (for opening websites)
- `datetime` (for current time display)
- `os` (for system-level operations)

Note that this was created using openai api keys, even if the openai part is removed the code will run with only 1 reduced functionality 

****Other Dependencies
- A microphone for capturing user input.
- OpenAI API key for GPT integration (replace `openai.api_key = ''` with your actual key).
- Internet connection for using OpenAI and browsing websites.

---

**Setup Instructions**
1. Clone the repository or download the script.
2. Install the required Python libraries using `pip`:
   ```
   pip install pyttsx3 speechrecognition openai
   ```
3. Replace the placeholders in the code:
   - OpenAI API Key:
     - Add your OpenAI API key at `openai.api_key = ''`.
   - Music Folder Path:
     - Define the folder path containing your music at `path_music`.
   - Code Editor Path:
     - Set the path to Visual Studio Code (or any other application) at `path_code`.

4. Run the script:
   ```
   python jarvis.py
   ```

---

How to Use
1. Launch the script. The assistant will verify if you are the authorized user by asking, *"Are you _______?"*.
2. If access is granted, the assistant will introduce itself as "Stew" or "Jarvis".
3. Use voice commands to interact. Example commands:
   - "Open YouTube": Opens YouTube in the browser.
   - "What is artificial intelligence?": Gets a detailed response from OpenAI.
   - "Play music": Plays music from the defined folder.
   - "Tell me the time": Announces the current time.
   - "Open code": Launches Visual Studio Code.
   - "Any updates?": Opens Gmail inbox.

4. To terminate the assistant, say *"terminate"*.

---

 **Notes**
- Ensure your microphone is working and configured correctly.
- Replace placeholder paths and API keys for optimal functionality.
- The assistant will create a folder named `Aiopen` to store AI-generated responses.

---

## Troubleshooting
1. Speech Recognition Issues:
   - Ensure you have a working microphone and background noise is minimal.
   - Install necessary audio drivers.

2. AI Response Issues:
   - Ensure the OpenAI API key is valid and you have an active internet connection.

3. File/Path Errors:
   - Double-check file paths for music and code editor.

---

Future Enhancements
- Add more websites and applications for automation.
- Improve authentication with user-specific keywords.
- Integrate calendar and reminders functionality.

---
