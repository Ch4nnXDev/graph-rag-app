import React from "react";
import { createBrowserRouter } from "react-router-dom";
import  MainLayout from "./layouts/mainLayout";
import ChatWindow from "./components/chatWindow";
import Home from "./components/Home";
import Signup from "./components/Signup";

export const router = createBrowserRouter([
    {
        path: "/",
        element: <MainLayout />,
        children: [
            {
                index: true,
                element: <Home />
            },
            {
                path: "/signup",
                element: <Signup />
            },
            {
                path: "/chat",
                element: <ChatWindow />
            }

        ]
    }
])