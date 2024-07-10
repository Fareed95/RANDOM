"use client"
import React, { useEffect, useState } from 'react'
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

function page() {
  const [data,setdata]=useState([])
useEffect(()=>{
const getData=async()=>{
  const query = await fetch('https://jsonplaceholder.typicode.com/users')
  const resp = await query.json() 
  console.log(resp)
  setdata(resp)
}
getData()
},[])
  return (
   
    <div className=' flex text-center flex-col '>





      {data&& data.length&& data.map((item)=>(
<div key={item}><Card>
  <CardHeader>
    <CardTitle> Name: {item?.username}</CardTitle>
    <CardDescription>Email: {item?.email}</CardDescription>
  </CardHeader>
  <CardContent>
  Phone Number: {item?.phone}
  </CardContent>
  <CardContent>
  Address: {item?.address?.street}
  </CardContent>
 
</Card>
      
      <br></br></div>
      ))}
      
    </div>

  )
}

export default page