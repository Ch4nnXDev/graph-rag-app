import React from "react";
import { useState } from "react";
import { ArrowUpIcon } from "lucide-react";
export default function Chatbar({sendInput}) {
  const [input, setInput] = useState("");
  async function handleSendMessage() {
    if (!input.trim()) return;
    sendInput(input);
    setInput("");


  }
  
  return (
    <div className="flex bg-white justify-center mb-4 p-4 gap-4 rounded-xl">
      <input type="text" value={input} placeholder="" onChange={(e) => setInput(e.target.value)} className="pl-4 border border-gray-400 rounded-2xl w-3/4 focus: outline-none" />
      <button onClick={handleSendMessage} className="bg-gray-200 text-white p-2 rounded-full hover:bg-blue-500"><ArrowUpIcon className=""/></button>
    </div>
  );
}
