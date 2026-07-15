import React from "react";
import Sidebar from "../components/sidebar";
import {Outlet} from "react-router-dom";

export default function MainLayout() {
    return (
        <div className="flex h-screen">
            <Sidebar />

            <main className="flex-1">
                <Outlet />
            </main>

        </div>
    );
}