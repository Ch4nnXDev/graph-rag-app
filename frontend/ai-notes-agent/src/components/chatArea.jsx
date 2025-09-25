import React, { useState, useRef, useEffect } from "react";
import Chatbar from "./chatBar";
import axios from "axios";

export default function ChatArea() {
  const [messages, setMessages] = useState([]);
  const chatEndRef = useRef(null);

  
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSendInput = async (newMessage) => {
    
    setMessages((prev) => [...prev, { role: "user", text: newMessage }]);

    try {
      
      const res = await axios.post("http://localhost:8000/answer", {
        question: newMessage,
      });

      
      setMessages((prev) => [
        ...prev,
        { role: "assistant", text: res.data.answer },
      ]);
    } catch (err) {
      console.error(err);
      setMessages((prev) => [
        ...prev,
        { role: "assistant", text: "Error contacting the model." },
      ]);
    }
  };

  return (
    <div className="flex flex-col flex-1 w-full bg-white p-4 rounded-t-lg h-full">
    
      <div className="flex-1 overflow-y-auto space-y-2">
        {messages.map((msg, i) => (
          <div
            key={i}
            className={`p-2 rounded-md max-w-xs ${
              msg.role === "user"
                ? "bg-blue-500 text-white ml-auto"
                : "bg-gray-200 text-black mr-auto"
            }`}
          >
            {msg.text}
          </div>
        ))}
        <div ref={chatEndRef} />
      </div>

      {/* Chat bar */}
      <Chatbar sendInput={handleSendInput} />
    </div>
  );
}
