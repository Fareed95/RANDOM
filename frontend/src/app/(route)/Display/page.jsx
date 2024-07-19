"use client"
import { useRouter } from "next/navigation";

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


  const router = useRouter();

 
useEffect(()=>{
const getData=async()=>{
  const query = await fetch('http://127.0.0.1:8000/formslist')
  const resp = await query.json() 
  // console.log(resp)
  setdata(resp)
}
getData()
},[])

  const InfoPage=(a)=>{
    if(a){
    router.push(`Main/${a}`)
  console.log("hello",a)}
else{
  alert("no data available")
}
  
}


  return (
   
    <div className=' flex text-center flex-col '>
  {data&& data.length&& data.map((item)=>(
    <div >
<div key={item}><Card className=" hover:bg-slate-100 transition delay-150 ease-out" onClick={()=>InfoPage(item?.form_id)}>
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
      </div>
      ))}
      
    </div>

  )
}

export default page
