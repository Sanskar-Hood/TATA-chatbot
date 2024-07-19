import os

VECTARA_API_KEY = "zwt_vwKISv4ZM-x7LDQmKq4X_yuKGMQ80sgIYLohtw"
VECTARA_CUSTOMER_ID = "3204614218"
VECTARA_CORPUS_ID = "2"

os.environ["VECTARA_CUSTOMER_ID"] = VECTARA_CUSTOMER_ID
os.environ["VECTARA_CORPUS_ID"] = VECTARA_CORPUS_ID
os.environ["VECTARA_API_KEY"] = VECTARA_API_KEY

from langchain_community.vectorstores import Vectara
vectara = Vectara(
                vectara_customer_id=VECTARA_CUSTOMER_ID,
                vectara_corpus_id=VECTARA_CORPUS_ID,
                vectara_api_key=VECTARA_API_KEY
            )


from langchain_community.vectorstores.vectara import (
    RerankConfig,
    SummaryConfig,
    VectaraQueryConfig,
)
from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader("punch-brochure_merged.pdf")
documents = loader.load()

vectara = Vectara.from_documents(documents, embedding=None)

summary_config = SummaryConfig(is_enabled=True, max_results=7, response_lang="eng")
rerank_config = RerankConfig(reranker="mmr", rerank_k=50, mmr_diversity_bias=0.2)
config = VectaraQueryConfig(
    k=10, lambda_val=0.005, rerank_config=rerank_config, summary_config=summary_config
)

bot = vectara.as_chat(config)
def bot_query(query):
    return (bot.invoke(query)["answer"])
while(1):
    bot_query(query=input())


# output = {}
# curr_key = None
# for chunk in bot.stream("?"):
#     for key in chunk:
#         if key not in output:
#             output[key] = chunk[key]
#         else:
#             output[key] += chunk[key]
#         if key == "answer":
#             print(chunk[key], end="", flush=True)
#         curr_key = key