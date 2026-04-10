import json

lead_data = {}

def detect_intent(text):
    text = text.lower()

    if any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"
    elif any(word in text for word in ["price", "pricing", "plan", "cost"]):
        return "pricing"
    elif any(word in text for word in ["buy", "subscribe", "want", "purchase"]):
        return "high_intent"
    return "other"


def get_pricing():
    with open("knowledge.json", "r") as f:
        data = json.load(f)

    basic = data["pricing"]["basic"]
    pro = data["pricing"]["pro"]

    return f"""
Basic Plan: {basic['price']} – {basic['videos']} – {basic['resolution']}
Pro Plan: {pro['price']} – {pro['videos']} – {pro['resolution']} + {pro['features']}
"""


def mock_lead_capture(name, email, platform):
    print(f"\n✅ Lead captured: {name}, {email}, {platform}\n")


print("Agent: Hi! Ask me anything about AutoStream.")

while True:
    user = input("You: ")
    intent = detect_intent(user)

    if intent == "greeting":
        print("Agent: Hey! How can I help you?")

    elif intent == "pricing":
        print("Agent:", get_pricing())

    elif intent == "high_intent" or lead_data:

        if "name" not in lead_data:
            print("Agent: What's your name?")
            name = input("You: ")
            if len(name) < 2:
                print("Agent: Please enter a valid name.")
            else:
                lead_data["name"] = name

        elif "email" not in lead_data:
            while True:
                print("Agent: What's your email?")
                email = input("You: ")
                if "@" not in email or "." not in email:
                    print("Agent: Please enter a valid email.")
                else:
                    lead_data["email"] = email
                    break

        elif "platform" not in lead_data:
            print("Agent: Which platform do you create on?")
            platform = input("You: ")
            if len(platform) < 2:
                print("Agent: Please enter a valid platform.")
            else:
                lead_data["platform"] = platform

        if len(lead_data) == 3:
            mock_lead_capture(
                lead_data["name"],
                lead_data["email"],
                lead_data["platform"]
            )
            print("Agent: Thanks! We'll reach out soon.")
            lead_data.clear()

    else:
        print("Agent: Can you rephrase that?")