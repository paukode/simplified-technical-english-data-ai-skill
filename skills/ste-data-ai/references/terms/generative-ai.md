# Technical names: generative AI

These are technical names for generative AI, large language models, retrieval-augmented generation, and model evaluation.
Use them as nouns, or as modifiers before a noun.
Do not use a technical name as a verb (rule W6).
Use the official spelling and case. Write model IDs and API parameters as inline code, for example `temperature` and `max_tokens`.
A name in parentheses is the short name or the acronym. Write the full name at the first use (rule W7).
This list is not complete. Any official name is a technical name (rule W5).
Model names change frequently. Give the full model ID and the version (rule M3).

## Models and model families

- deterministic, non-deterministic, deterministic output, generative AI (GenAI), generative model, large language model (LLM), small language model (SLM), language model, foundation model (FM), frontier model, open-weight model, open-source model, proprietary model, base model, instruction-tuned model, chat model, reasoning model
- multimodal model, vision-language model (VLM), text-to-image model, image generation model, speech model, mixture of experts (MoE), dense model, model family, model size, parameter count, knowledge cutoff, training cutoff, model ID, model alias, model provider
- Anthropic, Claude, Claude Opus, Claude Sonnet, Claude Haiku, Claude Fable, OpenAI, GPT, GPT-4o, GPT-4.1, GPT-5, ChatGPT, Google DeepMind, Meta, Llama, Mistral AI, Mistral, Mixtral, Codestral, Cohere, Cohere Embed, Cohere Rerank
- DeepSeek, DeepSeek-R1, DeepSeek-V3, Qwen, xAI, Grok, AI21 Labs, Jamba, Stability AI, Stable Diffusion, Midjourney, DALL-E, Sora, Whisper, ElevenLabs

## Prompts and context

- prompt, system prompt, system message, user prompt, user message, assistant message, developer message, conversation, conversation history, chat history, turn, multi-turn conversation, prompt template, prompt engineering, context engineering, instruction
- prompting, few-shot prompting, few-shot example, zero-shot prompting, one-shot prompting, chain of thought (CoT), chain-of-thought prompting, reasoning, extended thinking, thinking budget, reasoning effort, prefill, assistant prefill, role prompting, persona, delimiter, XML tag
- structured output, structured outputs, JSON mode, response format, output schema, output format, stop sequence, prompt chaining, prompt library, prompt version, prompt management, meta-prompt, prompt optimization, DSPy
- context, context length, long context, context compaction, context compression, summarization, grounding, grounding source, citation, source attribution

## Generation parameters

- temperature, top-p, nucleus sampling, top-k, max tokens, maximum output tokens, frequency penalty, presence penalty, repetition penalty, logprobs, log probability, sampling, greedy decoding, beam search
- streaming response, streamed response, response, completion, chat completion, Chat Completions API, Responses API, Messages API, finish reason, stop reason

## Tokens, cost, and limits

- input token, output token, reasoning token, cached token, cache write, cache read, prompt caching, cache hit, cache miss, tokenizer, tokenization, byte pair encoding (BPE), SentencePiece, tiktoken, token count, token limit
- tokens per second, time to first token (TTFT), time per output token (TPOT), inter-token latency, end-to-end latency, Batch API, Message Batches API, provisioned throughput, price per million tokens, cost per request, token budget, usage

## Retrieval-augmented generation

- retrieval-augmented generation (RAG), RAG pipeline, retriever, retrieval, document store, knowledge base, corpus, source document, document loader, document parser, document parsing, text splitter, retrieved context, top-k retrieval
- query rewriting, query expansion, query decomposition, hypothetical document embeddings (HyDE), multi-query retrieval, grounded answer, groundedness, faithfulness, answer relevance, context relevance, context precision, context recall
- knowledge graph, GraphRAG, graph retrieval, agentic RAG, corrective RAG, semantic cache, semantic caching, ingestion pipeline, indexing pipeline, parsing, table extraction, metadata extraction
- LlamaIndex, LangChain, Haystack, Unstructured, LlamaParse, Docling

## Fine-tuning and adaptation

- fine-tuning, supervised fine-tuning (SFT), instruction tuning, parameter-efficient fine-tuning (PEFT), low-rank adaptation (LoRA), QLoRA, adapter, LoRA adapter, full fine-tuning, continued pretraining, domain adaptation
- reinforcement learning from human feedback (RLHF), reinforcement learning from AI feedback (RLAIF), direct preference optimization (DPO), group relative policy optimization (GRPO), proximal policy optimization (PPO), reward model, preference data, preference pair
- training example, instruction dataset, data mixture, model distillation, model merging, GPTQ, AWQ, GGUF, bitsandbytes, catastrophic forgetting, alignment, model alignment, constitutional AI

## Evaluation

- evaluation, eval, LLM evaluation, evaluation dataset, eval set, golden dataset, test case, reference answer, expected output, rubric, scoring rubric, LLM-as-a-judge, judge model, pairwise comparison, human evaluation, human rater, inter-rater agreement
- exact match, string match, semantic similarity, BERTScore, pass@k, win rate, Elo rating, MMLU, GPQA, HumanEval, SWE-bench, Chatbot Arena, LMArena, evaluation harness, regression eval, LLM observability
- Langfuse, LangSmith, Arize Phoenix, Ragas, DeepEval, promptfoo, OpenAI Evals, Braintrust, TruLens
- hallucination, hallucination rate, factual accuracy, factuality, answer correctness, toxicity, refusal rate, over-refusal

## Safety, security, and governance

- AI safety, guardrail, guardrails, input guardrail, output guardrail, content filter, content moderation, moderation API, safety classifier, harm category, harmful content, jailbreak, jailbreak prompt
- prompt injection, direct prompt injection, indirect prompt injection, data exfiltration, sensitive information disclosure, PII detection, PII redaction, data loss prevention (DLP), training data extraction, membership inference, model extraction, denial of wallet
- OWASP Top 10 for LLM Applications, OWASP Top 10 for Large Language Model Applications, MITRE ATLAS, red teaming, red team, adversarial prompt, refusal, watermarking, content credentials, C2PA, AI disclosure, acceptable use policy (AUP)
- system card, transparency note, responsible scaling policy, AI policy, intellectual property, zero data retention (ZDR), human review

## Multimodal and speech

- multimodal input, image input, vision, image understanding, image generation, text-to-image, image-to-image, inpainting, outpainting, image editing, video generation, text-to-video, audio generation, speech synthesis
- text-to-speech (TTS), speech-to-text (STT), transcription, diarization, speaker diarization, voice activity detection (VAD), real-time voice, voice agent, speech-to-speech, Realtime API, document understanding, visual question answering (VQA), image caption, alt text

## Serving and runtime

- model hosting, self-hosted model, managed API, serverless inference, inference server, vLLM, Text Generation Inference (TGI), SGLang, llama.cpp, Ollama, LM Studio, MLX, LiteLLM, OpenRouter, Together AI, Fireworks AI, Groq, Cerebras, Replicate, Baseten, NVIDIA NIM
- KV cache, key-value cache, PagedAttention, paged attention, speculative decoding, quantized model, fallback model, model routing, model router, LLM gateway, AI gateway

## Platforms and tools

- Anthropic API, Claude API, Claude Developer Platform, Claude.ai, Claude Code, Claude Agent SDK, OpenAI API, OpenAI Platform, Hugging Face Inference Endpoints, Vercel AI SDK, AI SDK, Pydantic, Pydantic AI
- Guardrails AI, NeMo Guardrails, Llama Guard, Microsoft Presidio, Presidio, GitHub Copilot, Cursor, Windsurf, Whisper Studio
