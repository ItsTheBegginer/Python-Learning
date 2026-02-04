#TextSender
import json
invalid = []
sent = []
empty = []
with open("contacts.json","r") as f:
        data = json.load(f)
        for contact in data:
            number = contact["phone"]
            if len(number)!=10:
                print(f"message not sent to {contact["name"]} cause number is invalid")
                invalid.append(contact["name"])
            elif contact["message"]=="":
                print(f"message not sent to {contact["name"]} cause message is empty")
                empty.append(contact["name"])
            else:
                print(f"message sent to {contact["name"]} ")
                sent.append(contact["name"])

print("Summary:")
print(f"Messages are sent to {sent}\nMessages are not sent to {invalid} due to invalid numbers\nMessages are not sent to {empty} due to empty messages")



