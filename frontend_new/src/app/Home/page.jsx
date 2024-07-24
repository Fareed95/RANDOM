"use client";
import { useEffect, useState } from 'react';

function Page() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const resp = await fetch("http://localhost:8000/api/user", {
          credentials: 'include'
        });
        if (resp.ok) {
          const userData = await resp.json();
          setUser(userData);
        } else {
          console.error('Failed to fetch user data');
        }
      } catch (error) {
        console.error('Error fetching user:', error);
      }
    };

    fetchUser();
  }, []);

  return (
    <div className="flex items-center justify-center mt-[10rem]">
      <div className="bg-slate-50 p-8 rounded-lg shadow-md w-full max-w-md">
        {user ? (
          <>
            <h2 className="text-2xl font-bold mb-6 text-center">
              Welcome, {user.name}!
            </h2>
            <p className="text-center text-gray-600">Email: {user.email}</p>
          </>
        ) : (
          <p>Loading...</p>
        )}
      </div>
    </div>
  );
}

export default Page;
