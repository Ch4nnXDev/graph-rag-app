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
      className={`flex flex-col gap-10 bg-black text-white p-6 h-full transition-all shadow-lg duration-300 ${
        isOpen ? "w-64" : "w-18"
      }`}
    >
      <div className="flex justify-between items-center">
        

        <Flower onClick={isOpen ? handleFlowerClick : toggleSidebar} className="hover:cursor-pointer shrink-0 w-6 h-6"/>
        <Menu onClick={toggleSidebar} className={`w-6 h-6 hover:cursor-pointer ${isOpen ? "block" : "hidden"} `}/>
     

      </div>
      <div className="flex justify-between items-center">
        <Plus onClick={handlePlusClick} className="hover:cursor-pointer shrink-0 w-6 h-6"/>
      </div>
      <div>
        <NotepadText onClick={handleChatsClick} className="flex hover:cursor-pointer justify-between items-center shrink-0 w-6 h-6 "/>
      </div>
      <div>
        <Settings className="flex hover:cursor-pointer justify-between items-center shrink-0 w-6 h-6"/>
      </div>
    
    </div>
  );
}
