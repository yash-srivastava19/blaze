Access Deployed Blaze Here : [HFSpaces](https://yash-srivastava19-blaze.hf.space) 

# blaze
A Metaphor + Cohere alternative to [perplexity.ai](https://www.perplexity.ai) . Blaze is a chatbot that answers your query, and allows you to learn more on the subject matter with RAG(Retrieval Augmented Generation). Gone are the days of fact checking LLM output, with **Blaze** you can do it all. The value of information is more nowadays, and **Blaze** delivers all of this, for free of cost*    


![Screenshot 2023-09-30 234601](https://github.com/yash-srivastava19/blaze/assets/85068689/a8f92f50-79ad-4cad-a000-512fb2293169)

![Screenshot 2023-09-30 234957](https://github.com/yash-srivastava19/blaze/assets/85068689/ce372146-fcb5-4160-a4f1-0919fe4b0a0e)

## Why create something from scratch?

I love the chain of thought reasoning in real life, and having an assistant like perplexity.ai is really helpful. Although Cohere is rolling out Coral with RAG, we can 'mimic' RAG with leveraing Cohere Chat Model(to have a meaningful conversations with user) and Metaphor Neural Search(to get additional sources) to make really hacky Chatbot - that I call Blaze.

The project was made as a part of a weekend project(~ 3hr) for Metaphor as a part of their recruitement process,(and Blaze was something I had been planning to do from a long time !!!) and due to some time constraints, I could not polish this like I wanted to do(due to having university exams on both weekends and weekdays). I wanted to have an even great UI, and professionally deploy on docker.

Contrary to the name, Blaze is not lightning fast. I believe there is a huge scope for improvement, and that this can be enhanced even more(I haven't even used 10% of what Metaphor offered, but I hope with more time, I would've done an even great job !)

## Details

The file `app.py` contains all the logic for Blaze. Blaze creates a custom langchain LLM wrapper for Cohere's Chat model, and uses the user entered prompt to do a neural search using the Metaphor API. The chatbot is containerized using Docker and deployed on Huggingface Spaces.   

## Future Improvements
This is a very hacky solution to a really big and important problem. For future versions of Blaze, I'm planning to a clean and neat UI, and make the hacky RAG into a real one.

