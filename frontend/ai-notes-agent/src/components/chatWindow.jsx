import React from "react";
import { uiStore } from "../store/docUpStore";
import ChatArea from "./chatArea";
import FileUpload from "./fileUpload";
export default function ChatWindow() {
const activateWindow = uiStore((state) => state.window);
  return (
    <div className="flex flex-col flex-1 bg-white justify-between ">
      {activateWindow === "chat" && (
        <>
          <h2 className="text-xl font-bold p-10 bg-white">Chat</h2>
          <ChatArea />
          
         

        </>
      )}
      {activateWindow === "upload" && (
        <>
          <h2 className="text-xl font-bold p-8">Upload Docs</h2>
          <FileUpload />
          
         

        </>
      )}
      {activateWindow === "saved chats" && (
        <>
          <h2 className="text-xl font-bold p-10">Saved Chats</h2>
          <p className="p-10">This is the saved chats area.</p>
        </>
      )}
      
      

    </div>

  );
}
