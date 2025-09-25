import React, { useState } from "react";
import { ArrowUpIcon } from "lucide-react";

export default function Chatbar({ sendInput }) {
  const [input, setInput] = useState("");

  async function handleSendMessage() {
    if (!input.trim()) return;
    await sendInput(input); 
    setInput(""); 
  }

  return (
    <div className="flex items-center bg-white p-4 gap-4 rounded-xl border-t border-gray-300">
      <input
        type="text"
        value={input}
        placeholder="Type a message..."
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && handleSendMessage()}
        className="flex-1 pl-4 border border-gray-400 rounded-2xl focus:outline-none"
      />
      <button
        onClick={handleSendMessage}
        className="bg-blue-500 text-white p-2 rounded-full hover:bg-blue-600"
      >
        <ArrowUpIcon className="w-5 h-5" />
      </button>
    </div>
  );
}
