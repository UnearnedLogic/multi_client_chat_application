# Python Multi-Client Chat Application

## Overview
This project is a simple real-time chat application built using Python’s socket and threading modules. It allows multiple clients to connect to a server and exchange messages concurrently. The server broadcasts messages to all connected clients, enabling group chat functionality.

## Features
- Multi-client support with concurrent handling via threading
- Nickname-based identification of users
- Graceful handling of client connections and disconnections
- Commands supported:
  - `/quit` — disconnect from the chat

## Getting Started

### Prerequisites
- Python 3.x installed
- Basic knowledge of running Python scripts from the command line

# Chat Application

## 🚀 How to Run

1. Clone this repository or download the files: `server.py` and `client.py`.
2. Open a terminal and start the server:
   ```bash
   python server.py
   ```
3. Open one or more terminal windows and run the client for each user:
   ```bash
   python client.py
   ```
4. Follow the prompts:
   - Enter your nickname when prompted.
   - Start chatting! Type messages and press `Enter` to send.
   - To exit the chat, type `/quit` and press `Enter`.

---

## 🧠 Code Overview

### `server.py`
- Accepts incoming client connections.
- Manages a list of active clients and nicknames.
- Broadcasts messages to all connected clients.

### `client.py`
- Connects to the server.
- Sends user messages and listens for broadcasts.
- Uses separate threads for real-time input/output.

---

## ✨ Possible Improvements

- Add commands like private messaging and user listing.
- Implement a GUI for the client.
- Improve error handling and connection stability.
- Add encryption for secure communication.

