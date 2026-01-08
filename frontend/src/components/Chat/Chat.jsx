import React, { useState } from "react";
import { api } from "../../api/api";
import styles from "./Chat.module.css"; // <-- note o "styles"

export default function Chat() {
  const [question, setQuestion] = useState("");
  const [messageList, setMessageList] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!question.trim()) return;

    setMessageList((current) => [
      ...current,
      { sender: "user", text: question },
    ]);

    setLoading(true);
    setQuestion("");

    try {
      const response = await api.post("/api/chat", null, {
        params: { user_question: question },
      });

      setMessageList((current) => [
        ...current,
        { sender: "bot", text: response.data.response || "Sem resposta" },
      ]);
    } catch (err) {
      console.error(err);
      setMessageList((current) => [
        ...current,
        { sender: "bot", text: "Erro ao conectar com o servidor" },
      ]);
    }

    setLoading(false);
  };

  return (
    <div className={styles.chatContainer}>
      <div className={styles.chatBox}>
        <div className={styles.chatHeader}>Fruit Chat 🍎</div>

        <div className={styles.chatMessages}>
          {messageList.map((message, index) => (
            <div
              key={index}
              className={`${styles.message} ${
                message.sender === "user"
                  ? styles.userMessage
                  : styles.botMessage
              }`}
            >
              {message.text}
            </div>
          ))}

          {loading && <div className={styles.botLoading}>...</div>}
        </div>

        <div className={styles.chatInputContainer}>
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleSubmit()}
            placeholder="Digite sua pergunta..."
          />
          <button onClick={handleSubmit}>Enviar</button>
        </div>
      </div>
    </div>
  );
}
