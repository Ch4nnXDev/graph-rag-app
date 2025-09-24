import React from 'react';
import { useState } from 'react';
import { NotepadText } from 'lucide-react';
import { Settings } from 'lucide-react';
import { Plus } from 'lucide-react';
import { Flower } from 'lucide-react';
import { uiStore } from '../store/docUpStore';
import { Menu } from 'lucide-react';
export default function Sidebar() {

  const [isOpen, setIsOpen] = useState(true);
  const setWindow = uiStore((state) => state.setWindow);


  function toggleSidebar()  {
    setIsOpen(!isOpen);
  }

  function handlePlusClick() {
    setWindow("upload"); 
    
  }

  function handleChatsClick() {
    setWindow("saved chats")
  }

  function handleFlowerClick() {
    setWindow("chat");
  }
  return (
    <div
      className={`flex flex-col gap-10 bg-blue-500 text-white p-6 h-full transition-all shadow-lg duration-300 ${
        isOpen ? "w-64" : "w-18"
      }`}
    >
      <div className="flex justify-between mt-5 ml-1">
        

        <Flower onClick={isOpen ? handleFlowerClick : toggleSidebar} className="hover:cursor-pointer shrink-0 w-6 h-6 ml-1"/>
        <Menu onClick={toggleSidebar} className={`w-6 h-6 hover:cursor-pointer ${isOpen ? "block" : "hidden"} `}/>
     

      </div>

      <div className="flex rounded-lg hover:bg-blue-700 p-2 w-full">
        <Plus onClick={handlePlusClick} className="hover:cursor-pointer shrink-0 w-6 h-6 "/>
        <span className="ml-4 text-sm">Documents</span>
      </div>
      <div className="flex rounded-lg hover:bg-blue-700 p-2">
        <NotepadText onClick={handleChatsClick} className="flex hover:cursor-pointer justify-between items-center shrink-0 w-6 h-6 "/>
        <span className="ml-4 text-sm">Workspaces</span>
      </div>
      <div className="flex rounded-lg hover:bg-blue-700 p-2">
        <Settings className="flex hover:cursor-pointer justify-between items-center shrink-0 w-6 h-6"/>
        <span className="ml-4 text-sm">Settings</span>
      </div>
      
    
    </div>
    
  );
}
