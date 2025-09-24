import React from "react";
import axios from "axios";
import { useState, useEffect } from "react";
import { File } from "lucide-react";
export default function FileViewArea() {
    const [files, setFiles] = useState([]);
    
    useEffect(() => {
        async function fetchFiles() {
            try {
                const response = await axios.get("http://localhost:8000/files");
                const filesArray = Object.entries(response.data.file_urls).map(([key, value]) => ({
                    key,
                    ...value
                }));

                setFiles(filesArray);
            } catch (error) {
                console.error("Error fetching files:", error);
            }
        };
        fetchFiles();
        const interval = setInterval(fetchFiles, 10000);
        return () => clearInterval(interval);
    }, []);
    console.log(files);


    

    
    return (
    <section className="h-screen overflow-y-auto">
        <div className="text-lg font-bold">
            {files
                .filter(file => file.type === "pdf")
                .map(file => (
                <a href={file.url} target="_blank" key={file.key} className="flex items-center gap-2 p-2 bg-white rounded shadow">
                    <File className="w-10 h-10 m-2" />
                    <span className="break-all flex-1 min-w-0">{file.key.split("/").pop()}</span>
                </a>
                ))
            }
        </div>

    </section>

    )
    

}