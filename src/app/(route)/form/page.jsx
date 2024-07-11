"use client"
import React from 'react'
import { useRouter } from "next/navigation";
import { Router } from "next/router";
function page() {
    const router = useRouter();
    const directToDisplay=()=>{
        router.push('/Display')
    }
  return (
    <div >
            <>
    <div className="flex items-center justify-center h-[7rem] ">
    <div className="text-6xl font-bold bg-gradient-to-r from-blue-500 via-purple-400 to-pink-700 bg-clip-text text-transparent transition-colors duration-1000
     hover:bg-gradient-to-r hover:from-blue-800 hover:via-purple-600 hover:to-pink-400  ease-in  
    ">
      Fill the following FORM !
    </div>
  </div>
  
  
  
  
  <section className="text-gray-600 body-font relative">
      <div className="container px-5 py-24 mx-auto">
        <div className="flex flex-col text-center w-full mb-12">
          
          <p className="lg:w-2/3 mx-auto leading-relaxed text-base">Fill out the form below to see the deets on other page.</p>
        </div>
        <div className="lg:w-1/2 md:w-2/3 mx-auto">
          <div className="flex flex-wrap -m-2">
            <div className="p-2 w-full">
              <div className="relative">
                <label htmlFor="full-name" className="leading-7 text-sm text-gray-600">Full Name</label>
                <input type="text" id="full-name" name="full-name" className="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out" />
              </div>
            </div>
            <div className="p-2 w-full">
              <div className="relative">
                <label htmlFor="email" className="leading-7 text-sm text-gray-600">Email</label>
                <input type="email" id="email" name="email" className="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out" />
              </div>
            </div>
            <div className="p-2 w-full">
              <div className="relative">
                <label htmlFor="phone" className="leading-7 text-sm text-gray-600">Phone Number</label>
                <input type="tel" id="phone" name="phone" className="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out" />
              </div>
            </div>
            
            <div className="p-2 w-full">
              <div className="relative">
                <label htmlFor="experience" className="leading-7 text-sm text-gray-600">Address</label>
                <textarea id="experience" name="experience" className="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out"></textarea>
              </div>
            </div>
            
            <div className="p-2 w-full">
              <button className="flex mx-auto text-white bg-blue-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg" onClick={()=>directToDisplay()}>Submit</button>
            </div>
          </div>
        </div>
      </div>
    </section>
  
  
  </>
    </div>
  )
}

export default page
