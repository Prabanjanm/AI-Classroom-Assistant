en-IN-NeerjaNeural	Indian Female
en-IN-PrabhatNeural	Indian Male
en-US-JennyNeural	US Female
en-US-GuyNeural	US Male
ta-IN-PallaviNeural	Tamil Female
hi-IN-SwaraNeural	Hindi Female

CATEGORY 2 — IMAGE UNDERSTANDING
TEST 3 — IMAGE DESCRIPTION

Upload:

image

Request:

Describe this image
EXPECTED FLOW
ImageDescriptionAgent
TEST 4 — IMAGE EMBEDDING

Upload:

image

Request:

Generate embedding for this image
EXPECTED FLOW
CLIPEmbeddingAgent
CATEGORY 3 — AUDIO WORKFLOWS
TEST 5 — AUDIO TRANSCRIPTION

Upload:

mp3/wav

Request:

Transcribe this audio
EXPECTED FLOW
WhisperAgent
TEST 6 — TTS

Request:

Generate narration audio for:
Artificial intelligence is transforming education
EXPECTED FLOW
TTSAgent
CATEGORY 4 — RAG WORKFLOWS
TEST 7 — RAG CHAT

Request:

Answer question:
What is machine learning?
EXPECTED FLOW
RetrievalAgent
      ↓
RAGChatAgent
TEST 8 — RAG INGESTION

Upload:

PDF or image

Request:

Store this document into rag system
EXPECTED FLOW
OCR
 ↓
Chunking
 ↓
Embedding
 ↓
Storage
CATEGORY 5 — IMAGE GENERATION
TEST 9 — TEXT TO IMAGE

Request:

Generate image of futuristic AI classroom
EXPECTED FLOW
ImageGenerationAgent
CATEGORY 6 — VIDEO WORKFLOWS
TEST 10 — VIDEO SUMMARY

Upload:

mp4 lecture

Request:

Summarize this lecture video
EXPECTED FLOW
VideoSummaryAgent
     ↓
Whisper
     ↓
Summary
TEST 11 — YOUTUBE SUMMARY

Request:

Download and summarize this youtube lecture:
https://youtube.com/...
EXPECTED FLOW
YouTubeAgent
     ↓
WhisperAgent
     ↓
SummaryAgent
CATEGORY 7 — MULTI-AGENT COMBINATIONS
TEST 12 — OCR + SUMMARY

Upload:

PDF

Request:

Extract text and summarize this pdf
EXPECTED FLOW
PDFOCRAgent
      ↓
SummaryAgent
TEST 13 — OCR + RAG + QA

Upload:

PDF

Request:

Store this document and answer questions from it
EXPECTED FLOW
OCR
 ↓
RAG Ingestion
 ↓
Retrieval
 ↓
RAG Chat
TEST 14 — SUMMARY + TTS

Request:

Summarize lecture transcript and generate narration audio
EXPECTED FLOW
SummaryAgent
     ↓
TTSAgent
TEST 15 — IMAGE → VIDEO PIPELINE

Request:

Generate educational video about solar system
EXPECTED FLOW
SummaryAgent
      ↓
ImageGenerationAgent
      ↓
TTSAgent
      ↓
VideoGenerationAgent
CATEGORY 8 — AUTONOMOUS PLANNING
TEST 16 — COMPLEX MULTIMODAL REQUEST

Upload:

lecture video

Request:

Summarize this lecture,
generate narration audio,
and create study material
EXPECTED FLOW
VideoSummary
     ↓
Summary
     ↓
TTS
     ↓
RAG
TEST 17 — FULL AUTONOMOUS EDUCATIONAL PIPELINE

Request:

Create educational content about neural networks
with images and narration
EXPECTED FLOW
Summary
   ↓
Image Generation
   ↓
TTS
   ↓
Video Generation
CATEGORY 9 — FAILURE TESTS

VERY IMPORTANT.

TEST 18 — INVALID FILE TYPE

Upload:

random unsupported file

Request:

Analyze this file

Expected:

planner fallback
graceful error
TEST 19 — EMPTY REQUEST
{
  "user_request": ""
}

Expected:

validation error
TEST 20 — NONEXISTENT WORKFLOW
Teleport this file to Mars

Expected:

planner cannot map capabilities
fallback response
MOST IMPORTANT TEST
TEST 21 — FULL AGENT CHAIN

Upload:

lecture PDF

Request:

Extract text,
store into rag,
summarize it,
generate narration audio
EXPECTED COMPLETE FLOW
PDFOCRAgent
      ↓
RAGIngestionAgent
      ↓
SummaryAgent
      ↓
TTSAgent
DEBUGGING RECOMMENDATION

In workflow engine add:

print(
    f"Executing: "
    f"{task['agent_name']}"
)

and:

print("RESULT:", result)

This helps trace orchestration.