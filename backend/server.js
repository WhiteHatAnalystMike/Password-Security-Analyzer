const express = require("express");
const cors = require("cors");
const OpenAI = require("openai");

const app = express();
app.disable("x-powered-by");
app.use(
  cors({
    origin: process.env.CORS_ORIGIN || "http://localhost:5500"
  })
);
app.use(express.json());

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

if (!process.env.OPENAI_API_KEY) {
  console.warn("OPENAI_API_KEY is not set. /generate will fail until it is configured.");
}

app.post("/generate", async (req, res) => {
  const { text } = req.body;

  try {
    const response = await client.chat.completions.create({
      model: "gpt-4o-mini",
      messages: [
        {
          role: "system",
          content: "You are an AI study assistant. Create a summary and flashcards."
        },
        {
          role: "user",
          content: `Text: ${text}

Return JSON in this format:
{
  "summary": "...",
  "flashcards": [
    { "question": "...", "answer": "..." }
  ]
}`
        }
      ]
    });

    const aiText = response.choices[0].message.content;
    const parsed = JSON.parse(aiText);

    res.json(parsed);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Something went wrong" });
  }
});

app.listen(3000, () => console.log("Server running on port 3000"));