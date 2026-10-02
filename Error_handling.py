def agent(action):
    valid_actions = ["move", "stop", "wait"]

    if action not in valid_actions:
        return {"error": "Invalid action"}

    return {"success": f"Action '{action}' executed"}


print(agent("move"))
print(agent("jump"))