# deepseekrag-project
```markdown
# FastAPI Deepseek API with Docker and Uvicorn

This project demonstrates how to use the Deepseek-r1 1.5B model through `Ollama`, creating APIs with FastAPI, and deploying everything in Docker. The application handles database migrations with Alembic, SQLAlchemy for DB operations, and Pydantic for data validation. Docker Compose is used to set up a multi-container application.

## Project Setup

### 1. Ollama & Deepseek Model
The model is pulled from Ollama and served locally by running Ollama separately. The model is then accessed through the code and used to provide responses.

### 2. FastAPI API Creation
FastAPI is used to create the APIs. The APIs handle requests, process data using the Deepseek model, and return responses.

### 3. Uvicorn for API Running
Uvicorn is used to run the FastAPI application in an ASGI server.

### 4. Testing with Curl
The APIs are tested using `curl` for testing HTTP requests and responses.


### 5. Database and Migrations
- **Alembic** is used for database migrations to ensure that the schema is up-to-date.
- **SQLAlchemy** is used for interacting with the database.
- **Pydantic** is used for validating incoming data for the APIs.

### 6. Docker for Containerization
Docker is used to containerize the application, making it easier to deploy and run in isolated environments.

### 7. Docker Compose for Multi-Container Setup
Docker Compose is used to define and run multi-container Docker applications, making it easy to manage services like the application and database in one setup.

## Requirements

- Python 3.11+
- Docker
- Docker Compose
- FastAPI
- Uvicorn
- SQLAlchemy
- Alembic
- Pydantic
- Ollama (for running the Deepseek model)

## Installation

1. Clone the repository:

   ```bash
   git clone <your-repository-url>
   cd <your-project-directory>
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:

   Run the Alembic migrations to set up the initial database schema.

   ```bash
   alembic upgrade head
   ```

4. Start the application using Docker Compose:

   ```bash
   docker-compose up --build
   ```

5. This will start the FastAPI application on port 8000 and your database container.

## Usage

Once the application is up and running, you can test the API using `curl`.

### Example: Testing the API

```bash
curl -X POST "http://localhost:8000/api/ingest/" \
     -H "Content-Type: application/json" \
     -d '{"title": "Deepseek", "content": "Deepseek R1 is a reinforcement learning model"}'
```
Response
```
{"message": "Document stored successfully"}
```
```bash
curl -X POST "http://localhost:8000/api/qna/" -H "Content-Type: application/json" -d '{"query": "What is AI?"}'
```
Response
```
{"answer":"<think>\nOkay, so I'm trying to figure out what AI stands for and what it means based on the given document. The user provided a sentence: \"Artificial Intelligence is transforming industries.\" Hmm, that's interesting. Let me break this down.\n\nFirst, I know that AI is often mentioned in tech circles, but I'm not exactly sure about its definition. The phrase here is \"Artificial Intelligence,\" so maybe it refers to machines or systems that can perform tasks that typically require human intelligence.\n\nThe sentence says it's transforming industries. So, AI must be having a significant impact on different sectors. But how? Is it automation? Data analysis? Or something else?\n\nWait, the user just said: \"What is AI?\" So they're asking for an explanation of what AI stands for and its definition based on the given document.\n\nLooking at the sentence again, maybe I should extract the definition from it. The sentence starts with \"Artificial Intelligence\" followed by a description of its impact. So perhaps AI is defined as something that's transforming industries.\n\nBut to make this more precise, maybe I can rephrase it. Instead of just stating what it does (transforming industries), I could say what AI is. Maybe AI refers to systems designed to mimic human intelligence features like learning and problem-solving.\n\nAlternatively, considering the sentence given, perhaps AI is best defined as a technology that enables machines to perform intelligent tasks without human intervention.\n\nWait, but in the initial response, it was stated: \"Artificial Intelligence (AI) refers to the simulation of human intelligence processes by machines.\" That's more of an explanation rather than a direct answer based on the document. The user provided only one sentence, so maybe I should base the answer solely on that.\n\nSo if the document says AI is transforming industries, then perhaps the answer is: \"Artificial Intelligence is a technology that enables systems to perform intelligent tasks like learning and problem-solving autonomously.\"\n\nBut wait, maybe it's better to use the exact phrasing from the document. The user provided the sentence as: \"Artificial Intelligence is transforming industries.\" So I can use that as the core of the answer.\n\nSo putting it together, AI refers to machines designed to perform tasks that typically require human intelligence, thereby transforming various industries through automation and innovation.\n</think>\n\nArtificial Intelligence (AI) is defined as a technology that enables systems to perform intelligent tasks autonomously. These tasks include learning, reasoning, problem-solving, and adapting to new information or experiences without explicit programming for each situation. By enhancing efficiency and introducing innovative solutions across different industries, AI represents a transformative force in sectors such as healthcare, finance, manufacturing, and more."}
```
### API Documentation

The FastAPI app automatically generates an interactive API documentation that you can access at:

```
http://127.0.0.1:8000/docs
```

## Directory Structure

![Screenshot 2025-02-04 at 5 16 35 PM](https://github.com/user-attachments/assets/47adbac4-477a-4442-8e1f-4db468f448c9)
```
These are the 2 APIs in which i have used deepseek-r1 1.5B i have use ollama and pulled the model into my system then run the ollama seperately which serves me the deepseek model and then i have used the model in my code and then i have used the fastapi to create the api and then i have used the uvicorn to run the api and then i have used the curl to test the api.

I have used alembic for db migrations and i have used sqlalchemy for db operations and i have used pydantic for data validation and i have used fastapi for api creation and i have used uvicorn for api running and i have used curl for api testing. I have used docker for containerization and i have used docker-compose for multi-container docker applications.
I have used the following commands to run the application:
    python -m app.main

    ollama serve deepseek-r1-1.5B

Research Paper:- https://github.com/deepseek-ai/DeepSeek-R1/blob/main/DeepSeek_R1.pdf

Why Deepseek-r1
Deepseek-r1 1.5B is a powerful language model that excels at a wide range of natural language processing (NLP) tasks. The model has been chosen for its:
- **Reinforcement learning**: It uses reingforcement learning which is very different from OpenAI's o1 and other general models, aiming for higher efficiency than llama and o1 in certain benchmarks.It uses teach student model, this 1.5b tiny model has been trained as a student model to learn from a larger model, which is a common technique in the field of machine learning to improve the performance of smaller models by leveraging the knowledge of larger models.

- **Advanced Language Understanding**: Deepseek provides exceptional language understanding, enabling it to process complex queries, extract meaningful insights, and generate coherent responses. This makes it ideal for use in applications that require high-quality text generation, such as chatbots, automated content creation, and text summarization.
  
- **Scalability and Efficiency**: With 1.5 billion parameters, Deepseek strikes a balance between model size and computational efficiency. It's large enough to handle a broad spectrum of tasks but also optimized for real-time inference, making it suitable for API-based applications that need to respond quickly to user queries.

- **Fine-Tuning Capabilities**: Deepseek is designed to be fine-tuned for specific tasks, allowing it to be adapted to the needs of different industries and applications. Whether you’re working with general text generation or specialized fields like legal, medical, or customer support, Deepseek can be tailored to provide accurate and contextually relevant responses.

- **Ease of Integration with Ollama**: By utilizing Ollama to serve the Deepseek model locally, we can easily integrate the model into our FastAPI application without the complexity of managing server infrastructure for model deployment. Ollama provides a streamlined interface for loading and running models, simplifying the overall process.

- **State-of-the-Art NLP**: Deepseek competes with some of the best models in the market, offering a combination of precision, flexibility, and speed. By leveraging this model, the project ensures that users receive high-quality responses for a variety of NLP tasks.
**RESULTS
```
![Screenshot 2025-02-04 at 5 22 30 PM](https://github.com/user-attachments/assets/0acbce79-73b2-4ddb-9a6f-b2ed5476bcac)
![Screenshot 2025-02-04 at 5 22 49 PM](https://github.com/user-attachments/assets/89b89eb1-d08c-41b2-a0ec-aa7cb93de44a)
![Screenshot 2025-02-04 at 5 23 07 PM](https://github.com/user-attachments/assets/894bd74a-e295-4905-ad35-d0fca03eb074)
![Screenshot 2025-02-04 at 5 23 20 PM](https://github.com/user-attachments/assets/fd5f58c6-9797-4cb9-a44a-a25797f53333)
![Screenshot 2025-02-04 at 5 23 30 PM](https://github.com/user-attachments/assets/bfe2898e-bf8b-4f17-96c0-a67bb3c5af1c)
```

