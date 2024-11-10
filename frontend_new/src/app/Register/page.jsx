"use client"
import React, { useState } from 'react'
import { useRouter } from "next/navigation";
function page() {
  const router =useRouter()
  const[name,setname]=useState('')
  const[email,setemail]=useState('')
  const[password,setpassword]=useState('')
  const[confirm_password,setconfirm_password]=useState('')



  const submit=async(e)=>{
  e.preventDefault();
  await fetch('http://127.0.0.1:8000/api/register',{
      method:"POST",
      headers:{"Content-Type": "application/json"},
      body:JSON.stringify({
          name,
          email,
          password,
          confirm_password
      })
  })
  await router.push('/Login')
}



   
  return (
    <div>
        <form onSubmit={submit}>
  
      
    <div className="flex items-center justify-center mt-[8rem]">
      <div className="bg-slate-50 p-8 rounded-lg shadow-md w-full max-w-md">
        <h2 className="text-2xl font-bold mb-6 text-center">Register</h2>
        <div className="mb-4">
          <label htmlFor="name" className="leading-7 text-sm text-gray-600">Name</label>
          <input
            type="text"
            id="name"
            name="name"
            placeholder='Fareed Bhai'
            className="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:ring-2 focus:ring-indigo-200 focus:bg-transparent focus:border-indigo-500 text-base outline-none text-gray-700 py-2 px-4 leading-8 transition-colors duration-200 ease-in-out"
            onChange={(e)=>{setname(e.target.value)}}

          />
        </div>
        <div className="mb-4">
          <label htmlFor="email" className="leading-7 text-sm text-gray-600">Email</label>
          <input
            type="email"
            id="email"
            name="email"
            placeholder='xyz@gmail.com'
            className="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:ring-2 focus:ring-indigo-200 focus:bg-transparent focus:border-indigo-500 text-base outline-none text-gray-700 py-2 px-4 leading-8 transition-colors duration-200 ease-in-out"
            onChange={e=>setemail(e.target.value)}

          />
        </div>
        <div className="mb-6">
          <label htmlFor="password" className="leading-7 text-sm text-gray-600">Password</label>
          <input
            type="password"
            id="password"
            name="password"
            placeholder='password'
            className="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:ring-2 focus:ring-indigo-200 focus:bg-transparent focus:border-indigo-500 text-base outline-none text-gray-700 py-2 px-4 leading-8 transition-colors duration-200 ease-in-out"
            onChange={e=>setpassword(e.target.value)}
          />
        </div>
        <div className="mb-6">
          <label htmlFor="Cpassword" className="leading-7 text-sm text-gray-600">Confirm Password</label>
          <input
            type="password"
            id="confirm_password"
            name="confirm_password"
            placeholder='Confirm password'
            className="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:ring-2 focus:ring-indigo-200 focus:bg-transparent focus:border-indigo-500 text-base outline-none text-gray-700 py-2 px-4 leading-8 transition-colors duration-200 ease-in-out"
            onChange={e=>setconfirm_password(e.target.value)}

          />
        </div>
        <button className="w-full text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg" type='submit'>
          Register
        </button>
      </div>
    </div>
    </form>
    </div>
  )
}

export default page

