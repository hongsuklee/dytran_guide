from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from pathlib import Path

app = FastAPI()

# ── Reuse tool logic from your MCP server ──────────────────────────────────

def load_expert_document():
    expert_path = Path(__file__).parent / "expert.md"
    if not expert_path.exists():
        return None
    try:
        with open(expert_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error loading expert.md: {e}")
        return None


def _split_paragraphs(content: str) -> list:
    paragraphs, current = [], []
    for line in content.split("\n"):
        if line.strip():
            current.append(line)
        elif current:
            paragraphs.append("\n".join(current))
            current = []
    if current:
        paragraphs.append("\n".join(current))
    return paragraphs


def search_document(content: str, query: str) -> list:
    if not content or not query:
        return []
    query_lower = query.lower()
    paragraphs = _split_paragraphs(content)
    scored = []
    for para in paragraphs:
        para_lower = para.lower()
        score = 0
        if query_lower in para_lower:
            score += 100
        query_words = query_lower.split()
        words_found = sum(1 for w in query_words if w in para_lower)
        if words_found == len(query_words):
            score += 50
        score += words_found * 10
        key_terms = [w for w in query_words if len(w) > 3]
        score += sum(5 for t in key_terms if t in para_lower)
        if score > 0:
            scored.append((score, para))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [p for _, p in scored]


# ── API routes ─────────────────────────────────────────────────────────────

class QuestionRequest(BaseModel):
    question: str


class SearchRequest(BaseModel):
    phrase: str


@app.post("/api/ask")
def ask_expert(req: QuestionRequest):
    content = load_expert_document()
    if content is None:
        return JSONResponse({"answer": "expert.md not found on the server."})
    sections = search_document(content, req.question)
    if not sections:
        return JSONResponse({"answer": "I don't know — this topic isn't covered in the Dytran guide."})
    answer = "\n\n---\n\n".join(sections[:3])
    if len(answer) > 10_000:
        answer = answer[:10_000] + "\n\n… (truncated)"
    return JSONResponse({"answer": f"Based on the Dytran expert document:\n\n{answer}"})


@app.post("/api/search")
def search_expert(req: SearchRequest):
    content = load_expert_document()
    if content is None:
        return JSONResponse({"answer": "expert.md not found on the server."})
    if req.phrase.lower() not in content.lower():
        return JSONResponse({"answer": f"The phrase '{req.phrase}' was not found in the document."})
    matches = [p for p in _split_paragraphs(content) if req.phrase.lower() in p.lower()]
    result = "\n\n---\n\n".join(matches)
    if len(result) > 10_000:
        result = result[:10_000] + "\n\n… (truncated)"
    return JSONResponse({"answer": f"Found '{req.phrase}' in the expert document:\n\n{result}"})


@app.get("/api/topics")
def get_topics():
    content = load_expert_document()
    if content is None:
        return JSONResponse({"topics": []})
    headers = [l.strip() for l in content.split("\n") if l.strip().startswith("#")]
    return JSONResponse({"topics": headers})


# ── Serve the single-page UI ───────────────────────────────────────────────

@app.get("/")
def index():
    return FileResponse(Path(__file__).parent / "index.html")
