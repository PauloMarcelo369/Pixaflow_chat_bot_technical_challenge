import React, { useState } from "react";
import { api } from "../../api/api";

export default function Chat() {
  const [question, setQuestion] = useState("");
  const [messageList, setMessageList] = useState([]);

  const handleSubmit = async () => {
    if (!question.trim()) return;
    setMessageList((current) => [...current, question]);
    const response = await api.post(`/api/chat?user_question=${handleSubmit}`);
    setMessageList((current) => [...current, response]);
    setQuestion("");
  };

  return (
    <div>
      <h1>Chat</h1>
      {messageList.map((message, index) => (
        <p key={index}>
          {index % 2 == 0 ? "You" : "Fruit Bot"} : {message}
        </p>
      ))}
      <input
        type="text"
        value={question}
        placeholder="Digite sua pergunta..."
      />
      <button onClick={(e) => setQuestion(e.target.value)}>Enviar</button>
    </div>
  );
}
