import React from "react";
import { File } from "lucide-react";
import axios from "axios";
import { useDropzone } from "react-dropzone";

export default function FileUpload() {


 
    const {getRootProps, getInputProps, acceptedFiles} = useDropzone({
        accept: {
            'application/pdf': ['.pdf'],
            'text/plain': ['.txt'],
            'application/msword': ['.doc', '.docx'],
        },
        onDrop: (acceptedFiles) => {
            axios.post()
        },

    });

  

    return (
    <div
      {...getRootProps({
        className:
          " h-full border-2 flex flex-col border-dashed border-gray-400 p-6 rounded-lg text-center cursor-pointer",
      })}
    >
      <input {...getInputProps()} />
      <p>Drag & drop files here, or click to select</p>

      <ul className="mt-4">
        {acceptedFiles.map((file) => (
          <li key={file.name} className="on-click:bg-blue">{file.name.split(".").pop()== "pdf" ? "📄 PDF File" : "🗂️ Other File"}</li>
        ))}
      </ul>
    </div>
  );
}