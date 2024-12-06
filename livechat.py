import pytchat
import time
import json
import argparse
from datetime import datetime

def fetch_chat_messages(video_id, chat_file):
    chat = pytchat.create(video_id=video_id)
    print(f"Started fetching chat messages for video ID: {video_id}")
    print(f"Saving messages to: {chat_file}")
    print("Press Ctrl+C to stop")
    
    try:
        while chat.is_alive():
            for c in chat.get().sync_items():
                message = {
                    "timestamp": c.datetime,
                    "author": c.author.name,
                    "message": c.message
                }
                save_message_to_json(message, chat_file)
                print(f"{message['timestamp']} - {message['author']}: {message['message']}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping chat fetching...")
    finally:
        print(f"Chat messages saved to {chat_file}")

def save_message_to_json(message, filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(message)
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def main():
    parser = argparse.ArgumentParser(description="Fetch YouTube live chat messages.")
    parser.add_argument('video_id', type=str, help='YouTube video ID to fetch chat messages from.')
    parser.add_argument('output_file', type=str, help='JSON file to store chat messages.')
    args = parser.parse_args()

    fetch_chat_messages(args.video_id, args.output_file)

if __name__ == '__main__':
    main()
