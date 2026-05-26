from datetime import datetime

def log_step(agent, message):

    current_time = datetime.now().strftime("%H:%M:%S")

    print(
        f"\n[{current_time}] "
        f"[{agent.upper()}] "
        f"{message}"
    )