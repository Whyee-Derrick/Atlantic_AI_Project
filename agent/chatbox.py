import requests
from agent.conversation import get_conversation_history,save_conversation
from prompts.prompts import get_prompt
from agent.search import search_for_info


def get_AI_reponse(user_input,uploaded_text):
    history = get_conversation_history()
        
    if uploaded_text is not None:
        local_data = uploaded_text

    else:
        local_data = search_for_info(user_input)
        
    
    prompt = get_prompt(local_data,history,user_input)

    url = "http://localhost:11434/api/generate"
    
    data = {
        "model":"llama3.2",
        "prompt":prompt,
        "stream":False
    }
    res = requests.post(url,json=data)
    res = res.json()
    res = res["response"]
    save_conversation(user_input,res)
    return res

    
