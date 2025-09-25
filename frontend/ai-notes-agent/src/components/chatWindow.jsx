import React from "react";
import axios from "axios";
import { uiStore } from "../store/docUpStore";
import { Trash, Trash2} from "lucide-react";
import ChatArea from "./chatArea";
import FileUpload from "./fileUpload";
import FileViewArea from "./fileViewArea"
export default function ChatWindow() {
const activateWindow = uiStore((state) => state.window);

async function handleDelete() {
  axios.delete("http://localhost:8000/delete_all_files").then((response) => {
    console.log("All files deleted", response.data);
  }).catch((error) => {
    console.error("Error deleting files", error);
  });

}
  return (
    <div className="flex flex-col flex-1 bg-white justify-between mb-10">
      {activateWindow === "chat" && (
        <>
          <h2 className="text-2xl font-bold p-10 shadow-lg">Chat</h2>
          
          <ChatArea />
          
         

        </>
      )}
      {activateWindow === "upload" && (
        <>
          <h2 className="text-xl font-bold p-8">Upload Docs</h2>
          <button className="fixed bottom-4 right-4 bg-white text-black text-center px-4 py-2 rounded-2xl hover:cursor-pointer" onClick={handleDelete}><Trash2 /></button>
          <FileViewArea />
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
