from langchain import LLMChain
from custom_class import CustomLLM
import chainlit as cl
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
)

from metaphor_python import Metaphor

metaphor = Metaphor("56d9ca28-e84b-43ce-8f68-75e1a8bb4dd3")   ## This is metaphor API Key


template = """ You are a helpful AI assistant who is tasked to answer user queries.
{question}

Answer:
"""


@cl.on_chat_start
async def factory():
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    prompt = ChatPromptTemplate.from_messages([system_message_prompt])
    llm = CustomLLM()

    llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True,)

    cl.user_session.set("llm_chain", llm_chain)



@cl.on_message
async def main(message):
    llm_chain = cl.user_session.get("llm_chain")

    res = await llm_chain.acall(message, callbacks=[cl.AsyncLangchainCallbackHandler()])

    await cl.Message(content=res["text"]).send()



@cl.author_rename   # This will be particularly useful when we want to customize this thing for production.
def rename(orig_author):
    rename_dict = {
        'LLMChain': 'Blaze'
    }
    return rename_dict.get(orig_author, orig_author)
