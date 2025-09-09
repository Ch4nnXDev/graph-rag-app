import React from "react";
import { ArrowUpIcon } from "lucide-react";
export default function Chatbar() {
  return (
    <div className="flex bg-white justify-center mb-4 p-4 gap-4">
      <input type="text" placeholder="Ask Me Questions.." className="p-2 border rounded-xl w-3/4" />
      <button className="bg-gray-200 text-white p-2 rounded-full hover:bg-blue-500"><ArrowUpIcon className=""/></button>
    </div>
  );
}
