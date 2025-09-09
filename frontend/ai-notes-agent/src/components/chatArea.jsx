import React from "react";
import Chatbar from "./chatBar";
export default function ChatArea() {
    return (
        <div className="flex flex-col flex-1 w-full bg-white p-4 justify-between">
            <p>This is the chat area.</p>
            <Chatbar />

        </div>
    )
}