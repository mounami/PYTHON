from lanchain_ibm import chatWatsonX

llm = chatWatsonX(model_id="ibm/granite-3-2-8b-instruct",
                  url="https://api.us-south.watsonx.ai",
                  project_id="your_project_id",)