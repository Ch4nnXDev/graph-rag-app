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

          const fileList = new FormData();
          acceptedFiles.forEach((file)=> {
            fileList.append('files', file)
          });
            axios.post("http://localhost:8000/upload", fileList, {
              headers: {
                'Content-type': 'multipart/form-data',
              }

            }).then((response) => {
              console.log("Success", response.data);
            })
            
        },

    });

  

    return (
    <div
      {...getRootProps({
        className:
          " flex flex-col border-gray-400 p-6 rounded-lg text-center cursor-pointer items-center m-6",
      })}
    >
      <span>Click or Drag files here</span>
      <input {...getInputProps()} />
      <img src="upfile.jpeg" alt="" className="w-20 h-20"></img>

    </div>
  );
}