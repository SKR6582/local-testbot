import os
from openai import OpenAI
import subprocess

# Attempt to load .env if python-dotenv is available; ignore if not installed
try:
    import dotenv  # type: ignore
    dotenv.load_dotenv()
except Exception:
    pass
API_KEY = os.getenv("OPENAI_API_KEY") or os.getenv("APIKEY") or ""
if not API_KEY:
    raise RuntimeError(
        "OpenAI API key not found. Set OPENAI_API_KEY or APIKEY in your environment or .env file."
    )

client = OpenAI(api_key=API_KEY)

history = [{"role": "system", "content": "You are a helpful assistant."}]

def main(content) -> str:
    global history
    history.append({"role": "user", "content": content})

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=history,
        stream=True
    )

    collected_text = ""
    for event in response:
        if hasattr(event, "choices") and event.choices:
            delta = event.choices[0].delta
            if delta and delta.content:
                print(delta.content, end="", flush=True)
                collected_text += delta.content
    print()  # 줄바꿈

    history.append({"role": "assistant", "content": collected_text})
    return collected_text

print("Connected to Chat. To quit, `/quit`")

while True:
    try:
        user_content = input("> ")
        if not user_content.strip():
            response = "빈 메시지를 전송할 수 없습니다."
            print(response)
            continue
        elif user_content.strip() == "/clear":
            subprocess.run(["clear"])
            continue
        elif user_content.strip() == "/new":
            history = [{"role": "system", "content": "You are a helpful assistant."}]
            print("대화 기록 초기화 완료.")
            continue
        elif user_content.strip() == "/quit":
            break
        else:
            response = main(user_content)
    except RuntimeError as e:
        print("API 키를 확인하세요.")

    except Exception as e:
        print(f"An Error has occured: {e}")


print("Bye!")