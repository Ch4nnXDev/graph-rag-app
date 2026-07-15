import React from "react";
import { useForm } from "react-hook-form";



export default function Form() {
    const {
        register,
        handleSubmit,
        
    } = useForm();


    const onSubmit = (data) => {
        console.log(data);
    }
    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <label>First Name</label>
            <input {...register("firstname")} />
            <label>lastname</label>
            <input  {...register("lastname")}/>
            <label>username</label>
            <input {...register("username")}/>
            <label>password</label>
            <input {...register("password")}/>
        </form>
    )
}