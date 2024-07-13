"use client"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle
} from "@/components/ui/card"
import { useEffect, useState } from 'react'

function page() {
  const [data,setdata]=useState([])
useEffect(()=>{
const getData=async()=>{
  const query = await fetch('http://127.0.0.1:8000/formslist')
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
    <CardTitle> Name: {item?.name}</CardTitle>
    <CardDescription>Email: {item?.email}</CardDescription>
  </CardHeader>
  <CardContent>
  Phone Number: {item?.phone}
  </CardContent>
  <CardContent>
  Address: {item?.address}
  </CardContent>
 
</Card>
      
      <br></br></div>
      ))}
      
    </div>

  )
}

export default page
