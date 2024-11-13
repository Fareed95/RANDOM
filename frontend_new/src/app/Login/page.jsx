"use client"
import { useRouter } from "next/navigation";
import { useState } from 'react';

function page() {
  const router = useRouter();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const submit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:8000/api/login', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: 'include', // to store cookie
        body: JSON.stringify({
          email,
          password
        })
      });

      if (response.ok) {
        console.log('Login successful');
        router.push("/Home");
      } else {
        console.error('Login failed', response.statusText);
        const errorData = await response.json();
        console.error('Error details:', errorData);
        // Handle login failure (e.g., show an error message)
      }
    } catch (error) {
      console.error('Error occurred during login:', error);
    }
  };

  return (
    <form onSubmit={submit}>
      <div className="flex items-center justify-center mt-[10rem]">
        <div className="bg-slate-50 p-8 rounded-lg shadow-md w-full max-w-md">
          <h2 className="text-2xl font-bold mb-6 text-center">Login</h2>
          <div className="mb-4">
            <label htmlFor="email" className="leading-7 text-sm text-gray-600">Email</label>
            <input
              type="email"
              id="email"
              name="email"
              placeholder='xyz@gmail.com'
              className="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:ring-2 focus:ring-indigo-200 focus:bg-transparent focus:border-indigo-500 text-base outline-none text-gray-700 py-2 px-4 leading-8 transition-colors duration-200 ease-in-out"
              onChange={e => setEmail(e.target.value)}
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
              onChange={e => setPassword(e.target.value)}
            />
          </div>
          <button className="w-full text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg" type='submit'>
            Login
          </button>
        </div>
      </div>
    </form>
  );
}

export default page;
