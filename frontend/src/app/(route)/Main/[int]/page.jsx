"use client"
import React from 'react'
import { useEffect, useState } from 'react'
function page(params) {
  const [data,setdata]=useState([])
  useEffect(()=>{
    const getData=async()=>{
      const query = await fetch(`http://127.0.0.1:8000/formslist/${params?.params?.int}`)
      const resp = await query.json() 
      // console.log(resp)
      setdata(resp)
    }
    getData()
    
    },[])
  return (
    <div>
        <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="bg-white p-8 rounded shadow-md w-full max-w-sm">
        <h1 className="text-2xl font-bold mb-6 text-center">User Details</h1>
        <p className="mb-4">
          <span className="font-semibold">Name:</span> {data?.name}
        </p>
        <p className="mb-4">
          <span className="font-semibold">Email:</span> {data.email}
        </p>
        <p className="mb-4">
          <span className="font-semibold">Phone Number:</span> {data.phone}
        </p>
      </div>
    </div>
    </div>
  )
}

export default page
