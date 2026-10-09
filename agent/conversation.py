conversation_history=[]

def save_conversation (user_input,res):
    history = {
        "user":user_input,
        "AI":res
    }
    conversation_history.append(history)
    return conversation_history

def get_conversation_history ():
    return conversation_history