from string import Template
import httpx
import json


OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
OLLAMA_CONFIG = {"model":"mistral:7b-instruct-v0.2-q4_K_S",
                 "keep_alive":"5m",
                 "steam":False}
PROMPT_TEMPLATE =Template(
    """
    Answer this sentence in the shortest way possible:
    $text
    """
)


OLLAMA_ENDPOINT_MATH = "http://localhost:11434/api/generate"
OLLAMA_CONFIG__MATH = {"model":"wizard-math",
                 "keep_alive":"5m",
                 "steam":False}
PROMPT_TEMPLATE__MATH =Template(
    """
    Answer this sentence in the shortest way possible:
    $text
    """
)

def answer_model(text):
    prompt = PROMPT_TEMPLATE.substitute(text=text)
    response = httpx.post(OLLAMA_ENDPOINT,
                          json={"prompt": prompt, **OLLAMA_CONFIG},
                          headers={"Content-Type": "application/json"},
                          timeout=100)
    
    parts = response.text.strip().split('\n')   
    answer = ""
    for part in parts:
        try:
            json_part = json.loads(part)

            if json_part.get("done", False):
                answer += json_part.get("response", "")
                break
            else:
                answer += json_part.get("response", "")
        except json.JSONDecodeError as e:
            print(f"JSON decode error for part: {e}. Part content: {part}")
            return None
    
    return answer


def solve_problem(text):
    prompt = PROMPT_TEMPLATE__MATH.substitute(text=text)
    response = httpx.post(OLLAMA_ENDPOINT_MATH,
                          json={"prompt": prompt, **OLLAMA_CONFIG__MATH},
                          headers={"Content-Type": "application/json"},
                          timeout=100)
    
    parts = response.text.strip().split('\n')   
    solved = ""

    print("teste")
    for part in parts:
        try:
            json_part = json.loads(part)

            if json_part.get("done", False):
                solved += json_part.get("response", "")
                break
            else:
                solved += json_part.get("response", "")
        except json.JSONDecodeError as e:
            print(f"JSON decode error for part: {e}. Part content: {part}")
            return None
    
    return solved