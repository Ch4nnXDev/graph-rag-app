import React from "react";
import { useState } from "react";
import Chatbar from "./chatBar";
export default function ChatArea() {
    const [messages, setMessages] = useState([]);
    
    return (
        <div className="flex flex-col flex-1 w-full bg-white p-4 justify-between rounded-t-lg">
            <p></p>
            <Chatbar />

        </div>
    )
}