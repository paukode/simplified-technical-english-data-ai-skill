# Examples: generative AI

Each example shows text before and after the change to STE.
The rule IDs refer to `references/writing-rules.md`.

## 1. A retrieval-augmented generation pipeline

Type: description

Before:

~~~text
Our RAG setup chunks the docs into ~500 token pieces, embeds them, and at query time we grab the top 5 chunks and stuff them into the prompt so the LLM can answer grounded in our docs.
~~~

After:

~~~text
The help desk assistant uses retrieval-augmented generation (RAG).

When a document is new or changed, the pipeline divides the document into chunks of approximately 500 tokens. An embedding model makes a vector for each chunk. The pipeline writes the vectors to the vector index.

When a user asks a question, the retriever finds the 5 chunks with the nearest vectors. The application puts these chunks in the prompt. Then the model generates the answer from the chunks.
~~~

Changes: the full term before the acronym (W14), one topic in each paragraph (D2), and no slang or jargon (W9).

## 2. A system prompt

Type: procedure

Before:

~~~text
You are a helpful assistant for Acme's internal IT helpdesk. Try to answer questions using the provided context. If you're not sure, it's probably best to say you don't know rather than making something up. Keep answers short and friendly, and feel free to use bullet points.
~~~

After:

~~~text
You are the assistant of the IT help desk. You answer questions from personnel.

Obey these rules:

1. Use only the documents in the "Context" section to write the answer.
2. If the documents do not contain the answer, write: "The documents do not contain this information."
3. Do not write information that is not in the documents.
4. Write maximum 5 sentences.
5. Use a numbered list for steps.
6. At the end of the answer, give the title of each document that you used.
~~~

Changes: the prompt as a procedure (M4), one rule in each item (P2), and specific limits instead of vague words (W13).

## 3. Citations that are not correct

Type: description

Before:

~~~text
The model sometimes hallucinates citations because it thinks it needs to back up its claims, even when the retrieved docs don't support them.
~~~

After:

~~~text
We did a test on 2026-09-25 with 500 questions. In 23 answers (4.6%), the model returned a citation to a document that did not contain the quoted text. This error is a hallucination.

The system prompt tells the model to give a citation for each statement. If no retrieved chunk contains the statement, the model can generate a citation that is not correct.
~~~

Changes: no human qualities for the model (M1), a measured value with a date (M2), and "hallucination" as a noun only.

## 4. Guardrails for a customer assistant

Type: specification

Before:

~~~text
The chatbot shall not reveal customer PII, should refuse off-topic requests politely, and must never execute actions on behalf of the user without confirmation.
~~~

After:

~~~text
This specification uses the keywords MUST, MUST NOT, and SHOULD as RFC 2119 gives them.

- GR-01: The assistant MUST NOT show the personal data of a customer to a different customer.
- GR-02: The output guardrail MUST block each answer that contains a payment card number.
- GR-03: The assistant SHOULD reject a request that is not related to the orders of the customer.
- GR-04: The assistant MUST get the approval of the user before it calls a tool that changes data.
~~~

Changes: one requirement in each item with an ID (R2), the actor as the subject (R4), and MUST instead of "shall" (R1).

## 5. The effect of prompt caching on cost

Type: description

Before:

~~~text
By caching the 20k-token system prompt, we cut input costs by about 80% since cache reads are billed at a fraction of the normal rate.
~~~

After:

~~~text
The system prompt of the `support-agent` has 20,000 tokens. Prompt caching stores this prompt after the first request. Each request after that reads the prompt from the cache.

For this model, the price of a cache read is 10% of the price of a normal input token. In September 2026, prompt caching decreased the cost of the input tokens by 78%.
~~~

Changes: a measured value instead of "about" (W13, M2), no passive voice (V5), and no slang (W9).

## 6. Prepare the data for fine-tuning

Type: procedure

Before:

~~~text
Before fine-tuning, make sure the training data is cleaned up - dedupe it, strip any PII, and hold out 10% for eval.
~~~

After:

~~~text
Prepare the training data before you start the fine-tuning job:

1. Remove the duplicate examples.
2. Remove the personally identifiable information (PII) from each example.
3. Put 10% of the examples in a separate evaluation set. Do not use these examples for training.
4. Start the fine-tuning job with the remaining 90% of the examples.
~~~

Changes: one instruction in each step (P2), no jargon (W9), and the full term before the acronym (W14).

## 7. A judge model for evaluation

Type: description

Before:

~~~text
We use GPT-4 as a judge to grade answers on a 1-5 scale, which correlates pretty well with human ratings.
~~~

After:

~~~text
A judge model gives each answer a score from 1 to 5. The judge model is `gpt-4.1`, and the rubric is in the file `eval/rubric.md`.

On 2026-09-10, two human raters also gave scores to 300 answers. For 82% of these answers, the score of the judge model was the same as the score of the human raters.
~~~

Changes: the full model ID (M3), a measured value instead of a vague word (M2, W13), and the active voice (V5).
