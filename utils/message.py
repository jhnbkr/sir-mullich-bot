import re


def message_contains_text(message, text):
    return re.search(text, message.content, re.IGNORECASE)


def message_contains_mention(message, user):
    for mention in message.mentions:
        if mention.id == user:
            return True


def message_contains_role_mention(message, role):
    for mention in message.role_mentions:
        if mention.id == role:
            return True

    return False
