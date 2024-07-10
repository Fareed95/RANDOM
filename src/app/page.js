"use client"
import { useRouter } from "next/navigation";
import { Router } from "next/router";
import { useEffect } from "react";
export default function Home() {
  const router = useRouter();
useEffect(()=>{
  router.push('/form')
})
}
